import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Sayfa Konfigürasyonu
st.set_page_config(page_title="CodeSentinel AI", page_icon="🛡️", layout="wide")

# 1. API Ayarları
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Stil ve Başlık
st.title("🛡️ CodeSentinel: AI Kod Mimarı")
st.markdown("---")


def kodu_analiz_et(kod_icerigi):
    analiz_promptu = f"""
    Sen kıdemli bir yazılım mimarısın. Aşağıdaki kodu analiz et ve sonucu tam olarak şu formatta döndür:

    # MIMARI PUAN: (10 üzerinden)
    ## KRITIK HATALAR:
    ## SOLID PRENSIPLERI:
    ## IYILESTIRME ONERISI:

    Kod:
    {kod_icerigi}
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=analiz_promptu
    )
    return response.text


# Yan Menü (Sidebar)
with st.sidebar:
    st.header("Ayarlar")
    st.info("Analiz etmek istediğiniz Python dosyasını yükleyin.")

# Ana Ekran - Dosya Yükleme
yuklenen_dosya = st.file_uploader("Python Dosyası Seçin", type=["py"])

if yuklenen_dosya is not None:
    # Dosya içeriğini oku
    kod_metni = yuklenen_dosya.read().decode("utf-8")

    # Sol tarafta kodu göster
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📄 Yüklenen Kod")
        st.code(kod_metni, language='python')

    with col2:
        st.subheader("🔍 Analiz Raporu")
        if st.button("Analizi Başlat"):
            with st.spinner("AI Mimarı kodu inceliyor..."):
                try:
                    rapor = kodu_analiz_et(kod_metni)
                    st.markdown(rapor)
                    st.success("Analiz Tamamlandı!")
                except Exception as e:
                    st.error(f"Bir hata oluştu: {e}")
else:
    st.warning("Lütfen bir dosya yükleyin.")