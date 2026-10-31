<?php
// ============================================================
// Avisos de estreno — Marrero Bernal Media
// Lee la lista de avisos que trae data.js (la prepara Claude cada semana)
// y manda por OneSignal el aviso del día cuando ya son las 8:00 AM en Las Vegas.
// Se ejecuta solo con el Cron Job del hosting (cada 15 minutos).
// No hace falta tocar este archivo: las claves van en avisos-config.php.
// ============================================================

require __DIR__ . '/avisos-config.php';   // define $ONESIGNAL_APP_ID, $ONESIGNAL_REST_KEY y $CLAVE_CRON

$desdeWeb = php_sapi_name() !== 'cli';
if ($desdeWeb) {
  header('Content-Type: text/plain; charset=utf-8');
  if (empty($CLAVE_CRON) || !hash_equals($CLAVE_CRON, (string)($_GET['clave'] ?? ''))) { http_response_code(403); exit("No autorizado\n"); }
}
if (empty($ONESIGNAL_APP_ID) || empty($ONESIGNAL_REST_KEY)) exit("Faltan las claves de OneSignal en avisos-config.php\n");

date_default_timezone_set('America/Los_Angeles');
$hoy = date('Y-m-d');
$prueba = $desdeWeb ? isset($_GET['prueba']) : in_array('prueba', $argv ?? []);

// Leer data.js: "window.APPDATA = {...};"
$js = @file_get_contents(__DIR__ . '/data.js');
if ($js === false) exit("No encuentro data.js\n");
$ini = strpos($js, '{'); $fin = strrpos($js, '}');
$data = json_decode(substr($js, $ini, $fin - $ini + 1), true);
$avisos = $data['avisos'] ?? [];

$dir = __DIR__ . '/opiniones';   // carpeta ya protegida por feedback.php
if (!is_dir($dir)) mkdir($dir, 0750, true);
if (!file_exists("$dir/.htaccess")) file_put_contents("$dir/.htaccess", "<IfModule mod_authz_core.c>\nRequire all denied\n</IfModule>\n<IfModule !mod_authz_core.c>\nDeny from all\n</IfModule>\n");
$registro = "$dir/avisos_enviados.json";
$enviados = file_exists($registro) ? (json_decode(file_get_contents($registro), true) ?: []) : [];

function mandar($appId, $key, $titulo, $texto, $url, $imagen, $tituloEn = '', $textoEn = '') {
  $cuerpo = [
    'app_id' => $appId,
    'target_channel' => 'push',
    'included_segments' => ['Total Subscriptions'],
    'headings' => ['en' => ($tituloEn ?: $titulo), 'es' => $titulo],
    'contents' => ['en' => ($textoEn ?: $texto), 'es' => $texto],   // el idioma lo elige cada suscriptor en la app (ES/EN)
    'url' => $url,
  ];
  if ($imagen) $cuerpo['chrome_web_image'] = $imagen;
  $ch = curl_init('https://api.onesignal.com/notifications?c=push');
  curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => ['Content-Type: application/json; charset=utf-8', 'Authorization: Key ' . $key],
    CURLOPT_POSTFIELDS => json_encode($cuerpo, JSON_UNESCAPED_UNICODE),
    CURLOPT_TIMEOUT => 20,
  ]);
  $res = curl_exec($ch); $code = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
  return [$code, $res];
}

if ($prueba) {
  [$code, $res] = mandar($ONESIGNAL_APP_ID, $ONESIGNAL_REST_KEY, 'Prueba de avisos', 'Si ves esto, los avisos de estreno funcionan.', 'https://www.youtube.com/', '');
  exit("Prueba enviada: $code $res\n");
}

if (date('H:i') < '08:00') exit("Todavía no son las 8:00 AM en Las Vegas\n");

$hechos = 0;
foreach ($avisos as $a) {
  if (($a['fecha'] ?? '') !== $hoy) continue;
  $id = $a['fecha'] . '|' . ($a['url'] ?? '') . '|' . ($a['titulo'] ?? '');
  if (isset($enviados[$id])) continue;
  [$code, $res] = mandar($ONESIGNAL_APP_ID, $ONESIGNAL_REST_KEY, $a['titulo'] ?? '', $a['texto'] ?? '', $a['url'] ?? '', $a['imagen'] ?? '', $a['titulo_en'] ?? '', $a['texto_en'] ?? '');
  if ($code >= 200 && $code < 300) { $enviados[$id] = date('c'); $hechos++; echo "Enviado: {$a['titulo']}\n"; }
  else echo "Error $code al enviar {$a['titulo']}: $res\n";
}
foreach ($enviados as $k => $v) if (strtotime($v) < time() - 60 * 86400) unset($enviados[$k]);
file_put_contents($registro, json_encode($enviados, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT), LOCK_EX);
echo $hechos ? "Listo\n" : "Nada que mandar hoy\n";
