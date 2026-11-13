# Ícono (1024, sin transparencia) y pantalla de arranque de las apps de iPhone/iPad.
# Uso: python3 apple/generar_imagenes.py  (desde la raíz del repo). Necesita rsvg-convert y Pillow.
import subprocess, os
from PIL import Image
R = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(R)
def logo(app):
    if app == "elhome":
        im = Image.open(f"{RAIZ}/brand/elhome/elhome-papito.png").convert("RGBA"); return im.crop(im.getbbox()), (0, 0, 0), 0.88
    if app == "mba":
        im = Image.open(f"{RAIZ}/brand/mba/mba-isotipo.png").convert("RGBA"); return im.crop(im.getbbox()), (255, 255, 255), 0.84
    t = "/tmp/pelota.png"; subprocess.run(["rsvg-convert", "-h", "2000", f"{RAIZ}/brand/recta/pelota-x-isotipo.svg", "-o", t], check=True)
    im = Image.open(t).convert("RGBA"); return im.crop(im.getbbox()), (255, 255, 255), 0.98
def poner(fondo, im, lado, frac):
    c = Image.new("RGB", (lado, lado), fondo); x = im.copy(); x.thumbnail((int(lado * frac), int(lado * frac)), Image.LANCZOS)
    c.paste(x, ((lado - x.size[0]) // 2, (lado - x.size[1]) // 2), x); return c
FONDO_SPLASH = {"elhome": (11, 11, 13), "recta": (10, 20, 36), "mba": (255, 255, 255)}
for app in ["elhome", "recta", "mba"]:
    a = f"{R}/{app}/ios/App/App/Assets.xcassets"
    im, fondo, frac = logo(app)
    poner(fondo, im, 1024, frac).save(f"{a}/AppIcon.appiconset/AppIcon-512@2x.png")
    s = poner(FONDO_SPLASH[app], im, 2732, 0.22)
    for n in ["splash-2732x2732.png", "splash-2732x2732-1.png", "splash-2732x2732-2.png"]: s.save(f"{a}/Splash.imageset/{n}")
    print(app, "listo")
