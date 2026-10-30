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
# Enlace del sitio con las apps Android (assetlinks): va en la raíz del sitio
mkdir -p "$DEST/.well-known" && cp .well-known/assetlinks.json "$DEST/.well-known/assetlinks.json"
