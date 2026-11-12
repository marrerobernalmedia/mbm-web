<?php
// ============================================================
// Lista de reservas y control de la puerta — El Home de la Risa
// Entra con la contraseña (Eliam la tiene). El código QR de cada entrada abre esta página
// con ?entrada=CÓDIGO: quien está en la puerta lo escanea con la cámara del teléfono.
// Para cambiar la contraseña: php -r 'echo password_hash("NUEVA", PASSWORD_DEFAULT);' y pegar abajo.
// ============================================================
$CLAVE_HASH = '$2y$10$cdxXGdH6URGecet9DPav5ehqjFH/ayny/4ECETLVaOSesUDPSfjSO';

require __DIR__ . '/reservas-lib.php';
header('Cache-Control: no-store');
header('X-Robots-Tag: noindex');
session_set_cookie_params(['lifetime' => 60 * 60 * 24 * 30, 'httponly' => true, 'secure' => !empty($_SERVER['HTTPS']), 'samesite' => 'Lax']);
session_name('mbm_entradas'); session_start();
$h = fn($s) => htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8');
$G = grabaciones();
$entrada = strtoupper(preg_replace('/[^A-Za-z0-9]/', '', $_GET['entrada'] ?? ''));
$yo = strtok($_SERVER['REQUEST_URI'] ?? 'entradas-admin.php', '?');

// --- entrar / salir
if (isset($_POST['clave'])) {
  if (limite('admin', 10, 900) && password_verify($_POST['clave'], $CLAVE_HASH)) { session_regenerate_id(true); $_SESSION['ok'] = 1; }
  else $error = 'Contraseña incorrecta.';
}
if (isset($_GET['salir'])) { $_SESSION = []; session_destroy(); header("Location: $yo"); exit; }
$dentro = !empty($_SESSION['ok']);

// --- acciones (marcar entrada, confirmar, cancelar)
if ($dentro && isset($_POST['op'], $_POST['codigo'])) {
  $op = $_POST['op']; $cod = strtoupper(preg_replace('/[^A-Za-z0-9]/', '', $_POST['codigo']));
  con_reservas(function (&$db) use ($op, $cod) {
    foreach ($db['reservas'] as &$r) if ($r['codigo'] === $cod) {
      if ($op === 'entro') $r['entro'] = date('c');
      if ($op === 'desentro') $r['entro'] = null;
      if ($op === 'confirmar') $r['estado'] = 'confirmada';
      // Confirmación final por WhatsApp: "aviso" = se le escribió (empiezan las 24 h); "reconf" = confirmó que va
      if ($op === 'aviso' && empty($r['aviso']) && $r['estado'] !== 'cancelada') $r['aviso'] = date('c');
      if ($op === 'prorroga' && $r['estado'] !== 'cancelada') $r['aviso'] = date('c');
      if ($op === 'reconf' && $r['estado'] !== 'cancelada') { $r['reconf'] = date('c'); $r['reconf_via'] = 'equipo'; }
      if ($op === 'reactivar' && $r['estado'] === 'cancelada') {
        $g = grabaciones()[$r['grabacion']] ?? null;
        $r['estado'] = $g && $r['cantidad'] <= $g['cupo'] - ocupadas($db, $r['grabacion']) ? 'confirmada' : 'espera';
        $r['reconf'] = date('c'); $r['reconf_via'] = 'equipo'; unset($r['motivo']);
      }
      if ($op === 'cancelar') { $r['estado'] = 'cancelada'; promover($db, $r['grabacion']); }
      $r['actualizada'] = date('c'); return true;
    }
    return false;
  });
  $vuelta = $_POST['vuelta'] ?? $yo; header('Location: ' . (str_starts_with($vuelta, '/') ? $vuelta : $yo)); exit;
}

if ($dentro) {
  al_dia();
  // Las reservas hechas antes de este cambio no tienen enlace de confirmación: se les crea
  foreach (leer_reservas()['reservas'] as $x) if (empty($x['tok'])) { con_reservas(function (&$db) { foreach ($db['reservas'] as &$r) if (empty($r['tok'])) $r['tok'] = token_nuevo(); return true; }); break; }
}
$db = $dentro ? leer_reservas() : ['reservas' => []];

