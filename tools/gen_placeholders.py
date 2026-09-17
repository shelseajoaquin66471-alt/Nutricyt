#!/usr/bin/env python3
"""Dev-time only: generates placeholder imagery so the site renders correctly
before real photography is dropped into assets/img/. Not part of the shipped
site logic — safe to delete once real photos are in place."""

import math
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
os.makedirs(IMG, exist_ok=True)

PETROLEO = (46, 74, 84)
PETROLEO_D = (30, 50, 58)
CORAL = (228, 161, 142)
CREAM = (247, 243, 236)
GRAY_A = (226, 224, 219)
GRAY_B = (206, 203, 196)
INK = (26, 26, 26)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vertical_gradient(size, c1, c2):
    w, h = size
    img = Image.new("RGB", size, c1)
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        col = lerp(c1, c2, t)
        for x in range(w):
            px[x, y] = col
    return img


def radial_vignette(img, strength=0.35):
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    dm = ImageDraw.Draw(mask)
    dm.ellipse([-w * 0.25, -h * 0.15, w * 1.25, h * 1.1], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(w * 0.12))
    dark = Image.new("RGB", (w, h), (0, 0, 0))
    return Image.composite(img, Image.blend(img, dark, strength), mask)


def studio_portrait_placeholder(path, size, label):
    """Neutral studio-gray backdrop matching the real photography, with a
    soft silhouette so the layout reads as a portrait slot, not a broken image."""
    w, h = size
    img = vertical_gradient(size, GRAY_A, GRAY_B)
    d = ImageDraw.Draw(img, "RGBA")

    # soft floor shadow ellipse
    d.ellipse(
        [w * 0.22, h * 0.86, w * 0.78, h * 0.98],
        fill=(0, 0, 0, 18),
    )

    # simple silhouette (head + shoulders/coat triangle)
    cx = w * 0.5
    head_r = w * 0.10
    head_cy = h * 0.34
    d.ellipse(
        [cx - head_r, head_cy - head_r, cx + head_r, head_cy + head_r],
        fill=(255, 255, 255, 90),
    )
    body_top = head_cy + head_r * 0.7
    d.polygon(
        [
            (cx - w * 0.24, h * 0.92),
            (cx + w * 0.24, h * 0.92),
            (cx + w * 0.14, body_top),
            (cx - w * 0.14, body_top),
        ],
        fill=(255, 255, 255, 90),
    )

    img = img.filter(ImageFilter.GaussianBlur(1))
    d = ImageDraw.Draw(img, "RGBA")

    # caption strip
    cap_h = int(h * 0.055)
    d.rectangle([0, h - cap_h, w, h], fill=(26, 26, 26, 120))
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(cap_h * 0.34)
        )
    except Exception:
        font = ImageFont.load_default()
    text = f"Placeholder — sustituir por {label}"
    d.text((w * 0.03, h - cap_h * 0.72), text, fill=(255, 255, 255, 220), font=font)

    img.save(path, "JPEG", quality=82)


