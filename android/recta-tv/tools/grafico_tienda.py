# Gráfico de la ficha de Google Play de Recta (1024x500). Fondo de un solo color y todo el contenido
# lejos de los bordes, porque la tienda del televisor recorta los lados (Eliam, 17-nov-2026).
# Uso (desde la raíz del repo): python3 android/recta-tv/tools/grafico_tienda.py
import io, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
BG = (10, 20, 36); ROJO = (255, 75, 85); BLANCO = (244, 240, 230); GRIS = (154, 168, 189)
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"; FM = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
def logo(h):
    png = subprocess.run(["rsvg-convert", "-h", str(h), "brand/recta/recta-logo-vertical.svg"], capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(png)).convert("RGBA")
def hacer(path, en=False):
    W, H, M = 1024, 500, 120            # M = margen lateral seguro
    im = Image.new("RGB", (W, H), BG); dr = ImageDraw.Draw(im)
    if en:  # en inglés va el logo de Straight 2D Chest
        lg = Image.open("s2d/img/logo-sq.webp").convert("RGBA"); lg = lg.resize((int(lg.width * 330 / lg.height), 330), Image.LANCZOS)
    else: lg = logo(330)
    im.paste(lg, (M, (H - lg.height) // 2), lg)
    x = M + lg.width + 40; room = W - M - x
    l1, l2, l3 = (("BASEBALL,", "TOLD BY THE ONES", "WHO LIVED IT") if en else ("LA PELOTA,", "CONTADA POR LOS", "QUE LA VIVIERON"))
    sub = "Interviews, myths and stories" if en else "Entrevistas, mitos y noticias"
    pill = "New episode every Thursday" if en else "Estreno cada jueves"
    s = 60
    while max(dr.textlength(t, font=ImageFont.truetype(FB, s)) for t in (l1, l2, l3)) > room: s -= 1
    f = ImageFont.truetype(FB, s); fs = ImageFont.truetype(FM, 22); fp = ImageFont.truetype(FB, 20)
    lh = int(s * 1.12); alto = lh * 3 + 14 + 30 + 22 + 44; y = (H - alto) // 2
    dr.text((x, y), l1, font=f, fill=BLANCO); dr.text((x, y + lh), l2, font=f, fill=BLANCO); dr.text((x, y + 2 * lh), l3, font=f, fill=ROJO)
    y2 = y + 3 * lh + 14; dr.text((x, y2), sub, font=fs, fill=GRIS)
    y3 = y2 + 30 + 22; pw = int(dr.textlength(pill, font=fp)) + 44
    dr.rounded_rectangle((x, y3, x + pw, y3 + 44), 22, fill=ROJO); dr.text((x + 22, y3 + 8), pill, font=fp, fill=(255, 255, 255))
    im.save(path)
hacer("recta/tiendas/play/recta_grafico_1024x500.png")
hacer("recta/tiendas/play/s2d_grafico_1024x500.png", en=True)
print("ok")
