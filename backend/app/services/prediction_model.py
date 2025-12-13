import joblib
import os
import sys


class PredictionModel:
    """
    Sorumluluk: Eğitilmiş yapay zeka modelini yükler ve tahmin yapar.
    DURUM: 0=SAHTE, 1=GERÇEK (Eğitim testi ile doğrulandı)
    """

    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.load_model()

    def load_model(self):
        try:
            # backend/ml_models klasörünü bul
            current_file = os.path.abspath(__file__)
            # services -> app -> backend -> root (bir üst klasörde ml_models var)
            backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
            models_path = os.path.join(backend_dir, "ml_models")

            model_file = os.path.join(models_path, "model.pkl")
            vect_file = os.path.join(models_path, "vectorizer.pkl")

            if not os.path.exists(model_file):
                print(f"❌ HATA: Model dosyası bulunamadı: {model_file}")
                return

            self.model = joblib.load(model_file)
            self.vectorizer = joblib.load(vect_file)
            print("✅ BAŞARILI: Model ve Vektörleştirici API'ye yüklendi.")

        except Exception as e:
            print(f"❌ Model Yükleme Hatası: {e}")

    def predict(self, text: str) -> dict:
        """
        Dönüş Formatı:
        {
            "is_fake": True/False,
            "confidence_score": 95.5,
            "label": "SAHTE" / "GERÇEK"
        }
        """
        if not self.model:
            return {"error": "Model yok", "is_fake": False, "confidence_score": 0}

        try:
            # 1. Metni vektöre çevir
            vectorized = self.vectorizer.transform([text.lower()])  # Küçültme önemli!

            # 2. Olasılıkları al
            # Eğitimde doğruladık: Classes [0, 1] -> 0=SAHTE, 1=GERÇEK
            probs = self.model.predict_proba(vectorized)[0]

            prob_fake = probs[0]  # İndeks 0 (SAHTE Olasılığı)
            prob_real = probs[1]  # İndeks 1 (GERÇEK Olasılığı)

            # 3. Karar Ver
            if prob_fake > prob_real:
                return {
                    "is_fake": True,
                    "confidence_score": float(round(prob_fake * 100, 2)),
                    "label": "SAHTE"
                }
            else:
                return {
                    "is_fake": False,
                    "confidence_score": float(round(prob_real * 100, 2)),
                    "label": "GERÇEK"
                }

        except Exception as e:
            print(f"Tahmin Hatası: {e}")
            return {"label": "HATA", "confidence_score": 0, "is_fake": False}