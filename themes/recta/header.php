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
 <a class="brand" href="<?php echo esc_url(home_url('/')); ?>"><img src="<?php echo esc_url(get_theme_file_uri('img/logo.png')); ?>" alt="Recta al Pecho"><span><small>Deportes · El béisbol es la pasión</small></span></a>
 <nav class="main" aria-label="Series">
  <?php foreach (recta_series() as $slug => $s): if ($c = get_category_by_slug($slug)): ?>
   <a href="<?php echo esc_url(get_category_link($c)); ?>"><?php echo esc_html($slug === 'la-hipocresia-en-el-beisbol' ? 'Mitos' : $s[0]); ?></a>
  <?php endif; endforeach; ?>
  <a href="<?php echo esc_url(home_url('/quienes-somos/')); ?>">Quiénes somos</a>
  <a href="<?php echo esc_url(home_url('/nuestros-autores/')); ?>">Autores</a>
  <a class="app" href="<?php echo esc_url(home_url('/#app')); ?>">📲 App</a>
  <a class="yt" href="https://www.youtube.com/@RectaAlPecho" target="_blank" rel="noopener">▶ Entrevistas</a>
 </nav>
 <button class="burger" type="button" aria-expanded="false" aria-controls="menu-panel" onclick="var p=document.getElementById('menu-panel');p.classList.toggle('open');this.setAttribute('aria-expanded',p.classList.contains('open'))">MENÚ</button>
</div>
<div id="menu-panel" class="menu-panel">
  <?php foreach (recta_series() as $slug => $s): if ($c = get_category_by_slug($slug)): ?>
   <a href="<?php echo esc_url(get_category_link($c)); ?>"><?php echo esc_html($s[0]); ?></a>
  <?php endif; endforeach; ?>
  <a href="<?php echo esc_url(home_url('/quienes-somos/')); ?>">Quiénes somos</a>
  <a href="<?php echo esc_url(home_url('/nuestros-autores/')); ?>">Nuestros autores</a>
  <a href="<?php echo esc_url(home_url('/contacto/')); ?>">Contacto</a>
  <a href="<?php echo esc_url(home_url('/#app')); ?>">📲 Descargar la app</a>
  <a href="https://www.youtube.com/@RectaAlPecho" target="_blank" rel="noopener">▶ Entrevistas en YouTube</a>
</div>
</header>
<?php if (!empty($live['next']['guest']) || !empty($live['last']['guest'])): ?>
<div class="ticker"><div class="wrap">
 <?php if (!empty($live['next']['guest'])): ?><b>ESTE JUEVES</b><span><?php echo esc_html($live['next']['guest']); ?> · nueva entrevista en YouTube</span><?php endif; ?>
 <?php if (!empty($live['last']['guest'])): ?><span>•</span><span>Último capítulo: <?php echo esc_html($live['last']['guest']); ?></span><?php endif; ?>
</div></div>
<?php endif; ?>
