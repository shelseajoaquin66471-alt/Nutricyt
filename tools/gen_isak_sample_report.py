#!/usr/bin/env python3
"""Dev-time only: recreates the visual FORMAT of a narrative ISAK body-composition
report (as shared by the client) using a fully fictional example profile — no real
patient data. Matches the plain document look of the sample PDF."""

import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
os.makedirs(IMG, exist_ok=True)

W, H = 1600, 3000
MARGIN = 110
INK = (20, 20, 20)
MUTE = (90, 90, 90)
BG = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def load(name, size):
    try:
        return ImageFont.truetype(FONT_DIR + name, size)
    except Exception:
        return ImageFont.load_default()


f_title = load("DejaVuSans-Bold.ttf", 30)
f_h2 = load("DejaVuSans-Bold.ttf", 24)
f_body = load("DejaVuSans.ttf", 20)
f_small = load("DejaVuSans.ttf", 18)


def wrap(draw, text, font, max_width):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
content_w = W - 2 * MARGIN
y = MARGIN

title = "Informe Interpretado de Composición Corporal — Perfil de ejemplo"
title_lines = wrap(d, title, f_title, content_w)
for line in title_lines:
    tw = d.textlength(line, font=f_title)
    d.text(((W - tw) / 2, y), line, font=f_title, fill=INK)
    y += 40
y += 6
d.line([MARGIN, y, W - MARGIN, y], fill=(200, 200, 200), width=2)
y += 30

def h2(text):
    global y
    d.text((MARGIN, y), text, font=f_h2, fill=INK)
    y += 36

def para(text, font=f_body, color=INK, gap=14, line_h=29):
    global y
    for line in wrap(d, text, font, content_w):
        d.text((MARGIN, y), line, font=font, fill=color)
        y += line_h
    y += gap

h2("Análisis y conclusiones sobre la composición corporal")
para(
    "A partir de las mediciones antropométricas, el peso corporal registrado es de 74.5 kg "
    "(Z = 0.32), dentro del rango esperado, con un IMC de 23.4 kg/m², clasificado como peso "
    "saludable. Se observa una masa muscular de 34.2 kg (Z = 0.71), una masa ósea de 9.8 kg "
    "(Z = 0.05) y una masa adiposa de 13.1 kg, que representa un 17.6% del peso total, dentro "
    "de un rango considerado adecuado para el perfil evaluado."
)
para(
    "Los pliegues cutáneos muestran valores moderados: tríceps 8 mm, subescapular 10 mm, "
    "abdominal 14 mm y muslo 15 mm, con una distribución relativamente homogénea entre tren "
    "superior e inferior. No se observan patrones de acumulación marcada en una zona específica."
)
para(
    "El somatotipo corresponde a un perfil mesomorfo balanceado: mesomorfia 5.1, endomorfia 2.8 "
    "y ectomorfia 2.6, lo que indica una estructura corporal con buena base muscular y "
    "proporción moderada de masa grasa, compatible con las demandas de disciplinas que combinan "
    "fuerza y resistencia."
)
para(
    "Los perímetros corregidos (brazo: 29.4 cm, muslo: 52.1 cm, pierna: 36.0 cm) reflejan una "
    "distribución muscular consistente con el somatotipo observado. El índice adiposo-muscular "
    "se encuentra dentro de un rango intermedio, y el índice músculo/óseo dentro del rango "
    "esperado para el perfil."
)

h2("Gasto energético")
para(
    "Según la ecuación de Harris & Benedict, el metabolismo basal estimado es de 1,650 kcal. "
    "Con un nivel de actividad alta (1.9), el gasto energético total estimado es de "
    "aproximadamente 3,135 kcal, valor que se ajusta según fase de entrenamiento, objetivos y "
    "respuesta individual a lo largo del seguimiento."
)

h2("Recomendaciones generales")
recs = [
    "Ajustar la ingesta energética y de macronutrientes según fase de entrenamiento y objetivo.",
    "Distribuir la proteína a lo largo del día para apoyar recuperación y mantenimiento muscular.",
    "Planificar la hidratación antes, durante y después del entrenamiento.",
    "Organizar la alimentación alrededor de las sesiones de entrenamiento.",
    "Repetir la evaluación antropométrica cada 2-3 meses para dar seguimiento objetivo.",
]
for i, r in enumerate(recs, 1):
    for j, line in enumerate(wrap(d, r, f_body, content_w - 40)):
        prefix = f"{i}. " if j == 0 else "    "
        d.text((MARGIN, y), prefix + line, font=f_body, fill=INK)
        y += 29
    y += 6

y += 20
d.line([MARGIN, y, W - MARGIN, y], fill=(200, 200, 200), width=2)
y += 24
para(
    "Perfil y datos ilustrativos con fines demostrativos — no corresponden a ningún paciente real.",
    font=f_small, color=MUTE, gap=0, line_h=24,
)

img = img.crop((0, 0, W, min(H, y + 40)))
out_path = os.path.join(IMG, "informe-isak-deportivo.jpg")
img.save(out_path, "JPEG", quality=90)
print("wrote", out_path, img.size, "->", os.path.getsize(out_path) // 1024, "KB")
