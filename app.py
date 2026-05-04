import streamlit as st

st.set_page_config(page_title="Mi Portafolio", layout="wide")

# 🎨 CSS personalizado (ESTILO BONITO)
st.markdown("""
<style>
body {
    background-color: #f8f5f0;
}
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    margin-bottom: 30px;
}
.card {
    padding: 20px;
    border-radius: 20px;
    background-color: white;
    box-shadow: 2px 4px 15px rgba(0,0,0,0.1);
    text-align: center;
}
.stButton>button {
    border-radius: 10px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# 🏷️ TÍTULO
st.markdown("<div class='title'>🚀 Mi Portafolio</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>ML & AI Apps con Streamlit</div>", unsafe_allow_html=True)

st.markdown("---")

# 📦 TARJETAS (3 columnas)
col1, col2, col3 = st.columns(3)

# 🤖 CHATBOT
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🤖 Chatbot")
    st.write("Asistente con NLP.")
    if st.button("Abrir Chatbot"):
        st.switch_page("pages/chatbot.py")
    st.markdown("</div>", unsafe_allow_html=True)

# 😊 EMOCIONES
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("😊 Emociones")
    st.write("Detecta emociones en texto.")
    if st.button("Abrir Emociones"):
        st.switch_page("pages/emociones.py")
    st.markdown("</div>", unsafe_allow_html=True)

# 👁️ VISIÓN
with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("👁️ Visión")
    st.write("Reconocimiento de imágenes.")
    if st.button("Abrir Visión"):
        st.switch_page("pages/vision.py")
    st.markdown("</div>", unsafe_allow_html=True)
