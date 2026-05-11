import streamlit as st

st.set_page_config(
    page_title="Portafolio 2 - Valentina Marin",
    page_icon="sparkles",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif;
    background-color: #0D0D0D;
}

.stApp {
    background-color: #0D0D0D;
}

.header-wrap {
    text-align: center;
    padding: 56px 20px 20px;
}

.pill-badge {
    display: inline-block;
    background: transparent;
    color: #E8FF47;
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 0.78rem;
    letter-spacing: 5px;
    text-transform: uppercase;
    border: 2px solid #E8FF47;
    padding: 7px 26px;
    border-radius: 999px;
    margin-bottom: 24px;
}

.main-title {
    font-family: 'Pacifico', cursive;
    font-size: clamp(3rem, 8vw, 5.5rem);
    line-height: 1.05;
    background: linear-gradient(135deg, #FF3CAC, #784BA0, #2B86C5, #00F5D4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 14px;
}

.subtitle {
    font-family: 'Pacifico', cursive;
    font-size: 1.4rem;
    color: #E8FF47;
    letter-spacing: 1px;
}

.neon-line {
    height: 2px;
    background: linear-gradient(90deg,
        transparent, #FF3CAC, #784BA0, #2B86C5, #00F5D4, transparent);
    margin: 40px auto;
    max-width: 700px;
    border-radius: 2px;
}

.section-heading {
    font-family: 'Pacifico', cursive;
    font-size: 2rem;
    color: #ffffff;
    margin-bottom: 4px;
}

.section-underline {
    width: 80px;
    height: 4px;
    background: #E8FF47;
    border-radius: 99px;
    margin-bottom: 32px;
}

.card {
    border-radius: 18px;
    padding: 30px 26px 24px;
    position: relative;
    overflow: hidden;
    margin-bottom: 24px;
    height: 100%;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    border: 1.5px solid rgba(255,255,255,0.08);
}

.card:hover {
    transform: translateY(-6px);
}

.card::before {
    content: '';
    position: absolute;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    top: -30px;
    right: -30px;
    opacity: 0.35;
    filter: blur(30px);
}

.card-magenta { background: #1A0A14; box-shadow: 0 4px 30px rgba(255,60,172,0.15); }
.card-magenta::before { background: #FF3CAC; }

.card-cyan { background: #091516; box-shadow: 0 4px 30px rgba(0,245,212,0.12); }
.card-cyan::before { background: #00F5D4; }

.card-indigo { background: #0E0A1A; box-shadow: 0 4px 30px rgba(120,75,160,0.2); }
.card-indigo::before { background: #784BA0; }

.card-lime { background: #111500; box-shadow: 0 4px 30px rgba(232,255,71,0.12); }
.card-lime::before { background: #E8FF47; }

.card-blue { background: #060D1A; box-shadow: 0 4px 30px rgba(43,134,197,0.15); }
.card-blue::before { background: #2B86C5; }

.card-coral { background: #1A0D08; box-shadow: 0 4px 30px rgba(255,107,57,0.15); }
.card-coral::before { background: #FF6B39; }

.card-violet { background: #0F0818; box-shadow: 0 4px 30px rgba(189,100,255,0.15); }
.card-violet::before { background: #BD64FF; }

.card-emoji {
    font-size: 2.4rem;
    margin-bottom: 14px;
    display: block;
}

.card-title {
    font-family: 'Pacifico', cursive;
    font-size: 1rem;
    color: #ffffff;
    margin-bottom: 10px;
    line-height: 1.4;
}

.card-desc {
    font-size: 0.87rem;
    color: #aaa;
    line-height: 1.6;
    margin-bottom: 20px;
    font-weight: 500;
}

.btn {
    display: inline-block;
    text-decoration: none;
    font-family: 'Quicksand', sans-serif;
    font-weight: 700;
    font-size: 0.88rem;
    padding: 9px 22px;
    border-radius: 999px;
    letter-spacing: 0.5px;
    transition: opacity 0.2s, transform 0.2s;
}

.btn:hover {
    opacity: 0.85;
    transform: scale(1.04);
    text-decoration: none;
}

.btn-magenta { background: #FF3CAC; color: #fff; }
.btn-cyan    { background: #00F5D4; color: #0D0D0D; }
.btn-indigo  { background: #784BA0; color: #fff; }
.btn-lime    { background: #E8FF47; color: #0D0D0D; }
.btn-blue    { background: #2B86C5; color: #fff; }
.btn-coral   { background: #FF6B39; color: #fff; }
.btn-violet  { background: #BD64FF; color: #fff; }

.footer-text {
    text-align: center;
    padding: 28px 16px 40px;
    color: #555;
    font-weight: 600;
    font-size: 0.88rem;
}

.footer-text strong { color: #E8FF47; }

#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="header-wrap">
    <div class="pill-badge">&#10022; Streamlit Apps &nbsp;&bull;&nbsp; ML &amp; AI &#10022;</div>
    <div class="main-title">Portafolio 2</div>
    <div class="subtitle">Valentina Mar&#237;n</div>
</div>
<div class="neon-line"></div>
""", unsafe_allow_html=True)

# SECTION TITLE
st.markdown("""
<div class="section-heading">&#127775; Proyectos</div>
<div class="section-underline"></div>
""", unsafe_allow_html=True)

# PROJECTS
projects = [
    {
        "emoji": "&#128104;&#8205;&#127979;",
        "title": "Intro p&#225;gina profe",
        "desc": "P&#225;gina de introducci&#243;n del profesor, punto de partida del curso.",
        "link": "https://elprofe.streamlit.app/",
        "card": "card-cyan",
        "btn": "btn-cyan",
    },
    {
        "emoji": "&#127774;",
        "title": "Intro mi p&#225;gina",
        "desc": "Mi p&#225;gina de presentaci&#243;n personal como desarrolladora de apps con Streamlit.",
        "link": "https://kattyperry.streamlit.app/",
        "card": "card-magenta",
        "btn": "btn-magenta",
    },
    {
        "emoji": "&#128270;",
        "title": "OCR",
        "desc": "Reconocimiento &#243;ptico de caracteres: extrae texto de im&#225;genes de forma autom&#225;tica.",
        "link": "https://ocrvalentina.streamlit.app/",
        "card": "card-indigo",
        "btn": "btn-indigo",
    },
    {
        "emoji": "&#127908;",
        "title": "OCR Audio",
        "desc": "Extrae texto de im&#225;genes con OCR y lo convierte en audio de forma autom&#225;tica.",
        "link": "https://ocraudiovalen.streamlit.app/",
        "card": "card-lime",
        "btn": "btn-lime",
    },
    {
        "emoji": "&#128514;",
        "title": "Sentimientos GIFs",
        "desc": "Detecta el sentimiento de un texto y responde con un GIF animado acorde a la emoci&#243;n.",
        "link": "https://sentimientosvalen.streamlit.app/",
        "card": "card-coral",
        "btn": "btn-coral",
    },
    {
        "emoji": "&#127468;&#127463;",
        "title": "TDF Ingl&#233;s",
        "desc": "Aplicaci&#243;n de preguntas y respuestas en ingl&#233;s con modelos de lenguaje.",
        "link": "https://funcionapuessss.streamlit.app/",
        "card": "card-blue",
        "btn": "btn-blue",
    },
    {
        "emoji": "&#127466;&#127480;",
        "title": "TDF Espa&#241;ol",
        "desc": "Aplicaci&#243;n de preguntas y respuestas en espa&#241;ol con modelos de lenguaje.",
        "link": "https://espanolpreguntas.streamlit.app/",
        "card": "card-violet",
        "btn": "btn-violet",
    },
    {
        "emoji": "&#128266;",
        "title": "Texto a Audio",
        "desc": "Convierte cualquier texto en audio con opciones de idioma y voz personalizables.",
        "link": "https://otromas.streamlit.app/",
        "card": "card-magenta",
        "btn": "btn-magenta",
    },
    {
        "emoji": "&#127760;",
        "title": "Traductor",
        "desc": "Traductor autom&#225;tico entre idiomas usando modelos de lenguaje natural.",
        "link": "https://traductorvalen.streamlit.app/",
        "card": "card-cyan",
        "btn": "btn-cyan",
    },
    {
        "emoji": "&#9928;&#65039;",
        "title": "WordCloud",
        "desc": "Genera nubes de palabras visuales a partir de cualquier texto ingresado.",
        "link": "https://wordcloudvalen.streamlit.app/",
        "card": "card-lime",
        "btn": "btn-lime",
    },
    {
        "emoji": "&#128100;",
        "title": "Detecci&#243;n de Personas (YOLO)",
        "desc": "Detecta y resalta personas en im&#225;genes o video en tiempo real usando el modelo YOLO.",
        "link": "https://yoloreconocimiento.streamlit.app/",
        "card": "card-indigo",
        "btn": "btn-indigo",
    },
    {
        "emoji": "&#128400;&#65039;",
        "title": "Detector Gestos / Persona",
        "desc": "Reconoce gestos y movimientos de personas usando visi&#243;n artificial en tiempo real.",
        "link": "https://dectectordegestos.streamlit.app/",
        "card": "card-coral",
        "btn": "btn-coral",
    },
    {
        "emoji": "&#128021;",
        "title": "Chatbot sobre razas de perros",
        "desc": "Consulta un PDF sobre razas de perros mediante un chatbot interactivo con procesamiento de lenguaje natural.",
        "link": "https://chatpdfvalen.streamlit.app/",
        "card": "card-magenta",
        "btn": "btn-magenta",
    },
    {
        "emoji": "&#128247;",
        "title": "Interpretaci&#243;n de im&#225;genes multimodal",
        "desc": "Modelos que comprenden im&#225;genes y generan texto o descripciones visuales a partir de ellas.",
        "link": "https://imagenchatvalen.streamlit.app/",
        "card": "card-cyan",
        "btn": "btn-cyan",
    },
    {
        "emoji": "&#9997;&#65039;",
        "title": "Reconocimiento de D&#237;gitos a mano",
        "desc": "Modelo de visi&#243;n artificial que identifica y clasifica d&#237;gitos escritos a mano en tiempo real.",
        "link": "https://handwritevalen.streamlit.app/",
        "card": "card-indigo",
        "btn": "btn-indigo",
    },
    {
        "emoji": "&#127912;",
        "title": "Tablero Inteligente",
        "desc": "Lienzo interactivo para dibujar directamente en el navegador con herramientas creativas e IA.",
        "link": "https://drawvalentina.streamlit.app/",
        "card": "card-lime",
        "btn": "btn-lime",
    },
    {
        "emoji": "&#128054;&#10024;",
        "title": "Detector de razas y creador de historias",
        "desc": "Detecta la raza de un perro en una fotograf&#237;a y genera autom&#225;ticamente una historia creativa sobre &#233;l.",
        "link": "https://dibujovalen.streamlit.app/",
        "card": "card-blue",
        "btn": "btn-blue",
    },
    {
        "emoji": "&#127897;&#65039;",
        "title": "Control por Voz",
        "desc": "Interfaz que permite controlar acciones y comandos usando reconocimiento de voz en tiempo real.",
        "link": "https://controlporvozwokwi.streamlit.app/",
        "card": "card-coral",
        "btn": "btn-coral",
    },
    {
        "emoji": "&#127923;",
        "title": "Controlador de Valen",
        "desc": "Panel de control personalizado con comandos de voz y automatizaciones interactivas.",
        "link": "https://controlporvozwokwi.streamlit.app/",
        "card": "card-violet",
        "btn": "btn-violet",
    },
]

cols_per_row = 3
for i in range(0, len(projects), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(projects):
            p = projects[idx]
            with col:
                st.markdown(f"""
                <div class="card {p['card']}">
                    <span class="card-emoji">{p['emoji']}</span>
                    <div class="card-title">{p['title']}</div>
                    <p class="card-desc">{p['desc']}</p>
                    <a class="btn {p['btn']}" href="{p['link']}" target="_blank">Abrir app &#8599;</a>
                </div>
                """, unsafe_allow_html=True)

# FOOTER
st.markdown('<div class="neon-line"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer-text">
    hecho con &#128150; por <strong>Valentina Mar&#237;n</strong> &nbsp;&#183;&nbsp; Portafolio 2
</div>
""", unsafe_allow_html=True)
