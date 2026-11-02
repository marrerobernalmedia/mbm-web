<?php
// ============================================================
// Opiniones de la app — Marrero Bernal Media
// Recibe lo que la gente escribe en "¿Cómo mejoramos la app?"
// y lo guarda en opiniones/opiniones.csv (carpeta protegida).
// ============================================================

// Correo que recibe un aviso con cada opinión. Si se deja vacío, solo se guarda en el archivo.
$AVISAR_A = 'eliam@emarreroagency.com';
$APP = 'Recta Al Pecho';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }
if (!empty($_POST['web'])) { echo '{"ok":true}'; exit; } // trampa para robots

function campo($k, $max) { return mb_substr(trim(strip_tags($_POST[$k] ?? '')), 0, $max); }
$tipo     = campo('tipo', 40);
$texto    = campo('texto', 2000);
$contacto = campo('contacto', 120);
$pantalla = campo('pantalla', 40);
$nota     = intval($_POST['nota'] ?? 0);
if ($nota < 0 || $nota > 5) $nota = 0;
if ($texto === '' && $nota === 0) { http_response_code(400); echo '{"ok":false}'; exit; }

$dir = __DIR__ . '/opiniones';
if (!is_dir($dir)) mkdir($dir, 0750, true);
if (!file_exists("$dir/.htaccess")) {
  file_put_contents("$dir/.htaccess",
    "<IfModule mod_authz_core.c>\nRequire all denied\n</IfModule>\n<IfModule !mod_authz_core.c>\nDeny from all\n</IfModule>\n");
}
if (!file_exists("$dir/index.html")) file_put_contents("$dir/index.html", '');

// Una opinión cada 30 segundos por conexión
$marca = "$dir/.limite.json";
$ip = hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? '') . $APP);
$lim = file_exists($marca) ? (json_decode(file_get_contents($marca), true) ?: []) : [];
$ahora = time();
foreach ($lim as $k => $t) if ($ahora - $t > 3600) unset($lim[$k]);
if (isset($lim[$ip]) && $ahora - $lim[$ip] < 30) { http_response_code(429); echo '{"ok":false}'; exit; }
$lim[$ip] = $ahora;
file_put_contents($marca, json_encode($lim), LOCK_EX);

$archivo = "$dir/opiniones.csv";
$nuevo = !file_exists($archivo) || filesize($archivo) === 0;
$f = fopen($archivo, 'a');
if (!$f) { http_response_code(500); echo '{"ok":false}'; exit; }
flock($f, LOCK_EX);
if ($nuevo) { fwrite($f, "\xEF\xBB\xBF"); fputcsv($f, ['fecha', 'app', 'tipo', 'nota', 'opinion', 'contacto', 'pantalla']); }
fputcsv($f, [date('Y-m-d H:i'), $APP, $tipo, $nota ?: '', $texto, $contacto, $pantalla]);
flock($f, LOCK_UN);
fclose($f);

if ($AVISAR_A) {
  $cuerpo = "App: $APP\nTipo: $tipo\nNota: " . ($nota ?: '-') . "\nPantalla: $pantalla\nContacto: $contacto\n\n$texto\n";
  @mail($AVISAR_A, "=?UTF-8?B?" . base64_encode("Opinión de la app $APP") . "?=", $cuerpo,
        "Content-Type: text/plain; charset=UTF-8\r\nFrom: app@" . ($_SERVER['HTTP_HOST'] ?? 'localhost'));
}

echo '{"ok":true}';
