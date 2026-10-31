<?php get_header(); ?>
<main class="wrap">
<header class="arch-h">
<?php if (is_category()): $s = recta_series(); $cat = get_queried_object(); $lab = $s[$cat->slug] ?? [single_cat_title('', false), category_description() ? wp_strip_all_tags(category_description()) : '']; ?>
 <h1><?php echo esc_html($lab[0]); ?></h1><?php if ($lab[1]): ?><p><?php echo esc_html($lab[1]); ?></p><?php endif; ?>
<?php elseif (is_search()): ?><h1>Resultados para «<?php echo esc_html(get_search_query()); ?>»</h1>
<?php elseif (is_author()): ?><h1>Artículos de <?php echo esc_html(get_the_author()); ?></h1>
<?php else: ?><h1>Historias</h1><p>Todos los artículos de Recta al Pecho.</p><?php endif; ?>
</header>
<?php if (have_posts()): ?>
<div class="grid"><?php while (have_posts()): the_post(); recta_card(get_post()); endwhile; ?></div>
<div class="pager"><?php echo paginate_links(['prev_text' => '← Anteriores', 'next_text' => 'Siguientes →']); ?></div>
<?php else: ?><p class="empty">Todavía no hay artículos aquí.</p><?php endif; ?>
</main>
<?php get_footer();
