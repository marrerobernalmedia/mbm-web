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
define('RECTA_HOME_TITLE', 'Recta al Pecho — Entrevistas con peloteros y las historias del béisbol');
define('RECTA_HOME_DESC', 'Recta al Pecho: canal de deportes donde el béisbol es la pasión. Entrevistas largas con peloteros, las historias que el relato oficial borró, los que dijeron no, las fugas y los mitos frente a los números.');
add_filter('pre_option_blogdescription', fn() => RECTA_TAGLINE);
add_filter('wpseo_title', fn($t) => (is_front_page() || is_home()) ? RECTA_HOME_TITLE : $t);
add_filter('wpseo_opengraph_title', fn($t) => (is_front_page() || is_home()) ? RECTA_HOME_TITLE : $t);
add_filter('wpseo_metadesc', fn($d) => (is_front_page() || is_home()) ? RECTA_HOME_DESC : ($d ?: (is_singular() ? recta_excerpt(null, 28) : (is_category() ? (recta_series()[get_queried_object()->slug][1] ?? $d) : $d))));
add_filter('wpseo_opengraph_desc', fn($d) => (is_front_page() || is_home()) ? RECTA_HOME_DESC : $d);
add_filter('wpseo_opengraph_image', fn($i) => (is_front_page() || is_home() || !$i) ? get_theme_file_uri('img/og.jpg') : $i);
add_filter('wpseo_twitter_image', fn($i) => (is_front_page() || is_home() || !$i) ? get_theme_file_uri('img/og.jpg') : $i);
/** Vista previa al compartir (Facebook, WhatsApp, iMessage): logo de Recta, nunca una foto. Si Yoast no está, lo pone el tema. */
add_action('wp_head', function () {
  if (defined('WPSEO_VERSION')) return;
  $t = (is_front_page() || is_home()) ? RECTA_HOME_TITLE : wp_get_document_title();
  $d = (is_front_page() || is_home()) ? RECTA_HOME_DESC : (is_singular() ? recta_excerpt(null, 28) : RECTA_HOME_DESC);
  $i = (is_singular() && has_post_thumbnail()) ? get_the_post_thumbnail_url(null, 'recta-hero') : get_theme_file_uri('img/og.jpg');
  printf('<meta property="og:type" content="website"><meta property="og:site_name" content="Recta al Pecho"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:image" content="%s"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">' . "\n", esc_attr($t), esc_attr($d), esc_url($i));
}, 3);
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
  return ['home' => '/', 'beisbol' => '/', 'los-borrados' => '/category/los-borrados/', 'las-fugas-2' => '/category/las-fugas/', 'beisbol-2' => '/'];
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

/** ads.txt de AdSense servido por el tema (el ID de editor es público: está en el código de AdSense del sitio). */
add_action('init', function () {
  if (($_SERVER['REQUEST_URI'] ?? '') === '/ads.txt') {
    header('Content-Type: text/plain; charset=utf-8');
    echo "google.com, pub-9995971644235129, DIRECT, f08c47fec0942fa0\n";
    exit;
  }
});

