from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Sesli Banka taslagi")

class KomutIstegi(BaseModel):
    kullanici_id: str
    ses_metni: str

@app.get("/")
def ana_sayfa():
    return {"durum": "taslak", "kasa": "kapali", "mesaj": "Banka baglantisi yok."}

@app.post("/islem-yap")
def komut_isles(istek: KomutIstegi):
    metin = istek.ses_metni.lower()
    if "gonder" in metin or "gönder" in metin:
        raise HTTPException(status_code=402, detail="Odeme kaniti yok. Transfer yazilmadi.")
    if "bakiye" in metin:
        raise HTTPException(status_code=503, detail="Bakiye kaynagi yok.")
    raise HTTPException(status_code=400, detail="Anlasilmadi.")
