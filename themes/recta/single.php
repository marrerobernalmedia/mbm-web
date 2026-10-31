<?php get_header(); while (have_posts()): the_post(); [$serie, $slink] = recta_post_serie(get_the_ID()); ?>
<main class="wrap">
<header class="art-hero">
 <a class="kicker" href="<?php echo esc_url($slink); ?>"><?php echo esc_html($serie); ?></a>
 <h1><?php the_title(); ?></h1>
 <?php if (has_excerpt()): ?><p class="dek"><?php echo esc_html(get_the_excerpt()); ?></p><?php endif; ?>
 <div class="meta"><span><span class="av"><?php echo esc_html(mb_strtoupper(mb_substr(get_the_author_meta('first_name') ?: get_the_author(), 0, 1) . mb_substr(get_the_author_meta('last_name') ?: 'M', 0, 1))); ?></span><?php the_author(); ?></span><time datetime="<?php echo esc_attr(get_the_date('c')); ?>"><?php echo esc_html(recta_fecha()); ?></time><span>Lectura: <?php echo recta_reading_time(); ?> min</span></div>
</header>
<?php if (has_post_thumbnail()): ?>
<figure class="art-img"><?php the_post_thumbnail('recta-hero', ['loading' => 'eager', 'fetchpriority' => 'high']); ?><?php if ($cap = get_the_post_thumbnail_caption()): ?><figcaption><?php echo esc_html($cap); ?></figcaption><?php endif; ?></figure>
<?php endif; ?>
<article class="art" id="post-<?php the_ID(); ?>">
<?php the_content(); ?>
<div class="share">
 <a href="https://www.facebook.com/sharer/sharer.php?u=<?php echo rawurlencode(get_permalink()); ?>" target="_blank" rel="noopener">Compartir en Facebook</a>
 <a href="https://wa.me/?text=<?php echo rawurlencode(get_the_title() . ' ' . get_permalink()); ?>" target="_blank" rel="noopener">WhatsApp</a>
 <a href="https://x.com/intent/tweet?url=<?php echo rawurlencode(get_permalink()); ?>&text=<?php echo rawurlencode(get_the_title()); ?>" target="_blank" rel="noopener">X</a>
</div>
<div class="author-box"><span class="av"><?php echo esc_html(mb_strtoupper(mb_substr(get_the_author(), 0, 1))); ?></span><div><b><?php the_author(); ?></b><p><?php echo esc_html(get_the_author_meta('description') ?: 'Director de Recta al Pecho y de Marrero Bernal Media. Entrevista a los peloteros cubanos en Las Vegas, Miami y Cuba.'); ?></p></div></div>
<div class="sponsor-box">🤝 Recta al Pecho es patrocinado por <a href="https://www.marrerobernal.com" target="_blank" rel="noopener">Marrero Bernal &amp; Associates</a>: impuestos personales y comerciales, seguros, préstamos de casa, Medicare, inmigración, notaría y traducciones. Atendemos en línea: <a href="https://www.marrerobernal.com" target="_blank" rel="noopener">www.marrerobernal.com</a></div>
</article>
<?php
$rel = get_posts(['numberposts' => 4, 'post__not_in' => [get_the_ID()], 'category' => (get_the_category()[0]->term_id ?? 0), 'post_status' => 'publish']);
if (count($rel) < 4) $rel = array_merge($rel, get_posts(['numberposts' => 4 - count($rel), 'post__not_in' => array_merge([get_the_ID()], wp_list_pluck($rel, 'ID')), 'post_status' => 'publish']));
if ($rel): ?>
<section class="related"><div class="sec-h"><h2>Sigue leyendo</h2><p>Más historias de Recta al Pecho.</p></div><div class="grid"><?php foreach ($rel as $p) recta_card($p); ?></div></section>
<?php endif; ?>
</main>
<?php endwhile; get_footer();
