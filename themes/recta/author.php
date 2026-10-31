<?php get_header(); $a = get_queried_object(); ?>
<main class="wrap">
<section class="autor-hero"><?php echo recta_autor_foto($a->ID, 120); ?><div><small>Autor</small><h1><?php echo esc_html($a->display_name); ?></h1><p><?php echo esc_html(recta_autor_bio($a->ID)); ?></p></div></section>
<?php if (have_posts()): ?>
<section class="related"><div class="sec-h"><h2>Sus artículos</h2><p><?php echo (int) count_user_posts($a->ID); ?> en Recta al Pecho.</p></div><div class="grid"><?php while (have_posts()): the_post(); recta_card(get_post()); endwhile; ?></div></section>
<?php the_posts_pagination(['prev_text' => '← Anteriores', 'next_text' => 'Siguientes →']); else: ?>
<p class="vacio">Todavía no ha publicado artículos.</p>
<?php endif; ?>
<p class="volver"><a href="<?php echo esc_url(home_url('/nuestros-autores/')); ?>">← Todos los autores</a></p>
</main>
<?php get_footer();
