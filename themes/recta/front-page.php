<?php get_header(); $live = recta_live();
$latest = get_posts(['numberposts' => 4, 'post_status' => 'publish']);
$lead = $latest[0] ?? null; $side = array_slice($latest, 1, 3);
$shown = [];
?>
<main class="wrap">
<?php [$eLast, $eNext] = recta_estrenos(); if ($eLast || $eNext): ?>
<section class="estrenos" aria-label="Estrenos en YouTube">
<?php if ($eLast): ?>
 <article class="ep">
  <a class="th" href="https://youtu.be/<?php echo esc_attr($eLast['id']); ?>" target="_blank" rel="noopener"><img src="https://i.ytimg.com/vi/<?php echo esc_attr($eLast['id']); ?>/maxresdefault.jpg" alt="<?php echo esc_attr($eLast['guest']); ?>" fetchpriority="high"><span class="tag">Último estreno</span><span class="pl" aria-hidden="true">▶</span></a>
  <div class="tx"><b><?php echo esc_html($eLast['guest']); ?></b><span><?php echo esc_html($eLast['title']); ?></span><small>Estrenado el <?php echo esc_html($eLast['date']); ?></small>
  <p class="acts"><a class="btn" href="https://youtu.be/<?php echo esc_attr($eLast['id']); ?>" target="_blank" rel="noopener">Ver la entrevista</a></p></div>
 </article>
<?php endif; if ($eNext): ?>
 <article class="ep prox">
  <?php if (!empty($eNext['id'])): ?><a class="th" href="https://youtu.be/<?php echo esc_attr($eNext['id']); ?>" target="_blank" rel="noopener"><img src="https://i.ytimg.com/vi/<?php echo esc_attr($eNext['id']); ?>/maxresdefault.jpg" alt="<?php echo esc_attr($eNext['guest']); ?>" loading="lazy"><span class="tag">Próximo estreno</span></a>
  <?php else: ?><div class="th vacio"><img src="<?php echo esc_url(get_theme_file_uri('img/og.jpg')); ?>" alt="" loading="lazy"><span class="tag">Próximo estreno</span></div><?php endif; ?>
  <div class="tx"><b><?php echo esc_html($eNext['guest']); ?></b><?php if (!empty($eNext['title'])): ?><span><?php echo esc_html($eNext['title']); ?></span><?php endif; ?><small>Estreno el <?php echo esc_html($eNext['date']); ?> · 8:00 AM Las Vegas · 11:00 AM Miami · 5:00 PM Madrid</small>
  <p class="acts"><?php if (!empty($eNext['id'])): ?><a class="btn" href="https://youtu.be/<?php echo esc_attr($eNext['id']); ?>" target="_blank" rel="noopener">🔔 Recordármelo en YouTube</a><?php endif; ?></p></div>
 </article>
<?php endif; ?>
</section>
<?php endif; ?>
<?php if ($lead): [$serie, $slink] = recta_post_serie($lead->ID); $shown[] = $lead->ID; ?>
<section class="hero">
 <a class="big" href="<?php echo esc_url(get_permalink($lead)); ?>"><img src="<?php echo esc_url(get_the_post_thumbnail_url($lead, 'recta-hero') ?: get_theme_file_uri('img/portada.jpg')); ?>" alt="" loading="lazy"><div class="txt"><span class="kicker"><?php echo esc_html($serie); ?></span><h1><?php echo esc_html(get_the_title($lead)); ?></h1><p><?php echo esc_html(recta_excerpt($lead, 32)); ?></p></div></a>
 <aside class="side"><h3>Lo último</h3>
 <?php foreach ($side as $p): [$serie] = recta_post_serie($p->ID); $shown[] = $p->ID; ?>
  <a class="mini" href="<?php echo esc_url(get_permalink($p)); ?>"><img src="<?php echo esc_url(get_the_post_thumbnail_url($p, 'thumbnail') ?: get_theme_file_uri('img/portada.jpg')); ?>" alt="" loading="lazy"><span><small><?php echo esc_html($serie); ?></small><b><?php echo esc_html(get_the_title($p)); ?></b></span></a>
 <?php endforeach; ?>
 </aside>
</section>
<?php endif; ?>

<?php foreach (recta_series() as $slug => $s): $cat = get_category_by_slug($slug); if (!$cat) continue;
  $ps = get_posts(['numberposts' => 4, 'category' => $cat->term_id, 'post_status' => 'publish']); if (!$ps) continue; ?>
<section class="sec" id="<?php echo esc_attr($slug); ?>"><div class="sec-h"><h2><?php echo esc_html($s[0]); ?></h2><p><?php echo esc_html($s[1]); ?></p><a href="<?php echo esc_url(get_category_link($cat)); ?>">Ver todos →</a></div>
<?php if ($slug === 'la-hipocresia-en-el-beisbol' && !empty($live['mitos'])): ?>
<div class="mitos" style="margin-bottom:18px"><?php foreach ($live['mitos'] as $m): ?><div class="mito"><div class="q"><?php echo esc_html($m[0]); ?></div><p><?php echo esc_html($m[1]); ?></p><a href="https://youtu.be/<?php echo esc_attr($m[2]); ?>" target="_blank" rel="noopener">Escúchalo de su boca →</a></div><?php endforeach; ?></div>
<?php endif; ?>
<div class="grid"><?php foreach ($ps as $p) recta_card($p); ?></div></section>
<?php endforeach; ?>
<section class="app-band" id="app">
 <img src="<?php echo esc_url(get_theme_file_uri('img/app-icon.png')); ?>" alt="App Recta al Pecho" width="120" height="120" loading="lazy">
 <div>
  <small>App gratis</small><h2>Lleva Recta al Pecho en tu teléfono</h2>
  <p>Cada entrevista, cada estreno y los avisos, sin buscar en YouTube.</p>
  <div class="app-btns">
   <a class="b1" href="https://play.google.com/store/apps/details?id=com.marrerobernalmedia.recta" target="_blank" rel="noopener">Android · Bájala en Google Play</a>
   <a class="b2" href="https://marrerobernalmedia.com/recta/" target="_blank" rel="noopener">Abrir la app en el navegador</a>
  </div>
  <p class="nota">iPhone: abre <a href="https://marrerobernalmedia.com/recta/" target="_blank" rel="noopener">marrerobernalmedia.com/recta</a> en Safari, toca Compartir y luego "Agregar a inicio". Muy pronto en Google Play y App Store.</p>
 </div>
</section>
<section class="sec autores-strip"><div class="sec-h"><h2>Nuestros autores</h2><p>Periodistas y narradores que escriben en Recta al Pecho.</p><a href="<?php echo esc_url(home_url('/nuestros-autores/')); ?>">Conócelos →</a></div>
<div class="autores"><?php foreach (recta_autores() as $a) echo recta_autor_card($a, 80); ?></div></section>
</main>
<?php get_footer();
