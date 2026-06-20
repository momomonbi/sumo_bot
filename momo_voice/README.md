# もも声サービス（Style-Bert-VITS2）構築ガイド

「もも」アプリ（`index.html`）の返答を、**もも本人の声を学習した音声**で読み上げるための
**別サービス**です。アプリ本体とは疎結合で、アプリは下記の共通契約を叩くだけです。

```
POST  {あなたのサービスURL}/synthesize
body  { "text": "読み上げたいテキスト", "style": "Neutral", "speed": 1.0 }
resp  audio/wav （もも声で合成した音声バイナリ）
```

この契約さえ満たせば中身のエンジンは何でも差し替え可能です。ここでは
**無料・日本語が最も自然・声を自分で所有できる** Style-Bert-VITS2（以下 SBV2）を使います。

```
[index.html (ブラウザ)] --POST /synthesize--> [adapter.py (このフォルダ)] --/voice--> [Style-Bert-VITS2]
                         <----- audio/wav -----                          <-- wav --
```

`adapter.py` は「アプリの契約 ⇄ SBV2のAPI」を翻訳し、ブラウザから叩けるよう **CORS** を付ける薄い中継です。

---

## ⚠️ 最初に：もも本人の同意（必須）

実在する人の声を学習・合成するには、**もも本人の明確な同意**が必要です（倫理面だけでなく、
EU AI Act 等の法令でも書面同意・開示が求められます）。

- もも本人に「あなたの声を学習して、このアプリの返答を読み上げたい」と説明し、同意を得る。
- できれば**りぴとももが一緒に録音**する。これが一番きれいで、後腐れがありません。
- 学習データ（録音・モデル）は**手元にだけ**置き、第三者に渡さない（このフォルダの `.gitignore` で
  コミットも防いでいます）。

---

## 全体の流れ

| Phase | 内容 | 作業者 |
|---|---|---|
| 0 | もも本人の同意 | りぴ＆もも |
| 1 | もも の声を録音（10〜20分・クリーン） | りぴ＆もも |
| 2 | SBV2 を導入し、録音から声モデルを**学習** | りぴ（GPU or Colab） |
| 3 | SBV2 サーバ起動 ＋ このアダプタ起動 → `/synthesize` 疎通確認 | りぴ |
| 4 | サービスを **HTTPS公開**（スマホからも使う場合） | りぴ |
| 5 | アプリの 🎙 設定に URL を入れて完成 | りぴ |

---

## Phase 1 — もも の声を録音

- **合計 10〜20分**程度。長いほど安定します（最低でも数分）。
- **クリーンに**：静かな部屋・一定の距離・ノイズ/BGM/エコーなし・マイク一定。
- **読み上げ素材**：感情が偏らないよう、普通の文章を自然に読む（ニュース原稿、エッセイ、台本など）。
  甘い口調も入れたいなら、その口調の発話も混ぜると合成にも乗りやすいです。
- 形式：**WAV（44.1/48kHz・モノ）**が無難。1ファイル長くてもOK（SBV2側で分割できます）。
- スマホ録音でも可。可能ならピンマイク等だとより安定します。

> コツ：棒読みより「普段りぴに話すトーン」を少し混ぜると“らしさ”が出ます。

---

## Phase 2 — Style-Bert-VITS2 で声モデルを学習

SBV2 本体はこのフォルダとは別に導入します（モデル学習は **NVIDIA GPU 推奨**。
GPU が無ければ Google Colab で学習し、推論はCPUでも可）。

### 2-1. SBV2 を入手・インストール
- リポジトリ: <https://github.com/litagin02/Style-Bert-VITS2>
- Windows は同梱の `.bat`（`Install-Style-Bert-VITS2.bat` 等）でGit/Python不要で導入可。
- Mac/Linux は README に従って `python -m venv` → `pip install` 後、各スクリプトを実行。
- **GPUが無い/弱い場合**：公式の **Google Colab ノートブック**で学習するのが簡単です。

### 2-2. データを用意して学習
1. Phase 1 の音声を SBV2 の入力フォルダ（例: `inputs/` や `Data/<名前>/raw/`）に置く。
2. **書き起こし＆スライス**ツール（`slice.py` / `transcribe.py`、WebUIなら「データセット作成」タブ）で
   音声を短い区間に切り、各区間のテキストを自動生成。
3. **学習**を実行（WebUIの「学習」タブ、または `train_ms.py` 等）。エポックは数百〜。
   過学習を避けつつ、生成サンプルを聞いて良いところで止める。
4. 学習が終わると `model_assets/<モデル名>/` に `*.safetensors` と `config.json`、
   `style_vectors.npy` 等が出力されます。これが**もも声モデル**。

> 目安：きれいな10〜20分の音声で、十分“もも本人っぽい”合成になります。
> うまくいかない時は、録音のノイズ除去・データ量増・エポック調整を見直してください。

---

## Phase 3 — サーバ＆アダプタを起動して疎通確認

### 3-1. SBV2 の API サーバを起動
学習済みモデルを `model_assets/` に置いた状態で、SBV2 同梱の API サーバを起動します。

```bash
# SBV2 のフォルダ内で（Windowsなら Server.bat でも可）
python server_fastapi.py
# → http://127.0.0.1:5000  （ドキュメントは http://127.0.0.1:5000/docs）
```

