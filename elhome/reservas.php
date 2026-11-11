<?php
// ============================================================
// Entradas gratis a las grabaciones — El Home de la Risa (Eliam, 11-nov-2026)
// Las grabaciones están en grabaciones.json (fecha, lugar, cupo, máximo por persona).
// Las reservas se guardan en opiniones/reservas.json (carpeta protegida, no está en el repo).
// Lo usa entradas.js desde la app. La lista y la puerta: entradas-admin.php.
//   GET  ?accion=cupos                 → asientos libres de cada grabación
//   GET  ?accion=mias&disp=ID          → reservas de este teléfono
//   POST accion=reservar  (grabacion, nombre, telefono, cantidad, disp)
//   POST accion=cancelar  (codigo, disp)
// ============================================================
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
require __DIR__ . '/reservas-lib.php';

$accion = $_POST['accion'] ?? $_GET['accion'] ?? '';
$G = grabaciones();

if ($accion === 'cupos') {
  $db = leer_reservas();
  $out = [];
  foreach ($G as $id => $g) $out[$id] = ['cupo' => $g['cupo'], 'ocupadas' => ocupadas($db, $id), 'espera' => en_espera($db, $id)];
  echo json_encode(['ok' => true, 'cupos' => $out]); exit;
}

if ($accion === 'mias') {
  $disp = limpio($_GET['disp'] ?? '', 64);
  if (strlen($disp) < 12) { echo '{"ok":true,"reservas":[]}'; exit; }
  $db = leer_reservas();
  $out = [];
  foreach ($db['reservas'] as $r) if (($r['disp'] ?? '') === $disp && $r['estado'] !== 'cancelada') $out[] = publica($r);
  echo json_encode(['ok' => true, 'reservas' => $out]); exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }
if (!empty($_POST['web'])) { echo '{"ok":true}'; exit; } // trampa para robots

if ($accion === 'reservar') {
  $gid = limpio($_POST['grabacion'] ?? '', 40);
  $nombre = limpio($_POST['nombre'] ?? '', 80);
  $tel = preg_replace('/[^\d+]/', '', $_POST['telefono'] ?? '');
  $cant = intval($_POST['cantidad'] ?? 0);
  $disp = limpio($_POST['disp'] ?? '', 64);
  if (!isset($G[$gid])) fallo('Esa grabación ya no está disponible.');
  $g = $G[$gid];
  if (empty($g['abierta']) || $g['fecha'] < hoy_lv()) fallo('Las reservas para esta grabación están cerradas.');
  if (mb_strlen($nombre) < 2) fallo('Escribe tu nombre.');
  $dig = preg_replace('/\D/', '', $tel);
  if (strlen($dig) < 7 || strlen($dig) > 15) fallo('Escribe un teléfono válido, con el código del país si no es de EE. UU.');
  $max = max(1, intval($g['max'] ?? 4));
  if ($cant < 1 || $cant > $max) fallo("Puedes reservar de 1 a $max entradas.");
  if (!limite('reservar', 8, 3600)) fallo('Demasiados intentos. Prueba en un rato.', 429);

  $res = con_reservas(function (&$db) use ($gid, $g, $nombre, $tel, $dig, $cant, $disp) {
    // Mismo teléfono y misma grabación: se actualiza la reserva que ya tiene
    foreach ($db['reservas'] as &$r) {
      if ($r['grabacion'] === $gid && $r['estado'] !== 'cancelada' && preg_replace('/\D/', '', $r['telefono']) === $dig) {
        $libres = $g['cupo'] - ocupadas($db, $gid) + ($r['estado'] === 'confirmada' ? $r['cantidad'] : 0);
        $r['nombre'] = $nombre; $r['telefono'] = $tel; if ($disp) $r['disp'] = $disp;
        if ($cant <= $libres) { $r['cantidad'] = $cant; $r['estado'] = 'confirmada'; }
        elseif ($r['estado'] !== 'confirmada') { $r['cantidad'] = $cant; $r['estado'] = 'espera'; }
        $r['actualizada'] = date('c');
        return ['r' => $r, 'nueva' => false];
      }
    }
    unset($r);
    $libres = $g['cupo'] - ocupadas($db, $gid);
    $r = ['codigo' => codigo_nuevo($db), 'grabacion' => $gid, 'nombre' => $nombre, 'telefono' => $tel, 'cantidad' => $cant,
          'estado' => $cant <= $libres ? 'confirmada' : 'espera', 'creada' => date('c'), 'disp' => $disp, 'entro' => null];
    $db['reservas'][] = $r;
    return ['r' => $r, 'nueva' => true];
  });
  if (!$res) fallo('No se pudo guardar. Prueba otra vez.', 500);
  echo json_encode(['ok' => true, 'reserva' => publica($res['r']), 'nueva' => $res['nueva']]); exit;
}

if ($accion === 'cancelar') {
  $cod = strtoupper(limpio($_POST['codigo'] ?? '', 12));
  $disp = limpio($_POST['disp'] ?? '', 64);
  $ok = con_reservas(function (&$db) use ($cod, $disp) {
    foreach ($db['reservas'] as &$r) if ($r['codigo'] === $cod && ($r['disp'] ?? '') === $disp && $disp !== '') {
      $r['estado'] = 'cancelada'; $r['actualizada'] = date('c'); promover($db, $r['grabacion']); return true;
    }
    return false;
  });
  echo json_encode(['ok' => (bool)$ok]); exit;
}

fallo('Acción desconocida.');
