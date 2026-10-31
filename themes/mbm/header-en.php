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
      <li><a href="#red">The network</a></li>
      <li><a href="#apps">Apps</a></li>
      <li><a href="#servicios">Services</a></li>
      <li><a href="#trabajos">Work</a></li>
      <li><a href="#publicidad">Advertising</a></li>
      <li><a href="#facebook">Facebook</a></li>
      <li><a href="#nosotros">About</a></li>
    </ul>
    <span class="lang" role="group" aria-label="Idioma / Language"><a href="<?php echo esc_url(home_url('/')); ?>" hreflang="es" data-lang="es" title="Español"><svg viewBox="0 0 30 20" width="24" height="16" aria-hidden="true"><rect width="30" height="20" fill="#c60b1e"/><rect y="5" width="30" height="10" fill="#ffc400"/></svg><b>ES</b></a><a href="<?php echo esc_url(home_url('/en/')); ?>" hreflang="en" data-lang="en" class="on" title="English"><svg viewBox="0 0 38 20" width="24" height="16" aria-hidden="true"><rect width="38" height="20" fill="#fff"/><g fill="#b22234"><rect width="38" height="1.54"/><rect y="3.08" width="38" height="1.54"/><rect y="6.15" width="38" height="1.54"/><rect y="9.23" width="38" height="1.54"/><rect y="12.31" width="38" height="1.54"/><rect y="15.38" width="38" height="1.54"/><rect y="18.46" width="38" height="1.54"/></g><rect width="15.2" height="10.77" fill="#3c3b6e"/></svg><b>EN</b></a></span>
    <a class="btn btn-acc" href="#contacto">Let's talk</a>
  </div>
</header>

