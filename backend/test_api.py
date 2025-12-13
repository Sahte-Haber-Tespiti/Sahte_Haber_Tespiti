#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FastAPI test script - API'yi test eder
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    print("\n" + "="*60)
    print("TEST 1: Root endpoint'i test ediyoruz")
    print("="*60)
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200

def test_analyze_with_text():
    print("\n" + "="*60)
    print("TEST 2: Text ile analiz")
    print("="*60)

    test_data = {
        "text": "Cumhurbaşkanı Erdoğan bugün önemli bir açıklama yaptı. Ekonomik reformlar konusunda detaylı bilgi verdi."
    }

    response = requests.post(f"{BASE_URL}/analyze", json=test_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    assert response.status_code == 200

def test_analyze_with_url():
    print("\n" + "="*60)
    print("TEST 3: URL ile analiz")
    print("="*60)

    test_data = {
        "url": "https://www.trthaber.com/haber/gundem/cumhurbaskani-erdogan-kabine-toplantisina-baskanlik-edecek-819385.html"
    }

    response = requests.post(f"{BASE_URL}/analyze", json=test_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    assert response.status_code == 200

def test_analyze_without_data():
    print("\n" + "="*60)
    print("TEST 4: Boş request (hata bekleniyor)")
    print("="*60)

    test_data = {}

    response = requests.post(f"{BASE_URL}/analyze", json=test_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    assert response.status_code == 400

if __name__ == "__main__":
    print("\n🚀 FastAPI Test Başlıyor...")
    print(f"API URL: {BASE_URL}")
    print("\nÖNCE API SUNUCUSUNU BAŞLATTIĞINIZDAN EMİN OLUN!")
    print("Başlatmak için: cd backend/app && python main.py\n")

    try:
        test_root()
        test_analyze_with_text()
        test_analyze_with_url()
        test_analyze_without_data()

        print("\n" + "="*60)
        print("✅ TÜM TESTLER BAŞARILI!")
        print("="*60)

    except requests.exceptions.ConnectionError:
        print("\n❌ HATA: API sunucusuna bağlanılamadı!")
        print("Lütfen önce API'yi başlatın: cd backend/app && python main.py")
    except AssertionError as e:
        print(f"\n❌ TEST BAŞARISIZ: {e}")
    except Exception as e:
        print(f"\n❌ BEKLENMEYEN HATA: {e}")
