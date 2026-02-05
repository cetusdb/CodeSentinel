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
    prompt = f"""
        Sen kıdemli bir yazılım mimarısın. Aşağıdaki kodu analiz et ve sonucu tam olarak şu formatta döndür:

        1. MİMARİ PUAN: (10 üzerinden bir not ver)
        2. KRİTİK HATALAR: (Eğer varsa güvenlik veya mantık hataları)
        3. SOLID PRENSİPLERİ: (Hangi prensiplere uyulmuş, hangileri ihlal edilmiş?)
        4. İYİLEŞTİRME ÖNERİSİ: (Kodu daha profesyonel yapmak için 1 somut tavsiye)

        Analiz edilecek kod:
        {kod_icerigi}
        """
    # 3. Yanıtı yeni yöntemle al
    # response çağrısını şu şekilde değiştir:
    # 3. Yanıtı yeni yöntemle al
    response = client.models.generate_content(
        model="gemini-1.5-flash",  # Hata devam ederse "models/gemini-1.5-flash" olarak dene
        contents=prompt
    )

    return response.text


# Çalıştır
rapor = kodu_analiz_et("analyzer.py")
print("--- MIMARI ANALIZ RAPORU ---")
print(rapor)