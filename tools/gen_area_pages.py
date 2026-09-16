#!/usr/bin/env python3
"""Dev-time only: generates the 6 areas/*.html pages from AREAS content below.
Not referenced by the live site — safe to delete once pages are hand-edited."""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "areas")
os.makedirs(OUT_DIR, exist_ok=True)

WA = "18097499916"
CHECK_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 13l4 4L19 7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

AREAS = [
    {
        "slug": "perdida-de-peso",
        "img": "area-perdida-peso.jpg",
        "title": "Pérdida de peso",
        "card_desc": "Un proceso sostenible, sin dietas restrictivas ni resultados exprés.",
        "subtitle": "Un cambio que se sostiene, no una dieta de temporada.",
        "lede": "Bajar de peso no es solo comer menos: es entender por qué tu cuerpo llegó a este punto y qué necesita para cambiar de una forma que puedas mantener con el tiempo. Muchas personas llegan a consulta después de haber probado varias dietas restrictivas que funcionaron unas semanas y luego se abandonaron.",
        "help": "Un plan de alimentación bien diseñado crea un déficit calórico que tu cuerpo puede sostener sin pasar hambre constante ni eliminar grupos de alimentos completos. La meta es que el cambio se sienta manejable en tu día a día, no una prueba de voluntad.",
        "evaluate": [
            "Historia de peso: subidas, bajadas e intentos previos",
            "Hábitos alimenticios actuales y horarios reales",
            "Relación con la comida y patrones de comer emocional",
            "Nivel de actividad física",
            "Antropometría inicial: composición corporal, no solo la báscula",
        ],
        "structure": "Empezamos con ajustes que se puedan sostener desde la primera semana, priorizando la calidad de las comidas antes que la restricción severa. El plan se revisa y se ajusta según cómo responde tu cuerpo y tu rutina — no según una fórmula fija para todos.",
        "strategies": [
            "Ajuste progresivo de porciones sin pasar hambre",
            "Organización de comidas según tu horario real (trabajo, familia, entrenamientos)",
            "Herramientas para manejar antojos y comer emocional",
            "Estrategias para comer fuera de casa sin descarrilar el plan",
        ],
        "followup": "El peso no baja de forma lineal, y eso es normal. El seguimiento nos permite distinguir entre una meseta esperada y un ajuste que realmente hace falta, y adaptar el plan antes de que pierdas motivación.",
        "particular_title": "Lo particular de este abordaje",
        "particular": "A diferencia de un plan genérico de “contar calorías”, aquí el punto de partida es tu relación con la comida y tu rutina real — no una tabla estándar que ignora cómo vives.",
        "closing": "Si llevas tiempo intentando bajar de peso por tu cuenta sin resultados que se sostengan, una evaluación nutricional es el primer paso para entender qué necesita tu cuerpo específicamente.",
        "note": None,
    },
    {
        "slug": "aumento-de-peso",
        "img": "area-aumento-peso.jpg",
        "title": "Aumento de peso",
        "card_desc": "Ganar peso de forma saludable también requiere una estrategia.",
        "subtitle": "Ganar peso también es un proceso que se planifica.",
        "lede": "Aumentar de peso puede ser tan difícil como bajarlo, sobre todo cuando el apetito es bajo, hay antecedentes de bajo peso, o se busca ganar masa muscular de forma específica. No se trata simplemente de “comer más de todo”.",
        "help": "Diseñamos un plan con superávit calórico que prioriza la calidad nutricional: no cualquier caloría cuenta igual cuando el objetivo es ganar tejido magro y no solo mover la cifra en la báscula.",
        "evaluate": [
            "Apetito, saciedad temprana y hábitos de comida actuales",
            "Antecedentes médicos que puedan explicar la dificultad para ganar peso",
            "Nivel y tipo de actividad física (¿entrenas fuerza?)",
            "Antropometría que distingue masa grasa de masa muscular",
        ],
        "structure": "Aumentamos la densidad calórica y la frecuencia de comidas de forma gradual, sin generar malestar digestivo ni la sensación de estar “obligado a comer”. Si entrenas, el plan se alinea a tus sesiones para apoyar la recuperación.",
        "strategies": [
            "Comidas y snacks más densos en energía sin depender de ultraprocesados",
            "Distribución de proteína a lo largo del día para apoyar la ganancia muscular",
            "Ajustes específicos si hay saciedad temprana o poco apetito",
            "Coordinación con tu rutina de entrenamiento, si aplica",
        ],
        "followup": "Revisamos composición corporal — no solo el peso total — para confirmar que la ganancia es la que buscas: masa muscular, no solo grasa.",
        "particular_title": "Lo particular de este abordaje",
        "particular": "Este es de los procesos donde más rápido se nota si el plan no está bien calibrado. Por eso el seguimiento cercano es clave desde el inicio, ajustando antes de que pasen semanas sin cambios.",
        "closing": "Si sientes que “no importa cuánto comas, no subes”, vale la pena evaluar qué está pasando antes de seguir intentando por ensayo y error.",
        "note": None,
    },
    {
        "slug": "diabetes-tipo-2",
        "img": "area-diabetes.jpg",
        "title": "Diabetes mellitus tipo 2",
        "card_desc": "Manejo nutricional del azúcar en sangre, en conjunto con tu médico.",
        "subtitle": "La alimentación como parte del manejo, junto a tu tratamiento médico.",
        "lede": "La alimentación es una de las herramientas más importantes para el manejo de la diabetes tipo 2, junto con el tratamiento médico. Un plan adecuado ayuda a mantener niveles de glucosa más estables en el día a día.",
        "help": "A través del ajuste de la cantidad y el tipo de carbohidratos, su distribución en el día y su combinación con otros alimentos, buscamos evitar picos de glucosa pronunciados y apoyar el control metabólico general, siempre junto a tu tratamiento médico.",
        "evaluate": [
            "Tipo de tratamiento actual, en coordinación con tu médico",
            "Patrones de alimentación y horarios de medicación, si aplica",
            "Antecedentes familiares y otros factores de riesgo cardiovascular",
            "Composición corporal",
        ],
        "structure": "El plan no elimina los carbohidratos: los organiza. Trabajamos en el tipo, la cantidad y el momento en que los consumes, siempre en coordinación con el manejo médico que ya tengas.",
        "strategies": [
            "Distribución de carbohidratos a lo largo del día",
            "Combinaciones de alimentos que ayudan a moderar la respuesta glucémica",
            "Ajustes según actividad física y horarios de medicación",
            "Educación para leer etiquetas e identificar azúcares ocultos",
        ],
        "followup": "El seguimiento es especialmente importante aquí, porque los ajustes en el tratamiento médico pueden requerir cambios en el plan alimentario, y viceversa.",
        "particular_title": "Lo particular de este abordaje",
        "particular": "Este trabajo siempre se coordina con tu médico tratante. La nutrición complementa el manejo médico de la diabetes — no lo reemplaza ni toma decisiones sobre tu medicación.",
        "closing": "Si te diagnosticaron diabetes tipo 2 recientemente, o sientes que no tienes claro cómo comer con tu condición, una evaluación nutricional te puede dar ese mapa.",
        "note": "Este abordaje se trabaja siempre en conjunto con el médico que te da seguimiento — la nutrición es un complemento del tratamiento médico, no un sustituto.",
    },
    {
        "slug": "hipertension-arterial",
        "img": "area-hipertension.jpg",
        "title": "Hipertensión arterial",
        "card_desc": "Estrategias alimentarias para acompañar el control de la presión arterial.",
        "subtitle": "Ajustes concretos, más allá de “quitar la sal de la mesa”.",
        "lede": "La alimentación tiene un rol comprobado en el manejo de la presión arterial, especialmente a través del sodio, el patrón general de la dieta y el peso corporal.",
        "help": "Un plan ajustado en sodio, con énfasis en alimentos ricos en potasio, magnesio y fibra, puede contribuir al control de la presión arterial como parte de un abordaje conjunto con tu médico.",
        "evaluate": [
            "Consumo actual de sodio — muchas veces oculto en alimentos procesados",
            "Patrón de alimentación general y consumo de alcohol",
            "Peso corporal y nivel de actividad física",
            "Tratamiento médico actual",
        ],
        "structure": "No se trata solo de “quitar la sal de la mesa”: la mayoría del sodio que consumimos viene de alimentos procesados y comidas fuera de casa. Identificamos esas fuentes y las ajustamos de forma realista para tu rutina.",
        "strategies": [
            "Identificación de fuentes ocultas de sodio en tu alimentación actual",
            "Incorporación de alimentos ricos en potasio y magnesio",
            "Estrategias de sazón sin depender de la sal",
            "Ajustes si hay sobrepeso asociado",
        ],
        "followup": "Revisamos cómo responde tu presión arterial con los cambios implementados, siempre en coordinación con el control que lleva tu médico.",
        "particular_title": "Lo particular de este abordaje",
        "particular": "Aquí el trabajo de “detective” con las etiquetas y los alimentos procesados es central: el sodio oculto suele ser el principal punto de ajuste, más que la sal que agregas tú mismo.",
        "closing": "Si tienes hipertensión y quieres saber qué cambios alimentarios realmente hacen diferencia, empecemos con una evaluación.",
        "note": "El manejo nutricional de la hipertensión se trabaja junto al control médico que ya llevas — nunca como reemplazo de tu tratamiento.",
    },
    {
        "slug": "dislipidemias",
        "img": "area-dislipidemia.jpg",
        "title": "Dislipidemias",
        "card_desc": "Ajustes en el tipo de grasas y fibra de tu alimentación.",
        "subtitle": "El tipo de grasa importa tanto como la cantidad.",
        "lede": "Cuando los niveles de colesterol o triglicéridos están fuera de rango, la alimentación es una de las primeras herramientas de manejo, junto con el seguimiento médico correspondiente.",
        "help": "El enfoque se centra en el tipo de grasas que consumes (no solo la cantidad), el aporte de fibra soluble y el patrón general de alimentación — factores con impacto directo en el perfil lipídico.",
        "evaluate": [
            "Tipo de dislipidemia: colesterol LDL, triglicéridos, o ambos",
            "Patrón actual de consumo de grasas, fibra, alcohol y azúcares simples",
            "Antecedentes familiares",
            "Otros factores de riesgo cardiovascular presentes",
        ],
        "structure": "Ajustamos la calidad de las grasas —priorizando las insaturadas sobre las saturadas y evitando las grasas trans—, aumentamos la fibra soluble, y revisamos el consumo de azúcares simples si los triglicéridos están elevados.",
        "strategies": [
            "Sustitución de grasas saturadas por fuentes insaturadas",
            "Incorporación progresiva de fibra soluble (avena, leguminosas, frutas)",
            "Ajuste de azúcares simples y alcohol, según tu caso",
            "Lectura de etiquetas para identificar grasas trans",
        ],
        "followup": "Los marcadores de laboratorio que tu médico solicita periódicamente nos ayudan a confirmar si los ajustes están funcionando, y a afinar el plan con datos objetivos.",
        "particular_title": "Lo particular de este abordaje",
        "particular": "Aquí trabajamos mucho con tus resultados de laboratorio como guía objetiva del progreso — más allá de cómo te sientes día a día, que no siempre refleja lo que está pasando internamente.",
        "closing": "Si tu médico te indicó cambios en la alimentación por tus niveles de lípidos, una evaluación nutricional te ayuda a llevarlos a la práctica de forma concreta.",
        "note": "Trabajamos con tus resultados de laboratorio y en coordinación con el médico que te da seguimiento por tus niveles de colesterol o triglicéridos.",
    },
    {
        "slug": "sindrome-metabolico",
        "img": "area-sindrome-metabolico.jpg",
        "title": "Síndrome metabólico",
        "card_desc": "Un abordaje integral cuando varios factores de riesgo se combinan.",
        "subtitle": "Varios factores a la vez, con un solo plan integrado.",
        "lede": "El síndrome metabólico combina varios factores —como grasa abdominal, presión arterial, glucosa y lípidos alterados— que juntos aumentan el riesgo cardiovascular. Por eso el abordaje nutricional también es integral.",
        "help": "En lugar de tratar cada factor por separado, el plan de alimentación se diseña para impactar varios a la vez: composición corporal, sensibilidad a la insulina, presión arterial y perfil lipídico.",
        "evaluate": [
            "Composición corporal y distribución de grasa, especialmente abdominal",
            "Patrones de alimentación y nivel de actividad física",
            "Resultados médicos relacionados con cada factor presente en tu caso",
        ],
        "structure": "Priorizamos los cambios con mayor impacto combinado —como la reducción de grasa abdominal y la mejora en la calidad general de la dieta— antes de entrar en ajustes más específicos por factor.",
        "strategies": [
            "Reducción progresiva de grasa abdominal a través del plan alimentario",
            "Ajuste de carbohidratos y grasas según los factores presentes",
            "Incorporación de fibra y alimentos de bajo impacto en la glucosa",
            "Alineación con tu actividad física y tratamiento médico",
        ],
        "followup": "Por ser un abordaje con varios frentes a la vez, el seguimiento cercano permite ver qué está respondiendo mejor y ajustar prioridades sobre la marcha.",
        "particular_title": "Lo particular de este abordaje",
        "particular": "A diferencia de un plan enfocado en una sola condición, aquí se busca el mayor impacto posible en los distintos factores a la vez, priorizando lo que más beneficio trae primero.",
        "closing": "Si tienes varios de estos factores presentes, una evaluación nutricional integral es el punto de partida para abordarlos de forma coordinada.",
        "note": "El síndrome metabólico se maneja en conjunto con tu médico, dando seguimiento a cada factor de riesgo presente en tu caso.",
    },
]

