<?php if (!is_page()): ?>
<section class="band wrap" id="about">
 <div><h2>Recta al Pecho: deportes con la pelota como pasión</h2>
 <p>Un canal de deportes donde el béisbol es la pasión: entrevistas largas con peloteros de todas las épocas, dentro y fuera de Cuba, historias que el relato oficial borró y artículos que ponen los mitos del fanático frente a los números. Hablan los que lo vivieron.</p>
 <div class="apps"><a class="btn" href="https://www.youtube.com/@RectaAlPecho" target="_blank" rel="noopener">Ver las entrevistas</a><a class="btn ghost" href="https://marrerobernalmedia.com/recta/" target="_blank" rel="noopener">Instalar la app</a></div></div>
 <div><img src="<?php echo esc_url(get_theme_file_uri('img/about.jpg')); ?>" alt="Eliam Marrero Bernal con Rey Vicente Anglada" loading="lazy" style="width:100%;border-radius:10px;aspect-ratio:4/3;object-fit:cover"></div>
</section>
<?php endif; ?>
<footer><div class="wrap">
 <div><h4>Recta al Pecho</h4><p>Canal de deportes donde el béisbol es la pasión. Las historias, de los que las vivieron.</p><p>© <?php echo date('Y'); ?> Marrero Bernal Media LLC. Todos los derechos reservados.</p>
 <p class="sponsor">Patrocinado por <a href="https://www.marrerobernal.com" target="_blank" rel="noopener" style="display:inline;text-decoration:underline;opacity:1">Marrero Bernal &amp; Associates</a> — impuestos, seguros, inmigración, notaría y traducciones. <a href="https://www.marrerobernal.com" target="_blank" rel="noopener" style="display:inline;text-decoration:underline;opacity:1">www.marrerobernal.com</a></p></div>
 <div><h4>Series</h4><?php foreach (recta_series() as $slug => $s): if ($c = get_category_by_slug($slug)): ?><a href="<?php echo esc_url(get_category_link($c)); ?>"><?php echo esc_html($s[0]); ?></a><?php endif; endforeach; ?></div>
 <div><h4>Síguenos</h4><a href="https://www.youtube.com/@RectaAlPecho" target="_blank" rel="noopener">YouTube</a><a href="https://www.facebook.com/RectaAlPecho/" target="_blank" rel="noopener">Facebook</a><a href="https://www.instagram.com/rectaalpecho/" target="_blank" rel="noopener">Instagram</a><a href="https://marrerobernalmedia.com/recta/" target="_blank" rel="noopener">App Recta al Pecho</a></div>
 <div><h4>El sitio</h4><a href="<?php echo esc_url(home_url('/quienes-somos/')); ?>">Quiénes somos</a><a href="<?php echo esc_url(home_url('/contacto/')); ?>">Contacto</a><a href="<?php echo esc_url(home_url('/privacy-policy-2/')); ?>">Política de privacidad</a><a href="<?php echo esc_url(home_url('/terminos-y-condiciones/')); ?>">Términos y condiciones</a></div>
</div></footer>
<?php wp_footer(); ?>
</body></html>
