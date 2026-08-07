# SVG図解の作例集

もも が会話中に描く SVG 図解の型。**このファイルはシステムプロンプトには入れていない**
（毎回の送信すべてに乗ってしまい、通信量と費用が跳ね上がるため）。
プロンプトに入っているのは共通ルールと型の名前だけで、実際の描き方はモデルに任せている。

ここは人が見るための資料。図が思ったように出ないときに、ここの作例と見比べて
プロンプト側の指示を足す、という使い方をする。

---

## 図（SVG）を書くときの共通ルール
- ```` ```svg ```` フェンスに直接書く。`viewBox` は必須、`width`/`height` は書かない。横幅は 560 を基準（表だけの図は 480〜520 でもよい）
- 背景は #0d0d0f。文字 #e8e8e2（弱い字は `fill-opacity` .5〜.75）、線 #c8f0a0 / #1d8f7b、うすい線 rgba(255,255,255,.16)、強調 #f0a35a、良い #7fd6a6、注意 #ff8b8b
- 明るい面（#7fd6a6 / #c8f0a0 / #f0a35a）の上に載せる文字は必ず `fill="#0d0d0f"`
- `font-size` は 13〜15、行の間隔は 22 以上。`text` は折り返さないので、複数行は `tspan` か `text` を分ける
- 日本語1文字の幅 ≒ font-size（14px なら14px）、英数字はその約0.55倍。書く前に右端の座標を必ず計算する
- 禁止: script / foreignObject / 画像 / リンク / on* / `style` 属性 / class / 外部CSS。色も字も `fill` `font-size` などの属性で書く
- `marker`（`url(#…)`）は消えるので、矢じりは `polygon` で描き、線は矢じりの手前で止める
- 見出しは左上（15px 太字 #c8f0a0）、いちばん言いたい一言は最下部に1行（#f0a35a）だけ置く

---

## くらべる

### 比較表（項目 × 2案）
2つの選択肢を複数の観点でならべる。値の列は中央そろえ、1列178pxなので全角12字まで。有利な側だけ #7fd6a6。

```svg
<svg viewBox="0 0 560 308" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ノートPC 2機種の比較表" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif">
  <text x="8" y="22" font-size="15" font-weight="700" fill="#c8f0a0">ノートPC 2機種をくらべる</text>

  <rect x="8" y="108" width="544" height="34" fill="rgba(255,255,255,0.03)"/>
  <rect x="8" y="176" width="544" height="34" fill="rgba(255,255,255,0.03)"/>
  <rect x="8" y="244" width="544" height="34" fill="rgba(255,255,255,0.03)"/>

  <line x1="8" y1="40" x2="552" y2="40" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="74" x2="552" y2="74" stroke="#1d8f7b" stroke-width="1.5"/>
  <line x1="8" y1="108" x2="552" y2="108" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="142" x2="552" y2="142" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="176" x2="552" y2="176" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="210" x2="552" y2="210" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="244" x2="552" y2="244" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="278" x2="552" y2="278" stroke="rgba(255,255,255,.16)"/>
  <line x1="196" y1="40" x2="196" y2="278" stroke="rgba(255,255,255,.16)"/>
  <line x1="374" y1="40" x2="374" y2="278" stroke="rgba(255,255,255,.16)"/>

  <text x="20" y="62" font-size="14" font-weight="600" fill="rgba(232,232,226,0.62)">くらべる点</text>
  <text x="285" y="62" font-size="15" font-weight="700" fill="#e8e8e2" text-anchor="middle">Air 13</text>
  <text x="463" y="62" font-size="15" font-weight="700" fill="#e8e8e2" text-anchor="middle">Pro 14</text>

  <text x="20" y="96" font-size="14" fill="rgba(232,232,226,0.75)">価格</text>
  <text x="285" y="96" font-size="14" fill="#7fd6a6" text-anchor="middle">16.4 万円</text>
  <text x="463" y="96" font-size="14" fill="#e8e8e2" text-anchor="middle">24.8 万円</text>

  <text x="20" y="130" font-size="14" fill="rgba(232,232,226,0.75)">重さ</text>
  <text x="285" y="130" font-size="14" fill="#7fd6a6" text-anchor="middle">1.24 kg</text>
  <text x="463" y="130" font-size="14" fill="#e8e8e2" text-anchor="middle">1.55 kg</text>

  <text x="20" y="164" font-size="14" fill="rgba(232,232,226,0.75)">電池のもち</text>
  <text x="285" y="164" font-size="14" fill="#7fd6a6" text-anchor="middle">約 18 時間</text>
  <text x="463" y="164" font-size="14" fill="#e8e8e2" text-anchor="middle">約 12 時間</text>

  <text x="20" y="198" font-size="14" fill="rgba(232,232,226,0.75)">画面</text>
  <text x="285" y="198" font-size="14" fill="#e8e8e2" text-anchor="middle">13.6 型 液晶</text>
  <text x="463" y="198" font-size="14" fill="#7fd6a6" text-anchor="middle">14.2 型 有機EL</text>

  <text x="20" y="232" font-size="14" fill="rgba(232,232,226,0.75)">処理の速さ</text>
  <text x="285" y="232" font-size="14" fill="#e8e8e2" text-anchor="middle">ふだん使いは十分</text>
  <text x="463" y="232" font-size="14" fill="#7fd6a6" text-anchor="middle">動画編集も快適</text>

  <text x="20" y="266" font-size="14" fill="rgba(232,232,226,0.75)">外部端子</text>
  <text x="285" y="266" font-size="14" fill="#e8e8e2" text-anchor="middle">USB-C ×2</text>
  <text x="463" y="266" font-size="14" fill="#7fd6a6" text-anchor="middle">USB-C ×3 + HDMI</text>

  <text x="8" y="298" font-size="13" fill="rgba(232,232,226,0.62)">緑 = そちらのほうが有利な点</text>
</svg>
```

### ○×表（できること対応表）
プランや機種ごとに「できる／できない」を一覧にする。記号列は幅100px、記号は16px、色に頼らず下に凡例を置く。

```svg
<svg viewBox="0 0 560 308" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="料金プラン3種の対応表" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif">
  <text x="8" y="22" font-size="15" font-weight="700" fill="#c8f0a0">プランごとに できること</text>

  <rect x="452" y="40" width="100" height="238" fill="rgba(240,163,90,0.07)"/>
  <rect x="8" y="108" width="544" height="34" fill="rgba(255,255,255,0.03)"/>
  <rect x="8" y="176" width="544" height="34" fill="rgba(255,255,255,0.03)"/>
  <rect x="8" y="244" width="544" height="34" fill="rgba(255,255,255,0.03)"/>

  <line x1="8" y1="40" x2="552" y2="40" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="74" x2="552" y2="74" stroke="#1d8f7b" stroke-width="1.5"/>
  <line x1="8" y1="108" x2="552" y2="108" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="142" x2="552" y2="142" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="176" x2="552" y2="176" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="210" x2="552" y2="210" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="244" x2="552" y2="244" stroke="rgba(255,255,255,.16)"/>
  <line x1="8" y1="278" x2="552" y2="278" stroke="rgba(255,255,255,.16)"/>
  <line x1="252" y1="40" x2="252" y2="278" stroke="rgba(255,255,255,.16)"/>
  <line x1="352" y1="40" x2="352" y2="278" stroke="rgba(255,255,255,.16)"/>
  <line x1="452" y1="40" x2="452" y2="278" stroke="rgba(255,255,255,.16)"/>

  <text x="20" y="62" font-size="14" font-weight="600" fill="rgba(232,232,226,0.62)">できること</text>
  <text x="302" y="62" font-size="15" font-weight="700" fill="#e8e8e2" text-anchor="middle">無料</text>
  <text x="402" y="62" font-size="15" font-weight="700" fill="#e8e8e2" text-anchor="middle">標準</text>
  <text x="502" y="62" font-size="15" font-weight="700" fill="#f0a35a" text-anchor="middle">上位</text>

  <text x="20" y="96" font-size="14" fill="rgba(232,232,226,0.75)">月額料金</text>
  <text x="302" y="96" font-size="14" fill="#e8e8e2" text-anchor="middle">0 円</text>
  <text x="402" y="96" font-size="14" fill="#e8e8e2" text-anchor="middle">480 円</text>
  <text x="502" y="96" font-size="14" fill="#e8e8e2" text-anchor="middle">980 円</text>

  <text x="20" y="130" font-size="14" fill="rgba(232,232,226,0.75)">記事を読む</text>
  <text x="302" y="131" font-size="16" fill="#7fd6a6" text-anchor="middle">○</text>
  <text x="402" y="131" font-size="16" fill="#7fd6a6" text-anchor="middle">○</text>
  <text x="502" y="131" font-size="16" fill="#7fd6a6" text-anchor="middle">○</text>

  <text x="20" y="164" font-size="14" fill="rgba(232,232,226,0.75)">広告を消す</text>
  <text x="302" y="165" font-size="16" fill="#ff8b8b" text-anchor="middle">×</text>
  <text x="402" y="165" font-size="16" fill="#7fd6a6" text-anchor="middle">○</text>
  <text x="502" y="165" font-size="16" fill="#7fd6a6" text-anchor="middle">○</text>

  <text x="20" y="198" font-size="14" fill="rgba(232,232,226,0.75)">オフライン保存</text>
  <text x="302" y="199" font-size="16" fill="#ff8b8b" text-anchor="middle">×</text>
  <text x="402" y="199" font-size="16" fill="#f0a35a" text-anchor="middle">△</text>
  <text x="502" y="199" font-size="16" fill="#7fd6a6" text-anchor="middle">○</text>

  <text x="20" y="232" font-size="14" fill="rgba(232,232,226,0.75)">高画質で見る</text>
  <text x="302" y="233" font-size="16" fill="#ff8b8b" text-anchor="middle">×</text>
  <text x="402" y="233" font-size="16" fill="#ff8b8b" text-anchor="middle">×</text>
  <text x="502" y="233" font-size="16" fill="#7fd6a6" text-anchor="middle">○</text>

  <text x="20" y="266" font-size="14" fill="rgba(232,232,226,0.75)">優先サポート</text>
  <text x="302" y="267" font-size="16" fill="#ff8b8b" text-anchor="middle">×</text>
  <text x="402" y="267" font-size="16" fill="#ff8b8b" text-anchor="middle">×</text>
  <text x="502" y="267" font-size="16" fill="#7fd6a6" text-anchor="middle">○</text>

  <text x="8" y="298" font-size="13" fill="rgba(232,232,226,0.62)"><tspan fill="#7fd6a6">○</tspan> 使える　<tspan fill="#f0a35a">△</tspan> 月5本まで　<tspan fill="#ff8b8b">×</tspan> 使えない</text>
</svg>
```

### メリット／デメリットの2列
ひとつの物事の良い面と悪い面を対にする。パネル内の1行は全角14字まで、行送り30。

```svg
<svg viewBox="0 0 560 234" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="在宅勤務のメリットとデメリット" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif">
  <text x="8" y="22" font-size="15" font-weight="700" fill="#c8f0a0">在宅勤務の いいところ・つらいところ</text>

  <rect x="8" y="38" width="268" height="184" rx="8" fill="none" stroke="rgba(255,255,255,.16)"/>
  <rect x="284" y="38" width="268" height="184" rx="8" fill="none" stroke="rgba(255,255,255,.16)"/>
  <path d="M16 38 H268 a8 8 0 0 1 8 8 V70 H8 V46 a8 8 0 0 1 8 -8 Z" fill="rgba(127,214,166,0.12)"/>
  <path d="M292 38 H544 a8 8 0 0 1 8 8 V70 H284 V46 a8 8 0 0 1 8 -8 Z" fill="rgba(255,139,139,0.12)"/>
  <line x1="8" y1="70" x2="276" y2="70" stroke="rgba(255,255,255,.16)"/>
  <line x1="284" y1="70" x2="552" y2="70" stroke="rgba(255,255,255,.16)"/>

  <text x="22" y="59" font-size="14" font-weight="700" fill="#7fd6a6">＋ いいところ</text>
  <text x="298" y="59" font-size="14" font-weight="700" fill="#ff8b8b">− つらいところ</text>

  <circle cx="26" cy="95" r="3" fill="#7fd6a6"/>
  <text x="38" y="100" font-size="14" fill="#e8e8e2">通勤時間がゼロになる</text>
  <circle cx="26" cy="125" r="3" fill="#7fd6a6"/>
  <text x="38" y="130" font-size="14" fill="#e8e8e2">まとまった時間が取れる</text>
  <circle cx="26" cy="155" r="3" fill="#7fd6a6"/>
  <text x="38" y="160" font-size="14" fill="#e8e8e2">昼食代と交通費が減る</text>
  <circle cx="26" cy="185" r="3" fill="#7fd6a6"/>
  <text x="38" y="190" font-size="14" fill="#e8e8e2">家事や育児と両立できる</text>

  <circle cx="302" cy="95" r="3" fill="#ff8b8b"/>
  <text x="314" y="100" font-size="14" fill="#e8e8e2">体を動かす機会が減る</text>
  <circle cx="302" cy="125" r="3" fill="#ff8b8b"/>
  <text x="314" y="130" font-size="14" fill="#e8e8e2">雑談から出る話がない</text>
  <circle cx="302" cy="155" r="3" fill="#ff8b8b"/>
  <text x="314" y="160" font-size="14" fill="#e8e8e2">仕事と休みの境が消える</text>
  <circle cx="302" cy="185" r="3" fill="#ff8b8b"/>
  <text x="314" y="190" font-size="14" fill="#e8e8e2">光熱費と通信費は自腹</text>
</svg>
```

### 2軸4象限マトリクス
2つの軸で対象を4つに仕分ける。軸ラベルは回転せず枠の外に横書き、1象限は見出し1行＋本文2行（全角13字）まで。

```svg
<svg viewBox="0 0 560 338" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="やることを大事さと急ぎで仕分ける4象限" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif">
  <text x="8" y="22" font-size="15" font-weight="700" fill="#c8f0a0">やることを 大事さ × 急ぎ で仕分ける</text>

  <rect x="100" y="60" width="220" height="120" fill="rgba(127,214,166,0.07)"/>
  <rect x="320" y="60" width="220" height="120" fill="rgba(255,139,139,0.07)"/>
  <rect x="100" y="180" width="220" height="120" fill="rgba(255,255,255,0.03)"/>
  <rect x="320" y="180" width="220" height="120" fill="rgba(240,163,90,0.06)"/>
  <rect x="100" y="60" width="440" height="240" fill="none" stroke="rgba(255,255,255,.16)"/>
  <line x1="320" y1="60" x2="320" y2="300" stroke="#1d8f7b"/>
  <line x1="100" y1="180" x2="540" y2="180" stroke="#1d8f7b"/>

  <text x="52" y="78" font-size="14" fill="#e8e8e2" text-anchor="middle">大事</text>
  <text x="52" y="296" font-size="13" fill="rgba(232,232,226,0.62)" text-anchor="middle">大事でない</text>
  <text x="210" y="324" font-size="14" fill="#e8e8e2" text-anchor="middle">急がない</text>
  <text x="430" y="324" font-size="14" fill="#e8e8e2" text-anchor="middle">急ぐ</text>

  <text x="116" y="90" font-size="14" font-weight="700" fill="#7fd6a6">予定に入れてやる</text>
  <text x="116" y="122" font-size="13" fill="rgba(232,232,226,0.62)">・資格の勉強</text>
  <text x="116" y="148" font-size="13" fill="rgba(232,232,226,0.62)">・健康診断の予約</text>

  <text x="336" y="90" font-size="14" font-weight="700" fill="#ff8b8b">今すぐやる</text>
  <text x="336" y="122" font-size="13" fill="rgba(232,232,226,0.62)">・本番の障害対応</text>
  <text x="336" y="148" font-size="13" fill="rgba(232,232,226,0.62)">・今日締切の申請</text>

  <text x="116" y="210" font-size="14" font-weight="700" fill="rgba(232,232,226,0.5)">やめる</text>
  <text x="116" y="242" font-size="13" fill="rgba(232,232,226,0.62)">・惰性で続く定例</text>
  <text x="116" y="268" font-size="13" fill="rgba(232,232,226,0.62)">・目的のないSNS</text>

  <text x="336" y="210" font-size="14" font-weight="700" fill="#f0a35a">人にたのむ</text>
  <text x="336" y="242" font-size="13" fill="rgba(232,232,226,0.62)">・定型の問い合わせ</text>
  <text x="336" y="268" font-size="13" fill="rgba(232,232,226,0.62)">・数字の転記作業</text>
</svg>
```

### 評価マトリクス（スコア網掛け）
3つ以上の候補を複数の基準で採点する。セルは点数で濃さを変える（5→緑.30 / 4→緑.20 / 3→白.08 / 2→赤.18 / 1→赤.28）、勝った行だけ左端にバー。

```svg
<svg viewBox="0 0 560 238" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="引っ越し先候補3つの評価マトリクス" font-family="system-ui,-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif">
  <text x="8" y="22" font-size="15" font-weight="700" fill="#c8f0a0">引っ越し先の候補を 4つの基準で採点</text>

  <line x1="8" y1="70" x2="552" y2="70" stroke="rgba(255,255,255,.16)"/>
  <line x1="486" y1="40" x2="486" y2="202" stroke="rgba(255,255,255,.16)"/>

  <text x="192" y="61" font-size="13" fill="rgba(232,232,226,0.62)" text-anchor="middle">家賃</text>
  <text x="276" y="61" font-size="13" fill="rgba(232,232,226,0.62)" text-anchor="middle">通勤</text>
  <text x="360" y="61" font-size="13" fill="rgba(232,232,226,0.62)" text-anchor="middle">買い物</text>
  <text x="444" y="61" font-size="13" fill="rgba(232,232,226,0.62)" text-anchor="middle">静かさ</text>
  <text x="519" y="61" font-size="13" fill="rgba(232,232,226,0.62)" text-anchor="middle">合計</text>

  <text x="18" y="98" font-size="14" fill="#e8e8e2">A 駅前</text>
  <rect x="154" y="75" width="76" height="34" rx="4" fill="rgba(255,139,139,0.18)"/>
  <text x="192" y="98" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">2</text>
  <rect x="238" y="75" width="76" height="34" rx="4" fill="rgba(127,214,166,0.30)"/>
  <text x="276" y="98" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">5</text>
  <rect x="322" y="75" width="76" height="34" rx="4" fill="rgba(127,214,166,0.30)"/>
  <text x="360" y="98" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">5</text>
  <rect x="406" y="75" width="76" height="34" rx="4" fill="rgba(255,139,139,0.18)"/>
  <text x="444" y="98" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">2</text>
  <text x="519" y="98" font-size="15" font-weight="700" fill="#e8e8e2" text-anchor="middle">14</text>

  <rect x="8" y="119" width="3" height="34" fill="#f0a35a"/>
  <text x="18" y="142" font-size="14" fill="#e8e8e2">B 川ぞい</text>
  <rect x="154" y="119" width="76" height="34" rx="4" fill="rgba(127,214,166,0.20)"/>
  <text x="192" y="142" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">4</text>
  <rect x="238" y="119" width="76" height="34" rx="4" fill="rgba(127,214,166,0.20)"/>
  <text x="276" y="142" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">4</text>
  <rect x="322" y="119" width="76" height="34" rx="4" fill="rgba(127,214,166,0.20)"/>
  <text x="360" y="142" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">4</text>
  <rect x="406" y="119" width="76" height="34" rx="4" fill="rgba(127,214,166,0.20)"/>
  <text x="444" y="142" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">4</text>
  <text x="519" y="142" font-size="15" font-weight="700" fill="#f0a35a" text-anchor="middle">16</text>

  <text x="18" y="186" font-size="14" fill="#e8e8e2">C 郊外</text>
  <rect x="154" y="163" width="76" height="34" rx="4" fill="rgba(127,214,166,0.30)"/>
  <text x="192" y="186" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">5</text>
  <rect x="238" y="163" width="76" height="34" rx="4" fill="rgba(255,139,139,0.18)"/>
  <text x="276" y="186" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">2</text>
  <rect x="322" y="163" width="76" height="34" rx="4" fill="rgba(255,139,139,0.18)"/>
  <text x="360" y="186" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">2</text>
  <rect x="406" y="163" width="76" height="34" rx="4" fill="rgba(127,214,166,0.30)"/>
  <text x="444" y="186" font-size="15" font-weight="600" fill="#e8e8e2" text-anchor="middle">5</text>
  <text x="519" y="186" font-size="15" font-weight="700" fill="#e8e8e2" text-anchor="middle">14</text>

  <text x="8" y="224" font-size="13" fill="rgba(232,232,226,0.62)">5 = とても良い　1 = よくない　合計が高いほど有力</text>
</svg>
```

---

## 手順・流れ

### 分岐フローチャート（縦）
条件で答えが変わるとき。矢じりは polygon、分岐ラベルは横線のすぐ上に 13px で置く。

```svg
<svg viewBox="0 0 560 302" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="洗濯物を外に干すか決める流れ図"><title>洗濯物を外に干すか決める</title><rect x="170" y="14" width="220" height="42" rx="8" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.16)"/><text x="280" y="40" font-size="15" text-anchor="middle" fill="#e8e8e2">洗濯物を干したい</text><line x1="280" y1="58" x2="280" y2="68" stroke="#c8f0a0" stroke-opacity="0.55" stroke-width="1.6"/><polygon points="275,68 285,68 280,76" fill="#c8f0a0" fill-opacity="0.55"/><rect x="170" y="80" width="220" height="42" rx="8" fill="rgba(240,163,90,0.10)" stroke="#f0a35a" stroke-opacity="0.55"/><text x="280" y="106" font-size="15" text-anchor="middle" fill="#e8e8e2">雨の予報は？</text><line x1="280" y1="124" x2="280" y2="142" stroke="#c8f0a0" stroke-opacity="0.55" stroke-width="1.6"/><line x1="145" y1="142" x2="415" y2="142" stroke="#c8f0a0" stroke-opacity="0.55" stroke-width="1.6"/><line x1="145" y1="142" x2="145" y2="164" stroke="#c8f0a0" stroke-opacity="0.55" stroke-width="1.6"/><line x1="415" y1="142" x2="415" y2="164" stroke="#c8f0a0" stroke-opacity="0.55" stroke-width="1.6"/><polygon points="140,164 150,164 145,172" fill="#c8f0a0" fill-opacity="0.55"/><polygon points="410,164 420,164 415,172" fill="#c8f0a0" fill-opacity="0.55"/><text x="205" y="136" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.6">いいえ</text><text x="355" y="136" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.6">はい</text><rect x="28" y="176" width="234" height="44" rx="8" fill="rgba(127,214,166,0.10)" stroke="#7fd6a6" stroke-opacity="0.5"/><text x="145" y="203" font-size="15" text-anchor="middle" fill="#e8e8e2">そのまま外に干す</text><rect x="298" y="176" width="234" height="44" rx="8" fill="rgba(240,163,90,0.10)" stroke="#f0a35a" stroke-opacity="0.5"/><text x="415" y="203" font-size="15" text-anchor="middle" fill="#e8e8e2">部屋干しに切りかえる</text><line x1="145" y1="222" x2="145" y2="234" stroke="#c8f0a0" stroke-opacity="0.55" stroke-width="1.6"/><line x1="415" y1="222" x2="415" y2="234" stroke="#c8f0a0" stroke-opacity="0.55" stroke-width="1.6"/><polygon points="140,234 150,234 145,242" fill="#c8f0a0" fill-opacity="0.55"/><polygon points="410,234 420,234 415,242" fill="#c8f0a0" fill-opacity="0.55"/><rect x="28" y="246" width="234" height="42" rx="8" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.16)"/><text x="145" y="272" font-size="14" text-anchor="middle" fill="#e8e8e2">15時までに取りこむ</text><rect x="298" y="246" width="234" height="42" rx="8" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.16)"/><text x="415" y="272" font-size="14" text-anchor="middle" fill="#e8e8e2">サーキュレーターを回す</text></svg>
```

### 番号つきステップ（縦）
順番どおりにやる作業。1段は見出し1行＋補足1行、段の間隔は72、補足は全角20字まで。

```svg
<svg viewBox="0 0 560 366" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="カレーの作り方 5ステップ"><title>カレーの手順</title><line x1="34" y1="51" x2="34" y2="91" stroke="#c8f0a0" stroke-opacity="0.35" stroke-width="1.6"/><line x1="34" y1="123" x2="34" y2="163" stroke="#c8f0a0" stroke-opacity="0.35" stroke-width="1.6"/><line x1="34" y1="195" x2="34" y2="235" stroke="#c8f0a0" stroke-opacity="0.35" stroke-width="1.6"/><line x1="34" y1="267" x2="34" y2="307" stroke="#c8f0a0" stroke-opacity="0.35" stroke-width="1.6"/><circle cx="34" cy="35" r="15" fill="rgba(200,240,160,0.10)" stroke="#c8f0a0" stroke-opacity="0.6"/><text x="34" y="40" font-size="14" text-anchor="middle" fill="#c8f0a0">1</text><text x="64" y="40" font-size="15" fill="#e8e8e2">材料を切る</text><text x="64" y="64" font-size="13" fill="#e8e8e2" fill-opacity="0.55">玉ねぎ・にんじん・じゃがいもを一口大に</text><circle cx="34" cy="107" r="15" fill="rgba(200,240,160,0.10)" stroke="#c8f0a0" stroke-opacity="0.6"/><text x="34" y="112" font-size="14" text-anchor="middle" fill="#c8f0a0">2</text><text x="64" y="112" font-size="15" fill="#e8e8e2">肉を炒める</text><text x="64" y="136" font-size="13" fill="#e8e8e2" fill-opacity="0.55">油をひいて中火。色が変わるまで</text><circle cx="34" cy="179" r="15" fill="rgba(200,240,160,0.10)" stroke="#c8f0a0" stroke-opacity="0.6"/><text x="34" y="184" font-size="14" text-anchor="middle" fill="#c8f0a0">3</text><text x="64" y="184" font-size="15" fill="#e8e8e2">野菜を加えて炒める</text><text x="64" y="208" font-size="13" fill="#e8e8e2" fill-opacity="0.55">玉ねぎが透きとおるまで5分ほど</text><circle cx="34" cy="251" r="15" fill="rgba(200,240,160,0.10)" stroke="#c8f0a0" stroke-opacity="0.6"/><text x="34" y="256" font-size="14" text-anchor="middle" fill="#c8f0a0">4</text><text x="64" y="256" font-size="15" fill="#e8e8e2">水を入れて煮こむ</text><text x="64" y="280" font-size="13" fill="#e8e8e2" fill-opacity="0.55">アクを取りながら弱火で20分</text><circle cx="34" cy="323" r="15" fill="rgba(240,163,90,0.12)" stroke="#f0a35a" stroke-opacity="0.7"/><text x="34" y="328" font-size="14" text-anchor="middle" fill="#f0a35a">5</text><text x="64" y="328" font-size="15" fill="#e8e8e2">ルウを溶かす</text><text x="64" y="352" font-size="13" fill="#f0a35a" fill-opacity="0.85">火を止めてから入れる。とろみが出るまで10分</text></svg>
```

### 進み具合つき手順（済／いま／これから）
途中まで終わっている手続き。チェックは path、右端の状態ラベルは x=548 の text-anchor="end"。

```svg
<svg viewBox="0 0 560 350" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="確定申告の進み具合"><title>確定申告の進み具合</title><line x1="30" y1="46" x2="30" y2="88" stroke="#7fd6a6" stroke-opacity="0.5" stroke-width="1.6"/><line x1="30" y1="114" x2="30" y2="156" stroke="#7fd6a6" stroke-opacity="0.5" stroke-width="1.6"/><line x1="30" y1="182" x2="30" y2="224" stroke="rgba(255,255,255,0.16)" stroke-width="1.6"/><line x1="30" y1="250" x2="30" y2="292" stroke="rgba(255,255,255,0.16)" stroke-width="1.6"/><circle cx="30" cy="33" r="11" fill="#7fd6a6"/><path d="M25 33 L28.6 36.6 L35 30" fill="none" stroke="#0d0d0f" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><text x="54" y="38" font-size="15" fill="#e8e8e2" fill-opacity="0.5">必要書類をあつめる</text><text x="54" y="62" font-size="13" fill="#e8e8e2" fill-opacity="0.4">源泉徴収票・医療費の領収書</text><text x="548" y="38" font-size="13" text-anchor="end" fill="#7fd6a6">済</text><circle cx="30" cy="101" r="11" fill="#7fd6a6"/><path d="M25 101 L28.6 104.6 L35 98" fill="none" stroke="#0d0d0f" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><text x="54" y="106" font-size="15" fill="#e8e8e2" fill-opacity="0.5">マイナンバーカードを用意</text><text x="54" y="130" font-size="13" fill="#e8e8e2" fill-opacity="0.4">読み取りアプリも入れる</text><text x="548" y="106" font-size="13" text-anchor="end" fill="#7fd6a6">済</text><circle cx="30" cy="169" r="11" fill="rgba(240,163,90,0.12)" stroke="#f0a35a" stroke-width="2.5"/><circle cx="30" cy="169" r="4" fill="#f0a35a"/><text x="54" y="174" font-size="15" fill="#e8e8e2">e-Taxで入力する</text><text x="54" y="198" font-size="13" fill="#e8e8e2" fill-opacity="0.7">収入と控除を順に入れる</text><text x="548" y="174" font-size="13" text-anchor="end" fill="#f0a35a">いま</text><circle cx="30" cy="237" r="11" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="1.6"/><text x="54" y="242" font-size="15" fill="#e8e8e2" fill-opacity="0.85">内容を確認して送信</text><text x="54" y="266" font-size="13" fill="#e8e8e2" fill-opacity="0.5">送信後に受付番号が出る</text><text x="548" y="242" font-size="13" text-anchor="end" fill="#e8e8e2" fill-opacity="0.4">これから</text><circle cx="30" cy="305" r="11" fill="none" stroke="rgba(255,255,255,0.22)" stroke-width="1.6"/><text x="54" y="310" font-size="15" fill="#e8e8e2" fill-opacity="0.85">納付する</text><text x="54" y="334" font-size="13" fill="#e8e8e2" fill-opacity="0.5">口座振替なら4月下旬に引き落とし</text><text x="548" y="310" font-size="13" text-anchor="end" fill="#e8e8e2" fill-opacity="0.4">これから</text></svg>
```

### 横タイムライン
締切から逆算する予定。節目は5個まで、ラベルは全角6字まで、両端は x=48 と x=518 の内側。

```svg
<svg viewBox="0 0 560 100" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="引っ越しまでの流れ 横タイムライン"><title>引っ越しまでの流れ</title><line x1="24" y1="58" x2="536" y2="58" stroke="rgba(255,255,255,0.16)" stroke-width="1.5"/><text x="48" y="30" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.55">2か月前</text><circle cx="48" cy="58" r="5.5" fill="#c8f0a0"/><text x="48" y="88" font-size="14" text-anchor="middle" fill="#e8e8e2">物件を決める</text><text x="166" y="30" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.55">1か月前</text><circle cx="166" cy="58" r="5.5" fill="#c8f0a0"/><text x="166" y="88" font-size="14" text-anchor="middle" fill="#e8e8e2">解約を連絡</text><text x="283" y="30" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.55">2週間前</text><circle cx="283" cy="58" r="5.5" fill="#c8f0a0"/><text x="283" y="88" font-size="14" text-anchor="middle" fill="#e8e8e2">荷造り開始</text><text x="401" y="30" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.55">前日</text><circle cx="401" cy="58" r="5.5" fill="#c8f0a0"/><text x="401" y="88" font-size="14" text-anchor="middle" fill="#e8e8e2">冷蔵庫を空に</text><text x="518" y="30" font-size="13" text-anchor="middle" fill="#f0a35a">当日</text><circle cx="518" cy="58" r="7" fill="#f0a35a"/><text x="518" y="88" font-size="14" text-anchor="middle" fill="#e8e8e2">立ち会い</text></svg>
```

### ガントふう予定表
複数の作業が重なりながら進むとき。左の作業名は全角7字まで、列は4つまで、バーの中に文字は入れない。

```svg
<svg viewBox="0 0 560 258" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="引っ越し準備の4週間 予定表"><title>引っ越し準備の4週間</title><text x="201" y="22" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.55">1週目</text><text x="299" y="22" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.55">2週目</text><text x="397" y="22" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.55">3週目</text><text x="495" y="22" font-size="13" text-anchor="middle" fill="#e8e8e2" fill-opacity="0.55">4週目</text><line x1="152" y1="30" x2="544" y2="30" stroke="rgba(255,255,255,0.16)"/><line x1="152" y1="30" x2="152" y2="220" stroke="rgba(255,255,255,0.10)"/><line x1="250" y1="30" x2="250" y2="220" stroke="rgba(255,255,255,0.10)"/><line x1="348" y1="30" x2="348" y2="220" stroke="rgba(255,255,255,0.10)"/><line x1="446" y1="30" x2="446" y2="220" stroke="rgba(255,255,255,0.10)"/><line x1="544" y1="30" x2="544" y2="220" stroke="rgba(255,255,255,0.10)"/><text x="6" y="57" font-size="13" fill="#e8e8e2">物件さがし</text><rect x="155" y="42" width="190" height="20" rx="5" fill="#1d8f7b"/><text x="6" y="95" font-size="13" fill="#e8e8e2">解約の連絡</text><rect x="253" y="80" width="92" height="20" rx="5" fill="#1d8f7b"/><text x="6" y="133" font-size="13" fill="#e8e8e2">不用品の処分</text><rect x="253" y="118" width="190" height="20" rx="5" fill="#1d8f7b"/><text x="6" y="171" font-size="13" fill="#e8e8e2">荷造り</text><rect x="351" y="156" width="190" height="20" rx="5" fill="#f0a35a" fill-opacity="0.85"/><text x="6" y="209" font-size="13" fill="#e8e8e2">住所変更</text><rect x="449" y="194" width="92" height="20" rx="5" fill="#1d8f7b"/><line x1="299" y1="30" x2="299" y2="226" stroke="#ff8b8b" stroke-width="1.4" stroke-dasharray="4 4" stroke-opacity="0.8"/><text x="299" y="244" font-size="13" text-anchor="middle" fill="#ff8b8b">今日</text></svg>
```

---

## 量・割合

### 縦棒グラフ（推移）
日ごと・月ごとの増減。棒は7本まで、値のラベルは棒の上端 −7px、いちばん高い棒だけ #f0a35a。

```svg
<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="今週の勉強時間の棒グラフ">
  <text x="8" y="20" fill="#e8e8e2" font-size="15" font-weight="700">今週の勉強時間（分）</text>
  <line x1="52" y1="60" x2="544" y2="60" stroke="rgba(255,255,255,.12)" stroke-width="1"/>
  <line x1="52" y1="146" x2="544" y2="146" stroke="rgba(255,255,255,.12)" stroke-width="1"/>
  <line x1="52" y1="232" x2="544" y2="232" stroke="rgba(255,255,255,.28)" stroke-width="1"/>
  <text x="44" y="65" fill="#e8e8e2" fill-opacity=".55" font-size="14" text-anchor="end">120</text>
  <text x="44" y="151" fill="#e8e8e2" fill-opacity=".55" font-size="14" text-anchor="end">60</text>
  <text x="44" y="237" fill="#e8e8e2" fill-opacity=".55" font-size="14" text-anchor="end">0</text>
  <rect x="72" y="175" width="34" height="57" rx="3" fill="#1d8f7b"/>
  <rect x="142" y="139" width="34" height="93" rx="3" fill="#1d8f7b"/>
  <rect x="212" y="189" width="34" height="43" rx="3" fill="#1d8f7b"/>
  <rect x="282" y="117" width="34" height="115" rx="3" fill="#1d8f7b"/>
  <rect x="352" y="153" width="34" height="79" rx="3" fill="#1d8f7b"/>
  <rect x="422" y="74" width="34" height="158" rx="3" fill="#f0a35a"/>
  <rect x="492" y="96" width="34" height="136" rx="3" fill="#1d8f7b"/>
  <text x="89" y="168" fill="#e8e8e2" font-size="14" text-anchor="middle">40</text>
  <text x="159" y="132" fill="#e8e8e2" font-size="14" text-anchor="middle">65</text>
  <text x="229" y="182" fill="#e8e8e2" font-size="14" text-anchor="middle">30</text>
  <text x="299" y="110" fill="#e8e8e2" font-size="14" text-anchor="middle">80</text>
  <text x="369" y="146" fill="#e8e8e2" font-size="14" text-anchor="middle">55</text>
  <text x="439" y="67" fill="#f0a35a" font-size="14" text-anchor="middle">110</text>
  <text x="509" y="89" fill="#e8e8e2" font-size="14" text-anchor="middle">95</text>
  <text x="89" y="252" fill="#e8e8e2" font-size="14" text-anchor="middle">月</text>
  <text x="159" y="252" fill="#e8e8e2" font-size="14" text-anchor="middle">火</text>
  <text x="229" y="252" fill="#e8e8e2" font-size="14" text-anchor="middle">水</text>
  <text x="299" y="252" fill="#e8e8e2" font-size="14" text-anchor="middle">木</text>
  <text x="369" y="252" fill="#e8e8e2" font-size="14" text-anchor="middle">金</text>
  <text x="439" y="252" fill="#f0a35a" font-size="14" text-anchor="middle">土</text>
  <text x="509" y="252" fill="#e8e8e2" font-size="14" text-anchor="middle">日</text>
  <text x="8" y="282" fill="#f0a35a" font-size="14">土曜がいちばん多い（110分）</text>
</svg>
```

### 横棒ランキング
多い順にならべる。項目名は x=8 から全角3字、バーは x=120 から最大350px、値は x=478 から。

```svg
<svg viewBox="0 0 560 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="先月の支出の内訳ランキング">
  <text x="8" y="20" fill="#e8e8e2" font-size="15" font-weight="700">先月の支出 おおい順</text>
  <rect x="120" y="55" width="350" height="22" rx="4" fill="rgba(255,255,255,.06)"/>
  <rect x="120" y="95" width="350" height="22" rx="4" fill="rgba(255,255,255,.06)"/>
  <rect x="120" y="135" width="350" height="22" rx="4" fill="rgba(255,255,255,.06)"/>
  <rect x="120" y="175" width="350" height="22" rx="4" fill="rgba(255,255,255,.06)"/>
  <rect x="120" y="215" width="350" height="22" rx="4" fill="rgba(255,255,255,.06)"/>
  <rect x="120" y="55" width="350" height="22" rx="4" fill="#f0a35a"/>
  <rect x="120" y="95" width="215" height="22" rx="4" fill="#1d8f7b"/>
  <rect x="120" y="135" width="79" height="22" rx="4" fill="#1d8f7b"/>
  <rect x="120" y="175" width="55" height="22" rx="4" fill="#1d8f7b"/>
  <rect x="120" y="215" width="41" height="22" rx="4" fill="#1d8f7b"/>
  <text x="8" y="71" fill="#e8e8e2" font-size="14">家賃</text>
  <text x="8" y="111" fill="#e8e8e2" font-size="14">食費</text>
  <text x="8" y="151" fill="#e8e8e2" font-size="14">光熱費</text>
  <text x="8" y="191" fill="#e8e8e2" font-size="14">通信費</text>
  <text x="8" y="231" fill="#e8e8e2" font-size="14">日用品</text>
  <text x="478" y="71" fill="#f0a35a" font-size="14">62,000円</text>
  <text x="478" y="111" fill="#e8e8e2" font-size="14">38,000円</text>
  <text x="478" y="151" fill="#e8e8e2" font-size="14">14,000円</text>
  <text x="478" y="191" fill="#e8e8e2" font-size="14">9,800円</text>
  <text x="478" y="231" fill="#e8e8e2" font-size="14">7,200円</text>
  <line x1="8" y1="248" x2="552" y2="248" stroke="rgba(255,255,255,.16)" stroke-width="1"/>
  <text x="8" y="268" fill="#e8e8e2" fill-opacity=".6" font-size="14">合計 131,000円　家賃が全体の半分ちかく</text>
</svg>
```

### 積み上げ帯＋内訳表
全体・割合・実額を同時に見せる。帯は幅532を割合で分けて合計を検算し、帯の中の文字は明るい色の上にだけ #0d0d0f で置く。

```svg
<svg viewBox="0 0 560 258" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="今月の食費の内訳">
  <text x="14" y="22" font-size="14" font-weight="600" fill="#c8f0a0">今月の食費 42,000円の内訳</text>
  <text x="546" y="22" font-size="13" text-anchor="end" fill="#ff8b8b">先月より +3,200円</text>

  <rect x="14" y="36" width="266" height="26" fill="#7fd6a6"/>
  <rect x="280" y="36" width="106" height="26" fill="#1d8f7b"/>
  <rect x="386" y="36" width="64" height="26" fill="#c8f0a0"/>
  <rect x="450" y="36" width="53" height="26" fill="#f0a35a"/>
  <rect x="503" y="36" width="43" height="26" fill="rgba(255,255,255,.28)"/>
  <text x="147" y="54" font-size="13" text-anchor="middle" fill="#0d0d0f">スーパー 50%</text>

  <rect x="14" y="86" width="12" height="12" fill="#7fd6a6"/>
  <text x="36" y="96" font-size="14" fill="#e8e8e2">スーパーの買い出し</text>
  <text x="440" y="96" font-size="14" text-anchor="end" fill="#e8e8e2">21,000円</text>
  <text x="546" y="96" font-size="13" text-anchor="end" fill="rgba(232,232,226,.6)">50%</text>

  <rect x="14" y="114" width="12" height="12" fill="#1d8f7b"/>
  <text x="36" y="124" font-size="14" fill="#e8e8e2">外食</text>
  <text x="440" y="124" font-size="14" text-anchor="end" fill="#e8e8e2">8,400円</text>
  <text x="546" y="124" font-size="13" text-anchor="end" fill="rgba(232,232,226,.6)">20%</text>

  <rect x="14" y="142" width="12" height="12" fill="#c8f0a0"/>
  <text x="36" y="152" font-size="14" fill="#e8e8e2">コンビニ</text>
  <text x="440" y="152" font-size="14" text-anchor="end" fill="#e8e8e2">5,040円</text>
  <text x="546" y="152" font-size="13" text-anchor="end" fill="rgba(232,232,226,.6)">12%</text>

  <rect x="14" y="170" width="12" height="12" fill="#f0a35a"/>
  <text x="36" y="180" font-size="14" fill="#f0a35a">おやつ・飲みもの</text>
  <text x="440" y="180" font-size="14" text-anchor="end" fill="#f0a35a">4,200円</text>
  <text x="546" y="180" font-size="13" text-anchor="end" fill="#f0a35a">10%</text>

  <rect x="14" y="198" width="12" height="12" fill="rgba(255,255,255,.28)"/>
  <text x="36" y="208" font-size="14" fill="#e8e8e2">その他</text>
  <text x="440" y="208" font-size="14" text-anchor="end" fill="#e8e8e2">3,360円</text>
  <text x="546" y="208" font-size="13" text-anchor="end" fill="rgba(232,232,226,.6)">8%</text>

  <line x1="14" y1="224" x2="546" y2="224" stroke="#1d8f7b" stroke-width="1"/>
  <text x="36" y="246" font-size="14" font-weight="600" fill="#e8e8e2">合計</text>
  <text x="440" y="246" font-size="14" font-weight="600" text-anchor="end" fill="#e8e8e2">42,000円</text>
  <text x="546" y="246" font-size="13" text-anchor="end" fill="rgba(232,232,226,.6)">100%</text>
</svg>
```

### 進捗バー（複数）
いくつかのタスクの進みぐあいを並べる。塗りの幅 = 544 × 割合、うすい下地を必ず先に置き、行のピッチは46。

```svg
<svg viewBox="0 0 560 248" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="引っ越し準備の進みぐあい">
  <text x="8" y="20" fill="#e8e8e2" font-size="15" font-weight="700">引っ越し準備の進みぐあい</text>
  <text x="8" y="56" fill="#e8e8e2" font-size="14">荷物の梱包</text>
  <text x="552" y="56" fill="#e8e8e2" font-size="14" text-anchor="end">80%</text>
  <rect x="8" y="66" width="544" height="10" rx="5" fill="rgba(255,255,255,.10)"/>
  <rect x="8" y="66" width="435" height="10" rx="5" fill="#c8f0a0"/>
  <text x="8" y="102" fill="#e8e8e2" font-size="14">住所変更の手続き</text>
  <text x="552" y="102" fill="#e8e8e2" font-size="14" text-anchor="end">45%</text>
  <rect x="8" y="112" width="544" height="10" rx="5" fill="rgba(255,255,255,.10)"/>
  <rect x="8" y="112" width="245" height="10" rx="5" fill="#c8f0a0"/>
  <text x="8" y="148" fill="#e8e8e2" font-size="14">不用品の処分</text>
  <text x="552" y="148" fill="#7fd6a6" font-size="14" text-anchor="end">100%</text>
  <rect x="8" y="158" width="544" height="10" rx="5" fill="rgba(255,255,255,.10)"/>
  <rect x="8" y="158" width="544" height="10" rx="5" fill="#7fd6a6"/>
  <text x="8" y="194" fill="#e8e8e2" font-size="14">ネット回線の移転</text>
  <text x="552" y="194" fill="#f0a35a" font-size="14" text-anchor="end">20%</text>
  <rect x="8" y="204" width="544" height="10" rx="5" fill="rgba(255,255,255,.10)"/>
  <rect x="8" y="204" width="109" height="10" rx="5" fill="#f0a35a"/>
  <text x="8" y="238" fill="#e8e8e2" fill-opacity=".6" font-size="14">4つ平均で 61%　ネット回線がいちばん遅れている</text>
</svg>
```

---

## 関係・構造

### 関係図（矢印つき・循環）
モノ・お金・情報が誰から誰へ動くか。登場人物3〜4で一周する話に強い。矢じりは polygon、線は矢じりの手前11pxで止める。

```svg
<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif" role="img" aria-label="フリマアプリ 出品から入金までの関係図">
  <text x="8" y="22" font-size="15" fill="#e8e8e2">フリマアプリ　出品から入金まで</text>

  <rect x="40" y="56" width="150" height="54" rx="8" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="115" y="79" font-size="14" fill="#e8e8e2" text-anchor="middle">出品者（あなた）</text>
  <text x="115" y="99" font-size="12" fill="#c8f0a0" text-anchor="middle">写真を撮って出す</text>

  <rect x="370" y="56" width="150" height="54" rx="8" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="445" y="79" font-size="14" fill="#e8e8e2" text-anchor="middle">フリマアプリ</text>
  <text x="445" y="99" font-size="12" fill="#c8f0a0" text-anchor="middle">運営・お金あずかり</text>

  <rect x="40" y="216" width="150" height="54" rx="8" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="115" y="239" font-size="14" fill="#e8e8e2" text-anchor="middle">配送業者</text>
  <text x="115" y="259" font-size="12" fill="#c8f0a0" text-anchor="middle">コンビニで受付</text>

  <rect x="370" y="216" width="150" height="54" rx="8" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="445" y="239" font-size="14" fill="#e8e8e2" text-anchor="middle">購入者</text>
  <text x="445" y="259" font-size="12" fill="#c8f0a0" text-anchor="middle">買ってくれた人</text>

  <line x1="115" y1="110" x2="115" y2="205" stroke="#1d8f7b" stroke-width="1.6"/>
  <polygon points="115,216 109,204 121,204" fill="#1d8f7b"/>
  <text x="126" y="150" font-size="13" fill="#e8e8e2">品物を</text>
  <text x="126" y="172" font-size="13" fill="#e8e8e2">発送</text>

  <line x1="190" y1="243" x2="359" y2="243" stroke="#1d8f7b" stroke-width="1.6"/>
  <polygon points="370,243 358,237 358,249" fill="#1d8f7b"/>
  <text x="280" y="233" font-size="13" fill="#e8e8e2" text-anchor="middle">お届け</text>

  <line x1="445" y1="216" x2="445" y2="121" stroke="#1d8f7b" stroke-width="1.6"/>
  <polygon points="445,110 439,122 451,122" fill="#1d8f7b"/>
  <text x="434" y="150" font-size="13" fill="#e8e8e2" text-anchor="end">代金を</text>
  <text x="434" y="172" font-size="13" fill="#e8e8e2" text-anchor="end">支払う</text>

  <line x1="370" y1="83" x2="201" y2="83" stroke="#f0a35a" stroke-width="1.6"/>
  <polygon points="190,83 202,77 202,89" fill="#f0a35a"/>
  <text x="280" y="73" font-size="13" fill="#f0a35a" text-anchor="middle">売上金を入金</text>
</svg>
```

### 組織図／ツリー（3列＋箇条書き）
担当わけ・役割分担・分類の親子。第3階層は箱にせず 13px の文字リスト（全角7字まで）にする。

```svg
<svg viewBox="0 0 560 272" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif" role="img" aria-label="文化祭 実行委員会の担当を示す組織図">
  <text x="8" y="22" font-size="15" fill="#e8e8e2">文化祭　実行委員会の担当</text>

  <rect x="205" y="40" width="150" height="44" rx="8" fill="rgba(255,255,255,.06)" stroke="#c8f0a0"/>
  <text x="280" y="67" font-size="14" fill="#e8e8e2" text-anchor="middle">実行委員長</text>

  <line x1="280" y1="84" x2="280" y2="104" stroke="rgba(255,255,255,.16)"/>
  <line x1="90" y1="104" x2="470" y2="104" stroke="rgba(255,255,255,.16)"/>
  <line x1="90" y1="104" x2="90" y2="124" stroke="rgba(255,255,255,.16)"/>
  <line x1="280" y1="104" x2="280" y2="124" stroke="rgba(255,255,255,.16)"/>
  <line x1="470" y1="104" x2="470" y2="124" stroke="rgba(255,255,255,.16)"/>

  <rect x="10" y="124" width="160" height="44" rx="8" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="90" y="151" font-size="14" fill="#c8f0a0" text-anchor="middle">企画班</text>
  <rect x="200" y="124" width="160" height="44" rx="8" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="280" y="151" font-size="14" fill="#c8f0a0" text-anchor="middle">広報班</text>
  <rect x="390" y="124" width="160" height="44" rx="8" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="470" y="151" font-size="14" fill="#c8f0a0" text-anchor="middle">会計班</text>

  <polyline points="90,168 90,182 20,182 20,248" fill="none" stroke="rgba(255,255,255,.16)"/>
  <line x1="20" y1="204" x2="30" y2="204" stroke="rgba(255,255,255,.16)"/>
  <line x1="20" y1="226" x2="30" y2="226" stroke="rgba(255,255,255,.16)"/>
  <line x1="20" y1="248" x2="30" y2="248" stroke="rgba(255,255,255,.16)"/>
  <text x="36" y="208" font-size="13" fill="#e8e8e2">ステージ進行</text>
  <text x="36" y="230" font-size="13" fill="#e8e8e2">出し物の受付</text>
  <text x="36" y="252" font-size="13" fill="#e8e8e2">片づけの手配</text>

  <polyline points="280,168 280,182 210,182 210,248" fill="none" stroke="rgba(255,255,255,.16)"/>
  <line x1="210" y1="204" x2="220" y2="204" stroke="rgba(255,255,255,.16)"/>
  <line x1="210" y1="226" x2="220" y2="226" stroke="rgba(255,255,255,.16)"/>
  <line x1="210" y1="248" x2="220" y2="248" stroke="rgba(255,255,255,.16)"/>
  <text x="226" y="208" font-size="13" fill="#e8e8e2">ポスター制作</text>
  <text x="226" y="230" font-size="13" fill="#e8e8e2">SNSでの告知</text>
  <text x="226" y="252" font-size="13" fill="#e8e8e2">当日の案内係</text>

  <polyline points="470,168 470,182 400,182 400,248" fill="none" stroke="rgba(255,255,255,.16)"/>
  <line x1="400" y1="204" x2="410" y2="204" stroke="rgba(255,255,255,.16)"/>
  <line x1="400" y1="226" x2="410" y2="226" stroke="rgba(255,255,255,.16)"/>
  <line x1="400" y1="248" x2="410" y2="248" stroke="rgba(255,255,255,.16)"/>
  <text x="416" y="208" font-size="13" fill="#e8e8e2">予算のふりわけ</text>
  <text x="416" y="230" font-size="13" fill="#e8e8e2">買い出し担当</text>
  <text x="416" y="252" font-size="13" fill="#e8e8e2">領収書の整理</text>
</svg>
```

### ベン図（共通点と違い）
2つの「同じところ」と「違うところ」を同時に見せる。円は2つまで、中央の重なりは全角7字まで、円の名前は円の外（上）。

```svg
<svg viewBox="0 0 560 340" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif" role="img" aria-label="ノートPC 2機種の共通点と違いのベン図">
  <text x="8" y="22" font-size="15" fill="#e8e8e2">ノートPC　A社とB社をくらべる</text>

  <text x="150" y="64" font-size="14" fill="#c8f0a0" text-anchor="middle">A社 X14</text>
  <text x="410" y="64" font-size="14" fill="#f0a35a" text-anchor="middle">B社 Air13</text>

  <circle cx="205" cy="200" r="125" fill="#c8f0a0" fill-opacity="0.08" stroke="#c8f0a0" stroke-opacity="0.8"/>
  <circle cx="355" cy="200" r="125" fill="#f0a35a" fill-opacity="0.08" stroke="#f0a35a" stroke-opacity="0.8"/>

  <text x="150" y="178" font-size="13" fill="#e8e8e2" text-anchor="middle">メモリ32GB</text>
  <text x="150" y="200" font-size="13" fill="#e8e8e2" text-anchor="middle">指紋認証あり</text>
  <text x="150" y="222" font-size="13" fill="#e8e8e2" text-anchor="middle">やや重い</text>

  <text x="410" y="178" font-size="13" fill="#e8e8e2" text-anchor="middle">画面が明るい</text>
  <text x="410" y="200" font-size="13" fill="#e8e8e2" text-anchor="middle">USB-C 4口</text>
  <text x="410" y="222" font-size="13" fill="#e8e8e2" text-anchor="middle">ファンが静か</text>

  <text x="280" y="152" font-size="12" fill="#7fd6a6" text-anchor="middle">共通</text>
  <text x="280" y="182" font-size="13" fill="#e8e8e2" text-anchor="middle">14インチ</text>
  <text x="280" y="204" font-size="13" fill="#e8e8e2" text-anchor="middle">約1.4kg</text>
  <text x="280" y="226" font-size="13" fill="#e8e8e2" text-anchor="middle">約12万円</text>
</svg>
```

### 対応づけ（左のものを右の分類へ）
多対一のふりわけ（分別、症状と原因、書類と提出先）。線は x=344 で止め、矢じりは行き先ごとに1個だけ x=354 に置く。

```svg
<svg viewBox="0 0 560 280" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif" role="img" aria-label="ごみの分け方の対応図">
  <text x="8" y="22" font-size="15" fill="#e8e8e2">ごみの分け方（うちの市の場合）</text>

  <rect x="16" y="46" width="190" height="36" rx="6" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="30" y="69" font-size="13" fill="#e8e8e2">ペットボトル</text>
  <rect x="16" y="90" width="190" height="36" rx="6" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="30" y="113" font-size="13" fill="#e8e8e2">新聞・チラシ</text>
  <rect x="16" y="134" width="190" height="36" rx="6" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="30" y="157" font-size="13" fill="#e8e8e2">割りばし</text>
  <rect x="16" y="178" width="190" height="36" rx="6" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="30" y="201" font-size="13" fill="#e8e8e2">保冷剤</text>
  <rect x="16" y="222" width="190" height="36" rx="6" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.16)"/>
  <text x="30" y="245" font-size="13" fill="#e8e8e2">乾電池</text>

  <line x1="206" y1="64" x2="344" y2="86" stroke="#1d8f7b" stroke-width="1.5"/>
  <line x1="206" y1="108" x2="344" y2="86" stroke="#1d8f7b" stroke-width="1.5"/>
  <line x1="206" y1="152" x2="344" y2="174" stroke="#1d8f7b" stroke-width="1.5"/>
  <line x1="206" y1="196" x2="344" y2="174" stroke="#1d8f7b" stroke-width="1.5"/>
  <line x1="206" y1="240" x2="344" y2="240" stroke="#1d8f7b" stroke-width="1.5"/>
  <polygon points="354,86 344,81 344,91" fill="#1d8f7b"/>
  <polygon points="354,174 344,169 344,179" fill="#1d8f7b"/>
  <polygon points="354,240 344,235 344,245" fill="#1d8f7b"/>

  <rect x="354" y="64" width="190" height="44" rx="6" fill="rgba(127,214,166,.10)" stroke="#7fd6a6"/>
  <text x="368" y="83" font-size="14" fill="#e8e8e2">資源ごみ</text>
  <text x="368" y="101" font-size="12" fill="#7fd6a6">毎週 火曜の朝</text>

  <rect x="354" y="152" width="190" height="44" rx="6" fill="rgba(200,240,160,.10)" stroke="#c8f0a0"/>
  <text x="368" y="171" font-size="14" fill="#e8e8e2">燃えるごみ</text>
  <text x="368" y="189" font-size="12" fill="#c8f0a0">毎週 月・木</text>

  <rect x="354" y="218" width="190" height="44" rx="6" fill="rgba(255,139,139,.10)" stroke="#ff8b8b"/>
  <text x="368" y="237" font-size="14" fill="#e8e8e2">有害ごみ</text>
  <text x="368" y="255" font-size="12" fill="#ff8b8b">第4金曜だけ</text>
</svg>
```