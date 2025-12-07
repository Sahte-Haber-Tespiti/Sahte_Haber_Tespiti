# SAHTE HABER TESPİT SİSTEMİ - PROJE ÖZETİ

## PROJE TANIMI

Sahte Haber Tespit Sistemi, Türkçe haberlerin sahte veya güvenilir olma olasılığını analiz eden yapay zeka tabanlı bir web uygulamasıdır. Sistem, kullanıcıların haber metinlerini veya haber URL'lerini girerek, makine öğrenmesi algoritmaları kullanarak haberlerin güvenilirlik analizini yapar ve sonuçları görsel bir arayüzle sunar.

## MİMARİ YAPI

Proje üç katmanlı bir mimari yapıya sahiptir:

1. **Frontend Katmanı**: React tabanlı modern web arayüzü (Port 5173)
2. **Backend Katmanı**: FastAPI tabanlı RESTful API servisi (Port 8000)
3. **Veritabanı Katmanı**: MySQL 8.0 veritabanı (Port 3306)
4. **AI Model Katmanı**: Scikit-learn tabanlı makine öğrenmesi modeli

Tüm sistem Docker ve Docker Compose kullanılarak containerize edilmiş ve tek komutla çalıştırılabilir hale getirilmiştir.

## KULLANILAN TEKNOLOJİLER

### Backend Teknolojileri

**Framework ve Sunucu:**
- FastAPI 0.104.1: Modern, hızlı Python web framework'ü
- Uvicorn 0.24.0: ASGI sunucu, FastAPI için yüksek performanslı HTTP sunucusu

**Veritabanı:**
- MySQL 8.0: İlişkisel veritabanı yönetim sistemi
- SQLAlchemy 2.0.23: Python için ORM (Object-Relational Mapping) kütüphanesi
- PyMySQL 1.1.0: MySQL veritabanı bağlantı sürücüsü
- Cryptography 41.0.7: Güvenli bağlantı için şifreleme kütüphanesi

**Yapay Zeka ve Makine Öğrenmesi:**
- Scikit-learn 1.3.2: Makine öğrenmesi kütüphanesi
- Joblib 1.3.2: Model serialization ve paralel işleme
- NLTK 3.8.1: Doğal dil işleme kütüphanesi (Türkçe metin işleme için)

**Web Scraping ve HTTP:**
- BeautifulSoup4 4.12.2: HTML/XML parsing kütüphanesi
- Requests 2.31.0: HTTP istekleri için kütüphane
- Lxml 4.9.3: XML/HTML parser

**Diğer:**
- Pydantic 2.5.0: Veri validasyonu ve ayarlar yönetimi
- Python-dotenv 1.0.0: Ortam değişkenleri yönetimi

### Frontend Teknolojileri

**Framework ve Kütüphaneler:**
- React 18.2.0: Kullanıcı arayüzü oluşturma kütüphanesi
- React-DOM 18.2.0: React'in DOM render etme kütüphanesi
- Axios 1.6.2: HTTP istekleri için promise tabanlı kütüphane

**Build Tools ve Styling:**
- Vite 5.0.8: Hızlı frontend build tool ve dev server
- Tailwind CSS 3.3.6: Utility-first CSS framework
- PostCSS 8.4.32: CSS post-processing tool
- Autoprefixer 10.4.16: CSS vendor prefix ekleme aracı
- @vitejs/plugin-react 4.2.1: Vite için React plugin'i

**Type Definitions:**
- @types/react 18.2.43: React için TypeScript type tanımları
- @types/react-dom 18.2.17: React-DOM için TypeScript type tanımları

### DevOps ve Containerization

- Docker: Containerization platformu
- Docker Compose: Çoklu container yönetimi
- Dockerfile (Backend): Python uygulaması için container image
- Dockerfile (Frontend): React uygulaması için container image

## PROJE YAPISI