NAV = """<header class="nav" data-nav>
  <div class="nav-inner">
    <a class="brand" href="../index.html#top" aria-label="NUTRICYT — inicio">
      <svg class="brand-icon" viewBox="0 0 32 32" fill="none" aria-hidden="true">
        <path d="M11 5C11 5 22 9 22 16C22 23 11 27 11 27" stroke="var(--coral)" stroke-width="2.1" stroke-linecap="round"/>
        <path d="M21 5C21 5 10 9 10 16C10 23 21 27 21 27" stroke="var(--coral)" stroke-width="2.1" stroke-linecap="round" opacity="0.5"/>
        <line x1="12" y1="9" x2="20" y2="9" stroke="var(--coral)" stroke-width="1.6" stroke-linecap="round"/>
        <line x1="10.3" y1="16" x2="21.7" y2="16" stroke="var(--coral)" stroke-width="1.6" stroke-linecap="round"/>
        <line x1="12" y1="23" x2="20" y2="23" stroke="var(--coral)" stroke-width="1.6" stroke-linecap="round"/>
      </svg>
      <span class="brand-word">nutricyt</span>
    </a>

    <nav class="nav-links" aria-label="Navegación principal">
      <a href="../index.html#sobre-mi">Sobre mí</a>
      <a href="../index.html#areas-atencion">Áreas</a>
      <a href="../index.html#servicios">Servicios</a>
      <a href="../index.html#blog">Blog</a>
      <a href="../index.html#contacto">Contacto</a>
    </nav>

    <div class="nav-actions">
      <a class="btn btn-primary btn-sm nav-cta" href="https://wa.me/{wa}?text=Hola%2C%20quiero%20reservar%20una%20consulta%20de%20nutrici%C3%B3n" target="_blank" rel="noopener">Reservar consulta</a>
      <button class="nav-toggle" data-nav-toggle aria-expanded="false" aria-controls="nav-mobile" aria-label="Abrir menú">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<nav id="nav-mobile" class="nav-mobile" data-nav-mobile aria-label="Navegación móvil">
  <a href="../index.html#sobre-mi">Sobre mí</a>
  <a href="../index.html#areas-atencion">Áreas de atención</a>
  <a href="../index.html#servicios">Servicios</a>
  <a href="../index.html#blog">Blog</a>
  <a href="../index.html#contacto">Contacto</a>
  <a class="btn btn-primary" href="https://wa.me/{wa}?text=Hola%2C%20quiero%20reservar%20una%20consulta%20de%20nutrici%C3%B3n" target="_blank" rel="noopener">Reservar consulta</a>
</nav>""".format(wa=WA)

