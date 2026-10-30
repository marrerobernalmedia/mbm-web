# mbm-web — Marrero Bernal Media

Código de las apps web instalables de la red (se publican en https://marrerobernalmedia.com/).

- `elhome/` → https://marrerobernalmedia.com/elhome/  (El Home de la Risa)
- `recta/`  → https://marrerobernalmedia.com/recta/   (Recta Al Pecho)

Claude actualiza este repositorio (data.js el día de cada estreno, mejoras de index.html). El servidor lo copia solo a `public_html/marrerobernalmedia.com/` con `deploy.sh` (cron de cPanel cada 5 min, tarea t125 de Melanie); `.cpanel.yml` hace lo mismo cuando se pulsa "Deploy HEAD Commit" en cPanel.

Nunca están aquí (viven solo en el servidor): `onesignal-config.js`, `avisos-config.php` y la carpeta `opiniones/`.
