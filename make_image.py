#!/usr/bin/env python3
"""Maakt een vierkante post-afbeelding (1080x1080) voor Marijke Muoi Odd Fellows Leeuwarden.

Gebruik:
  python3 make_image.py --titel "Vriendschap begint met luisteren" \
      --sub "Vriendschap · Liefde · Waarheid" --thema herfst --uit images/2026-11-03.jpg

Thema's: herfst, winter, lente, zomer, nacht, goud
"""
import argparse
import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W = H = 1080
LORA = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
POPPINS = "/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf"
POPPINS_MED = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"

# (achtergrond boven, achtergrond onder, accent/goud, tekst, subtekst)
THEMAS = {
    "herfst": ((92, 38, 28), (34, 16, 14), (222, 170, 82), (250, 240, 225), (230, 200, 160)),
    "winter": ((28, 46, 72), (10, 16, 30), (214, 186, 120), (240, 244, 250), (190, 205, 225)),
    "lente":  ((46, 84, 64), (16, 34, 28), (226, 196, 110), (245, 248, 238), (205, 225, 200)),
    "zomer":  ((150, 84, 40), (60, 28, 22), (250, 210, 120), (255, 246, 230), (245, 215, 175)),
    "nacht":  ((40, 30, 66), (12, 10, 24), (220, 182, 104), (244, 238, 252), (200, 190, 225)),
    "goud":   ((70, 22, 30), (24, 8, 14), (232, 190, 96), (252, 242, 228), (235, 205, 170)),
}


def font(path, size, weight=None):
    f = ImageFont.truetype(path, size)
    if weight is not None:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def achtergrond(top, bottom, seed):
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        for x in range(W):
            # lichte diagonale gloed linksboven
            d = math.hypot(x - W * 0.3, y - H * 0.25) / (W * 1.1)
            g = max(0.0, 1 - d) * 0.35
            r = top[0] * (1 - t) + bottom[0] * t
            gg = top[1] * (1 - t) + bottom[1] * t
            b = top[2] * (1 - t) + bottom[2] * t
            px[x, y] = (int(min(255, r + 60 * g)), int(min(255, gg + 45 * g)), int(min(255, b + 25 * g)))
    # zachte lichtdeeltjes
    rnd = random.Random(seed)
    laag = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    for _ in range(70):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        r = rnd.randint(2, 9)
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 230, 180, rnd.randint(10, 45)))
    laag = laag.filter(ImageFilter.GaussianBlur(4))
    img = Image.alpha_composite(img.convert("RGBA"), laag)
    # vignet
    vig = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vig)
    vd.ellipse((-200, -200, W + 200, H + 200), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(160))
    donker = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    img = Image.composite(img, donker, vig.point(lambda v: int(90 + v * 165 / 255)))
    return img


def drie_schakels(img, cx, cy, kleur):
    """Drie in elkaar grijpende schakels (symbool van de Odd Fellows)."""
    schaal = 4
    laag = Image.new("RGBA", (W * schaal, H * schaal), (0, 0, 0, 0))
    d = ImageDraw.Draw(laag)
    bw, bh, dik, stap = 120, 78, 13, 96
    for i in (-1, 0, 1):
        x = (cx + i * stap) * schaal
        y = cy * schaal
        box = (x - bw * schaal // 2, y - bh * schaal // 2, x + bw * schaal // 2, y + bh * schaal // 2)
        d.ellipse(box, outline=kleur + (255,), width=dik * schaal)
    laag = laag.resize((W, H), Image.LANCZOS)
    gloed = laag.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(gloed)
    img.alpha_composite(laag)


def wrap(draw, tekst, f, maxw):
    woorden, regels, huidig = tekst.split(), [], ""
    for w in woorden:
        test = (huidig + " " + w).strip()
        if draw.textlength(test, font=f) <= maxw:
            huidig = test
        else:
            regels.append(huidig)
            huidig = w
    if huidig:
        regels.append(huidig)
    return regels


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--titel", required=True)
    p.add_argument("--sub", default="Vriendschap · Liefde · Waarheid")
    p.add_argument("--thema", default="herfst", choices=THEMAS.keys())
    p.add_argument("--uit", required=True)
    a = p.parse_args()

    top, bottom, goud, tekst, subkleur = THEMAS[a.thema]
    img = achtergrond(top, bottom, seed=a.titel)
    drie_schakels(img, W // 2, 300, goud)

    d = ImageDraw.Draw(img)
    # titel: zo groot mogelijk binnen 4 regels
    for size in range(84, 40, -4):
        f = font(LORA, size, weight=600)
        regels = wrap(d, a.titel, f, 860)
        if len(regels) <= 4:
            break
    lh = int(size * 1.25)
    y = 560 - (len(regels) * lh) // 2 + lh // 2
    for r in regels:
        d.text((W // 2, y), r, font=f, fill=tekst, anchor="mm")
        y += lh

    # dunne gouden lijn + subtitel
    y += 20
    d.line((W // 2 - 70, y, W // 2 + 70, y), fill=goud, width=2)
    fs = font(POPPINS, 30)
    d.text((W // 2, y + 46), a.sub, font=fs, fill=subkleur, anchor="mm")

    # voettekst
    ff = font(POPPINS_MED, 26)
    d.text((W // 2, H - 92), "Marijke Muoi · Odd Fellows Leeuwarden", font=ff, fill=goud, anchor="mm")
    fu = font(POPPINS, 22)
    d.text((W // 2, H - 56), "marijke-muoi-odd-fellows.nl", font=fu, fill=subkleur, anchor="mm")

    img.convert("RGB").save(a.uit, "JPEG", quality=90)
    print(a.uit)


if __name__ == "__main__":
    main()
