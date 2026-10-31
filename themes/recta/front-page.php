<?php get_header(); $live = recta_live();
$latest = get_posts(['numberposts' => 4, 'post_status' => 'publish']);
$lead = $latest[0] ?? null; $side = array_slice($latest, 1, 3);
$shown = [];
?>
<main class="wrap">
<?php if ($lead): [$serie, $slink] = recta_post_serie($lead->ID); $shown[] = $lead->ID; ?>
<section class="hero">
 <a class="big" href="<?php echo esc_url(get_permalink($lead)); ?>"><img src="<?php echo esc_url(get_the_post_thumbnail_url($lead, 'recta-hero') ?: get_theme_file_uri('img/portada.jpg')); ?>" alt="" fetchpriority="high"><div class="txt"><span class="kicker"><?php echo esc_html($serie); ?></span><h1><?php echo esc_html(get_the_title($lead)); ?></h1><p><?php echo esc_html(recta_excerpt($lead, 32)); ?></p></div></a>
 <aside class="side"><h3>Lo último</h3>
 <?php foreach ($side as $p): [$serie] = recta_post_serie($p->ID); $shown[] = $p->ID; ?>
  <a class="mini" href="<?php echo esc_url(get_permalink($p)); ?>"><img src="<?php echo esc_url(get_the_post_thumbnail_url($p, 'thumbnail') ?: get_theme_file_uri('img/portada.jpg')); ?>" alt="" loading="lazy"><span><small><?php echo esc_html($serie); ?></small><b><?php echo esc_html(get_the_title($p)); ?></b></span></a>
 <?php endforeach; ?>
 </aside>
</section>
<?php endif; ?>

<?php if (!empty($live['last']['id'])): $l = $live['last']; ?>
<section class="yt-strip">
 <a class="play" href="https://youtu.be/<?php echo esc_attr($l['id']); ?>" target="_blank" rel="noopener"><img src="https://i.ytimg.com/vi/<?php echo esc_attr($l['id']); ?>/maxresdefault.jpg" alt="" loading="lazy"></a>
 <div><h3>Último capítulo en YouTube</h3><h2><?php echo esc_html($l['guest']); ?>: <?php echo esc_html($l['title']); ?></h2><p>Estrenado el <?php echo esc_html($l['date']); ?>. Entrevista completa en el canal.</p><a class="btn" href="https://youtu.be/<?php echo esc_attr($l['id']); ?>" target="_blank" rel="noopener">Ver la entrevista</a>
 <?php if (!empty($live['next']['guest'])): ?><div class="next"><h3>Próximo estreno</h3><b><?php echo esc_html($live['next']['guest']); ?></b> · <?php echo esc_html($live['next']['date']); ?><br><span class="ui" style="font-size:14px;opacity:.85">Activa los avisos en la app y te llega al teléfono el día del estreno.</span></div><?php endif; ?>
 </div>
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
 <img src="<?php echo esc_url(get_theme_file_uri('img/app-icon.png')); ?>" alt="" width="120" height="120" loading="lazy">
 <div>
  <small>App gratis</small><h2>Lleva Recta al Pecho en tu teléfono</h2>
  <p>Cada entrevista, cada estreno y los avisos, sin buscar en YouTube.</p>
  <div class="app-btns">
   <a class="b1" href="https://marrerobernalmedia.com/apk/recta.apk">Android · Descargar (APK)</a>
   <a class="b2" href="https://marrerobernalmedia.com/recta/" target="_blank" rel="noopener">Abrir la app en el navegador</a>
  </div>
  <p class="nota">iPhone: abre <a href="https://marrerobernalmedia.com/recta/" target="_blank" rel="noopener">marrerobernalmedia.com/recta</a> en Safari, toca Compartir y luego "Agregar a inicio". Muy pronto en Google Play y App Store.</p>
 </div>
</section>
<section class="sec autores-strip"><div class="sec-h"><h2>Nuestros autores</h2><p>Periodistas y narradores que escriben en Recta al Pecho.</p><a href="<?php echo esc_url(home_url('/nuestros-autores/')); ?>">Conócelos →</a></div>
<div class="autores"><?php foreach (recta_autores() as $a) echo recta_autor_card($a, 80); ?></div></section>
</main>
<?php get_footer();
