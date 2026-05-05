<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Portafolio 2 · Valentina Marín</title>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet"/>
  <style>
    :root {
      --pink:   #FF6B9D;
      --yellow: #FFD166;
      --green:  #06D6A0;
      --blue:   #118AB2;
      --purple: #A259FF;
      --orange: #FF9F1C;
      --red:    #EF476F;
      --bg:     #FFF8F0;
      --dark:   #1A1A2E;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Nunito', sans-serif;
      background: var(--bg);
      color: var(--dark);
      overflow-x: hidden;
    }

    /* ── CONFETTI BLOBS ── */
    .blob {
      position: absolute;
      border-radius: 50%;
      opacity: 0.18;
      pointer-events: none;
    }

    /* ── HEADER ── */
    header {
      position: relative;
      text-align: center;
      padding: 60px 20px 40px;
      overflow: hidden;
    }

    .blob-1  { width:180px; height:180px; background:var(--pink);   top:-30px;  left:-40px; }
    .blob-2  { width:120px; height:120px; background:var(--green);  top:40px;   left:180px; }
    .blob-3  { width:200px; height:200px; background:var(--yellow); top:-50px;  right:-50px; }
    .blob-4  { width:100px; height:100px; background:var(--blue);   bottom:0;   right:200px; }
    .blob-5  { width:140px; height:140px; background:var(--purple); top:20px;   right:240px; }

    .badge {
      display: inline-block;
      background: var(--dark);
      color: #fff;
      font-family: 'Fredoka One', cursive;
      font-size: 0.85rem;
      letter-spacing: 3px;
      padding: 10px 28px;
      border-radius: 999px;
      margin-bottom: 18px;
      animation: fadeDown 0.6s ease both;
    }

    h1.main-title {
      font-family: 'Fredoka One', cursive;
      font-size: clamp(2.6rem, 7vw, 5rem);
      line-height: 1;
      animation: fadeDown 0.7s 0.1s ease both;
    }

    /* Rainbow letter colors */
    h1.main-title span:nth-child(1)  { color: var(--red);    }
    h1.main-title span:nth-child(2)  { color: var(--orange); }
    h1.main-title span:nth-child(3)  { color: var(--yellow); }
    h1.main-title span:nth-child(4)  { color: var(--green);  }
    h1.main-title span:nth-child(5)  { color: var(--blue);   }
    h1.main-title span:nth-child(6)  { color: var(--purple); }
    h1.main-title span:nth-child(7)  { color: var(--pink);   }
    h1.main-title span:nth-child(8)  { color: var(--red);    }
    h1.main-title span:nth-child(9)  { color: var(--orange); }
    h1.main-title span:nth-child(10) { color: var(--yellow); }
    h1.main-title span:nth-child(11) { color: var(--green);  }

    .subtitle {
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--dark);
      margin-top: 10px;
      letter-spacing: 1px;
      animation: fadeDown 0.7s 0.2s ease both;
    }

    /* ── RAINBOW BAR ── */
    .rainbow-bar {
      height: 10px;
      background: linear-gradient(90deg,
        var(--red), var(--orange), var(--yellow),
        var(--green), var(--blue), var(--purple), var(--pink),
        var(--red), var(--orange), var(--yellow));
      background-size: 200%;
      animation: slide 4s linear infinite;
      margin: 36px 0 0;
    }

    @keyframes slide { from{background-position:0%} to{background-position:200%} }

    /* ── SECTION ── */
    section {
      max-width: 1200px;
      margin: 0 auto;
      padding: 52px 24px 60px;
    }

    .section-title {
      font-family: 'Fredoka One', cursive;
      font-size: 2rem;
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 8px;
    }

    .section-line {
      height: 5px;
      border-radius: 99px;
      background: linear-gradient(90deg, var(--pink), var(--yellow), var(--green), var(--blue), var(--purple));
      margin-bottom: 40px;
    }

    /* ── GRID ── */
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 24px;
    }

    /* ── CARD ── */
    .card {
      background: #fff;
      border: 2.5px solid var(--dark);
      border-radius: 20px;
      padding: 28px 24px 22px;
      position: relative;
      overflow: hidden;
      box-shadow: 5px 5px 0 var(--dark);
      transition: transform 0.2s, box-shadow 0.2s;
      animation: fadeUp 0.5s ease both;
    }

    .card:hover {
      transform: translate(-3px, -3px);
      box-shadow: 8px 8px 0 var(--dark);
    }

    /* Decorative circle top-right */
    .card::after {
      content:'';
      position: absolute;
      width: 80px;
      height: 80px;
      border-radius: 50%;
      top: -20px;
      right: -20px;
      opacity: 0.25;
    }

    /* Card color variants */
    .card:nth-child(1) { background: #FFF0F5; } .card:nth-child(1)::after { background: var(--pink);   }
    .card:nth-child(2) { background: #F0F8FF; } .card:nth-child(2)::after { background: var(--blue);   }
    .card:nth-child(3) { background: #F0FFF8; } .card:nth-child(3)::after { background: var(--green);  }
    .card:nth-child(4) { background: #FFFBF0; } .card:nth-child(4)::after { background: var(--yellow); }
    .card:nth-child(5) { background: #F8F0FF; } .card:nth-child(5)::after { background: var(--purple); }
    .card:nth-child(6) { background: #FFF4F0; } .card:nth-child(6)::after { background: var(--orange); }
    .card:nth-child(7) { background: #FFF0F2; } .card:nth-child(7)::after { background: var(--red);    }

    .card-emoji {
      font-size: 2rem;
      margin-bottom: 12px;
      display: block;
    }

    .card-title {
      font-family: 'Fredoka One', cursive;
      font-size: 1.1rem;
      margin-bottom: 8px;
      color: var(--dark);
    }

    .card-desc {
      font-size: 0.88rem;
      color: #555;
      line-height: 1.5;
      margin-bottom: 18px;
    }

    /* Button per card color */
    .btn {
      display: inline-block;
      text-decoration: none;
      font-family: 'Fredoka One', cursive;
      font-size: 0.9rem;
      padding: 8px 20px;
      border-radius: 999px;
      color: #fff;
      border: 2px solid var(--dark);
      box-shadow: 3px 3px 0 var(--dark);
      transition: transform 0.15s, box-shadow 0.15s;
    }
    .btn:hover {
      transform: translate(-2px,-2px);
      box-shadow: 5px 5px 0 var(--dark);
    }

    .card:nth-child(1) .btn { background: var(--pink);   }
    .card:nth-child(2) .btn { background: var(--blue);   }
    .card:nth-child(3) .btn { background: var(--green);  }
    .card:nth-child(4) .btn { background: var(--yellow); color: var(--dark); }
    .card:nth-child(5) .btn { background: var(--purple); }
    .card:nth-child(6) .btn { background: var(--orange); }
    .card:nth-child(7) .btn { background: var(--red);    }

    /* ── FOOTER ── */
    footer {
      text-align: center;
      padding: 28px 16px 40px;
      font-size: 0.85rem;
      color: #888;
      font-weight: 700;
    }

    /* ── ANIMATIONS ── */
    @keyframes fadeDown {
      from { opacity:0; transform:translateY(-20px); }
      to   { opacity:1; transform:translateY(0); }
    }
    @keyframes fadeUp {
      from { opacity:0; transform:translateY(30px); }
      to   { opacity:1; transform:translateY(0); }
    }

    /* stagger cards */
    .card:nth-child(1) { animation-delay: 0.05s; }
    .card:nth-child(2) { animation-delay: 0.12s; }
    .card:nth-child(3) { animation-delay: 0.19s; }
    .card:nth-child(4) { animation-delay: 0.26s; }
    .card:nth-child(5) { animation-delay: 0.33s; }
    .card:nth-child(6) { animation-delay: 0.40s; }
    .card:nth-child(7) { animation-delay: 0.47s; }
  </style>
</head>
<body>

<!-- ── HEADER ── -->
<header>
  <div class="blob blob-1"></div>
  <div class="blob blob-2"></div>
  <div class="blob blob-3"></div>
  <div class="blob blob-4"></div>
  <div class="blob blob-5"></div>

  <div class="badge">✦ ML &amp; AI APPS · STREAMLIT ✦</div>

  <h1 class="main-title">
    <span>P</span><span>O</span><span>R</span><span>T</span><span>A</span><span>F</span><span>O</span><span>L</span><span>I</span><span>O</span><span> 2</span>
  </h1>

  <p class="subtitle">✨ Valentina Marín ✨</p>
</header>

<div class="rainbow-bar"></div>

<!-- ── PROJECTS ── -->
<section>
  <h2 class="section-title">🚀 Proyectos</h2>
  <div class="section-line"></div>

  <div class="grid">

    <div class="card">
      <span class="card-emoji">🐕</span>
      <div class="card-title">Chatbot sobre razas de perros</div>
      <p class="card-desc">App que permite consultar un PDF sobre razas de perros mediante un chatbot interactivo.</p>
      <a class="btn" href="https://chatpdfvalen.streamlit.app/" target="_blank">Abrir app ↗</a>
    </div>

    <div class="card">
      <span class="card-emoji">🖼️</span>
      <div class="card-title">Interpretación de imágenes multimodal</div>
      <p class="card-desc">Los modelos comprenden imágenes y generan texto o descripciones visuales a partir de ellas.</p>
      <a class="btn" href="https://imagenchatvalen.streamlit.app/" target="_blank">Abrir app ↗</a>
    </div>

    <div class="card">
      <span class="card-emoji">✍️</span>
      <div class="card-title">Reconocimiento de Dígitos escritos a mano</div>
      <p class="card-desc">Modelo que identifica y clasifica dígitos escritos a mano usando visión artificial.</p>
      <a class="btn" href="https://handwritevalen.streamlit.app/" target="_blank">Abrir app ↗</a>
    </div>

    <div class="card">
      <span class="card-emoji">🎨</span>
      <div class="card-title">Tablero Inteligente</div>
      <p class="card-desc">Lienzo interactivo para dibujar directamente en el navegador con herramientas creativas e IA.</p>
      <a class="btn" href="https://drawvalentina.streamlit.app/" target="_blank">Abrir app ↗</a>
    </div>

    <div class="card">
      <span class="card-emoji">🐶📖</span>
      <div class="card-title">Detector de razas y creador de historias</div>
      <p class="card-desc">Detecta la raza de un perro en una imagen y genera una historia creativa sobre él.</p>
      <a class="btn" href="https://dibujovalen.streamlit.app/" target="_blank">Abrir app ↗</a>
    </div>

    <div class="card">
      <span class="card-emoji">🎙️</span>
      <div class="card-title">Control por Voz</div>
      <p class="card-desc">Interfaz que permite controlar acciones y comandos usando reconocimiento de voz en tiempo real.</p>
      <a class="btn" href="https://controlporvozwokwi.streamlit.app/" target="_blank">Abrir app ↗</a>
    </div>

    <div class="card">
      <span class="card-emoji">🎛️</span>
      <div class="card-title">Controlador de Valen</div>
      <p class="card-desc">Panel de control personalizado con comandos de voz y automatizaciones interactivas.</p>
      <a class="btn" href="https://controlporvozwokwi.streamlit.app/" target="_blank">Abrir app ↗</a>
    </div>

  </div>
</section>

<div class="rainbow-bar"></div>

<footer>
  Hecho con 💖 por <strong>Valentina Marín</strong> · Portafolio 2
</footer>

</body>
</html>