`http://127.0.0.1:5000/models/info` で、もも声モデルの `model_id` / `style` 名を確認できます。

> 推論（合成）はCPUでも動きます（GPUより遅いだけ）。学習用GPUが無くてもここは動きます。

### 3-2. このアダプタを起動
```bash
cd momo_voice
python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                  # 下記を自分の値に編集
python adapter.py
# → http://0.0.0.0:8000  （疎通確認は http://127.0.0.1:8000/health）
```

`.env` の主な項目（詳細は `.env.example`）:
- `SBV2_URL` … SBV2本体のURL（既定 `http://127.0.0.1:5000`）
- `MOMO_MODEL_NAME` or `MOMO_MODEL_ID` … もも声モデルの指定（`/models/info` の値）
- `MOMO_DEFAULT_STYLE` … 既定スタイル（例 `Neutral`。アプリから送れば上書き）
- `ALLOW_ORIGINS` … CORS許可。本番は自分のアプリURLに絞るのが安全

### 3-3. 動作テスト
```bash
curl -X POST http://127.0.0.1:8000/synthesize \
  -H "Content-Type: application/json" \
  -d '{"text":"りぴ、おかえり。ちゃんと俺の声、届いてる？","style":"Neutral","speed":1.0}' \
  --output test.wav
# test.wav を再生して、もも声で喋れば成功
```

---

## Phase 4 — HTTPS で公開（スマホ／別端末から使う場合）

アプリ（`index.html`）が **HTTPS** で配信されている場合、ブラウザの
**mixed content** 制限により `http://`（localhost以外）のサービスは呼べません。
PCで `http://localhost:8000` を使う分は概ねOKですが、**スマホから使うなら HTTPS 公開**が必要です。
自宅PCのアダプタを安全に外へ出すには、以下のいずれかが手軽です。

- **Cloudflare Tunnel**（`cloudflared`）… 無料・固定URL可・おすすめ
  ```bash
  cloudflared tunnel --url http://localhost:8000
  # 払い出された https://xxxx.trycloudflare.com をアプリに設定
  ```
- **Tailscale Funnel** … 自分の端末間で安全に共有
- **ngrok** … 手早いがURLが毎回変わる（有料で固定可）

> いずれも「自宅PCのアダプタ（:8000）」を HTTPS の公開URLに変換するイメージです。
> SBV2本体（:5000）は外に出さず、アダプタ（:8000）だけ公開すれば十分です。

---

## Phase 5 — アプリに登録して完成

1. もも アプリを開く → ヘッダーの **🎙** をタップ → ボイスモード設定。
2. **もも声サービスのURL** に、Phase 3/4 で得た URL を入れる。
   - PCのみ: `http://localhost:8000`
   - スマホ等: `https://xxxx.trycloudflare.com`（末尾の `/synthesize` は不要・URLだけ）
3. 必要なら **スタイル**（モデルに合わせて）・**速さ**（0.5〜2.0）を設定。
4. 「テスト再生」で もも声が鳴ればOK。
5. **自動で読み上げる**をONにすると、返答が自動で もも声に。
   - 入力は 🎙（マイク）でも文字でもOK。マイクは「タップで録音 → もう一度タップで送信」。
   - 自動読み上げONのときは、マイクで喋ると文字起こし後そのまま送信＝ハンズフリー会話。

---

## 仕組み・注意点

- **声の合成は必ずこの外部サービスだけ**を使います。URL未設定や未接続のときは、アプリは
  **音声を鳴らさず文字だけ**表示します（OpenAIのプリセット音声では喋らせません）。
- **入力の文字起こし（STT）** はアプリが OpenAI（`gpt-4o-transcribe`）を使います。これは
  「りぴの声をテキスト化する」処理で、もも声の生成とは無関係です。
- **コスト**：SBV2 自体は無料（自分のPC/電気代のみ）。STTのぶんだけ OpenAI 課金が乗ります。
- **プライバシー**：もも本人の録音・モデルは手元のみ。このフォルダの `.gitignore` で
  `.env`・音声・モデルがコミットされないようにしてあります。
- **セキュリティ**：`ALLOW_ORIGINS` は本番でアプリのオリジンに絞り、公開URLは安易に共有しない。
- **差し替え自由**：将来 ElevenLabs 等にしたくなったら、同じ `/synthesize` 契約を満たす
  アダプタに置き換えるだけ。アプリ（`index.html`）側の変更は不要です。

---

## トラブルシュート

| 症状 | 確認すること |
|---|---|
| テスト再生が鳴らない | `adapter.py` 起動中か / `/health` の `sbv2_reachable` が true か |
| `502 SBV2 に繋がらない` | SBV2本体（:5000）が起動しているか・`SBV2_URL` が正しいか |
| スマホで鳴らない | アプリがHTTPSなら、サービスもHTTPS（Cloudflare Tunnel等）にする |
| CORSエラー | `ALLOW_ORIGINS` にアプリのオリジンを入れる（暫定は `*`） |
| 声が もも に似ない | 録音の質/量を上げる・エポックや学習データを見直す |
| マイクが使えない | サイトがHTTPSか・ブラウザのマイク権限を許可したか |
