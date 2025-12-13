import requests
from bs4 import BeautifulSoup
import feedparser  # RSS desteği için
import re


class NewsScraperService:
    """
    Sorumluluk: Verilen URL'e gider, HTML içeriğini indirir ve
    sadece haber metnini (paragrafları) ayıklayıp döndürür.
    Eski adı: MetinCikariciServisi
    """

    def __init__(self):
        # Haber siteleri botları engellemesin diye kendimizi Chrome tarayıcısı gibi tanıtıyoruz
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_url(self, url: str) -> str:
        """
        Verilen URL'den ana haber metnini çeker.
        """
        try:
            # 1. İstek at (Siteye bağlan)
            response = requests.get(url, headers=self.headers, timeout=10)

            # Bağlantı başarılı mı? (200 = OK)
            if response.status_code != 200:
                print(f"HATA: Siteye ulaşılamadı. Kod: {response.status_code}")
                return ""

            # 2. HTML'i parçala
            soup = BeautifulSoup(response.content, 'html.parser')

            # 3. Metni Ayıkla (Strateji: <p> etiketlerini topla)
            # Not: Farklı siteler farklı yapılar kullanır ama <p> genelde standarttır.
            paragraphs = soup.find_all('p')

            # Paragrafları birleştir
            article_text = " ".join([p.get_text() for p in paragraphs])

            # Boşlukları temizle
            clean_text = re.sub(r'\s+', ' ', article_text).strip()

            return clean_text

        except Exception as e:
            print(f"Scraper Hatası: {str(e)}")
            return ""

    def parse_rss(self, rss_url: str) -> list:
        """
        RSS linki verilirse, oradaki son haberlerin linklerini döndürür.
        """
        try:
            feed = feedparser.parse(rss_url)
            news_links = []
            for entry in feed.entries[:10]:  # Son 10 haberi al
                news_links.append({
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.get("published", "")
                })
            return news_links
        except Exception as e:
            print(f"RSS Hatası: {str(e)}")
            return []