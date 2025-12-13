import pandas as pd
import os

# Klasör yolları
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- DÜZELTME BURADA YAPILDI ---
# data klasörü artık 'backend' klasörünün içinde aranacak
DATA_DIR = os.path.join(BASE_DIR, "backend", "data")

# Klasör kontrolü (Garanti olsun diye bırakıyoruz)
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
    print(f"Uyarı: '{DATA_DIR}' oluşturuldu.")

# --- CİDDİ SAHTE HABER ÖRNEKLERİ ---
yeni_veriler = [
    # TÜR 1: SAĞLIK YALANLARI
    {
        "text": "Ünlü profesör açıkladı: Limon ve karbonatı karıştırıp içerseniz kanser 24 saatte yok oluyor. İlaç firmaları bunu saklıyor!",
        "label": 0},
    {"text": "Şok iddia! Aşıların içinde takip çipi olduğu kanıtlandı. Belgeler sızdırıldı.", "label": 0},
    {"text": "Bu çayı içen haftada 10 kilo veriyor! Diyetisyenlerin gizlediği mucize formül.", "label": 0},
    {"text": "Soğan kabuğunu kaynatıp içerseniz virüs vücudunuza giremez. Bilim dünyası şaşkın.", "label": 0},

    # TÜR 2: CLICKBAIT / TIK TUZAĞI
    {"text": "Emekliye dev müjde! Sabah saatlerinde açıklandı, maaşlara rekor zam geliyor. İşte yeni tablo...",
     "label": 0},
    {"text": "Ünlü oyuncu hayatını kaybetti mi? Sevenleri yasta! İşte o paylaşım...", "label": 0},
    {"text": "Whatsapp kullananlar dikkat! Yarından itibaren paralı oluyor. Hemen bu ayarı kapatın.", "label": 0},
    {"text": "Meteoroloji uyardı: Kar geliyor, kapıdan dışarı çıkmayın! Tarih verildi.", "label": 0},

    # TÜR 3: DOLANDIRICILIK
    {"text": "Yatırım tavsiyesidir! Bu coini alan yarın zengin olacak. Elon Musk sinyali verdi.", "label": 0},
    {"text": "Devlet herkese karşılıksız 5000 TL dağıtıyor! Başvuru için linke tıklayın.", "label": 0},
    {"text": "Bedava internet kampanyası başladı! Telefon numaranızı girin 10 GB kazanın.", "label": 0},

    # TÜR 4: KOMPLO TEORİLERİ
    {"text": "Dünyayı yöneten 5 aile toplantı yaptı. İnsan nüfusunu azaltma kararı aldılar.", "label": 0},
    {"text": "Harp teknolojisi ile deprem yapıldı. Gökyüzündeki ışıklar bunu kanıtlıyor.", "label": 0},

    # --- DENGELEMEK İÇİN GERÇEK HABERLER ---
    {"text": "Sağlık Bakanlığı, grip vakalarındaki artışa karşı vatandaşları uyardı. Maske ve mesafe önem taşıyor.",
     "label": 1},
    {"text": "Meteoroloji Genel Müdürlüğü, Marmara Bölgesi için sağanak yağış uyarısında bulundu.", "label": 1},
    {"text": "Merkez Bankası faiz kararını açıkladı. Politika faizi sabit tutuldu.", "label": 1},
    {"text": "Milli Eğitim Bakanlığı, okulların açılacağı tarihi resmi sitesinden duyurdu.", "label": 1},
    {"text": "Polis ekipleri, uyuşturucu satıcılarına yönelik şafak operasyonu düzenledi. Çok sayıda gözaltı var.",
     "label": 1}
]


def veriyi_kaydet():
    # DataFrame oluştur
    df_yeni = pd.DataFrame(yeni_veriler)

    # Kaydet
    kayit_yolu = os.path.join(DATA_DIR, "ek_veri.csv")
    df_yeni.to_csv(kayit_yolu, index=False)

    print(f"✅ BAŞARILI: Yeni veri seti şuraya kaydedildi: {kayit_yolu}")
    print(f"Toplam {len(df_yeni)} adet yeni 'Ciddi Haber' örneği eklendi.")


if __name__ == "__main__":
    veriyi_kaydet()