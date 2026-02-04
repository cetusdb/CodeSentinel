from google import genai
import os
from dotenv import load_dotenv

# 1. .env dosyasındaki anahtarı yükle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Yeni SDK ile Client oluştur
client = genai.Client(api_key=api_key)


def kodu_analiz_et(dosya_yolu):
    # Dosyayı oku
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        kod_icerigi = f.read()

    # AI'ya talimat (Prompt)
    prompt = f"Sen kıdemli bir yazılım mimarısın. Aşağıdaki kodu SOLID ve temiz kod kurallarına göre analiz et: \n\n{kod_icerigi}"

    # 3. Yanıtı yeni yöntemle al
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return response.text


# Çalıştır
rapor = kodu_analiz_et("analyzer.py")
print("--- MIMARI ANALIZ RAPORU ---")
print(rapor)