```
sahte-haber-tespit/
├── backend/                          # Backend uygulaması
│   ├── app/                          # Ana uygulama klasörü
│   │   ├── main.py                   # FastAPI ana uygulama dosyası
│   │   ├── database.py               # MySQL veritabanı bağlantı yönetimi
│   │   ├── routes/                    # API route'ları
│   │   │   └── analyze_route.py      # Analiz endpoint'leri (/api/analyze/)
│   │   ├── services/                 # İş mantığı servisleri
│   │   │   ├── model_predictor.py    # AI model tahmin servisi
│   │   │   ├── text_extractor.py     # URL'den metin çıkarma servisi
│   │   │   └── text_preprocessor.py  # Türkçe metin ön işleme servisi
│   │   ├── models/                   # Veri modelleri
│   │   │   ├── analysis_result.py    # API request/response modelleri
│   │   │   └── db_models.py          # Veritabanı ORM modelleri
│   │   ├── utils/                    # Yardımcı fonksiyonlar
│   │   │   └── scraper.py            # URL validasyon ve yardımcı fonksiyonlar
│   │   └── ai_model/                 # AI model dosyaları
│   │       ├── model.pkl             # Eğitilmiş Logistic Regression modeli
│   │       ├── vectorizer.pkl        # Eğitilmiş TF-IDF vectorizer
│   │       └── README.md              # Model dokümantasyonu
│   ├── requirements.txt              # Python bağımlılıkları
│   ├── Dockerfile                    # Backend container image tanımı
│   └── train_model.py                # Model eğitim scripti
│
├── frontend/                          # Frontend uygulaması
│   ├── src/                          # Kaynak kodlar
│   │   ├── components/               # React bileşenleri
│   │   │   ├── Navbar.jsx            # Navigasyon çubuğu bileşeni
│   │   │   ├── InputForm.jsx         # Haber giriş formu bileşeni
│   │   │   └── ResultCard.jsx       # Analiz sonuç gösterim bileşeni
│   │   ├── App.jsx                   # Ana React uygulama bileşeni
│   │   ├── main.jsx                  # React uygulama giriş noktası
│   │   └── index.css                 # Tailwind CSS stilleri
│   ├── package.json                  # Node.js bağımlılıkları ve scriptler
│   ├── Dockerfile                    # Frontend container image tanımı
│   ├── vite.config.js                # Vite yapılandırma dosyası
│   ├── tailwind.config.js            # Tailwind CSS yapılandırması
│   └── postcss.config.js             # PostCSS yapılandırması
│
├── docker-compose.yml                # Docker Compose yapılandırması
├── docker-start.bat                  # Windows başlatma scripti
├── docker-start.sh                   # Linux/Mac başlatma scripti
└── README.md                          # Proje dokümantasyonu
```

## ÖZELLİKLER

### 1. Metin Analizi
Kullanıcılar haber metnini doğrudan sisteme girerek analiz yapabilir. Sistem minimum 50 karakterlik metin kabul eder ve metni ön işleme tabi tutarak AI modeline gönderir.

### 2. URL Analizi
Kullanıcılar haber URL'si girerek, sistem otomatik olarak URL'den metin çıkarır ve analiz eder. BeautifulSoup kullanılarak farklı haber sitelerinden metin çıkarımı yapılır.

### 3. AI Tabanlı Tahmin
Scikit-learn kütüphanesi kullanılarak eğitilmiş Logistic Regression modeli ile TF-IDF vectorization tekniği kullanılarak sahte haber tespiti yapılır. Model, metni analiz ederek sahte ve gerçek haber olasılıklarını yüzde olarak döndürür.

### 4. Modern Kullanıcı Arayüzü
React ve Tailwind CSS kullanılarak oluşturulmuş modern, responsive ve kullanıcı dostu arayüz. Gradient renkler, animasyonlar ve görsel grafiklerle sonuçlar sunulur.

### 5. RESTful API
FastAPI ile oluşturulmuş hızlı, güvenilir ve otomatik dokümantasyonlu REST API. Swagger UI ile interaktif API testi yapılabilir.

### 6. Veritabanı Entegrasyonu
MySQL veritabanı kullanılarak analiz geçmişi saklanır. Her analiz sonucu veritabanına kaydedilir ve geçmiş analizler görüntülenebilir.

### 7. Docker Desteği
Tüm sistem Docker container'ları içinde çalışır. Tek komutla tüm servisler başlatılabilir ve yönetilebilir.

## API ENDPOINT'LERİ

### 1. Ana Endpoint
- **GET** `/`: API bilgileri ve versiyon bilgisi döndürür
- **GET** `/health`: Sistem sağlık kontrolü yapar

### 2. Analiz Endpoint'i
- **POST** `/api/analyze/`: Haber metni veya URL'sini analiz eder
  - Request Body: `{"text": "haber metni", "url": null}` veya `{"text": null, "url": "https://..."}`
  - Response: `{"fake_probability": 65.5, "real_probability": 34.5, "is_fake": true, "analyzed_text": "...", "message": "..."}`

### 3. Geçmiş Analizler
- **GET** `/api/analyze/history?limit=50`: Analiz geçmişini getirir

### 4. İstatistikler
- **GET** `/api/analyze/stats`: Toplam analiz sayısı, sahte/gerçek haber istatistikleri

## AI MODEL DETAYLARI

### Model Algoritması
- **Algoritma**: Logistic Regression
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Özellik Sayısı**: Maksimum 5000 özellik
- **N-gram Aralığı**: 1-2 (unigram ve bigram)
- **Minimum Doküman Frekansı**: 2
- **Maksimum Doküman Frekansı**: 0.95

### Metin Ön İşleme
1. Küçük harfe çevirme
2. URL ve email adreslerini kaldırma
3. Özel karakterleri temizleme (Türkçe karakterler korunur)
4. NLTK ile tokenization
5. Türkçe stopwords kaldırma
6. Kısa kelimeleri (2 karakterden az) filtreleme

### Model Eğitimi
Model eğitimi için CSV formatında veri gereklidir:
- `text`: Haber metni
- `label`: 0 (gerçek) veya 1 (sahte)

