import streamlit as st

st.set_page_config(
    page_title="Portafolio 2 - Valentina Marin",
    page_icon="rocket",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
    background-color: #FFF8F0;
}

.stApp {
    background-color: #FFF8F0;
}

/* Header */
.header-container {
    text-align: center;
    padding: 40px 20px 20px;
    position: relative;
}

.badge {
    display: inline-block;
    background: #1A1A2E;
    color: white;
    font-family: 'Fredoka One', cursive;
    font-size: 0.9rem;
    letter-spacing: 3px;
    padding: 10px 28px;
    border-radius: 999px;
    margin-bottom: 18px;
}

.main-title {
    font-family: 'Fredoka One', cursive;
    font-size: 4rem;
    line-height: 1.1;
    margin-bottom: 10px;
}

.main-title span:nth-child(1)  { color: #EF476F; }
.main-title span:nth-child(2)  { color: #FF9F1C; }
.main-title span:nth-child(3)  { color: #FFD166; }
.main-title span:nth-child(4)  { color: #06D6A0; }
.main-title span:nth-child(5)  { color: #118AB2; }
.main-title span:nth-child(6)  { color: #A259FF; }
.main-title span:nth-child(7)  { color: #FF6B9D; }
.main-title span:nth-child(8)  { color: #EF476F; }
.main-title span:nth-child(9)  { color: #FF9F1C; }
.main-title span:nth-child(10) { color: #FFD166; }
.main-title span:nth-child(11) { color: #06D6A0; }

.subtitle {
    font-family: 'Fredoka One', cursive;
    font-size: 1.6rem;
    color: #1A1A2E;
    margin-top: 6px;
}

/* Rainbow bar */
.rainbow-bar {
    height: 10px;
    background: linear-gradient(90deg,
        #EF476F, #FF9F1C, #FFD166,
        #06D6A0, #118AB2, #A259FF, #FF6B9D,
        #EF476F, #FF9F1C, #FFD166);
    border-radius: 0;
    margin: 30px 0;
}

/* Section title */
.section-title {
    font-family: 'Fredoka One', cursive;
    font-size: 2rem;
    color: #1A1A2E;
    margin-bottom: 6px;
}

.section-line {
    height: 5px;
    border-radius: 99px;
    background: linear-gradient(90deg, #FF6B9D, #FFD166, #06D6A0, #118AB2, #A259FF);
    margin-bottom: 30px;
}

/* Cards */
.card {
    border: 2.5px solid #1A1A2E;
    border-radius: 20px;
    padding: 28px 24px 22px;
    position: relative;
    overflow: hidden;
    box-shadow: 5px 5px 0 #1A1A2E;
    transition: transform 0.2s, box-shadow 0.2s;
    margin-bottom: 24px;
    height: 100%;
}

.card:hover {
    transform: translate(-3px, -3px);
    box-shadow: 8px 8px 0 #1A1A2E;
}

.card-pink   { background: #FFF0F5; }
.card-blue   { background: #F0F8FF; }
.card-green  { background: #F0FFF8; }
.card-yellow { background: #FFFBF0; }
.card-purple { background: #F8F0FF; }
.card-orange { background: #FFF4F0; }
.card-red    { background: #FFF0F2; }

.card-emoji {
    font-size: 2.2rem;
    margin-bottom: 10px;
    display: block;
}

.card-title {
    font-family: 'Fredoka One', cursive;
    font-size: 1.1rem;
    color: #1A1A2E;
    margin-bottom: 8px;
}

.card-desc {
    font-size: 0.88rem;
    color: #555;
    line-height: 1.5;
    margin-bottom: 16px;
}

.btn-pink   { background: #FF6B9D; }
.btn-blue   { background: #118AB2; }
.btn-green  { background: #06D6A0; }
.btn-yellow { background: #FFD166; color: #1A1A2E !important; }
.btn-purple { background: #A259FF; }
.btn-orange { background: #FF9F1C; }
.btn-red    { background: #EF476F; }

.btn {
    display: inline-block;
    text-decoration: none;
    font-family: 'Fredoka One', cursive;
    font-size: 0.95rem;
    padding: 8px 22px;
    border-radius: 999px;
    color: white;
    border: 2px solid #1A1A2E;
    box-shadow: 3px 3px 0 #1A1A2E;
    transition: transform 0.15s, box-shadow 0.15s;
}

.btn:hover {
    transform: translate(-2px,-2px);
    box-shadow: 5px 5px 0 #1A1A2E;
    text-decoration: none;
}

footer-custom {
    text-align: center;
    padding: 20px;
    color: #888;
    font-weight: 700;
    font-size: 0.9rem;
}

/* Hide streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── HEADER ──
st.markdown("""
<div class="header-container">
    <div class="badge">&#10022; ML & AI APPS &middot; STREAMLIT &#10022;</div>
    <div class="main-title">
        <span>P</span><span>O</span><span>R</span><span>T</span><span>A</span><span>F</span><span>O</span><span>L</span><span>I</span><span>O</span><span>&nbsp;2</span>
    </div>
    <div class="subtitle">&#10024; Valentina Mar&#237;n &#10024;</div>
</div>
<div class="rainbow-bar"></div>
""", unsafe_allow_html=True)

# ── PROJECTS SECTION ──
st.markdown("""
<div class="section-title">&#128640; Proyectos</div>
<div class="section-line"></div>
""", unsafe_allow_html=True)

# Projects data
projects = [
    {
        "emoji": "&#128021;",
        "title": "Chatbot sobre razas de perros",
        "desc": "App que permite consultar un PDF sobre razas de perros mediante un chatbot interactivo.",
        "link": "https://chatpdfvalen.streamlit.app/",
        "card_class": "card-pink",
        "btn_class": "btn-pink",
    },
    {
        "emoji": "&#128444;&#65039;",
        "title": "Interpretaci&#243;n de im&#225;genes multimodal",
        "desc": "Los modelos comprenden im&#225;genes y generan texto o descripciones visuales a partir de ellas.",
        "link": "https://imagenchatvalen.streamlit.app/",
        "card_class": "card-blue",
        "btn_class": "btn-blue",
    },
    {
        "emoji": "&#9997;&#65039;",
        "title": "Reconocimiento de D&#237;gitos escritos a mano",
        "desc": "Modelo que identifica y clasifica d&#237;gitos escritos a mano usando visi&#243;n artificial.",
        "link": "https://handwritevalen.streamlit.app/",
        "card_class": "card-green",
        "btn_class": "btn-green",
    },
    {
        "emoji": "&#127912;",
        "title": "Tablero Inteligente",
        "desc": "Lienzo interactivo para dibujar directamente en el navegador con herramientas creativas e IA.",
        "link": "https://drawvalentina.streamlit.app/",
        "card_class": "card-yellow",
        "btn_class": "btn-yellow",
    },
    {
        "emoji": "&#128054;&#128214;",
        "title": "Detector de razas y creador de historias",
        "desc": "Detecta la raza de un perro en una imagen y genera una historia creativa sobre &#233;l.",
        "link": "https://dibujovalen.streamlit.app/",
        "card_class": "card-purple",
        "btn_class": "btn-purple",
    },
    {
        "emoji": "&#127897;&#65039;",
        "title": "Control por Voz",
        "desc": "Interfaz que permite controlar acciones y comandos usando reconocimiento de voz en tiempo real.",
        "link": "https://controlporvozwokwi.streamlit.app/",
        "card_class": "card-orange",
        "btn_class": "btn-orange",
    },
    {
        "emoji": "&#127923;",
        "title": "Controlador de Valen",
        "desc": "Panel de control personalizado con comandos de voz y automatizaciones interactivas.",
        "link": "https://controlporvozwokwi.streamlit.app/",
        "card_class": "card-red",
        "btn_class": "btn-red",
    },
]

# Render in rows of 3
cols_per_row = 3
for i in range(0, len(projects), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(projects):
            p = projects[idx]
            with col:
                st.markdown(f"""
                <div class="card {p['card_class']}">
                    <span class="card-emoji">{p['emoji']}</span>
                    <div class="card-title">{p['title']}</div>
                    <p class="card-desc">{p['desc']}</p>
                    <a class="btn {p['btn_class']}" href="{p['link']}" target="_blank">Abrir app &#8599;</a>
                </div>
                """, unsafe_allow_html=True)

# ── FOOTER ──
st.markdown("<div class='rainbow-bar'></div>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding:20px; color:#888; font-weight:700; font-size:0.9rem;">
    Hecho con &#128150; por <strong>Valentina Mar&#237;n</strong> &nbsp;&middot;&nbsp; Portafolio 2
</div>
""", unsafe_allow_html=True)
