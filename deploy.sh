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
# Enlace del sitio con las apps Android (assetlinks): va en la raíz del sitio
mkdir -p "$DEST/.well-known" && cp .well-known/assetlinks.json "$DEST/.well-known/assetlinks.json"
# Archivos sueltos de la raíz de marrerobernalmedia.com (verificaciones, etc.)
[ -d root ] && cp root/* "$DEST/"