Eğitim scripti (`train_model.py`) veriyi yükler, train-test split yapar, TF-IDF vectorizer oluşturur, Logistic Regression modelini eğitir ve model dosyalarını kaydeder.

## VERİTABANI YAPISI

### AnalysisHistory Tablosu
- `id`: Primary key (Integer)
- `text`: Analiz edilen metin (Text, ilk 1000 karakter)
- `url`: Haber URL'si (String, nullable)
- `fake_probability`: Sahte olasılığı (Float)
- `real_probability`: Gerçek olasılığı (Float)
- `is_fake`: Sahte mi? (Boolean)
- `created_at`: Oluşturulma zamanı (DateTime)

## FRONTEND BİLEŞENLERİ

### Navbar.jsx
Üst navigasyon çubuğu, proje başlığı ve bilgilendirme içerir.

### InputForm.jsx
Kullanıcı giriş formu bileşeni:
- Metin veya URL girişi seçimi
- Metin girişi için textarea (minimum 50 karakter)
- URL girişi için input alanı
- Karakter sayacı
- Analiz ve temizle butonları
- Loading durumu gösterimi

### ResultCard.jsx
Analiz sonuçlarını görselleştiren bileşen:
- Büyük ikon ve mesaj gösterimi (sahte/gerçek durumuna göre)
- Dairesel grafik (SVG ile olasılık dağılımı)
- Progress bar'lar (sahte ve gerçek olasılıkları)
- Risk seviyesi göstergesi
- Analiz edilen metin önizlemesi

## ÇALIŞMA AKIŞI

1. **Kullanıcı Girişi**: Kullanıcı frontend'de haber metni veya URL girer
2. **İstek Gönderimi**: Frontend, Axios ile backend API'ye POST isteği gönderir
3. **Metin Çıkarma**: Eğer URL girildiyse, backend URL'den metin çıkarır
4. **Metin Ön İşleme**: Metin Türkçe ön işleme adımlarından geçirilir
5. **AI Tahmin**: Ön işlenmiş metin AI modeline gönderilir ve tahmin yapılır
6. **Veritabanı Kaydı**: Analiz sonucu veritabanına kaydedilir
7. **Sonuç Döndürme**: Backend, analiz sonucunu JSON formatında döndürür
8. **Görselleştirme**: Frontend, sonuçları görsel grafikler ve kartlar ile gösterir

## GÜVENLİK ÖZELLİKLERİ

- CORS (Cross-Origin Resource Sharing) yapılandırması
- Input validasyonu (minimum karakter kontrolü, URL format kontrolü)
- SQL injection koruması (SQLAlchemy ORM kullanımı)
- Error handling ve exception yönetimi
- Timeout ayarları (URL istekleri için)

## PERFORMANS ÖZELLİKLERİ

- FastAPI'nin yüksek performanslı async desteği
- Uvicorn'un ASGI sunucu optimizasyonları
- TF-IDF vectorization'un hızlı işleme kapasitesi
- Vite'nin hızlı development server'ı
- React'in virtual DOM optimizasyonu
- Docker container'ların izole çalışma ortamı

## GELİŞTİRME ORTAMI

- **Backend Port**: 8000
- **Frontend Port**: 5173
- **MySQL Port**: 3306
- **Hot Reload**: Backend ve frontend'de otomatik yeniden yükleme
- **API Dokümantasyonu**: http://localhost:8000/docs (Swagger UI)

## KURULUM VE ÇALIŞTIRMA

### Docker ile (Önerilen)
```bash
docker-compose up -d
```

### Manuel Kurulum
1. Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
2. Frontend: `cd frontend && npm install && npm run dev`
3. MySQL: Yerel MySQL kurulumu veya Docker container

## MODEL EĞİTİMİ

Model dosyaları (`model.pkl` ve `vectorizer.pkl`) yoksa sistem placeholder değerler döndürür. Gerçek analiz için:
1. CSV formatında eğitim verisi hazırlanır
2. `python train_model.py turkish_fake_news.csv` komutu çalıştırılır
3. Model dosyaları `backend/app/ai_model/` klasörüne kaydedilir
4. Backend yeniden başlatılır

## NOTLAR

- Model dosyaları yoksa sistem placeholder değerler (45% fake, 55% real) döndürür
- Türkçe stopwords için NLTK kullanılır
- URL'den metin çıkarma, farklı haber sitelerinde çalışabilir
- Veritabanı tabloları otomatik olarak oluşturulur (ilk çalıştırmada)
- Docker container'ları volume mount ile kod değişikliklerini anında yansıtır

## GELECEK GELİŞTİRMELER

- JWT tabanlı kullanıcı girişi ve kimlik doğrulama
- Geçmiş sorgular görüntüleme sayfası
- İstatistik dashboard'u ve grafikler
- Daha gelişmiş NLP modelleri (BERT, DistilBERT gibi transformer modelleri)
- Detaylı raporlama ve export özellikleri
- Çoklu dil desteği
- API rate limiting
- Caching mekanizması

## LİSANS

Bu proje eğitim amaçlıdır.