FOOTER_WIDGET = """<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div>
        <a class="brand" href="../index.html#top">
          <svg class="brand-icon" viewBox="0 0 32 32" fill="none" aria-hidden="true">
            <path d="M11 5C11 5 22 9 22 16C22 23 11 27 11 27" stroke="var(--coral)" stroke-width="2.1" stroke-linecap="round"/>
            <path d="M21 5C21 5 10 9 10 16C10 23 21 27 21 27" stroke="var(--coral)" stroke-width="2.1" stroke-linecap="round" opacity="0.5"/>
            <line x1="12" y1="9" x2="20" y2="9" stroke="var(--coral)" stroke-width="1.6" stroke-linecap="round"/>
            <line x1="10.3" y1="16" x2="21.7" y2="16" stroke="var(--coral)" stroke-width="1.6" stroke-linecap="round"/>
            <line x1="12" y1="23" x2="20" y2="23" stroke="var(--coral)" stroke-width="1.6" stroke-linecap="round"/>
          </svg>
          <span class="brand-word">nutricyt</span>
        </a>
        <p class="footer-tagline">Nutriendo tus células, potenciando tu vida.</p>
      </div>

      <div class="footer-cols">
        <div class="footer-col">
          <h3>Navegación</h3>
          <a href="../index.html#sobre-mi">Sobre mí</a>
          <a href="../index.html#areas-atencion">Áreas de atención</a>
          <a href="../index.html#servicios">Servicios</a>
          <a href="../index.html#blog">Blog</a>
          <a href="../index.html#contacto">Contacto</a>
        </div>
        <div class="footer-col">
          <h3>Consultorio</h3>
          <p>[DIRECCIÓN DEL CONSULTORIO]</p>
          <p>Santo Domingo, RD</p>
        </div>
        <div class="footer-col">
          <h3>Contacto</h3>
          <a href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp: +1 809 749 9916</a>
          <a href="mailto:contacto@nutricyt.com">contacto@nutricyt.com</a>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <span>© <span data-year>2026</span> NUTRICYT — Shelsea García, Nutricionista-Dietista.</span>
    </div>
  </div>
</footer>

<div class="wa-widget" data-wa-widget>
  <div class="wa-panel" data-wa-panel role="dialog" aria-label="Chat de NUTRICYT">
    <div class="wa-head">
      <span class="wa-avatar" aria-hidden="true">N</span>
      <div class="wa-head-text">
        <strong>NUTRICYT</strong>
        <span>En línea</span>
      </div>
    </div>
    <div class="wa-body" data-wa-body>
      <div class="wa-msg bot">¡Hola! 👋 Soy el asistente virtual de NUTRICYT, ¿en qué te puedo ayudar?</div>
    </div>
    <form class="wa-form" data-wa-form>
      <label class="sr-only" for="wa-input">Escribe tu mensaje</label>
      <input id="wa-input" data-wa-input type="text" placeholder="Escribe un mensaje…" autocomplete="off">
      <button type="submit" aria-label="Enviar">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M4 12l16-8-6 16-3-6-7-2z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
      </button>
    </form>
  </div>

  <button class="wa-fab" data-wa-fab aria-expanded="false" aria-label="Abrir chat de WhatsApp">
    <span class="wa-badge" aria-hidden="true"></span>
    <svg class="icon-chat" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3C7.03 3 3 6.58 3 11c0 2.1.94 4.02 2.5 5.46L4.8 20.2a.6.6 0 00.79.7l3.98-1.6c.77.22 1.6.34 2.43.34 4.97 0 9-3.58 9-8s-4.03-8-9-8z" fill="currentColor"/></svg>
    <svg class="icon-close" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"/></svg>
  </button>
</div>

<script defer src="../lib/manifest.js"></script>
<script defer src="../main.js?v=20260916"></script>
</body>
</html>
""".format(wa=WA)

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — NUTRICYT</title>
<meta name="description" content="{card_desc}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="../styles.css?v=20260916">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%232e4a54'/%3E%3Cpath d='M11 5c0 0 12 4 12 11s-12 11-12 11' stroke='%23e4a18e' stroke-width='2.2' fill='none' stroke-linecap='round'/%3E%3C/svg%3E">
</head>
<body>
<a class="skip-link" href="#main">Saltar al contenido</a>

