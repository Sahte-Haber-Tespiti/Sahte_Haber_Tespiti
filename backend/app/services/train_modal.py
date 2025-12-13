import pandas as pd
import os
import joblib
import random
import numpy as np
from pathlib import Path
# GÖRSELLEŞTİRME İÇİN GEREKLİ KÜTÜPHANELER EKLENDİ
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc, f1_score, log_loss
import warnings

# Gereksiz uyarıları kapat
warnings.filterwarnings("ignore")

# --- 1. DOSYA YOLLARINI BUL ---
current_file_path = Path(__file__).resolve()
search_dir = current_file_path.parent
found_data_path = None

for _ in range(3):
    check_path = search_dir / 'data'
    if check_path.exists() and check_path.is_dir():
        found_data_path = check_path
        break
    search_dir = search_dir.parent

if not found_data_path:
    print("❌ HATA: Data klasörü bulunamadı.")
    exit()

models_dir = found_data_path.parent / 'ml_models'
if not models_dir.exists():
    os.makedirs(models_dir)

# --- 2. VERİ YÜKLEME ---
print("⏳ Veriler yükleniyor...")
try:
    df_final = pd.read_csv(found_data_path / 'final_dataset.csv')
    df_ek = pd.read_csv(found_data_path / 'ek_veri.csv')
except Exception as e:
    print(f"Dosya okuma hatası: {e}")
    exit()

# --- 3. VERİ AŞISI (DATA INJECTION - TAM KADRO) ---
fake_injection = [
    "ŞOK ŞOK ŞOK! Devlet herkese bedava para dağıtıyor! Tıklayın.",
    "Acil duyuru! Kimlik numaranızın sonu çiftse hemen başvurun.",
    "Bankalar bunu sizden saklıyor! Borçlarınız siliniyor.",
    "Bu kürü içen 3 günde 10 kilo veriyor! Doktorlar şokta.",
    "WhatsApp kapanıyor mu? Mavi tik için bu linke tıklayın.",
    "Tebrikler! Çekilişi kazandınız, ödülünüzü almak için tıklayın.",
    "Ev hanımlarına müjde! Oturduğunuz yerden günde 5000 TL kazanın.",
    "Aşıların içinde takip çipi olduğu kesinleşti.",
    "Büyük oyunu görün! Küresel güçler bizi yok edecek.",
    "Gökyüzünden zehir yağıyor, uçaklar kimyasal sıkıyor.",
    "Maskeler sizi korumaz, aksine hasta eder.",
    "Bill Gates insan nüfusunu azaltmak istiyor.",
    "5G istasyonları virüs yayıyor, hemen önlem alın.",
    "Dünya aslında düzdür, NASA bizden saklıyor.",
    "Bakanlık açıkladı: Nefes almak artık vergiye tabi olacak.",
    "Hükümetten yeni karar: Mutsuz olmak yasaklandı.",
    "Bilim insanları açıkladı: Tembellik aslında zeka belirtisiymiş.",
    "Maliye Bakanlığı: Rüya görenlerden eğlence vergisi alınacak.",
    "Trafik cezalarına zam: Yürümek de artık ücretli.",
    "Meteoroloji: Yarın gökten köfte yağması bekleniyor.",
    "Merkür retrosu bitiyor, cüzdanlar parayla dolacak.",
    "Bu dolunayda dilek tutanların borçları siliniyor.",
    "Burç yorumları: Aslanlar bu hafta zengin oluyor.",
    "Evrene mesaj gönderin, 777 yazın paranız gelsin.",
    "Yıldız haritasına göre bu hafta aşk kapınızı çalacak.",
    "Ritüel yapın, giden sevgiliniz 24 saatte geri dönsün."
]

real_injection = [
    "Merkez Bankası faiz kararını açıkladı.",
    "Meteoroloji uyardı: Yarın sağanak yağış bekleniyor.",
    "Milli Eğitim Bakanlığı okulların açılacağı tarihi duyurdu.",
    "Türkiye İstatistik Kurumu enflasyon verilerini paylaştı.",
    "Cumhurbaşkanlığı Kabinesi yarın toplanacak.",
    "Bilim insanları yeni bir gezegen keşfetti.",
    "Sağlık Bakanı aşı takvimi hakkında konuştu."
]

