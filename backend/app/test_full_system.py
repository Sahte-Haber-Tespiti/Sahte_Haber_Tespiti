# test_full_system.py
from services.scraper import NewsScraperService
from services.preprocessing import TextPreprocessingService
from services.prediction_model import PredictionModel


def sistemi_test_et():
    print("--- SAHTE HABER TESPİT SİSTEMİ TESTİ BAŞLIYOR ---")

    # 1. Servisleri Başlat
    scraper = NewsScraperService()
    cleaner = TextPreprocessingService()
    model = PredictionModel()

    # 2. Test Edilecek Gerçek Haber Linki (Örn: Rastgele bir haber)
    # Not: Eğer link çalışmazsa güncel bir haber linkiyle değiştirin.
    test_metni = """
    A Milli Kadın Voleybol Takımı, Milletler Ligi finalinde Çin'i 3-1 mağlup ederek şampiyon oldu. 
    Karşılaşmanın en değerli oyuncusu seçilen Melissa Vargas, turnuva boyunca gösterdiği üstün 
    performansla göz doldurdu. Başantrenör Daniele Santarelli maç sonu yaptığı açıklamada, 
    "Bu takımla gurur duyuyorum, Türk halkına armağan olsun" dedi. Takım kaptanı Eda Erdem ise 
    destek veren herkese teşekkür etti.
    """

    # URL kısmını devre dışı bırakıp (yorum satırı yapıp) doğrudan temizlemeye geçiyoruz
    # ham_metin = scraper.scrape_url(test_url)  <-- BU SATIRI SİLİN VEYA BAŞINA # KOYUN
    ham_metin = test_metni
    # 3. Temizle
    print("\n2. Metin temizleniyor ve ön işleniyor...")
    temiz_metin = cleaner.clean_text(ham_metin)
    print(f"   -> Temizlenmiş (Tarzanca): {temiz_metin[:100]}...")

    # 4. Analiz Et
    print("\n3. Yapay Zeka Modeli analiz ediyor...")
    sonuc = model.predict(temiz_metin)

    print("\n" + "=" * 40)
    print(f"SONUÇ RAPORU:")
    print(f"Durum: {sonuc['label']}")
    print(f"Güven Skoru: %{sonuc['confidence_score']}")
    print(f"Sahte mi?: {sonuc['is_fake']}")
    print("=" * 40)


if __name__ == "__main__":
    sistemi_test_et()