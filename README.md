# 🎯 Sahte Haber Tespit Sistemi

Türkçe haberlerin sahte veya güvenilir olma olasılığını analiz eden yapay zeka tabanlı bir web uygulaması.

## 📋 Özellikler

- ✅ **Metin Analizi**: Haber metnini doğrudan analiz edebilme
- ✅ **URL Analizi**: Haber URL'sinden otomatik metin çıkarma ve analiz
- ✅ **AI Tabanlı Tahmin**: Scikit-learn ve TF-IDF kullanarak sahte haber tespiti
- ✅ **Modern UI**: React + Tailwind CSS ile şık ve kullanıcı dostu arayüz
- ✅ **RESTful API**: FastAPI ile hızlı ve güvenilir backend
- ✅ **MySQL Veritabanı**: Analiz geçmişi ve istatistikler
- ✅ **Docker Desteği**: Tek komutla tüm sistem çalışır

## 🏗️ Mimari

Proje 3 katmanlı bir yapıya sahiptir:

1. **Frontend**: React + Vite + Tailwind CSS
2. **Backend**: FastAPI + Python
3. **AI Model**: Scikit-learn (TF-IDF + Logistic Regression)
4. **Veritabanı**: MySQL 8.0

## 🐳 Docker ile Hızlı Başlangıç

### 1. Tüm Sistemi Başlat

```bash
docker-compose up -d
```

Bu komut şunları yapar:
- MySQL veritabanını başlatır
- Backend API'yi başlatır
- Frontend'i başlatır

### 2. Servisleri Kontrol Et

```bash
# Servislerin durumunu gör
docker-compose ps

# Logları gör
docker-compose logs -f
```

### 3. Uygulamaya Eriş

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Dokümantasyonu**: http://localhost:8000/docs
- **MySQL**: localhost:3306

### 4. Servisleri Durdur

```bash
docker-compose down
```

### 5. Verileri de Silmek İçin

```bash
docker-compose down -v
```

## 🚀 Manuel Kurulum (Docker Olmadan)

### 1. Backend Kurulumu

```bash
cd backend
pip install -r requirements.txt

# .env dosyası oluştur (isteğe bağlı)
cp .env.example .env
```

### 2. MySQL Veritabanı Ayarları

MySQL'i kendiniz kurduysanız, `.env` dosyasında şunları ayarlayın:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=fake_news_db
```

### 3. Backend'i Başlat

```bash
cd backend
uvicorn app.main:app --reload
```

### 4. Frontend Kurulumu

```bash
cd frontend
npm install
npm run dev
```

## 📊 Model Eğitimi (Opsiyonel)

Model dosyaları (`model.pkl` ve `vectorizer.pkl`) yoksa, önce modeli eğitmeniz gerekir:

```bash
# Eğitim verisi CSV formatında olmalı
# Format: 'text' (haber metni) ve 'label' (0=gerçek, 1=sahte) kolonları

cd backend
python train_model.py turkish_fake_news.csv
```

Model dosyaları `backend/app/ai_model/` klasörüne kaydedilecektir.

**Not**: Model dosyaları yoksa sistem placeholder değerler döndürecektir. Gerçek analiz için model eğitimi gereklidir.

## 📁 Proje Yapısı

```
.
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI ana dosyası
│   │   ├── database.py             # Veritabanı bağlantısı
│   │   ├── routes/
│   │   │   └── analyze_route.py    # Analiz endpoint'i
│   │   ├── services/
│   │   │   ├── text_extractor.py   # URL'den metin çıkarma
│   │   │   ├── text_preprocessor.py # Metin ön işleme
│   │   │   └── model_predictor.py  # Model tahmin
│   │   ├── models/
│   │   │   ├── analysis_result.py  # API modelleri
│   │   │   └── db_models.py        # Veritabanı modelleri
│   │   ├── utils/
│   │   │   └── scraper.py          # URL yardımcı fonksiyonları
│   │   └── ai_model/               # Model dosyaları
│   ├── requirements.txt
│   ├── Dockerfile
│   └── train_model.py              # Model eğitim scripti
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx          # Navigasyon çubuğu
│   │   │   ├── InputForm.jsx        # Giriş formu
│   │   │   └── ResultCard.jsx      # Sonuç kartı (grafiklerle)
│   │   ├── App.jsx                 # Ana uygulama
│   │   ├── main.jsx                # Giriş noktası
│   │   └── index.css               # Tailwind CSS
│   ├── package.json
│   ├── Dockerfile
│   └── vite.config.js
│
├── docker-compose.yml              # Docker Compose yapılandırması
└── README.md
```

## 🔧 API Kullanımı

### Analiz Endpoint'i

**POST** `/api/analyze/`

**Request Body:**
```json
{
  "text": "Haber metni buraya...",
  "url": null
}
```

veya

```json
{
  "text": null,
  "url": "https://example.com/haber"
}
```

**Response:**
```json
{
  "fake_probability": 65.5,
  "real_probability": 34.5,
  "is_fake": true,
  "analyzed_text": "Analiz edilen metin...",
  "message": "⚠️ Bu haberin sahte olma olasılığı %65.5. Dikkatli olun!"
}
```

### Geçmiş Analizler

**GET** `/api/analyze/history?limit=50`

### İstatistikler

**GET** `/api/analyze/stats`

## 📝 Model Eğitimi İçin Veri Formatı

CSV dosyası şu formatta olmalıdır:

| text | label |
|------|-------|
| "Haber metni 1..." | 0 |
| "Haber metni 2..." | 1 |

- `text`: Haber metni (string)
- `label`: 0 = Gerçek haber, 1 = Sahte haber

## 🛠️ Teknolojiler

### Backend
- FastAPI
- SQLAlchemy (MySQL ORM)
- Scikit-learn
- NLTK
- BeautifulSoup4
- Requests

### Frontend
- React 18
- Vite
- Tailwind CSS
- Axios

### Veritabanı
- MySQL 8.0

### DevOps
- Docker
- Docker Compose

## 📝 Notlar

- Model dosyaları yoksa sistem placeholder değerler döndürür
- Gerçek analiz için model eğitimi gereklidir
- Türkçe stopwords için NLTK kullanılır
- URL'den metin çıkarma, farklı haber sitelerinde çalışabilir
- Veritabanı otomatik olarak oluşturulur (ilk çalıştırmada)

## 🔮 Gelecek Geliştirmeler

- [ ] JWT tabanlı kullanıcı girişi
- [ ] Geçmiş sorgular görüntüleme sayfası
- [ ] İstatistik dashboard'u
- [ ] Daha gelişmiş NLP modelleri (BERT, etc.)
- [ ] Grafik ve raporlama

## 📄 Lisans

Bu proje eğitim amaçlıdır.
