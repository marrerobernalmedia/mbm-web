<?php get_header(); ?>
<main class="wrap">
<div class="sec-h"><h1>Nuestros autores</h1><p>Las voces que escriben en Recta al Pecho.</p></div>
<div class="autores">
<?php foreach (recta_autores() as $a) echo recta_autor_card($a); ?>
</div>
</main>
<?php get_footer();
