<?php
// ============================================================
// Entradas gratis a las grabaciones — El Home de la Risa (Eliam, 11-nov-2026)
// Las grabaciones están en grabaciones.json (fecha, lugar, cupo, máximo por persona).
// Reglas (Eliam, 11-nov-2026): solo celulares de Cuba (+53); máximo 4 entradas por reserva y UNA reserva por teléfono (por número y por aparato) en cada grabación.
// Las reservas se guardan en opiniones/reservas.json (carpeta protegida, no está en el repo).
// Lo usa entradas.js desde la app. La lista y la puerta: entradas-admin.php.
//   GET  ?accion=cupos                 → asientos libres de cada grabación
//   GET  ?accion=mias&disp=ID          → reservas de este teléfono
//   POST accion=reservar  (grabacion, nombre, telefono, cantidad, disp)
//   POST accion=cancelar  (codigo, disp)
// ============================================================
//   POST accion=reconfirmar (codigo, disp)  → confirmación final desde la app
//   GET  ?c=TOKEN                      → página del enlace de WhatsApp para confirmar o cancelar (reservas-confirmar.php)
require __DIR__ . '/reservas-lib.php';
header('Cache-Control: no-store');
al_dia();
if (isset($_GET['c']) || isset($_POST['c'])) { require __DIR__ . '/reservas-confirmar.php'; exit; }
header('Content-Type: application/json; charset=utf-8');

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
  // Reservas de ensayo (disp "prueba-…", creadas por el equipo): devuelven su enlace de confirmación y, con avisar=1, arrancan las 24 horas como si ya se les hubiera escrito
  $ensayo = strncmp($disp, 'prueba-', 7) === 0;
  if ($ensayo && !empty($_GET['avisar'])) con_reservas(function (&$db) use ($disp) {
    foreach ($db['reservas'] as &$r) if (($r['disp'] ?? '') === $disp && $r['estado'] !== 'cancelada' && empty($r['aviso'])) { $r['aviso'] = date('c'); $r['actualizada'] = date('c'); }
  });
  // borrar=1: quita del archivo todas las reservas de ese aparato de ensayo (también las canceladas), para dejar la lista limpia
  if ($ensayo && !empty($_GET['borrar'])) {
    $n = con_reservas(function (&$db) use ($disp) {
      $antes = count($db['reservas']);
      $db['reservas'] = array_values(array_filter($db['reservas'], fn($r) => ($r['disp'] ?? '') !== $disp));
      return $antes - count($db['reservas']);
    });
    echo json_encode(['ok' => true, 'borradas' => $n, 'quedan' => count(leer_reservas()['reservas'])]); exit;
  }
  $db = leer_reservas();
  $out = [];
  foreach ($db['reservas'] as $r) if (($r['disp'] ?? '') === $disp && $r['estado'] !== 'cancelada') { $p = publica($r); if ($ensayo) $p['enlace'] = enlace_confirmar($r); $out[] = $p; }
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
  // Solo celulares de Cuba (+53): la grabación es en Cuba y la confirmación final va por WhatsApp a ese número (Eliam, 11-nov-2026)
  $dig = preg_replace('/^00/', '', preg_replace('/\D/', '', $tel));
  if (strlen($dig) === 10 && str_starts_with($dig, '53')) $dig = substr($dig, 2);
  if (!preg_match('/^[56]\d{7}$/', $dig)) fallo('Escribe tu celular de Cuba: el 5 y siete números más (ejemplo: +53 5 3787159). Las entradas son para quienes están en Cuba.');
  $tel = '+53' . $dig; $dig = '53' . $dig;
  $max = max(1, intval($g['max'] ?? 4));
  if ($cant < 1 || $cant > $max) fallo("Puedes reservar de 1 a $max entradas.");
  if (strlen($disp) < 12) fallo('Las entradas se reservan desde la app de El Home de la Risa.');
  if (!limite('reservar', 8, 3600)) fallo('Demasiados intentos. Prueba en un rato.', 429);

  $res = con_reservas(function (&$db) use ($gid, $g, $G, $nombre, $tel, $dig, $cant, $disp) {
    // Un teléfono, un solo turno por grabación
    foreach ($db['reservas'] as $x) {
      if ($x['grabacion'] !== $gid && $x['estado'] !== 'cancelada' && ($G[$x['grabacion']]['grupo'] ?? '') === $g['grupo'] && preg_replace('/\D/', '', $x['telefono']) === $dig)
        return ['otro' => $G[$x['grabacion']]['hora'] ?? ''];
    }
    // Una sola reserva por teléfono (aparato): si esta app ya reservó con otro número para esta grabación, no puede hacer otra (Eliam, 11-nov-2026)
    foreach ($db['reservas'] as $x) {
      if ($x['estado'] !== 'cancelada' && ($x['disp'] ?? '') === $disp && ($G[$x['grabacion']]['grupo'] ?? '') === $g['grupo'] && preg_replace('/\D/', '', $x['telefono']) !== $dig)
        return ['aparato' => true];
    }
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
          'estado' => $cant <= $libres ? 'confirmada' : 'espera', 'creada' => date('c'), 'disp' => $disp, 'entro' => null, 'tok' => token_nuevo()];
    $db['reservas'][] = $r;
    return ['r' => $r, 'nueva' => true];
  });
  if (!$res) fallo('No se pudo guardar. Prueba otra vez.', 500);
  if (isset($res['aparato'])) fallo('Este teléfono ya tiene una reserva para esta grabación (máximo ' . $max . ' entradas). Cada persona reserva desde su propia app.');
  if (isset($res['otro'])) fallo('Ya tienes entradas para el turno de las ' . $res['otro'] . ' de esta grabación. Si quieres cambiar de turno, cancela esas primero.');
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

if ($accion === 'reconfirmar') {
  $cod = strtoupper(limpio($_POST['codigo'] ?? '', 12));
  $disp = limpio($_POST['disp'] ?? '', 64);
  $r = con_reservas(function (&$db) use ($cod, $disp) {
    foreach ($db['reservas'] as &$r) if ($r['codigo'] === $cod && ($r['disp'] ?? '') === $disp && $disp !== '') {
      if ($r['estado'] === 'cancelada') return ['cancelada' => true];
      $r['reconf'] = date('c'); $r['reconf_via'] = 'app'; $r['actualizada'] = date('c'); return ['r' => $r];
    }
    return null;
  });
  if (!$r) fallo('No encontramos esa reserva.');
  if (isset($r['cancelada'])) fallo('Esa reserva ya se canceló porque no se confirmó a tiempo. Si quedan entradas, puedes reservar de nuevo.');
  echo json_encode(['ok' => true, 'reserva' => publica($r['r'])]); exit;
}

fallo('Acción desconocida.');
