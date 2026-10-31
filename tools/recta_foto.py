#!/usr/bin/env python3
"""Foto editorial de Recta al Pecho a partir de un fotograma del video.
Uso: recta_foto.py entrada.jpg salida.jpg "KICKER" "Nombre del pelotero" [--zoom 1.08] [--focus 0.5,0.45]
Tratamiento: recorte 16:9 con zoom, nitidez, grado cálido de contraste, viñeta, grano fino,
degradado inferior, barra roja + kicker + nombre (Poppins) y logo de Recta abajo a la derecha."""
import sys, random
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont, ImageOps, ImageChops
W, H = 1600, 900
RED = (226, 38, 47)
def main():
    a = sys.argv[1:]
    src, dst = a[0], a[1]
    kicker = a[2] if len(a) > 2 and not a[2].startswith('--') else ''
    name = a[3] if len(a) > 3 and not a[3].startswith('--') else ''
    zoom = float(a[a.index('--zoom') + 1]) if '--zoom' in a else 1.08
    fx, fy = (0.5, 0.45)
    if '--focus' in a: fx, fy = map(float, a[a.index('--focus') + 1].split(','))
    im = Image.open(src).convert('RGB')
    # recorte 16:9 con zoom alrededor del punto de interés
    w, h = im.size
    cw, ch = w / zoom, h / zoom
    if cw / ch > 16 / 9: cw = ch * 16 / 9
    else: ch = cw * 9 / 16
    x0 = min(max(fx * w - cw / 2, 0), w - cw); y0 = min(max(fy * h - ch / 2, 0), h - ch)
    im = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.LANCZOS)
    # grado: nitidez, contraste, saturación suave, tono cálido en sombras
    im = im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=90, threshold=2))
    im = ImageEnhance.Contrast(im).enhance(1.12)
    im = ImageEnhance.Color(im).enhance(0.92)
    warm = Image.new('RGB', (W, H), (255, 214, 170))
    im = Image.blend(im, ImageChops.multiply(im, warm), 0.18)
    im = ImageEnhance.Brightness(im).enhance(1.04)
    # viñeta
    vig = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(vig); d.ellipse((-W * 0.25, -H * 0.35, W * 1.25, H * 1.35), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(220))
    im = Image.composite(im, ImageEnhance.Brightness(im).enhance(0.55), vig)
    # grano fino
    random.seed(7)
    noise = Image.effect_noise((W, H), 18).convert('L')
    im = Image.blend(im, Image.merge('RGB', (noise, noise, noise)), 0.06)
    # degradado inferior para el texto
    grad = Image.new('L', (1, H), 0); gd = ImageDraw.Draw(grad)
    for y in range(H):
        t = max(0, (y - H * 0.55) / (H * 0.45)); gd.point((0, y), int(200 * t ** 1.6))
    grad = grad.resize((W, H))
    im = Image.composite(Image.new('RGB', (W, H), (8, 8, 10)), im, ImageChops.invert(grad)) if False else Image.composite(Image.new('RGB', (W, H), (8, 8, 10)), im, grad)
    draw = ImageDraw.Draw(im)
    fb = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'; fs = '/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf'
    if kicker or name:
        draw.rectangle((64, H - 64 - 118, 72, H - 64), fill=RED)
        if kicker:
            draw.text((92, H - 64 - 118), kicker.upper(), font=ImageFont.truetype(fs, 26), fill=RED)
        if name:
            draw.text((92, H - 64 - 78), name, font=ImageFont.truetype(fb, 56), fill=(255, 255, 255))
    # logo
    logo = Image.open(__file__.rsplit('/tools/', 1)[0] + '/themes/recta/img/logo.png').convert('RGBA')
    lw = 300; logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    im.paste(logo, (W - lw - 56, H - logo.height - 48), logo)
    im.save(dst, quality=90, optimize=True)
    im.resize((800, 450), Image.LANCZOS).save(dst.replace('.jpg', '-card.jpg'), quality=88)
    print(dst)
main()
