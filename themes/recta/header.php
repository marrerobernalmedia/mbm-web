<!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); $live = recta_live(); ?>
<header class="top"><div class="wrap">
 <a class="brand" href="<?php echo esc_url(home_url('/')); ?>" aria-label="Recta al Pecho — inicio"><img src="<?php echo esc_url(get_theme_file_uri('img/logo-h.png')); ?>" alt="Recta al Pecho" width="158" height="80"></a>
 <nav class="main" aria-label="Series">
  <?php foreach (recta_series() as $slug => $s): if ($c = get_category_by_slug($slug)): ?>
   <a href="<?php echo esc_url(get_category_link($c)); ?>"><?php echo esc_html($slug === 'la-hipocresia-en-el-beisbol' ? 'Mitos' : $s[0]); ?></a>
  <?php endif; endforeach; ?>
  <a href="<?php echo esc_url(home_url('/quienes-somos/')); ?>">Quiénes somos</a>
  <a href="<?php echo esc_url(home_url('/nuestros-autores/')); ?>">Autores</a>
  <a class="app" href="<?php echo esc_url(home_url('/#app')); ?>"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-2px;margin-right:4px"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M12 7v7M9 11l3 3 3-3"/></svg>App</a>
  <a class="yt" href="https://www.youtube.com/@RectaAlPecho" target="_blank" rel="noopener">▶ Entrevistas</a>
 </nav>
 <span class="lang" role="group" aria-label="Idioma / Language"><a href="<?php echo esc_url(home_url('/')); ?>" hreflang="es" class="on" title="Español"><svg viewBox="0 0 30 20" width="22" height="15" aria-hidden="true"><rect width="30" height="20" fill="#c60b1e"/><rect y="5" width="30" height="10" fill="#ffc400"/></svg><b>ES</b></a><a href="https://www.straight2dchest.com/" hreflang="en" title="English — Straight 2D Chest"><svg viewBox="0 0 38 20" width="22" height="15" aria-hidden="true"><rect width="38" height="20" fill="#fff"/><g fill="#b22234"><rect width="38" height="1.54"/><rect y="3.08" width="38" height="1.54"/><rect y="6.15" width="38" height="1.54"/><rect y="9.23" width="38" height="1.54"/><rect y="12.31" width="38" height="1.54"/><rect y="15.38" width="38" height="1.54"/><rect y="18.46" width="38" height="1.54"/></g><rect width="15.2" height="10.77" fill="#3c3b6e"/></svg><b>EN</b></a></span>
 <button class="burger" type="button" aria-expanded="false" aria-controls="menu-panel" onclick="var p=document.getElementById('menu-panel');p.classList.toggle('open');this.setAttribute('aria-expanded',p.classList.contains('open'))">MENÚ</button>
</div>
<div id="menu-panel" class="menu-panel">
  <?php foreach (recta_series() as $slug => $s): if ($c = get_category_by_slug($slug)): ?>
   <a href="<?php echo esc_url(get_category_link($c)); ?>"><?php echo esc_html($s[0]); ?></a>
  <?php endif; endforeach; ?>
  <a href="<?php echo esc_url(home_url('/quienes-somos/')); ?>">Quiénes somos</a>
  <a href="<?php echo esc_url(home_url('/nuestros-autores/')); ?>">Nuestros autores</a>
  <a href="<?php echo esc_url(home_url('/contacto/')); ?>">Contacto</a>
  <a href="<?php echo esc_url(home_url('/#app')); ?>"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-2px;margin-right:4px"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M12 7v7M9 11l3 3 3-3"/></svg>Descargar la app</a>
  <a href="https://www.youtube.com/@RectaAlPecho" target="_blank" rel="noopener">▶ Entrevistas en YouTube</a>
</div>
</header>
<?php if (!empty($live['next']['guest']) || !empty($live['last']['guest'])): ?>
<div class="ticker"><div class="wrap">
 <?php if (!empty($live['next']['guest'])): ?><b>ESTE JUEVES</b><span><?php echo esc_html($live['next']['guest']); ?> · nueva entrevista en YouTube</span><?php endif; ?>
 <?php if (!empty($live['last']['guest'])): ?><span>•</span><span>Último capítulo: <?php echo esc_html($live['last']['guest']); ?></span><?php endif; ?>
</div></div>
<?php endif; ?>
