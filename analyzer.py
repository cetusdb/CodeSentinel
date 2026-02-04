import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. .env dosyasındaki anahtarı yükle
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Gemini'yi yapılandır
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


def kodu_analiz_et(dosya_yolu):
    # Dosyayı oku
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        kod_icerigi = f.read()

    # AI'ya gönderilecek talimat (Prompt)
    prompt = f"""
    Sen kıdemli bir yazılım mimarısın. Aşağıdaki kodu SOLID prensipleri ve 
    temiz kod kuralları açısından incele. Kısa ve öz bir rapor hazırla.

    Analiz edilecek kod:
    {kod_icerigi}
    """

    # Yanıtı al
    response = model.generate_content(prompt)
    return response.text


# Test etmek için: Projendeki bir dosyayı analiz ettir
# (Örneğin venv içindeki bir dosyayı veya yeni oluşturduğun bir dosyayı seçebilirsin)
rapor = kodu_analiz_et("analyzer.py")
print("--- MIMARI ANALIZ RAPORU ---")
print(rapor)