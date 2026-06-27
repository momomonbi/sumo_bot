"""
もも声サービス アダプタ (Style-Bert-VITS2 ⇄ もも アプリ)
=========================================================

index.html（もも アプリ）は、返答テキストを次の共通契約で叩く:

    POST {MOMO_VOICE_URL}/synthesize
    body: {"text": "...", "style": "Neutral", "speed": 1.0}
    resp: audio/wav (バイナリ)

このアダプタはその契約を、Style-Bert-VITS2 標準の FastAPI サーバ
(`server_fastapi.py` の GET/POST /voice) に翻訳して中継するだけの薄い層。
役割は2つ:
  1) ブラウザから直接叩けるよう CORS を許可する
  2) アプリ側の契約（text/style/speed）を SBV2 のパラメータ（length 等）へ変換する

これにより index.html は「エンジンが何であっても /synthesize を叩くだけ」で済み、
将来 ElevenLabs 等へ差し替える時もこのアダプタを置き換えるだけでよい（疎結合）。

起動:
    pip install -r requirements.txt
    cp .env.example .env   # 必要に応じて編集
    python adapter.py
"""

import os

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


# ── 設定（環境変数 / .env で上書き可能） ─────────────────────────────
SBV2_URL = os.getenv("SBV2_URL", "http://127.0.0.1:5000").rstrip("/")
# もも の学習済みモデル。model_name を入れれば model_id より優先される
MOMO_MODEL_ID = int(os.getenv("MOMO_MODEL_ID", "0"))
MOMO_MODEL_NAME = os.getenv("MOMO_MODEL_NAME", "").strip()
MOMO_SPEAKER_ID = int(os.getenv("MOMO_SPEAKER_ID", "0"))
MOMO_DEFAULT_STYLE = os.getenv("MOMO_DEFAULT_STYLE", "Neutral")
MOMO_STYLE_WEIGHT = float(os.getenv("MOMO_STYLE_WEIGHT", "1.0"))
MOMO_LANGUAGE = os.getenv("MOMO_LANGUAGE", "JP")
# CORS: 本番は自分のアプリのオリジンに絞るのが安全（カンマ区切り）。既定は全許可。
ALLOW_ORIGINS = [o.strip() for o in os.getenv("ALLOW_ORIGINS", "*").split(",") if o.strip()]

ADAPTER_HOST = os.getenv("ADAPTER_HOST", "0.0.0.0")
ADAPTER_PORT = int(os.getenv("ADAPTER_PORT", "8000"))

# 速度→length 変換のクランプ範囲（length は長さ倍率なので speed の逆数）
SPEED_MIN, SPEED_MAX = 0.5, 2.0


app = FastAPI(title="もも声サービス アダプタ", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SynthesizeRequest(BaseModel):
    text: str
    style: str | None = None
    speed: float | None = None


@app.get("/health")
async def health():
    """疎通確認。SBV2 本体にも届くか軽くチェックする。"""
    sbv2_ok = False
    detail = ""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"{SBV2_URL}/docs")
            sbv2_ok = r.status_code < 500
    except Exception as e:  # noqa: BLE001
        detail = str(e)
    return {
        "status": "ok",
        "sbv2_url": SBV2_URL,
        "sbv2_reachable": sbv2_ok,
        "model_id": MOMO_MODEL_ID,
        "model_name": MOMO_MODEL_NAME or None,
        "detail": detail or None,
    }


@app.post("/synthesize")
async def synthesize(req: SynthesizeRequest):
    """アプリ契約 {text, style, speed} → SBV2 /voice → audio/wav を返す。"""
    text = (req.text or "").strip()
    if not text:
        return JSONResponse(status_code=400, content={"error": "text が空だよ"})

    # speed（速さ）を length（長さ倍率）へ。speed が大きいほど length は小さく＝速く。
    speed = req.speed if (req.speed and req.speed > 0) else 1.0
    speed = max(SPEED_MIN, min(SPEED_MAX, speed))
    length = 1.0 / speed

    params = {
        "text": text,
        "speaker_id": MOMO_SPEAKER_ID,
        "style": (req.style or MOMO_DEFAULT_STYLE),
        "style_weight": MOMO_STYLE_WEIGHT,
        "length": length,
        "language": MOMO_LANGUAGE,
    }
    # model_name があれば優先、なければ model_id
    if MOMO_MODEL_NAME:
        params["model_name"] = MOMO_MODEL_NAME
    else:
        params["model_id"] = MOMO_MODEL_ID

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            # SBV2 の /voice は GET/POST 両対応。パラメータはクエリで渡す。
            r = await client.post(f"{SBV2_URL}/voice", params=params)
    except httpx.RequestError as e:
        return JSONResponse(
            status_code=502,
            content={"error": f"Style-Bert-VITS2 に繋がらないよ: {e}"},
        )

    if r.status_code != 200:
        return JSONResponse(
            status_code=502,
            content={"error": f"SBV2 がエラーを返したよ (HTTP {r.status_code})",
                     "body": r.text[:500]},
        )

    return Response(content=r.content, media_type="audio/wav")


if __name__ == "__main__":
    import uvicorn

    print(f"[もも声アダプタ] listen http://{ADAPTER_HOST}:{ADAPTER_PORT}  → SBV2 {SBV2_URL}")
    uvicorn.run(app, host=ADAPTER_HOST, port=ADAPTER_PORT)
