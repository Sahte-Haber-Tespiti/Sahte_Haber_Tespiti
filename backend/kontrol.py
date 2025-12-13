import pandas as pd
import os

# Dosya yollarını bul
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')

try:
    # Dosyaları oku
    df_final = pd.read_csv(os.path.join(data_dir, 'final_dataset.csv'))
    df_ek = pd.read_csv(os.path.join(data_dir, 'ek_veri.csv'))

    print("--- 1. DOSYA: final_dataset.csv ---")
    print(df_final['label'].value_counts())
    print("\nÖrnek 0 (Gerçek mi Sahte mi oku):")
    print(df_final[df_final['label'] == 0]['text'].iloc[0][:100])
    print("\nÖrnek 1 (Gerçek mi Sahte mi oku):")
    print(df_final[df_final['label'] == 1]['text'].iloc[0][:100])

    print("\n" + "="*30 + "\n")

    print("--- 2. DOSYA: ek_veri.csv ---")
    print(df_ek['label'].value_counts())
    try:
        print("\nÖrnek 0 (Burası da diğer dosyayla aynı mantıkta mı?):")
        print(df_ek[df_ek['label'] == 0]['text'].iloc[0][:100])
        print("\nÖrnek 1 (Burası da diğer dosyayla aynı mantıkta mı?):")
        print(df_ek[df_ek['label'] == 1]['text'].iloc[0][:100])
    except:
        print("Örnek alınamadı (belki bu label yok).")

    # Birleştirilmiş kontrol
    df_combined = pd.concat([df_final, df_ek], ignore_index=True)
    print("\n" + "="*30 + "\n")
    print("--- TOPLAM DURUM ---")
    print(f"Toplam Veri Sayısı: {len(df_combined)}")
    print(df_combined['label'].value_counts())

except Exception as e:
    print(f"Hata: {e}")