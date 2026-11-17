# Genera íconos, banner de TV (320x180 / 640x360) y pantalla de arranque de la app de Android TV de Recta Al Pecho.
# Fuente: recta/icons (logo oficial). Correr desde android/recta-tv: python3 tools/generar_imagenes.py
from PIL import Image, ImageDraw, ImageFont
import os
R = "android/app/src/main/res"
LOGO = Image.open("../../recta/icons/icon-512.png").convert("RGBA")
MASK = Image.open("../../recta/icons/maskable-512.png").convert("RGBA")
BG = (10, 20, 36, 255); LIME = (255, 75, 85, 255)
F = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
def font(s):
    try: return ImageFont.truetype(F, s)
    except Exception: return ImageFont.load_default()
D = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
for d, s in D.items():
    p = f"{R}/mipmap-{d}"; os.makedirs(p, exist_ok=True)
    sq = LOGO.resize((s, s), Image.LANCZOS)
    sq.save(f"{p}/ic_launcher.png")
    rd = Image.new("RGBA", (s, s), (0, 0, 0, 0)); m = Image.new("L", (s, s), 0)
    ImageDraw.Draw(m).ellipse((0, 0, s - 1, s - 1), fill=255); rd.paste(sq, (0, 0), m); rd.save(f"{p}/ic_launcher_round.png")
    fg = int(s * 108 / 48)  # capa del ícono adaptable (108dp)
    MASK.resize((fg, fg), Image.LANCZOS).save(f"{p}/ic_launcher_foreground.png")
def banner(w, h, path):
    im = Image.new("RGBA", (w, h), BG); dr = ImageDraw.Draw(im)
    pad = int(h * .10); lg = LOGO.resize((int(h * .80), int(h * .80)), Image.LANCZOS)
    cm = Image.new("L", lg.size, 0); ImageDraw.Draw(cm).ellipse((0, 0, lg.width - 1, lg.height - 1), fill=255)
    im.paste(lg, (pad, (h - lg.height) // 2), cm)
    x = pad * 2 + lg.width; room = w - x - pad
    def fit(t, s):
        while s > 6 and dr.textlength(t, font=font(s)) > room: s -= 1
        return font(s)
    f1 = fit("AL PECHO", int(h * .22)); f2 = fit("Puro béisbol", int(h * .12))
    dr.text((x, h * .20), "RECTA", font=f1, fill=(243, 239, 230, 255))
    dr.text((x, h * .43), "AL PECHO", font=f1, fill=LIME)
    dr.text((x, h * .68), "Puro béisbol", font=f2, fill=(154, 168, 189, 255))
    im.convert("RGB").save(path)
os.makedirs(f"{R}/drawable-xhdpi", exist_ok=True)
banner(320, 180, f"{R}/drawable/banner.png")
banner(640, 360, f"{R}/drawable-xhdpi/banner.png")
# Arranque: logo centrado sobre fondo oscuro
for root, _, files in os.walk(R):
    for fn in files:
        if fn == "splash.png":
            p = os.path.join(root, fn); w, h = Image.open(p).size
            im = Image.new("RGBA", (w, h), BG); s = int(min(w, h) * .35)
            lg = LOGO.resize((s, s), Image.LANCZOS); cm = Image.new("L", (s * 4, s * 4), 0)
            ImageDraw.Draw(cm).ellipse((6, 6, s * 4 - 7, s * 4 - 7), fill=255); cm = cm.resize((s, s), Image.LANCZOS)
            im.paste(lg, ((w - s) // 2, (h - s) // 2), cm)  # solo la pelota redonda, sin el cuadrado blanco
            im.convert("RGB").save(p)
print("ok")
