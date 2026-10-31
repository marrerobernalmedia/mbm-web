<?php
/**
 * Recta al Pecho — tema propio (Marrero Bernal Media LLC).
 * Diseño aprobado por Eliam el 30-oct-2026. Se despliega desde el repo mbm-web (themes/recta).
 */
if (!defined('ABSPATH')) exit;

define('RECTA_VER', '1.0.0');

add_action('after_setup_theme', function () {
  add_theme_support('title-tag');
  add_theme_support('post-thumbnails');
  add_theme_support('html5', ['search-form','gallery','caption','script','style']);
  add_theme_support('responsive-embeds');
  add_image_size('recta-card', 800, 500, true);
  add_image_size('recta-hero', 1600, 900, true);
  register_nav_menus(['principal' => 'Menú principal']);
});

add_action('wp_enqueue_scripts', function () {
  wp_enqueue_style('recta-fonts', 'https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Barlow:wght@500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap', [], null);
  wp_enqueue_style('recta', get_stylesheet_uri(), ['recta-fonts'], RECTA_VER);
});

add_action('wp_head', function () {
  echo '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
}, 1);

/** Series (categorías) en el orden de la portada y el menú. */
function recta_series() {
  return [
    'los-borrados'               => ['Los Borrados', 'Los que Cuba sacó de las estadísticas y de la televisión.'],
    'las-fugas'                  => ['Las Fugas', 'Cómo escaparon, contado en primera persona.'],
    'los-que-dijeron-no'         => ['Los que dijeron no', 'Rechazaron los millones. Esto fue lo que recibieron.'],
    'las-glorias-en-el-piso'     => ['Las glorias en el piso', 'Campeones del equipo Cuba que hoy viven olvidados.'],
    'la-hipocresia-en-el-beisbol'=> ['Mitos y análisis', 'Lo que repite el fanático, contra los números.'],
  ];
}
function recta_serie_label($slug) { $s = recta_series(); return $s[$slug][0] ?? null; }

/** Etiqueta de serie de un post (la primera categoría conocida). */
function recta_post_serie($post_id) {
  foreach (get_the_category($post_id) as $c) {
    if ($l = recta_serie_label($c->slug)) return [$l, get_category_link($c)];
  }
  $cats = get_the_category($post_id);
  if ($cats && $cats[0]->slug !== 'uncategorized') return [$cats[0]->name, get_category_link($cats[0])];
  return ['Historias', home_url('/')];
}

/** Datos vivos (último capítulo, próximo estreno, mitos): themes/recta/live.json, lo actualiza Claude desde el repo. */
function recta_live() {
  static $d = null;
  if ($d === null) {
    $f = get_theme_file_path('live.json');
    $d = file_exists($f) ? (json_decode(file_get_contents($f), true) ?: []) : [];
  }
  return $d;
}

function recta_fecha($post = null) { return get_the_date('j M Y', $post); }

function recta_reading_time($post = null) {
  $w = str_word_count(wp_strip_all_tags(get_post_field('post_content', $post)));
  return max(1, (int) round($w / 220));
}

/** Los artículos viejos traen su propio <style> y clase .recta-article: se quita el <style> para que mande el tema. */
add_filter('the_content', function ($c) {
  if (is_singular('post')) $c = preg_replace('#<style\b[^>]*>.*?</style>#is', '', $c);
  return $c;
}, 5);

/** Extracto corto para tarjetas. */
function recta_excerpt($post = null, $len = 24) {
  $p = get_post($post);
  $t = $p->post_excerpt ?: wp_strip_all_tags(strip_shortcodes($p->post_content));
  $t = preg_replace('/\s+/', ' ', trim($t));
  return wp_trim_words($t, $len, '…');
}
add_filter('excerpt_length', fn() => 24);

/** Tarjeta de artículo. */
function recta_card($post) {
  [$serie, $link] = recta_post_serie($post->ID);
  $img = get_the_post_thumbnail_url($post, 'recta-card') ?: get_theme_file_uri('img/portada.jpg');
  printf('<a class="card" href="%s"><img src="%s" alt="" loading="lazy"><div class="b"><small>%s</small><h3>%s</h3><p>%s</p><time datetime="%s">%s</time></div></a>',
    esc_url(get_permalink($post)), esc_url($img), esc_html($serie), esc_html(get_the_title($post)), esc_html(recta_excerpt($post)), esc_attr(get_the_date('c', $post)), esc_html(recta_fecha($post)));
}

/** Sin "Uncategorized" en el sitio: lo que no tiene serie se muestra como Historias. */
add_filter('get_the_categories', function ($cats) {
  return array_values(array_filter($cats, fn($c) => $c->slug !== 'uncategorized'));
});