// --- CSV para Excel
if ($dentro && isset($_GET['csv'])) {
  $gid = $_GET['csv'];
  header('Content-Type: text/csv; charset=utf-8');
  header('Content-Disposition: attachment; filename="reservas-' . preg_replace('/[^a-z0-9-]/', '', $gid) . '.csv"');
  $o = fopen('php://output', 'w'); fwrite($o, "\xEF\xBB\xBF");
  fputcsv($o, ['codigo', 'nombre', 'telefono', 'entradas', 'estado', 'reservo', 'entro', 'avisado', 'confirmo', 'motivo']);
  foreach ($db['reservas'] as $r) if ($r['grabacion'] === $gid)
    fputcsv($o, [$r['codigo'], $r['nombre'], $r['telefono'], $r['cantidad'], $r['estado'], substr($r['creada'], 0, 16), $r['entro'] ? substr($r['entro'], 11, 5) : '', substr($r['aviso'] ?? '', 0, 16), substr($r['reconf'] ?? '', 0, 16), $r['motivo'] ?? '']);
  exit;
}
$fechaLarga = function ($f) { $d = strtotime($f . ' 12:00'); $dias = ['domingo','lunes','martes','miércoles','jueves','viernes','sábado']; $m = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']; return $dias[date('w', $d)] . ' ' . date('j', $d) . ' de ' . $m[date('n', $d) - 1] . ' de ' . date('Y', $d); };
// Mensaje de WhatsApp de la confirmación final (sale escrito; quien lo manda solo toca Enviar)
$msj = function ($r, $g) {
  $n = (int)$r['cantidad'];
  return 'Hola, ' . $r['nombre'] . ' 👋 Te escribimos de El Home de la Risa. Tienes ' . ($n === 1 ? '1 entrada' : $n . ' entradas') . ' para la grabación de ' . $g['titulo']
    . ' el ' . fecha_larga($g['fecha']) . (!empty($g['hora']) ? ', turno de las ' . $g['hora'] : '') . (!empty($g['lugar']) ? ', en ' . $g['lugar'] : '') . ".\n\n"
    . 'Confirma tu asistencia aquí en las próximas ' . HORAS_CONFIRMAR . " horas:\n" . enlace_confirmar($r) . "\n\n"
    . 'Si no confirmas, la reserva se cancela sola y tus entradas pasan a otra persona.';
};
$hace = function ($iso) { $s = time() - strtotime($iso); return $s < 3600 ? max(1, intdiv($s, 60)) . ' min' : ($s < 172800 ? intdiv($s, 3600) . ' h' : intdiv($s, 86400) . ' días'); };
$wa = fn($t) => 'https://wa.me/' . preg_replace('/\D/', '', (strlen(preg_replace('/\D/', '', $t)) === 10 && $t[0] !== '+' ? '1' : '') . $t);
?><!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex"><title>Entradas — El Home de la Risa</title><link rel="icon" href="icons/icon-192.png">
<style>:root{--bg:#0c0a0d;--card:#1c181f;--line:#2f2834;--fg:#f7f2ea;--mute:#a99fa8;--lime:#8fd11f;--red:#e2262f;--bulb:#ffd36b;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.w{max-width:900px;margin:0 auto;padding:16px max(16px,env(safe-area-inset-left)) 60px}
h1{font-size:22px;margin:4px 0 14px}h2{font-size:18px;margin:22px 0 4px}a{color:var(--lime)}
.top{display:flex;align-items:center;gap:10px;justify-content:space-between}.top img{width:36px;height:36px;border-radius:9px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;margin:10px 0}
input,button,select{font:inherit}input[type=password],input[type=search]{width:100%;padding:12px;border-radius:10px;border:1px solid var(--line);background:#120f14;color:var(--fg)}
.b{border:0;border-radius:10px;padding:10px 14px;font-weight:700;cursor:pointer;background:var(--lime);color:#111}.b.r{background:var(--red);color:#fff}.b.g{background:#2a2430;color:var(--fg)}
.stats{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}.stats div{background:#120f14;border:1px solid var(--line);border-radius:10px;padding:8px 12px}.stats b{display:block;font-size:20px}
table{width:100%;border-collapse:collapse;font-size:14px}td,th{padding:8px 6px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}th{color:var(--mute);font-weight:600}
.e{font-size:12px;font-weight:700;border-radius:6px;padding:2px 6px}.e.confirmada{background:#20351a;color:var(--lime)}.e.espera{background:#3a3010;color:var(--bulb)}.e.cancelada{background:#3a1416;color:#ff8a8a}
.ok{background:#20351a}.big{font-size:44px;font-weight:900;letter-spacing:.06em}.err{color:#ff8a8a}form.i{display:inline}
.mute{color:var(--mute)}.wa{display:inline-block;text-decoration:none;background:#25d366;color:#07240f;border-radius:8px;padding:6px 10px;font-weight:700;font-size:13px;margin-top:4px}
.cf{font-size:12px;margin-top:4px}.cf.si{color:var(--lime)}.cf.pe{color:var(--bulb)}.b.s{padding:6px 10px;font-size:13px;margin-top:4px}.nota{border-left:3px solid var(--bulb);padding:8px 12px;background:#120f14;border-radius:0 10px 10px 0;margin:8px 0;font-size:14px}</style></head><body><div class="w">
<div class="top"><div style="display:flex;gap:10px;align-items:center"><img src="icons/icon-192.png" alt=""><b>Entradas · El Home de la Risa</b></div><?php if ($dentro): ?><a href="<?= $h($yo) ?>?salir=1">Salir</a><?php endif; ?></div>
<?php if (!$dentro): ?>
  <h1>Entrar</h1>
  <form method="post" class="card"><p class="mute">Solo para el equipo. Escribe la contraseña.</p>
  <input type="password" name="clave" autocomplete="current-password" autofocus required><p><button class="b">Entrar</button></p>
  <?php if (!empty($error)) echo '<p class="err">' . $h($error) . '</p>'; ?></form>
<?php elseif ($entrada): // --- vista de la puerta: una entrada
  $r = null; foreach ($db['reservas'] as $x) if ($x['codigo'] === $entrada) $r = $x;
  $vuelta = $yo . '?entrada=' . $entrada; ?>
  <?php if (!$r): ?><div class="card"><h1 class="err">Esa entrada no existe</h1><p>Código <?= $h($entrada) ?></p></div>
  <?php else: $g = $G[$r['grabacion']] ?? ['titulo' => $r['grabacion'], 'fecha' => '']; ?>
  <div class="card <?= $r['entro'] ? '' : ($r['estado'] === 'confirmada' ? 'ok' : '') ?>">
    <p class="mute"><?= $h($g['titulo']) ?> · <?= $h($g['fecha'] ? $fechaLarga($g['fecha']) : '') ?></p>
    <?php if (!empty($g['hora'])): ?><h2 style="margin:0;color:var(--bulb)">TURNO DE LAS <?= $h($g['hora']) ?></h2><?php endif; ?>
    <div class="big"><?= (int)$r['cantidad'] ?> <?= $r['cantidad'] == 1 ? 'entrada' : 'entradas' ?></div>
    <h1 style="margin:6px 0"><?= $h($r['nombre']) ?></h1>
    <p><a href="<?= $h($wa($r['telefono'])) ?>"><?= $h($r['telefono']) ?></a> · código <b><?= $h($r['codigo']) ?></b> · <span class="e <?= $h($r['estado']) ?>"><?= $h($r['estado']) ?></span></p>
    <?php if ($r['entro']): ?><h2 class="err">⚠️ YA ENTRÓ a las <?= $h(substr($r['entro'], 11, 5)) ?></h2>
      <form method="post" class="i"><input type="hidden" name="codigo" value="<?= $h($r['codigo']) ?>"><input type="hidden" name="vuelta" value="<?= $h($vuelta) ?>"><button class="b g" name="op" value="desentro">Deshacer</button></form>
    <?php elseif ($r['estado'] === 'cancelada'): ?><h2 class="err">Reserva cancelada</h2>
    <?php else: ?>
      <?php if ($r['estado'] === 'espera'): ?><h2 style="color:var(--bulb)">Está en lista de espera</h2><?php endif; ?>
      <form method="post"><input type="hidden" name="codigo" value="<?= $h($r['codigo']) ?>"><input type="hidden" name="vuelta" value="<?= $h($vuelta) ?>">
      <button class="b" name="op" value="entro" style="width:100%;padding:16px;font-size:18px">✓ Marcar que entró</button></form>
    <?php endif; ?>
  </div>
  <?php endif; ?>
  <p><a href="<?= $h($yo) ?>">← Todas las reservas</a></p>
<?php else: // --- lista por grabación ?>
  <h1>Reservas</h1>
  <input type="search" id="q" placeholder="Buscar por nombre, teléfono o código">
  <?php foreach ($G as $gid => $g):
    $l = array_values(array_filter($db['reservas'], fn($r) => $r['grabacion'] === $gid));
    usort($l, fn($a, $b) => strcmp($a['creada'], $b['creada']));
    $conf = ocupadas($db, $gid); $esp = en_espera($db, $gid);
    $ent = array_sum(array_map(fn($r) => $r['entro'] ? $r['cantidad'] : 0, $l));
    $viv = array_filter($l, fn($r) => $r['estado'] !== 'cancelada');
    $nSi = count(array_filter($viv, fn($r) => !empty($r['reconf'])));
    $nPe = count(array_filter($viv, fn($r) => por_confirmar($r)));
    $nNo = count($viv) - $nSi - $nPe;
    $nCa = count(array_filter($l, fn($r) => ($r['motivo'] ?? '') === 'sin-confirmar'));
    $desde = date('Y-m-d', strtotime($g['fecha'] . ' 12:00') - DIAS_AVISO * 86400);
    $toca = (hoy_lv() >= $desde && hoy_lv() <= $g['fecha']) || !empty($_GET['prueba']); // ?prueba=1: muestra los botones antes de la fecha, para ensayar ?>
    <h2><?= $h($g['titulo']) ?><?= !empty($g['hora']) ? ' · turno de las ' . $h($g['hora']) : '' ?> — <?= $h($g['sub'] ?? '') ?></h2>
    <div class="mute"><?= $h($fechaLarga($g['fecha'])) ?><?= !empty($g['hora']) ? ' · ' . $h($g['hora']) : '' ?><?= !empty($g['lugar']) ? ' · ' . $h($g['lugar']) : '' ?> · <?= empty($g['abierta']) ? 'reservas cerradas' : 'reservas abiertas' ?></div>
    <div class="stats"><div><b><?= $conf ?><?= $g['cupo'] >= SIN_LIMITE ? '' : ' / ' . $g['cupo'] ?></b>confirmadas<?= $g['cupo'] >= SIN_LIMITE ? ' · sin límite' : '' ?></div><div><b><?= $esp ?></b>en espera</div><div><b><?= $ent ?></b>ya entraron</div><div><b><?= count(array_filter($l, fn($r) => $r['estado'] !== 'cancelada')) ?></b>reservas</div></div>
    <?php if ($toca): ?><div class="nota"><b>Confirmación final por WhatsApp.</b> Toca el botón verde de cada persona: se abre WhatsApp con el mensaje ya escrito y solo hay que enviarlo. Desde ese momento tiene <?= HORAS_CONFIRMAR ?> horas; si no confirma, su reserva se cancela sola.
      <div class="stats"><div><b><?= $nSi ?></b>confirmaron</div><div><b><?= $nPe ?></b>esperando respuesta</div><div><b><?= $nNo ?></b>sin avisar</div><div><b><?= $nCa ?></b>canceladas por no confirmar</div></div></div>
    <?php elseif (hoy_lv() < $desde): ?><div class="nota">La confirmación final por WhatsApp se manda desde el <b><?= $h(fecha_larga($desde)) ?></b> (<?= DIAS_AVISO ?> días antes). Ese día aparecen aquí los botones.</div><?php endif; ?>
    <p><a class="b g" style="text-decoration:none;display:inline-block" href="<?= $h($yo) ?>?csv=<?= $h($gid) ?>">Descargar para Excel</a></p>
    <div class="card" style="overflow-x:auto"><table><tr><th>Nombre</th><th>Teléfono</th><th>#</th><th>Estado</th><th></th></tr>
    <?php foreach ($l as $r): ?>
      <tr class="fila" data-q="<?= $h(mb_strtolower($r['nombre'] . ' ' . $r['telefono'] . ' ' . $r['codigo'])) ?>">
      <td><a href="<?= $h($yo) ?>?entrada=<?= $h($r['codigo']) ?>"><?= $h($r['nombre']) ?></a><div class="mute"><?= $h($r['codigo']) ?> · <?= $h(substr($r['creada'], 5, 5)) ?></div></td>
      <td><a href="<?= $h($wa($r['telefono'])) ?>"><?= $h($r['telefono']) ?></a></td><td><?= (int)$r['cantidad'] ?></td>
      <td><span class="e <?= $h($r['estado']) ?>"><?= $h($r['estado']) ?></span><?= $r['entro'] ? '<div class="mute">entró ' . $h(substr($r['entro'], 11, 5)) . '</div>' : '' ?>
        <?php if ($r['estado'] === 'cancelada'): ?><?= ($r['motivo'] ?? '') === 'sin-confirmar' ? '<div class="cf pe">no confirmó a tiempo</div>' : (($r['motivo'] ?? '') === 'no-va' ? '<div class="cf">avisó que no va</div>' : '') ?>
        <?php elseif (!empty($r['reconf'])): ?><div class="cf si">✓ confirmó que va</div>
        <?php elseif (!empty($r['aviso'])): $q = vence($r) - time(); ?><div class="cf pe">⏳ avisado hace <?= $h($hace($r['aviso'])) ?> · le quedan <?= $q >= 3600 ? intdiv($q, 3600) . ' h' : max(1, intdiv($q, 60)) . ' min' ?></div>
          <a class="wa" target="_blank" rel="noopener" href="<?= $h($wa($r['telefono']) . '?text=' . rawurlencode($msj($r, $g))) ?>">Reenviar</a>
        <?php elseif ($toca): ?><a class="wa" target="_blank" rel="noopener" data-aviso="<?= $h($r['codigo']) ?>" href="<?= $h($wa($r['telefono']) . '?text=' . rawurlencode($msj($r, $g))) ?>">📲 Pedir confirmación</a>
        <?php endif; ?></td>
      <td style="white-space:nowrap"><form method="post" class="i"><input type="hidden" name="codigo" value="<?= $h($r['codigo']) ?>">
        <?php if ($r['estado'] === 'espera'): ?><button class="b" name="op" value="confirmar">Confirmar</button><?php endif; ?>
        <?php if ($r['estado'] !== 'cancelada' && empty($r['reconf']) && ($toca || !empty($r['aviso']))): ?><button class="b s" name="op" value="reconf" title="Si confirmó contestando el mensaje en vez de tocar el enlace">✓ Confirmó</button><?php endif; ?>
        <?php if ($toca && $r['estado'] !== 'cancelada' && empty($r['aviso']) && empty($r['reconf'])): ?><button class="b g s" name="op" value="aviso" title="Anota que ya se le escribió por WhatsApp: empiezan sus 24 horas">Ya le escribí</button><?php endif; ?>
        <?php if (por_confirmar($r)): ?><button class="b g s" name="op" value="prorroga" title="Le da 24 horas más desde ahora">+24 h</button><?php endif; ?>
        <?php if ($r['estado'] === 'cancelada' && $g['fecha'] >= hoy_lv()): ?><button class="b g s" name="op" value="reactivar">Reactivar</button><?php endif; ?>
        <?php if ($r['estado'] !== 'cancelada'): ?><button class="b r" name="op" value="cancelar" onclick="return confirm('¿Cancelar la reserva de <?= $h(addslashes($r['nombre'])) ?>?')">Cancelar</button><?php endif; ?>
      </form></td></tr>
    <?php endforeach; if (!$l) echo '<tr><td colspan="5" class="mute">Todavía no hay reservas.</td></tr>'; ?>
    </table></div>
  <?php endforeach; ?>
  <script>// Al tocar "Pedir confirmación" se abre WhatsApp y queda anotado que se le escribió (empiezan las 24 h)
  document.addEventListener("click", e => { const a = e.target.closest("[data-aviso]"); if (!a) return;
    const fd = new FormData(); fd.set("op", "aviso"); fd.set("codigo", a.dataset.aviso); navigator.sendBeacon(location.pathname, fd);
    a.removeAttribute("data-aviso"); a.textContent = "Reenviar"; a.insertAdjacentHTML("beforebegin", '<div class="cf pe">⏳ avisado ahora · le quedan 24 h</div>'); });</script>
  <script>document.getElementById("q").addEventListener("input", e => { const q = e.target.value.toLowerCase().trim(); document.querySelectorAll(".fila").forEach(f => f.style.display = !q || f.dataset.q.includes(q) ? "" : "none"); });</script>
<?php endif; ?>
</div></body></html>
