<!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>


<header>
  <div class="wrap nav">
    <a href="<?php echo esc_url(home_url('/')); ?>"><img src="<?php echo esc_url(get_theme_file_uri('img/logo.svg')); ?>" alt="Marrero Bernal Media"></a>
    <ul>
      <li><a href="#red">La red</a></li>
      <li><a href="#servicios">Servicios</a></li>
      <li><a href="#trabajos">Trabajos</a></li>
      <li><a href="#publicidad">Publicidad</a></li>
      <li><a href="#facebook">Facebook</a></li>
      <li><a href="#nosotros">Nosotros</a></li>
    </ul>
    <span class="lang"><a href="#" data-lang="es">ES</a> · <a href="#" data-lang="en">EN</a></span>
    <a class="btn btn-acc" href="#contacto">Hablemos</a>
  </div>
</header>