/** SEO. Lema del sitio (manda sobre el de Ajustes) y textos de portada para Yoast; sin meta duplicada. */
define('RECTA_TAGLINE', 'Deportes · El béisbol es la pasión');
define('RECTA_HOME_TITLE', 'Recta al Pecho — Entrevistas con peloteros cubanos y las historias del béisbol');
define('RECTA_HOME_DESC', 'Recta al Pecho: canal de deportes donde el béisbol es la pasión. Entrevistas largas con peloteros cubanos, las historias que el relato oficial borró, los que dijeron no, las fugas y los mitos frente a los números.');
add_filter('pre_option_blogdescription', fn() => RECTA_TAGLINE);
add_filter('wpseo_title', fn($t) => (is_front_page() || is_home()) ? RECTA_HOME_TITLE : $t);
add_filter('wpseo_opengraph_title', fn($t) => (is_front_page() || is_home()) ? RECTA_HOME_TITLE : $t);
add_filter('wpseo_metadesc', fn($d) => (is_front_page() || is_home()) ? RECTA_HOME_DESC : ($d ?: (is_singular() ? recta_excerpt(null, 28) : (is_category() ? (recta_series()[get_queried_object()->slug][1] ?? $d) : $d))));
add_filter('wpseo_opengraph_desc', fn($d) => (is_front_page() || is_home()) ? RECTA_HOME_DESC : $d);
add_filter('wpseo_opengraph_image', fn($i) => $i ?: get_theme_file_uri('img/portada.jpg'));
add_filter('wpseo_schema_website', function ($data) { $data['description'] = RECTA_HOME_DESC; return $data; });
add_filter('wpseo_schema_organization', function ($data) {
  $data['description'] = RECTA_HOME_DESC; $data['url'] = home_url('/');
  $data['sameAs'] = ['https://www.youtube.com/@RectaAlPecho', 'https://www.facebook.com/RectaAlPecho/', 'https://www.instagram.com/rectaalpecho/'];
  return $data;
});
/** Si Yoast no está activo, cabecera mínima propia. */
add_action('wp_head', function () {
  if (defined('WPSEO_VERSION')) return;
  $d = (is_front_page() || is_home()) ? RECTA_HOME_DESC : (is_singular() ? recta_excerpt(null, 28) : '');
  if ($d) echo '<meta name="description" content="' . esc_attr($d) . '">' . "\n";
}, 2);
/** Títulos legibles en archivos de serie. */
add_filter('wpseo_title', function ($t) { if (is_category() && ($l = recta_serie_label(get_queried_object()->slug))) return $l . ' — Recta al Pecho'; return $t; }, 20);

/** El tema manda: Elementor Pro no sustituye cabecera, pie ni plantillas de artículo. */
add_filter('elementor/theme/need_override_location', '__return_false');
add_action('elementor/theme/register_locations', function ($manager) {
  // El tema declara que gestiona sus propias zonas; como nunca llama a elementor_theme_do_location(),
  // las plantillas de cabecera/pie/single de Elementor Pro no se pintan.
  $manager->register_all_core_location();
});
/** La portada es siempre la de este tema (no la página "Home" de Elementor). */
add_filter('pre_option_show_on_front', fn() => 'posts');
add_filter('pre_option_page_on_front', fn() => 0);

/** Limpieza de cabecera. */
remove_action('wp_head', 'wp_generator');
add_filter('emoji_svg_url', '__return_false');

/** Páginas viejas de Elementor que quedaron vacías con el tema: redirección permanente a su equivalente (no se borra nada). */
function recta_redirects() {
  return ['home' => '/', 'beisbol' => '/', 'los-borrados' => '/category/los-borrados/', 'las-fugas-2' => '/category/las-fugas/', 'nuestros-autores' => '/quienes-somos/'];
}
add_action('template_redirect', function () {
  if (is_page()) { $slug = get_queried_object()->post_name ?? ''; $r = recta_redirects(); if (isset($r[$slug])) { wp_redirect(home_url($r[$slug]), 301); exit; } }
  if (is_author()) { wp_redirect(home_url('/quienes-somos/'), 301); exit; }
});
add_filter('wpseo_sitemap_entry', function ($url, $type, $post) {
  if ($type === 'post' && is_object($post) && $post->post_type === 'page' && isset(recta_redirects()[$post->post_name])) return false;
  return $url;
}, 10, 3);
add_filter('wpseo_sitemap_exclude_author', '__return_true');
add_filter('wpseo_sitemap_exclude_taxonomy', fn($x, $tax) => $tax === 'post_tag' ? true : $x, 10, 2);
/** Sin indexar: archivo "Uncategorized", búsquedas y paginaciones de etiquetas. */
add_filter('wpseo_robots', function ($r) {
  if ((is_category() && get_queried_object()->slug === 'uncategorized') || is_tag() || is_search() || is_date()) return 'noindex, follow';
  return $r;
});
