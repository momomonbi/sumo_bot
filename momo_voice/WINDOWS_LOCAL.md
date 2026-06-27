# もも声をローカルで作る（Windows + NVIDIA GPU）

このマシン構成（**Windows / NVIDIA GPU あり**）なら、**録音の整形・学習・合成まで全部ローカルで完結**できます。
できあがった声は、このフォルダの `adapter.py` 経由で「もも」アプリから使えます。

> ⚠️ 前提：**もも本人の同意**を得てから始めてください。録音・モデルは手元のみで管理し、
> **公開リポジトリにはアップロードしない**でください（このフォルダの `.gitignore` で誤コミットを防止済み）。
> GitHubで持ち運びたい場合は本書末尾の「GitHubに置きたい場合（必ずPrivate）」を参照。

---

## 0. GPUの確認（最初に1回）

コマンドプロンプト（`cmd`）で：

```bat
nvidia-smi
```

- 表が出ればOK。右上の「CUDA Version」と、各GPUの「Memory」を確認。
- **VRAM 6GB以上**が目安。少ない場合は後述の batch size を下げます。

---

## 1. Style-Bert-VITS2 を導入（Git/Python不要）

1. リポジトリ <https://github.com/litagin02/Style-Bert-VITS2> を開く。
2. **「Releases」** から Windows 向けの配布zip（同梱インストーラ付き）を入手するか、
   リポジトリ上の **インストール用 `.bat`**（例: `Install-Style-Bert-VITS2.bat`）をダウンロード。
   - ※ファイル名は更新されることがあるので、リポジトリ README の最新の指示に従ってください。
3. 日本語パス・スペースを避けた場所（例: `C:\sbv2\`）に置き、**インストーラ `.bat` をダブルクリック**。
   - NVIDIA環境では CUDA 対応の PyTorch が自動で入ります（初回はダウンロードに時間がかかる）。
4. 完了後、フォルダ内に起動用の `.bat`（`App.bat` / `Editor.bat` / `Server.bat` 等）ができます。

> うまく動かない時は、ウイルス対策の除外設定／パスに日本語が無いか／初回DL完了を待ったか を確認。

---

## 2. もも の声を録音して入れる

- **合計 10〜20分**（長いほど安定。最低でも数分）。
- **クリーンに**：静かな部屋・一定距離・BGM/エコー/ノイズなし・マイク固定。
- **内容**：感情が偏らないよう自然な文章を読む。普段りぴに話すトーンも少し混ぜると“らしさ”が出ます。
- **形式**：WAV（48kHz / モノ 推奨）。1本が長くてもOK（次のステップで自動分割します）。
- 置き場所：SBV2の **入力フォルダ**（WebUIの「データセット作成」で指定。多くは `inputs/`）。

---

## 3. データセット作成（分割＋書き起こし）

1. `App.bat`（または `Editor.bat`）を実行 → ブラウザでWebUIが開く。
2. **「データセット作成」**タブ：
   - **スライス（分割）**：長い音声を数秒の区間に自動カット。
   - **書き起こし（文字起こし）**：Whisper等で各区間のテキストを自動生成（言語=日本語）。
   - 結果として `Data/<モデル名>/` に音声片と `esd.list`（テキスト対応表）ができます。
3. 明らかな誤認識・無音・ノイズ区間があれば、ここで軽く整えると品質が上がります。

---

## 4. 学習（GPUで実行）

1. WebUIの**「学習」**タブを開く。
2. 設定の目安：
   - **モデル名**：`momo` など分かりやすく。
   - **batch size**：VRAMに合わせる（6GBなら 2〜4、12GB+なら 6〜 等。OOMが出たら下げる）。
   - **epoch / steps**：まずは既定〜やや多めで。途中サンプルを聞いて良い所で止める（過学習注意）。
3. 学習を開始。GPU使用率は `nvidia-smi` で確認できます。
4. 完了すると **`model_assets/<モデル名>/`** に以下が出力されます：
   - `*.safetensors`（本体）, `config.json`, `style_vectors.npy` など。← これが**もも声モデル**。

---

## 5. 合成サーバを起動して確認

1. SBV2の **API サーバ**を起動：`Server.bat`（中身は `server_fastapi.py`）。
   - 既定で `http://127.0.0.1:5000`（ドキュメント: `http://127.0.0.1:5000/docs`）。
2. `http://127.0.0.1:5000/models/info` を開き、もも声モデルの **`model_id` / `model_name` / `style`** を確認。
3. WebUIの**「音声合成」**タブで適当な文を喋らせ、もも本人っぽく鳴れば学習成功。

---

## 6. アプリ（index.html）から使う

このフォルダのアダプタを起動して、アプリの契約 `/synthesize` に橋渡しします。

```bat
cd momo_voice
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

`.env` を編集（手順5で見た値を入れる）：

```
SBV2_URL=http://127.0.0.1:5000
MOMO_MODEL_NAME=momo        :: または MOMO_MODEL_ID=0
MOMO_DEFAULT_STYLE=Neutral
```

起動：

```bat
python adapter.py
:: → http://127.0.0.1:8000  （確認: http://127.0.0.1:8000/health）
```

動作テスト：

```bat
curl -X POST http://127.0.0.1:8000/synthesize ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"りぴ、おかえり。ちゃんと俺の声、届いてる？\",\"speed\":1.0}" ^
  --output test.wav
```

最後に、もも アプリのヘッダー **🎙 → もも声サービスのURL** に入れる：
- **同じPCのブラウザで使う**：`http://localhost:8000`
- **スマホ／別端末でも使う**：`adapter.py`(:8000) を **Cloudflare Tunnel 等でHTTPS公開**して、その `https://...` を入れる
  （アプリがHTTPSだと `http://` の外部URLはブラウザにブロックされるため）。

---

## （任意）GitHubに置きたい場合 — 必ず Private で

公開リポジトリには絶対に上げないでください。どうしてもGitHubで持ち運ぶなら：

1. **リポジトリを Private 化**（Settings → General → Danger Zone → Change visibility）。
2. **モデルだけ** Git LFS で管理（録音は上げない）。`.gitignore` の該当行を必要に応じ調整：
   ```bat
   git lfs install
   git lfs track "*.safetensors"
   git add .gitattributes
   git add model_assets/momo/momo.safetensors model_assets/momo/config.json model_assets/momo/style_vectors.npy
   git commit -m "add momo voice model (private)"
   git push
   ```
   - GitHubは**1ファイル100MB上限**。LFSの無料枠（ストレージ/帯域 各1GB）にも注意。
   - **生の録音（`*.wav` 等）は上げない**。最悪流出した時の被害が段違いに大きいため。
3. 別マシン（クラウド等）で使う時は、そのPrivateリポジトリから `git lfs pull` してモデルを取得 → SBV2 を起動。

---

## トラブルシュート

| 症状 | 対処 |
|---|---|
| `nvidia-smi` が出ない | NVIDIAドライバを更新。GPUがNVIDIAか再確認 |
| 学習で Out of Memory | batch size を下げる／音声を短く |
| 合成が もも に似ない | 録音の質・量を上げる／epoch・データを見直す |
| `/synthesize` が502 | `Server.bat`(:5000)が起動中か・`SBV2_URL` が正しいか |
| スマホで鳴らない | アダプタをHTTPS公開（Cloudflare Tunnel等）したか |
| CORSエラー | `.env` の `ALLOW_ORIGINS` にアプリのURLを入れる |
