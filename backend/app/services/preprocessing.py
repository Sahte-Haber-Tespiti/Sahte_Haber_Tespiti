import re
import string


class TextPreprocessingService:
    """
    Sorumluluk: Ham metni alır ve modelin anlayacağı 'Tarzanca' (kök/temiz) formata çevirir.
    Eski adı: MetinOnIslemeServisi
    """

    @staticmethod
    def clean_text(text: str) -> str:
        if not isinstance(text, str):
            return ""

        # 1. Küçük harfe çevir
        text = text.lower()

        # 2. URL'leri kaldır
        text = re.sub(r'https?://\S+|www\.\S+', '', text)

        # 3. HTML etiketlerini temizle
        text = re.sub(r'<.*?>', '', text)

        # 4. Noktalama işaretlerini kaldır
        text = text.translate(str.maketrans('', '', string.punctuation))

        # 5. Sayıları temizle
        text = re.sub(r'\d+', '', text)

        # 6. Fazla boşlukları sil ve trimle
        text = re.sub(r'\s+', ' ', text).strip()

        return text