# --- 4. SENTETİK ÜRETİM ---
fake_gen = []
subjects = ["Aşılar", "Dolar", "Seçim", "Deprem", "Gizli örgütler", "Koronavirüs", "5G", "Uzaylılar"]
starts = ["ŞOK ŞOK!", "GİZLİ GERÇEK!", "OYUN BOZULDU!", "DOKTORLAR ŞOKTA!", "HÜKÜMET SAKLIYOR!"]
patterns = ["hakkında inanılmaz gerçekler ifşa oldu.", "ile bizi zehirliyorlar.", "aslında insanları kontrol etmek için.", "verileri çalındı tehlike büyük."]

for _ in range(2000):
    text = f"{random.choice(starts)} {random.choice(subjects)} {random.choice(patterns)}"
    fake_gen.append(text)

# --- 5. BİRLEŞTİRME ---
df_fake_inject = pd.DataFrame({'text': fake_injection * 100, 'label': 0})
df_real_inject = pd.DataFrame({'text': real_injection * 50, 'label': 1})
df_fake_gen = pd.DataFrame({'text': fake_gen, 'label': 0})

df = pd.concat([df_final, df_ek, df_fake_inject, df_real_inject, df_fake_gen], ignore_index=True)

if 'text' not in df.columns:
    df.columns = ['text', 'label'] + list(df.columns[2:])

df['label'] = df['label'].astype(int)
df = df.dropna(subset=['text'])

# --- 6. PREPROCESSING ---
print("⏳ Veri işleniyor...")
df['text'] = df['text'].astype(str).str.lower()
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

X = df['text']
y = df['label']

# --- 7. EĞİTİM ---
print(f"⏳ Model eğitiliyor (Toplam {len(df)} veri)...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1,3))
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

model = LogisticRegression(class_weight='balanced', C=1.0, max_iter=1000)
model.fit(X_train_vect, y_train)

# --- 8. TEST VE METRİKLER ---
y_pred = model.predict(X_test_vect)
y_proba = model.predict_proba(X_test_vect)

# --- GÖRSELLEŞTİRME ---
print("📊 Grafikler oluşturuluyor...")

# GRAFİK 1: Confusion Matrix (Karmaşıklık Matrisi) Isı Haritası
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['SAHTE (0)', 'GERÇEK (1)'],
            yticklabels=['SAHTE (0)', 'GERÇEK (1)'])
plt.title('Karmaşıklık Matrisi (Confusion Matrix)')
plt.ylabel('Gerçek Değer')
plt.xlabel('Tahmin Edilen')
plt.savefig(models_dir / '1_confusion_matrix.png')
plt.close() # Belleği temizlemek için figürü kapat
print("   -> 1_confusion_matrix.png")

# GRAFİK 2: Classification Report (Sınıflandırma Karnesi) Tablosu
plt.figure(figsize=(10, 6))
report = classification_report(y_test, y_pred, output_dict=True)
# Raporu bir DataFrame'e dönüştür ve gereksiz satırları at
df_report = pd.DataFrame(report).iloc[:-1, :3].T
sns.heatmap(df_report, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Sınıflandırma Başarı Raporu')
plt.savefig(models_dir / '2_classification_report.png')
plt.close()
print("   -> 2_classification_report.png")

# GRAFİK 3: ROC Eğrisi
fpr, tpr, thresholds = roc_curve(y_test, y_proba[:, 1])
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC Eğrisi (Alan = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Eğrisi')
plt.legend(loc="lower right")
plt.grid(alpha=0.3)
plt.savefig(models_dir / '3_roc_curve.png')
plt.close()
print("   -> 3_roc_curve.png")

# Kaydet
joblib.dump(model, models_dir / 'model.pkl')
joblib.dump(vectorizer, models_dir / 'vectorizer.pkl')
print(f"\n✅ Bitti! Tüm grafikler ve model '{models_dir}' klasörüne kaydedildi.")