def duotone_icon_card(path, size, icon="clipboard", tag=""):
    w, h = size
    img = vertical_gradient(size, PETROLEO, PETROLEO_D)
    img = radial_vignette(img, 0.18)
    d = ImageDraw.Draw(img, "RGBA")

    cx, cy = w * 0.5, h * 0.44
    s = min(w, h) * 0.16
    stroke = (247, 243, 236, 235)
    accent = (228, 161, 142, 255)
    lw = max(3, int(s * 0.09))

    if icon == "clipboard":
        d.rounded_rectangle([cx - s, cy - s * 1.2, cx + s, cy + s * 1.2], radius=s * 0.18, outline=stroke, width=lw)
        d.rounded_rectangle([cx - s * 0.4, cy - s * 1.35, cx + s * 0.4, cy - s * 1.05], radius=s * 0.1, fill=stroke)
        for i, yy in enumerate([-0.5, -0.1, 0.3]):
            d.line([cx - s * 0.55, cy + s * yy, cx + s * 0.55, cy + s * yy], fill=accent if i == 1 else stroke, width=lw)
    elif icon == "heart-person":
        d.ellipse([cx - s * 0.32, cy - s * 1.15, cx + s * 0.32, cy - s * 0.5], outline=stroke, width=lw)
        d.arc([cx - s * 0.7, cy - s * 0.35, cx + s * 0.7, cy + s * 1.0], 200, 340, fill=stroke, width=lw)
        hs = s * 0.42
        d.polygon(
            [
                (cx, cy + s * 0.55 + hs * 0.35),
                (cx - hs, cy + s * 0.55 - hs * 0.25),
                (cx - hs * 0.5, cy + s * 0.55 - hs * 0.75),
                (cx, cy + s * 0.55 - hs * 0.25),
                (cx + hs * 0.5, cy + s * 0.55 - hs * 0.75),
                (cx + hs, cy + s * 0.55 - hs * 0.25),
            ],
            outline=accent, width=lw,
        )
    elif icon == "calendar-leaf":
        d.rounded_rectangle([cx - s, cy - s * 0.9, cx + s, cy + s * 1.0], radius=s * 0.15, outline=stroke, width=lw)
        d.line([cx - s, cy - s * 0.35, cx + s, cy - s * 0.35], fill=stroke, width=lw)
        d.line([cx - s * 0.5, cy - s * 1.15, cx - s * 0.5, cy - s * 0.75], fill=stroke, width=lw)
        d.line([cx + s * 0.5, cy - s * 1.15, cx + s * 0.5, cy - s * 0.75], fill=stroke, width=lw)
        d.pieslice([cx - s * 0.35, cy + s * 0.05, cx + s * 0.35, cy + s * 0.75], 200, 20, fill=accent)
    elif icon == "trend":
        pts = [(cx - s, cy + s * 0.7), (cx - s * 0.3, cy - s * 0.1), (cx + s * 0.2, cy + s * 0.2), (cx + s, cy - s * 0.9)]
        d.line(pts, fill=accent, width=lw, joint="curve")
        d.line([cx + s * 0.5, cy - s * 0.9, cx + s, cy - s * 0.9, cx + s, cy - s * 0.4], fill=accent, width=lw)
    elif icon == "runner":
        d.ellipse([cx - s * 0.15, cy - s * 1.15, cx + s * 0.15, cy - s * 0.85], outline=stroke, width=lw)
        d.line([cx, cy - s * 0.8, cx - s * 0.1, cy - s * 0.1], fill=stroke, width=lw)
        d.line([cx - s * 0.1, cy - s * 0.1, cx + s * 0.55, cy - s * 0.35], fill=stroke, width=lw)
        d.line([cx - s * 0.1, cy - s * 0.1, cx - s * 0.5, cy + s * 0.15], fill=stroke, width=lw)
        d.line([cx - s * 0.1, cy - s * 0.1, cx + s * 0.15, cy + s * 0.75], fill=accent, width=lw)
        d.line([cx - s * 0.1, cy - s * 0.1, cx - s * 0.6, cy + s * 0.85], fill=stroke, width=lw)
    elif icon == "tape":
        d.ellipse([cx - s * 1.05, cy - s * 0.55, cx + s * 0.15, cy + s * 0.55], outline=stroke, width=lw)
        d.ellipse([cx - s * 0.55, cy - s * 0.22, cx - s * 0.22, cy + s * 0.1], fill=stroke)
        d.line([cx - s * 0.1, cy, cx + s * 1.05, cy + s * 0.85], fill=accent, width=lw)
        for t in range(0, 6):
            px = cx - s * 0.1 + (s * 1.15) * (t / 5)
            py = cy + (s * 0.85) * (t / 5)
            d.line([px, py - lw, px, py + lw], fill=CREAM + (255,), width=max(2, lw // 2))
    elif icon == "leaf":
        d.arc([cx - s, cy - s * 0.9, cx + s, cy + s * 0.9], 140, 340, fill=stroke, width=lw)
        d.arc([cx - s, cy - s * 0.9, cx + s, cy + s * 0.9], -40, 160, fill=accent, width=lw)
        d.line([cx, cy - s * 0.75, cx, cy + s * 0.75], fill=stroke, width=max(2, lw // 2))
    elif icon == "plate":
        d.ellipse([cx - s, cy - s, cx + s, cy + s], outline=stroke, width=lw)
        d.ellipse([cx - s * 0.55, cy - s * 0.55, cx + s * 0.55, cy + s * 0.55], outline=accent, width=max(2, lw // 2))

    # label ribbon
    cap_h = int(h * 0.16)
    d.rectangle([0, h - cap_h, w, h], fill=(255, 255, 255, 14))
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(cap_h * 0.22)
        )
    except Exception:
        font = ImageFont.load_default()
    if tag:
        d.text((w * 0.5, h - cap_h * 0.5), tag, fill=(247, 243, 236, 235), font=font, anchor="mm")

    img.save(path, "JPEG", quality=85)


def isak_report_mock(path, size):
    w, h = size
    img = Image.new("RGB", size, CREAM)
    d = ImageDraw.Draw(img, "RGBA")
    margin = w * 0.08
    d.rounded_rectangle([margin, margin, w - margin, h - margin], radius=18, outline=INK + (255,), width=3, fill=(255, 255, 255, 255))
    try:
        f_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(w * 0.030))
        f_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(w * 0.021))
    except Exception:
        f_title = f_small = ImageFont.load_default()

    pad = margin + w * 0.05
    d.text((pad, margin + h * 0.045), "INFORME ANTROPOMÉTRICO ISAK", fill=PETROLEO, font=f_title)
    d.text((pad, margin + h * 0.10), "Perfil restringido · Nivel 1", fill=(110, 110, 110), font=f_small)
    d.line([pad, margin + h * 0.145, w - pad, margin + h * 0.145], fill=(220, 218, 212), width=2)

    rows = [
        "Masa grasa", "Masa muscular", "Pliegues cutáneos (6)",
        "Perímetros", "Diámetros óseos", "Somatotipo",
    ]
    y0 = margin + h * 0.20
    row_h = h * 0.068
    for i, r in enumerate(rows):
        yy = y0 + i * row_h
        d.text((pad, yy), r, fill=INK, font=f_small)
        bar_x0 = pad + w * 0.34
        bar_x1 = w - pad
        d.rounded_rectangle([bar_x0, yy + row_h * 0.18, bar_x1, yy + row_h * 0.62], radius=6, fill=(230, 228, 222))
        fill_ratio = 0.35 + 0.5 * ((i * 37) % 100) / 100
        col = CORAL if i % 2 == 0 else PETROLEO
        d.rounded_rectangle([bar_x0, yy + row_h * 0.18, bar_x0 + (bar_x1 - bar_x0) * fill_ratio, yy + row_h * 0.62], radius=6, fill=col)

    # measuring tape graphic diagonal accent
    tape_y = h - margin - h * 0.075
    d.line([pad, tape_y, w - pad, tape_y - h * 0.015], fill=CORAL, width=9)
    for i in range(24):
        tx = pad + (w - pad - pad) * (i / 23)
        ty = tape_y - h * 0.015 * (i / 23)
        d.line([tx, ty - 9, tx, ty + 9], fill=CREAM, width=3)
    d.text((pad, tape_y + h * 0.028), "Cinta antropométrica · medición ISAK", fill=(110, 110, 110), font=f_small)

    img.save(path, "JPEG", quality=88)


PORTRAITS = [
    ("hero-frente-estetoscopio.jpg", (1400, 1750), "Foto 1 — cuerpo completo, frente, estetoscopio"),
    ("retrato-bata-manos.jpg", (1200, 1600), "Foto 3 — cuerpo completo, sonrisa amplia de frente"),
    ("mirada-lateral.jpg", (1200, 1600), "Foto 4 — cuerpo completo, mirando de lado"),
    ("banquito-sentada.jpg", (1100, 1500), "Foto 5 — sentada en banquito de madera"),
    ("closeup-lateral.jpg", (1200, 1500), "Foto 2 — close-up sentada, mirando de lado"),
]

for fname, size, label in PORTRAITS:
    studio_portrait_placeholder(os.path.join(IMG, fname), size, label)

SERVICES = [
    ("servicio-evaluacion-inicial.jpg", "clipboard", "EVALUACIÓN INICIAL"),
    ("servicio-asesoria-personal.jpg", "heart-person", "ASESORÍA PERSONAL"),
    ("servicio-estilo-vida.jpg", "calendar-leaf", "ESTILO DE VIDA"),
    ("servicio-seguimiento.jpg", "trend", "SEGUIMIENTO"),
    ("servicio-evaluacion-deportiva.jpg", "runner", "EVAL. DEPORTIVA"),
]
for fname, icon, tag in SERVICES:
    duotone_icon_card(os.path.join(IMG, fname), (1000, 1250), icon, tag)

BLOG = [
    ("blog-recetas.jpg", "plate", "RECETAS"),
    ("blog-consejos.jpg", "leaf", "CONSEJOS"),
    ("blog-enfermedades.jpg", "trend", "SALUD"),
    ("blog-anemia.jpg", "heart-person", "ARTÍCULOS"),
]
for fname, icon, tag in BLOG:
    duotone_icon_card(os.path.join(IMG, fname), (900, 700), icon, tag)

isak_report_mock(os.path.join(IMG, "informe-isak.jpg"), (1400, 1000))

print("done:", os.listdir(IMG))