"""


def render_list(items):
    lis = "\n".join(f'          <li>{CHECK_SVG} {item}</li>' for item in items)
    return f"        <ul>\n{lis}\n        </ul>\n"


def render_area(a):
    others = [x for x in AREAS if x["slug"] != a["slug"]]
    other_links = "\n".join(
        f'          <a class="area-link" href="{o["slug"]}.html" style="display:flex;align-items:center;justify-content:space-between;padding:1rem 0;border-bottom:1px solid var(--line-soft);">{o["title"]} {ARROW_SVG}</a>'
        for o in others
    )

    note_html = ""
    if a["note"]:
        note_html = f'        <p class="area-note">{a["note"]}</p>\n'

    html = HEAD.format(title=a["title"], card_desc=a["card_desc"])
    html += NAV
    html += f"""

<main id="main">
  <section class="area-hero">
    <div class="container">
      <p class="area-breadcrumb"><a href="../index.html#areas-atencion">Áreas de atención</a> · {a["title"]}</p>
      <h1 class="area-hero-title reveal">{a["title"]}</h1>
      <p class="area-hero-sub reveal">{a["subtitle"]}</p>
    </div>
  </section>

  <article class="area-article">
    <div class="container area-article-inner reveal">
      <p class="lede">{a["lede"]}</p>

      <h2>¿Cómo puede ayudar la nutrición?</h2>
      <p>{a["help"]}</p>

      <h2>Qué evaluamos en la consulta</h2>
{render_list(a["evaluate"])}
      <h2>Cómo se estructura el abordaje</h2>
      <p>{a["structure"]}</p>
{note_html}
      <h2>Estrategias que podemos trabajar juntos</h2>
{render_list(a["strategies"])}
      <h2>Seguimiento e individualización</h2>
      <p>{a["followup"]}</p>

      <div class="area-particular">
        <h2>{a["particular_title"]}</h2>
        <p style="margin-bottom:0;">{a["particular"]}</p>
      </div>

      <div class="area-closing">
        <p>{a["closing"]}</p>
        <a class="btn btn-primary" href="https://wa.me/{WA}?text=Hola%2C%20quiero%20una%20evaluaci%C3%B3n%20nutricional%20sobre%20{a["slug"].replace("-", "%20")}" target="_blank" rel="noopener">Reservar evaluación por WhatsApp</a>
      </div>
    </div>
  </article>

  <section class="area-other">
    <div class="container" style="max-width:720px;">
      <p class="eyebrow">Otras áreas de atención</p>
{other_links}
    </div>
  </section>
</main>

"""
    html += FOOTER_WIDGET
    return html


for a in AREAS:
    out_path = os.path.join(OUT_DIR, f"{a['slug']}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(render_area(a))
    print("wrote", out_path)
