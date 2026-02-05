from google import genai
import os
from dotenv import load_dotenv

# 1. .env dosyasındaki değişkeni yükle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Client oluştur (v1 zorlaması 404 hatalarını önler)
client = genai.Client(api_key=api_key)

def kodu_analiz_et(dosya_yolu):
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        kod_icerigi = f.read()
    # AI'ya talimat (Prompt)
    analiz_promptu = f"Sen kıdemli bir yazılım mimarısın. Bu kodu analiz et: \n\n{kod_icerigi}"


    # 3. Yanıtı al
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=analiz_promptu  # Değişken adını düzelttik
    )
    return response.text

# Çalıştır
try:
    rapor = kodu_analiz_et("analyzer.py")
    print("--- MIMARI ANALIZ RAPORU ---")
    print(rapor)
except Exception as e:
    print(f"Hata oluştu: {e}")