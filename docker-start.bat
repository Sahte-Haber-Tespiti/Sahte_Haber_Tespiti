@echo off
echo 🚀 Sahte Haber Tespit Sistemi başlatılıyor...
echo.

REM Docker Compose ile servisleri başlat
docker-compose up -d

echo.
echo ⏳ Servislerin hazır olması bekleniyor...
timeout /t 10 /nobreak >nul

echo.
echo ✅ Servisler başlatıldı!
echo.
echo 📍 Erişim Adresleri:
echo    Frontend:  http://localhost:5173
echo    Backend:   http://localhost:8000
echo    API Docs:  http://localhost:8000/docs
echo    MySQL:     localhost:3306
echo.
echo 📝 Logları görmek için: docker-compose logs -f
echo 🛑 Durdurmak için: docker-compose down

