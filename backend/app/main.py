from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn
from urllib.parse import urlparse

# Kendi servislerini import et
from services.prediction_model import PredictionModel
from services.preprocessing import TextPreprocessingService
from services.scraper import NewsScraperService

app = FastAPI(title="Sahte Haber Tespit API", version="2.0")

# --- SERVİSLERİ BAŞLAT ---
print("🚀 Servisler başlatılıyor...")
ai_model = PredictionModel()
cleaner = TextPreprocessingService()
scraper = NewsScraperService()

# --- GÜVENİLİR KAYNAKLAR (WHITELIST) ---
# Bu siteler "Yalancı Çoban" değildir, direk geçiş izni verilir.
TRUSTED_DOMAINS = [
    "trthaber.com", "hurriyet.com.tr", "aa.com.tr", "cnnturk.com",
    "ntv.com.tr", "haberturk.com", "sozcu.com.tr", "cumhuriyet.com.tr",
    "fanatik.com.tr", "beinsports.com.tr", "sabah.com.tr", "bbc.com",
    "milliyet.com.tr", "onedio.com", "webtekno.com", "shiftdelete.net"
]


# --- REQUEST & RESPONSE MODELLERİ ---
class AnalyzeRequest(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None


class AnalyzeResponse(BaseModel):
    durum: str  # "GERÇEK HABER" / "SAHTE HABER"
    renk: str  # "green" / "red"
    guven_skoru: float  # 0.0 - 100.0
    ozet: str
    kaynak_turu: str  # "Yapay Zeka" veya "Whitelist"


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_news(request: AnalyzeRequest):
    ham_metin = ""
    is_trusted_source = False
    trusted_source_name = ""

    # --- SENARYO 1: URL ANALİZİ ---
    if request.url:
        try:
            # 1. Domain Kontrolü (Whitelist)
            parsed_url = urlparse(request.url)
            domain = parsed_url.netloc.replace("www.", "")

            # Domainin içinde trusted listesinden biri geçiyor mu?
            for trusted in TRUSTED_DOMAINS:
                if trusted in domain:
                    is_trusted_source = True
                    trusted_source_name = trusted
                    break

            # Eğer güvenilirse hemen dön (AI'yı yorma)
            if is_trusted_source:
                return AnalyzeResponse(
                    durum="GERÇEK HABER",
                    renk="green",
                    guven_skoru=100.0,
                    ozet=f"Bu haber, doğrulanmış güvenilir kaynaklar listesinde bulunan ({trusted_source_name}) sitesinden alınmıştır.",
                    kaynak_turu="Güvenilir Kaynak (Whitelist)"
                )

            # Güvenilir değilse siteye git ve veriyi çek
            ham_metin = scraper.scrape_url(request.url)
            if not ham_metin or len(ham_metin) < 50:
                raise HTTPException(status_code=400, detail="Haber içeriği çekilemedi veya çok kısa.")

        except Exception as e:
            # URL hatası olursa, kullanıcıya bildir
            raise HTTPException(status_code=400, detail=f"URL Hatası: {str(e)}")

    # --- SENARYO 2: TEXT ANALİZİ ---
    elif request.text:
        ham_metin = request.text
        if len(ham_metin) < 10:
            raise HTTPException(status_code=400, detail="Lütfen daha uzun bir metin giriniz.")
    else:
        raise HTTPException(status_code=400, detail="Lütfen bir URL veya Metin (text) giriniz.")

    # --- YAPAY ZEKA SÜRECİ (Sadece Whitelist'e takılmayanlar buraya gelir) ---

    # 1. Temizleme (Preprocessing) - ÇOK ÖNEMLİ
    # Bunu yapmazsan model "Şok" kelimesini tanımaz çünkü eğitimde "şok" olarak öğrendi.
    temiz_metin = cleaner.clean_text(ham_metin)

    # 2. Tahmin
    sonuc = ai_model.predict(temiz_metin)

    # 3. Cevabı Hazırla
    if sonuc["is_fake"]:
        durum_mesaji = "SAHTE HABER"
        renk_kodu = "red"
    else:
        durum_mesaji = "GERÇEK HABER"
        renk_kodu = "green"

    # Özetleme (Metnin ilk 200 karakteri)
    ozet_metin = ham_metin[:200] + "..." if len(ham_metin) > 200 else ham_metin

    return AnalyzeResponse(
        durum=durum_mesaji,
        renk=renk_kodu,
        guven_skoru=sonuc["confidence_score"],
        ozet=ozet_metin,
        kaynak_turu="Yapay Zeka Analizi"
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)