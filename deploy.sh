#!/bin/bash
# Despliegue de las apps MBM: lo llama el cron de cPanel cada 5 minutos.
# Baja los cambios del repositorio y los copia a la carpeta real del sitio,
# sin tocar nunca las claves (*-config.js / *-config.php) ni la carpeta opiniones/.
set -e
REPO=$HOME/repositories/mbm-web
DEST=$HOME/public_html/marrerobernalmedia.com
cd "$REPO"
git pull -q origin main
EXC="--exclude=*-config.js --exclude=*-config.php --exclude=opiniones/ --exclude=.git"
rsync -a $EXC elhome/ "$DEST/elhome/"
rsync -a $EXC recta/  "$DEST/recta/"
# Maquetas de rediseño de los sitios (solo para revisión de Eliam)
[ -d maquetas ] && rsync -a --delete --exclude=build.py --exclude=frames/out maquetas/ "$DEST/maquetas/"
# Tema propio de rectaalpecho.com (themes/recta) → wp-content/themes/recta del sitio
RECTA=$HOME/public_html/rectaalpecho
[ -d themes/recta ] && [ -d "$RECTA/wp-content/themes" ] && rsync -a --delete themes/recta/ "$RECTA/wp-content/themes/recta/"
# Tema propio de marrerobernal.com (themes/mba) → wp-content/themes/mba del dominio primario (public_html)
MBA=$HOME/public_html
[ -d themes/mba ] && [ -d "$MBA/wp-content/themes" ] && rsync -a --delete themes/mba/ "$MBA/wp-content/themes/mba/"
# App de Marrero Bernal & Associates (mba-app) → marrerobernal.com/app/ y su enlace con la app Android
[ -d mba-app ] && mkdir -p "$MBA/app" && rsync -a --delete mba-app/ "$MBA/app/"
# Página corta para bajar la app: marrerobernal.com/download (y /bajar, la misma página)
[ -d mba-bajar ] && mkdir -p "$MBA/bajar" && rsync -a --delete mba-bajar/ "$MBA/bajar/"
[ -d mba-bajar ] && mkdir -p "$MBA/download" && rsync -a --delete mba-bajar/ "$MBA/download/"
[ -f .well-known/assetlinks-mba.json ] && mkdir -p "$MBA/.well-known" && cp .well-known/assetlinks-mba.json "$MBA/.well-known/assetlinks.json"
# Tema propio de marrerobernalmedia.com (themes/mbm) → wp-content/themes/mbm del mismo DEST
[ -d themes/mbm ] && [ -d "$DEST/wp-content/themes" ] && rsync -a --delete themes/mbm/ "$DEST/wp-content/themes/mbm/"
# Enlace del sitio con las apps Android (assetlinks): va en la raíz del sitio
mkdir -p "$DEST/.well-known" && cp .well-known/assetlinks.json "$DEST/.well-known/assetlinks.json"
# Archivos sueltos de la raíz de marrerobernalmedia.com (verificaciones, etc.)
[ -d root ] && cp root/* "$DEST/"
# Archivos sueltos de la raíz de rectaalpecho.com (verificación de Search Console, etc.)
[ -d root_recta ] && [ -d "$HOME/public_html/rectaalpecho" ] && cp root_recta/* "$HOME/public_html/rectaalpecho/"
# Straight 2D Chest (www.straight2dchest.com, sitio en inglés generado por tools/build_s2d.js).
# Vista previa en marrerobernalmedia.com/s2d/ y, cuando exista la carpeta del dominio adicional, en el dominio.
[ -d s2d ] && rsync -a --delete $EXC s2d/ "$DEST/s2d/"
for D in "$HOME/public_html/straight2dchest.com" "$HOME/straight2dchest.com"; do
  [ -d s2d ] && [ -d "$D" ] && rsync -a --delete --exclude=.well-known --exclude=cgi-bin $EXC s2d/ "$D/"
done
# Avisos de estreno (OneSignal): se mandan desde aquí cada 5 minutos, así no dependen de otro cron.
# avisos.php no repite un aviso ya enviado (lo anota en opiniones/avisos_enviados.json) y no manda nada antes de las 8:00 AM LV.
# El resultado de la última corrida queda en <app>/avisos-estado.txt (sin claves) para poder revisarlo desde fuera.
PHP=""
for P in /usr/local/bin/php /usr/bin/php /opt/cpanel/ea-php82/root/usr/bin/php /opt/cpanel/ea-php81/root/usr/bin/php "$(command -v php 2>/dev/null)"; do
  [ -n "$P" ] && [ -x "$P" ] && { PHP="$P"; break; }
done
for A in elhome recta; do
  [ -f "$DEST/$A/avisos.php" ] || continue
  if [ -n "$PHP" ]; then
    OUT=$(cd "$DEST/$A" && "$PHP" avisos.php 2>&1 | tail -n 5) || true
  else
    OUT="No encontré php en el servidor"
  fi
  { TZ=America/Los_Angeles date '+%Y-%m-%d %H:%M:%S'; echo "$OUT" | head -c 500; echo; } > "$DEST/$A/avisos-estado.txt" 2>/dev/null || true
done
