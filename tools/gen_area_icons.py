#!/usr/bin/env python3
"""Dev-time only: generates the 6 'Áreas de atención' card images,
matching the visual style of the service cards (duotone icon on gradient)."""

import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
os.makedirs(IMG, exist_ok=True)

PETROLEO = (46, 74, 84)
PETROLEO_D = (30, 50, 58)
CREAM = (247, 243, 236)


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


def radial_vignette(img, strength=0.18):
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    dm = ImageDraw.Draw(mask)
    dm.ellipse([-w * 0.25, -h * 0.15, w * 1.25, h * 1.1], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(w * 0.12))
    dark = Image.new("RGB", (w, h), (0, 0, 0))
    return Image.composite(img, Image.blend(img, dark, strength), mask)


def duotone_icon_card(path, size, icon, tag):
    w, h = size
    img = vertical_gradient(size, PETROLEO, PETROLEO_D)
    img = radial_vignette(img, 0.18)
    d = ImageDraw.Draw(img, "RGBA")

    cx, cy = w * 0.5, h * 0.44
    s = min(w, h) * 0.16
    stroke = (247, 243, 236, 235)
    accent = (228, 161, 142, 255)
    lw = max(3, int(s * 0.09))

    if icon == "scale-down":
        d.line([cx - s, cy - s * 0.9, cx - s * 0.1, cy + s * 0.1], fill=stroke, width=lw, joint="curve")
        d.line([cx - s * 0.1, cy + s * 0.1, cx + s * 0.5, cy - s * 0.6], fill=stroke, width=lw)
        d.polygon([(cx + s, cy - s * 1.1), (cx + s * 0.55, cy - s * 0.7), (cx + s * 0.75, cy - s * 0.45)], fill=accent)
        d.line([cx + s * 0.55, cy - s * 0.7, cx + s, cy - s * 1.1], fill=accent, width=lw)
        d.line([cx - s, cy + s * 0.55, cx + s, cy + s * 0.55], fill=stroke, width=max(2, lw // 2))
    elif icon == "scale-up":
        d.line([cx - s, cy + s * 0.9, cx - s * 0.1, cy - s * 0.1], fill=stroke, width=lw, joint="curve")
        d.line([cx - s * 0.1, cy - s * 0.1, cx + s * 0.5, cy + s * 0.6], fill=stroke, width=lw)
        d.line([cx + s * 0.5, cy + s * 0.6, cx + s, cy - s * 0.2], fill=stroke, width=lw)
        d.polygon([(cx + s, cy - s * 0.9), (cx + s * 0.6, cy - s * 0.75), (cx + s * 0.85, cy - s * 0.45)], fill=accent)
        d.line([cx + s * 0.6, cy - s * 0.75, cx + s, cy - s * 0.9], fill=accent, width=lw)
        d.line([cx + s, cy - s * 0.9, cx + s, cy - s * 0.35], fill=accent, width=lw)
    elif icon == "droplet":
        d.pieslice([cx - s * 0.75, cy - s * 0.4, cx + s * 0.75, cy + s], 0, 180, outline=stroke, width=lw)
        d.line([cx - s * 0.75, cy - s * 0.4, cx, cy - s * 1.15], fill=stroke, width=lw)
        d.line([cx, cy - s * 1.15, cx + s * 0.75, cy - s * 0.4], fill=stroke, width=lw)
        d.ellipse([cx - s * 0.22, cy + s * 0.05, cx + s * 0.22, cy + s * 0.5], fill=accent)
    elif icon == "heart-pulse":
        hs = s * 0.55
        d.polygon(
            [
                (cx, cy + s * 0.75 + hs * 0.35),
                (cx - hs * 1.05, cy + s * 0.75 - hs * 0.35),
                (cx - hs * 0.5, cy + s * 0.75 - hs * 0.95),
                (cx, cy + s * 0.75 - hs * 0.35),
                (cx + hs * 0.5, cy + s * 0.75 - hs * 0.95),
                (cx + hs * 1.05, cy + s * 0.75 - hs * 0.35),
            ],
            outline=stroke, width=lw,
        )
        d.line([cx - s, cy - s * 0.55, cx - s * 0.3, cy - s * 0.55, cx - s * 0.05, cy - s * 1.15,
                cx + s * 0.2, cy - s * 0.15, cx + s * 0.45, cy - s * 0.55, cx + s, cy - s * 0.55],
               fill=accent, width=lw, joint="curve")
    elif icon == "lipid":
        for dx, dy, r in [(-0.35, -0.3, 0.42), (0.38, -0.35, 0.38), (0, 0.35, 0.46)]:
            d.ellipse([cx + s * dx - s * r, cy + s * dy - s * r, cx + s * dx + s * r, cy + s * dy + s * r],
                      outline=stroke, width=lw)
        d.ellipse([cx - s * 0.12, cy + s * 0.35 - s * 0.16, cx + s * 0.12, cy + s * 0.35 + s * 0.16], fill=accent)
    elif icon == "orbit":
        d.ellipse([cx - s, cy - s * 0.55, cx + s, cy + s * 0.55], outline=stroke, width=lw)
        d.ellipse([cx - s * 0.55, cy - s, cx + s * 0.55, cy + s], outline=stroke, width=lw)
        d.ellipse([cx - s * 0.18, cy - s * 0.18, cx + s * 0.18, cy + s * 0.18], fill=accent)
    elif icon == "dumbbell":
        d.line([cx - s * 0.9, cy, cx + s * 0.9, cy], fill=accent, width=lw)
        for dx in (-1, 1):
            d.rounded_rectangle(
                [cx + dx * s * 0.7 - s * 0.16, cy - s * 0.55, cx + dx * s * 0.7 + s * 0.16, cy + s * 0.55],
                radius=s * 0.08, outline=stroke, width=lw,
            )
            d.rounded_rectangle(
                [cx + dx * s * 0.95 - s * 0.1, cy - s * 0.32, cx + dx * s * 0.95 + s * 0.1, cy + s * 0.32],
                radius=s * 0.05, outline=stroke, width=lw,
            )

    cap_h = int(h * 0.16)
    d.rectangle([0, h - cap_h, w, h], fill=(255, 255, 255, 14))
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(cap_h * 0.20)
        )
    except Exception:
        font = ImageFont.load_default()
    if tag:
        d.text((w * 0.5, h - cap_h * 0.5), tag, fill=(247, 243, 236, 235), font=font, anchor="mm")

    img.save(path, "JPEG", quality=85)


AREAS = [
    ("area-perdida-peso.jpg", "scale-down", "PÉRDIDA DE PESO"),
    ("area-aumento-peso.jpg", "scale-up", "AUMENTO DE PESO"),
    ("area-diabetes.jpg", "droplet", "DIABETES TIPO 2"),
    ("area-hipertension.jpg", "heart-pulse", "HIPERTENSIÓN ARTERIAL"),
    ("area-dislipidemia.jpg", "lipid", "DISLIPIDEMIAS"),
    ("area-sindrome-metabolico.jpg", "orbit", "SÍNDROME METABÓLICO"),
    ("area-nutricion-deportiva.jpg", "dumbbell", "NUTRICIÓN DEPORTIVA"),
]

for fname, icon, tag in AREAS:
    duotone_icon_card(os.path.join(IMG, fname), (1000, 1250), icon, tag)

print("done:", [f for f, _, _ in AREAS])
