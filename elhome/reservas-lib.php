<?php
// Funciones comunes de las entradas (reservas.php y entradas-admin.php). No se abre directo.
if (basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) { http_response_code(404); exit; }
date_default_timezone_set('America/Los_Angeles');

function dir_datos() {
  $dir = __DIR__ . '/opiniones';
  if (!is_dir($dir)) mkdir($dir, 0750, true);
  if (!file_exists("$dir/.htaccess")) file_put_contents("$dir/.htaccess", "<IfModule mod_authz_core.c>\nRequire all denied\n</IfModule>\n<IfModule !mod_authz_core.c>\nDeny from all\n</IfModule>\n");
  if (!file_exists("$dir/index.html")) file_put_contents("$dir/index.html", '');
  return $dir;
}
function limpio($s, $max) { return mb_substr(trim(strip_tags((string)$s)), 0, $max); }
function fallo($msg, $code = 400) { http_response_code($code); echo json_encode(['ok' => false, 'error' => $msg]); exit; }
function hoy_lv() { return date('Y-m-d'); }

// Cada grabación puede tener varios TURNOS (p. ej. 3 PM y 6 PM): cada turno es una función con su propio cupo
// y su propio id "<grabación>-<turno>"; "grupo" = la grabación a la que pertenece.
function grabaciones() {
  $l = json_decode(@file_get_contents(__DIR__ . '/grabaciones.json'), true) ?: [];
  $o = [];
  foreach ($l as $g) {
    if (empty($g['id'])) continue;
    $turnos = $g['turnos'] ?? null; unset($g['turnos']);
    $g['grupo'] = $g['id'];
    if (!$turnos) { $g['cupo'] = intval($g['cupo'] ?? 0); $o[$g['id']] = $g; continue; }
    foreach ($turnos as $t) { $f = $g; $f['id'] = $g['id'] . '-' . $t['id']; $f['hora'] = $t['hora'] ?? ''; $f['cupo'] = intval($t['cupo'] ?? 0); $o[$f['id']] = $f; }
  }
  return $o;
}
function leer_reservas() {
  $f = dir_datos() . '/reservas.json';
  $db = file_exists($f) ? json_decode(file_get_contents($f), true) : null;
  return is_array($db) && isset($db['reservas']) ? $db : ['reservas' => []];
}
// Lee, cambia y guarda con candado (dos personas reservando a la vez no pisan el cupo)
function con_reservas($fn) {
  $f = dir_datos() . '/reservas.json';
  $h = fopen($f, 'c+'); if (!$h) return null;
  flock($h, LOCK_EX);
  $txt = stream_get_contents($h);
  $db = $txt ? json_decode($txt, true) : null;
  if (!is_array($db) || !isset($db['reservas'])) $db = ['reservas' => []];
  $res = $fn($db);
  ftruncate($h, 0); rewind($h);
  fwrite($h, json_encode($db, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
  fflush($h); flock($h, LOCK_UN); fclose($h);
  @copy($f, dir_datos() . '/reservas-respaldo-' . date('Y-m-d') . '.json');
  return $res;
}
function ocupadas($db, $gid) { $n = 0; foreach ($db['reservas'] as $r) if ($r['grabacion'] === $gid && $r['estado'] === 'confirmada') $n += $r['cantidad']; return $n; }
function en_espera($db, $gid) { $n = 0; foreach ($db['reservas'] as $r) if ($r['grabacion'] === $gid && $r['estado'] === 'espera') $n += $r['cantidad']; return $n; }
// Al liberarse asientos, pasan a confirmadas las de la lista de espera que quepan, por orden de llegada
function promover(&$db, $gid) {
  $g = grabaciones()[$gid] ?? null; if (!$g) return;
  foreach ($db['reservas'] as &$r) {
    if ($r['grabacion'] !== $gid || $r['estado'] !== 'espera') continue;
    if ($r['cantidad'] <= $g['cupo'] - ocupadas($db, $gid)) { $r['estado'] = 'confirmada'; $r['actualizada'] = date('c'); }
  }
}
function codigo_nuevo($db) {
  $abc = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  $usados = array_column($db['reservas'], 'codigo');
  do { $c = ''; for ($i = 0; $i < 6; $i++) $c .= $abc[random_int(0, strlen($abc) - 1)]; } while (in_array($c, $usados, true));
  return $c;
}
function publica($r) {
  return ['codigo' => $r['codigo'], 'grabacion' => $r['grabacion'], 'nombre' => $r['nombre'], 'cantidad' => $r['cantidad'], 'estado' => $r['estado'], 'entro' => $r['entro'] ?? null];
}
function limite($que, $n, $seg) {
  $f = dir_datos() . '/.limite-' . $que . '.json';
  $ip = hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? '') . 'elhome-' . $que);
  $l = file_exists($f) ? (json_decode(file_get_contents($f), true) ?: []) : [];
  $ahora = time();
  foreach ($l as $k => $ts) { $l[$k] = array_values(array_filter($ts, fn($t) => $ahora - $t < $seg)); if (!$l[$k]) unset($l[$k]); }
  if (count($l[$ip] ?? []) >= $n) return false;
  $l[$ip][] = $ahora; file_put_contents($f, json_encode($l), LOCK_EX); return true;
}