/** AUTORES (escritores colaboradores). Foto propia en el perfil (URL o subida a la biblioteca), bio y página de autor. */
function recta_autor_foto($uid, $size = 96) {
  $u = recta_autor_foto_url($uid);
  if ($u) return '<img class="av av-img" src="' . esc_url($u) . '" alt="" width="' . $size . '" height="' . $size . '" loading="lazy">';
  $n = get_the_author_meta('display_name', $uid);
  $ini = mb_strtoupper(mb_substr(get_the_author_meta('first_name', $uid) ?: $n, 0, 1) . mb_substr(get_the_author_meta('last_name', $uid) ?: '', 0, 1));
  return '<span class="av">' . esc_html($ini) . '</span>';
}
function recta_autor_bio($uid) {
  $d = get_the_author_meta('description', $uid);
  if ($d) return $d;
  return in_array('administrator', (array) get_userdata($uid)->roles, true) ? 'Director de Recta al Pecho y de Marrero Bernal Media. Entrevista a peloteros en Las Vegas, Miami y Cuba.' : 'Escribe para Recta al Pecho.';
}
add_action('show_user_profile', 'recta_perfil_foto'); add_action('edit_user_profile', 'recta_perfil_foto');
function recta_perfil_foto($user) {
  $v = esc_attr(get_user_meta($user->ID, 'recta_foto', true));
  echo '<h2>Recta al Pecho</h2><table class="form-table"><tr><th><label for="recta_foto">Foto de autor</label></th><td><input type="url" class="regular-text" name="recta_foto" id="recta_foto" value="' . $v . '" placeholder="https://rectaalpecho.com/wp-content/uploads/..."><p class="description">Sube tu foto en Medios → Añadir nuevo, copia la URL del archivo y pégala aquí (cuadrada, mínimo 400×400). La biografía de arriba sale debajo de cada artículo tuyo.</p></td></tr></table>';
}
add_action('personal_options_update', 'recta_perfil_foto_guardar'); add_action('edit_user_profile_update', 'recta_perfil_foto_guardar');
function recta_perfil_foto_guardar($uid) { if (current_user_can('edit_user', $uid) && isset($_POST['recta_foto'])) update_user_meta($uid, 'recta_foto', esc_url_raw($_POST['recta_foto'])); }
/** Los autores (rol Autor/Colaborador) pueden subir su foto e imágenes de sus artículos. */
add_action('init', function () { foreach (['author', 'contributor'] as $r) { if ($role = get_role($r)) $role->add_cap('upload_files'); } });
/** Página "Nuestros autores" (/nuestros-autores/) con la plantilla del tema aunque la página esté vacía. */
add_filter('template_include', function ($t) { if (is_page('nuestros-autores')) { $f = get_theme_file_path('page-autores.php'); if (file_exists($f)) return $f; } return $t; }, 999);
/** Equipo de autores: todos los usuarios con rol de escritura menos "admin" (cuenta técnica). Foto: campo del perfil o, si no, la del tema por nombre de usuario (img/autores/<login>.jpg). */
function recta_fotos_tema() { return ['eliammarrero' => 'eliam', 'arnelioalvarez' => 'arnelio', 'manuelalejandro' => 'manolo', 'josealbertoportela' => 'portela', 'raulrodriguez' => 'raul']; }
function recta_autor_foto_url($uid) {
  if ($u = get_user_meta($uid, 'recta_foto', true)) return $u;
  $login = get_userdata($uid)->user_login ?? '';
  $k = recta_fotos_tema()[$login] ?? $login;
  return file_exists(get_theme_file_path("img/autores/$k.jpg")) ? get_theme_file_uri("img/autores/$k.jpg") : '';
}
function recta_autores() {
  $out = [];
  foreach (get_users(['role__in' => ['administrator', 'editor', 'author', 'contributor'], 'orderby' => 'post_count', 'order' => 'DESC']) as $u) {
    if ($u->ID === 1 || strtolower($u->user_login) === 'admin' || strtolower($u->display_name) === 'admin') continue;
    $out[] = ['nombre' => $u->display_name, 'foto' => recta_autor_foto_url($u->ID), 'bio' => wp_trim_words(recta_autor_bio($u->ID), 22), 'url' => get_author_posts_url($u->ID), 'n' => (int) count_user_posts($u->ID), 'rol' => in_array('administrator', (array) $u->roles, true) ? 'Director y fundador' : 'Colaborador'];
  }
  return $out;
}
function recta_autor_card($a, $size = 96) {
  $img = $a['foto'] ? '<img class="av av-img" src="' . esc_url($a['foto']) . '" alt="" width="' . $size . '" height="' . $size . '" loading="lazy">' : '<span class="av">' . esc_html(mb_strtoupper(mb_substr($a['nombre'], 0, 1))) . '</span>';
  return '<a class="autor-card" href="' . esc_url($a['url']) . '">' . $img . '<b>' . esc_html($a['nombre']) . '</b><small>' . esc_html($a['rol']) . '</small><p>' . esc_html($a['bio']) . '</p></a>';
}
