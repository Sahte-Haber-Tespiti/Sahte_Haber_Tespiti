#!/bin/bash

echo "🚀 Sahte Haber Tespit Sistemi başlatılıyor..."
echo ""

# Docker Compose ile servisleri başlat
docker-compose up -d

echo ""
echo "⏳ Servislerin hazır olması bekleniyor..."
sleep 10

# MySQL'in hazır olmasını bekle
echo "📊 MySQL veritabanı kontrol ediliyor..."
until docker exec fake_news_mysql mysqladmin ping -h localhost --silent; do
    echo "MySQL bekleniyor..."
    sleep 2
done

echo ""
echo "✅ Tüm servisler hazır!"
echo ""
echo "📍 Erişim Adresleri:"
echo "   Frontend:  http://localhost:5173"
echo "   Backend:   http://localhost:8000"
echo "   API Docs:  http://localhost:8000/docs"
echo "   MySQL:     localhost:3306"
echo ""
echo "📝 Logları görmek için: docker-compose logs -f"
echo "🛑 Durdurmak için: docker-compose down"

