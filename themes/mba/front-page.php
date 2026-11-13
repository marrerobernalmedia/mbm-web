<?php get_header(); ?>
<section class="hero">
  <div class="wrap">
    <div>
      <div class="kicker">Desde 2008 · En persona y a distancia</div>
      <span class="habla">We speak English</span>
      <h1>Seguros, taxes y trámites, <em>en tu idioma</em> y en un solo lugar.</h1>
      <p class="lead">Somos una agencia de seguros independiente con contratos con múltiples compañías de primer nivel, como Farmers y Progressive, además de preparadores de impuestos y especialistas en trámites. Diecisiete años atendiendo a la comunidad hispana, en nuestra oficina y a distancia, en todo Estados Unidos y desde cualquier parte del mundo.</p>
      <div class="search" id="search">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5" stroke-linecap="round"/></svg>
        <input id="q" type="search" placeholder="¿Qué necesitas? Ej. seguro de auto, Medicare, LLC, notaría…" autocomplete="off">
        <button type="button">Buscar</button>
        <div class="sugg" id="sugg"></div>
      </div>
      <div class="pop">Lo más buscado:
        <a href="/seguro-de-auto/">Seguro de auto</a><a href="#s-medicare">Medicare Advantage</a><a href="/taxes/">Taxes personales</a><a href="#s-llc">Crear una LLC</a><a href="/traducciones/">Traducciones DMV</a><a href="/notary-public/">Notaría</a>
      </div>
      <a class="gstars" href="https://g.page/r/CRuuvSm15kNDEAI" target="_blank" rel="noopener"><b>★★★★★</b> 4.9 en Google · 27 reseñas</a>
      <div class="badges"><span>Licencia NV · CA · AZ</span><span>Agencia independiente · 10 aseguradoras</span><span>Español e inglés</span><span>Cotización sin costo</span></div>
    </div>
    <div class="heroimg" style="background:url(<?php echo esc_url(get_theme_file_uri('img/eliam-retrato.jpg')); ?>) center/cover">
      <div><span class="lab">Eliam Marrero Bernal · fundador</span><b>Te atendemos como a familia.</b></div>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="tiles">
    <a class="tile" href="#personal"><div class="ic">🚗</div><b>Seguros personales</b><span>Auto, hogar, vida, mascotas, dispositivos y más</span></a>
    <a class="tile" href="#workers-comp"><div class="ic">🏢</div><b>Seguros de negocio</b><span>Workers' comp, responsabilidad, auto comercial · contabilidad y nómina</span></a>
    <a class="tile" href="/taxes/"><div class="ic">🧾</div><b>Taxes</b><span>Personales y de negocio, desde cualquier parte del país</span></a>
    <a class="tile" href="#dmv"><div class="ic">📝</div><b>Traducciones</b><span>Aprobadas por el DMV de Nevada</span></a>
    <a class="tile" href="/notary-public/"><div class="ic">✒️</div><b>Notaría y traducciones</b><span>Documentos certificados en español e inglés</span></a>
    <a class="tile" href="#s-llc"><div class="ic">📑</div><b>Licencias y LLC</b><span>Abre tu negocio</span></a>
  </div>
  <div class="carriers"><span>Trabajamos con</span><b>Farmers</b><b>Progressive</b><b>Travelers</b><b>Liberty Mutual</b><b>Mercury</b><b>National General</b><b>Bristol West</b><b>Foremost</b><b>Homeowners of America</b><b>Lemonade</b></div>
  <div class="cli">
    <a class="cli-card" href="https://marrerobernal.securefilepro.com/portal/#/login" target="_blank" rel="noopener"><div class="ic">🔐</div><div><b>Acceso de clientes</b><span>Entra al portal seguro para subir y descargar tus documentos (SecureFilePro).</span></div><em>Entrar →</em></a>
    <a class="cli-card" href="https://55a7805c-ea2c-4f0e-951b-1aa3c932e857.paylinks.godaddy.com" target="_blank" rel="noopener"><div class="ic">💳</div><div><b>Pagar en línea</b><span>Paga tu servicio con tarjeta de forma segura, desde el teléfono o la computadora.</span></div><em>Pagar →</em></a>
  </div>
  <div class="quote" id="cotizar">
    <div><div class="kicker" style="margin-bottom:6px">Cotiza en línea</div><h3>Tu cotización llega directo a nuestra oficina.</h3><p>Cinco minutos, sin llamadas. Un especialista la revisa y te contacta con opciones de varias compañías.</p></div>
    <div class="qbtns">
      <a href="/solicitud/?serv=auto">🚗 Auto</a>
      <a href="/solicitud/?serv=casa">🏠 Casa</a>
      <a href="/solicitud/?serv=casa">🏢 Condominio</a>
      <a href="/solicitud/?serv=renters">🔑 Renters</a>
      <a href="/solicitud/?serv=vida">❤️ Vida</a>
      <a href="/solicitud/?serv=negocio">💼 Negocio</a>
      <a href="/solicitud/?serv=auto,casa">🚗+🏠 Auto + casa</a>
      <a href="/solicitud/?serv=auto,renters">🚗+🔑 Auto + renters</a>
      <a href="/solicitud/?serv=mexico">🇲🇽 Auto para México</a>
      <a href="/solicitud/">📋 Taxes, traducciones y más</a>
      <a href="/citas/">📅 Agendar una cita</a>
    </div>
  </div>
</div>

<section class="svc" id="personal">
  <div class="wrap">
    <div class="kicker">Índice de servicios</div>
    <h2>Todo lo que hacemos, en una sola página.</h2>
    <p class="lead">Cada servicio tiene su propia página con lo que necesitas traer, cuánto demora y preguntas frecuentes. Haz clic y entérate antes de llamar.</p>
    <div class="cols">
      <div class="card">
        <img class="cimg" style="object-position:40% 55%" src="<?php echo esc_url(get_theme_file_uri('img/familia.jpg')); ?>" alt="Familia frente a su casa y su auto en North Las Vegas" width="1280" height="720" loading="lazy">
        <h3>Personal</h3>
        <div class="sub">Para ti y tu familia</div>
        <div class="grp"><b>Vehículos</b><ul><li><a id="s-auto" href="/solicitud/?serv=auto">Auto</a></li><li><a href="/solicitud/?serv=recre">Motocicleta</a></li><li><a href="/solicitud/?serv=recre">Bote y jet ski</a></li><li><a href="/solicitud/?serv=auto">Autos clásicos</a></li><li><a href="/solicitud/?serv=recre">ATV y off-road</a></li><li><a href="/solicitud/?serv=recre">RV y casa rodante</a></li></ul></div>
        <div class="grp"><b>Propiedad</b><ul><li><a href="/solicitud/?serv=casa">Casa</a></li><li><a href="/solicitud/?serv=casa">Condominio</a></li><li><a href="/solicitud/?serv=renters">Renters</a></li><li><a href="/solicitud/?serv=casa">Landlord</a></li><li><a href="/solicitud/?serv=casa">Casa móvil</a></li><li><a href="/solicitud/?serv=casa">Casa de vacaciones</a></li><li><a href="/solicitud/?serv=casa">Inundación</a></li><li><a href="/solicitud/?serv=casa">Terremoto</a></li></ul></div>
        <div class="grp"><b>Vida y salud</b><ul><li><a href="/solicitud/?serv=vida">Vida</a></li><li><a href="/solicitud/?serv=vida">Vida a término</a></li><li><a href="/solicitud/?serv=vida">Vida entera</a></li><li><a href="/solicitud/?serv=vida">Vida universal</a></li><li><a id="s-medicare" href="#medicare">Medicare Advantage</a></li><li><a href="/obamacare-nevada/">Obamacare (Nevada Health Link)</a></li><li><a href="/medicaid-nevada/">Medicaid de Nevada</a></li></ul></div>
        <div class="grp"><b>Otros seguros</b><ul><li><a href="/solicitud/?serv=otros">Umbrella</a></li><li><a href="/solicitud/?serv=otros">Mascotas</a></li><li><a href="/proteccion-de-dispositivos/">Dispositivos electrónicos</a></li><li><a href="/solicitud/?serv=auto,casa">Paquete auto + casa</a></li><li><a href="/solicitud/?serv=auto,renters">Paquete auto + renters</a></li><li><a href="/solicitud/?serv=mexico">Auto para manejar en México</a></li></ul></div>
        <div class="grp"><b>Trámites</b><ul><li><a id="s-taxes" href="/solicitud/?serv=taxes">Taxes personales</a></li><li><a href="/taxes/">E-file directo al IRS</a></li><li><a href="/itin/">Número ITIN (Agentes Certificados CAA)</a></li><li><a id="s-notaria" href="/solicitud/?serv=notaria">Notaría</a></li><li><a href="/solicitud/?serv=trad">Traducciones certificadas</a></li><li><a href="/traducciones/">Traducciones para el DMV (traductor aprobado)</a></li><li><a href="/solicitud/">Revisión gratuita de coberturas</a></li></ul></div>
        <p class="note">Seguros con múltiples compañías de primer nivel, entre ellas Farmers y Progressive. La disponibilidad de coberturas varía por compañía y por estado.</p>
      </div>
      <div class="card" id="negocios">
        <img class="cimg" style="object-position:70% 12%" src="<?php echo esc_url(get_theme_file_uri('img/negocio.jpg')); ?>" alt="Dueño de un negocio en su local" width="1280" height="720" loading="lazy">
        <h3>Negocios</h3>
        <div class="sub">Para tu empresa, desde el primer día</div>
        <div class="grp"><b>Seguros comerciales</b><ul><li><a href="/solicitud/?serv=negocio">Seguro de negocio</a></li><li><a href="/solicitud/?serv=negocio">Auto comercial</a></li><li><a href="/solicitud/?serv=negocio">Propiedad comercial</a></li><li><a href="/solicitud/?serv=negocio">Responsabilidad civil</a></li><li><a href="/solicitud/?serv=negocio">Workers' compensation</a></li><li><a href="/solicitud/?serv=negocio">Por industria</a></li></ul></div>
        <div class="grp"><b>Contabilidad y nómina</b><ul><li><a href="/contabilidad-y-nomina/">Contabilidad (bookkeeping)</a></li><li><a href="/contabilidad-y-nomina/">Nómina (payroll)</a></li><li><a href="/contabilidad-y-nomina/">Sales tax de Nevada</a></li></ul></div>
        <div class="grp"><b>Impuestos y formación</b><ul><li><a href="/solicitud/?serv=taxneg">Taxes de negocio</a></li><li><a href="/solicitud/?serv=llc">Licencias de negocio</a></li><li><a id="s-llc" href="/solicitud/?serv=llc">Creación de LLC</a></li><li><a href="/solicitud/?serv=llc">EIN y registro estatal</a></li></ul></div>
        <div class="grp"><b>Industrias que atendemos</b><ul><li><a href="#contacto">Restaurantes</a></li><li><a href="#contacto">Construcción</a></li><li><a href="#contacto">Transporte</a></li><li><a href="#contacto">Limpieza</a></li><li><a href="#contacto">Salones y barberías</a></li><li><a href="#contacto">Tiendas</a></li></ul></div>
        <div style="margin-top:26px;padding:18px;background:var(--cream);border-radius:14px">
          <b style="display:block;margin-bottom:4px">¿Vas a abrir tu negocio?</b>
          <span style="font-size:14px;color:var(--mut)">Te formamos la LLC, sacamos la licencia y dejamos el seguro listo en una sola visita.</span>
          <div style="margin-top:12px"><a class="btn btn-navy" href="#contacto">Hablar con un asesor</a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="dmvt wcsec" id="workers-comp">
  <div class="wrap">
    <div class="wc-top"><div>
    <div class="kicker">Seguros comerciales para el negocio hispano</div>
    <h2>Workers' Compensation: el seguro que más te van a pedir.</h2>
    <p>En Nevada, si tienes uno o más empleados, la ley te obliga a tener seguro de compensación al trabajador (workers' comp). Y aunque trabajes solo, muchos contratistas generales, dueños de obra y clientes no te dan el trabajo sin un certificado de seguro. Te lo cotizamos en español y te mandamos los certificados cuando te los pidan.</p>
    </div><img class="mimg" src="<?php echo esc_url(get_theme_file_uri('img/workers.jpg')); ?>" alt="Dueño de una cuadrilla de construcción con su agente de seguros en la obra" width="1280" height="720" loading="lazy"></div>
    <div class="why2">
      <div><b>Obligatorio en Nevada</b><p>Con uno o más empleados. En construcción, aunque el trabajo sea corto.</p></div>
      <div><b>Multas de hasta $15,000</b><p>Sin cobertura, el estado puede multarte y ordenar que cierres el negocio hasta tener el seguro, y pagas tú los costos de cualquier accidente de trabajo.</p></div>
      <div><b>Certificados cuando te los pidan</b><p>Si un contratista o un cliente te pide el certificado de seguro, te lo enviamos para que no pierdas el trabajo.</p></div>
      <div><b>Todo el negocio</b><p>Además del workers' comp: responsabilidad civil, auto comercial, propiedad y paquetes por industria.</p></div>
    </div>
    <div class="chips"><span>Construcción</span><span>Limpieza</span><span>Jardinería</span><span>Restaurantes</span><span>Transporte y camiones</span><span>Salones y barberías</span><span>Tiendas</span></div>
    <div class="btns"><a class="btn btn-acc" href="/solicitud/?serv=negocio">Cotizar mi workers' comp</a><a class="btn btn-ghost" href="tel:+18888772583">Llamar al 888-877-2583</a></div>
    <small>Fuente de los requisitos: División de Relaciones Industriales de Nevada. Las coberturas y las primas dependen de la aseguradora, la industria y la nómina.</small>
    <div class="libros" id="contabilidad">
      <img class="limg" src="<?php echo esc_url(get_theme_file_uri('img/contabilidad.jpg')); ?>" alt="Dueña de un negocio revisando su contabilidad y nómina con un contador" width="1280" height="720" loading="lazy">
      <div>
        <div class="kicker" style="color:var(--acc)">Para tu negocio</div>
        <h3>Contabilidad (bookkeeping) y nómina (payroll).</h3>
        <p>Llevamos los libros de tu negocio y la nómina de tus empleados, para que tú te ocupes de trabajar. Y como también preparamos tus taxes y tu seguro de workers' comp, que se calcula sobre la nómina, todo cuadra en un mismo lugar.</p>
      </div>
      <ul><li>Contabilidad mensual del negocio</li><li>Nómina de empleados con las planillas del IRS y de Nevada</li><li>Declaraciones de sales tax</li><li>Todo en español, en la oficina o a distancia</li><li><a href="/contabilidad-y-nomina/">Qué incluye: 941, 940, DETR, MBT y sales tax →</a></li></ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="kicker">Por qué nosotros</div>
    <h2>Diecisiete años, la misma gente, para clientes en todo el mundo.</h2>
    <div class="why">
      <div><b>2008</b><p>Año en que abrimos en North Las Vegas. Seguimos en el mismo lugar.</p></div>
      <div><b>Sin fronteras</b><p>Taxes, ITIN, traducciones y trámites a distancia para todo Estados Unidos y para quienes viven en otros países. Seguros con licencia en Nevada, California y Arizona.</p></div>
      <div><b>10 compañías</b><p>Somos independientes. En auto cotizamos con Farmers, Progressive, Travelers, Liberty Mutual, Mercury, National General y Bristol West; en casa, con Farmers, Foremost, Progressive, Mercury, National General, Homeowners of America y Lemonade. Te damos la mejor opción.</p></div>
      <div><b>1 visita</b><p>Seguro, taxes, contabilidad, nómina, ITIN, traducciones, notaría y más, en la misma oficina.</p></div>
    </div>
    <div class="resenas">
      <h3>Lo que dicen nuestros clientes en Google</h3>
      <div class="ti"><?php echo do_shortcode('[trustindex no-registration=google]'); ?></div>
      <div class="premios">
        
        <a class="wh" href="https://wallethub.com/profile/eliam-bernal-67214649i#reviews" target="_blank" rel="noopener"><img src="<?php echo esc_url(get_theme_file_uri('img/wallethub-best.svg')); ?>" alt="WalletHub Best Award: mejor agente de seguros" width="120" height="181" loading="lazy"><span><b>Mejor agente de seguros en Las Vegas</b><small>según WalletHub · 4.8 ★ · 81 reseñas</small></span></a>
      </div>
    </div>
  </div>
</section>

<section class="med" id="medicare">
  <div class="wrap">
    <div>
      <div class="kicker">Seguros de salud</div>
      <h2>Medicare Advantage, explicado sin letra pequeña.</h2>
      <p class="lead">Si tienes 65 años o más, o calificas por discapacidad, te ayudamos a comparar planes Medicare Advantage disponibles en tu condado y a entender qué cubre cada uno: médico, hospital, medicinas, dental, visión y más.</p>
      <ul>
        <li>Revisión gratuita de tu plan actual, sin compromiso.</li>
        <li>Inscripción anual del 15 de octubre al 7 de diciembre.</li>
        <li>Atención en español durante todo el año, no solo en temporada.</li>
        <li>Trabajamos con Alignment Health, Humana, SCAN y UnitedHealthcare.</li>
      </ul>
      <div style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-acc" href="#contacto">Revisar mi plan</a><a class="btn btn-ghost" style="background:transparent;color:#fff;border-color:#4a5a75" href="/medicare/">Todo sobre Medicare</a></div>
    </div>
    <div>
    <img class="mimg" src="<?php echo esc_url(get_theme_file_uri('img/medicare.jpg')); ?>" alt="Pareja mayor revisando su plan de salud en casa" width="1280" height="720" loading="lazy">
    <div class="box">
      <h3>Antes de que llames, debes saber:</h3>
      <small>No ofrecemos todos los planes disponibles en su área. Actualmente representamos 4 organizaciones que ofrecen 38 productos en su área. Comuníquese con Medicare.gov, al 1-800-MEDICARE (TTY 1-877-486-2048) o con su Programa Estatal de Asistencia sobre Seguros de Salud (SHIP) para obtener información sobre todas sus opciones.</small>
      <small>Marrero Bernal &amp; Associates es una agencia de seguros independiente con licencia y no está afiliada ni respaldada por el gobierno de EE. UU. ni por el programa federal Medicare.</small>
      <small>Las coberturas, primas y beneficios varían según el plan y el condado. Los textos finales se ajustan a la guía de mercadeo de CMS vigente.</small>
    </div>
    </div>
  </div>
</section>

<section class="irs" id="irs">
  <div class="wrap">
    <div class="kicker">Impuestos e ITIN</div>
    <h2>Tus taxes van directo al IRS. Sin intermediarios.</h2>
    <div class="irs-remoto">
      <div class="ic">🌎</div>
      <div>
        <h3>Taxes a distancia, en todo el país y desde el extranjero</h3>
        <p>No tienes que vivir en Nevada. Preparamos los taxes de clientes en cualquier estado de EE. UU. y también de estadounidenses que viven en otros países. Nos mandas tus documentos por el portal seguro de clientes o por correo a nuestra oficina, te explicamos todo por teléfono o videollamada y transmitimos tu declaración directo al IRS.</p>
        <p class="irs-dir">Dirección para correo: Marrero Bernal &amp; Associates · 3455 W Craig Rd Ste D · North Las Vegas, NV 89032</p>
        <div class="irs-btns"><a class="btn btn-acc" href="https://marrerobernal.securefilepro.com/portal/#/login" target="_blank" rel="noopener">Subir mis documentos</a><a class="btn btn-navy" href="#contacto">Hablar con un preparador</a></div>
      </div>
    </div>
    <div class="irs-pp">
      <img src="<?php echo esc_url(get_theme_file_uri('img/protectionplus.jpg')); ?>" alt="Protection Plus: $1 Million Tax Protection" width="1250" height="488" loading="lazy">
      <div>
        <div class="kicker">Tus taxes, protegidos</div>
        <h3>¿«Te garantizamos el mayor reembolso»? ¿Te lo dan por escrito?</h3>
        <p>Es la frase más repetida en los anuncios de taxes. Pero, ¿te has preguntado cómo te lo garantizan y qué pasa si después el IRS te manda una carta?</p>
        <p>Con nosotros, tu declaración va protegida con Protection Plus, por escrito y no de palabra:</p>
        <ul>
          <li>Hasta $1,000,000 en servicios de defensa si recibes una carta, una auditoría o una consulta del IRS o del estado.</li>
          <li>Evaluación profesional de tu caso, respuesta preparada por expertos y representación ante el IRS o el estado.</li>
          <li>Ayuda para restaurar tu identidad si te la roban.</li>
        </ul>
      </div>
    </div>
    <div class="irs-grid">
      <div class="card">
        <div class="ic">📡</div>
        <h3>Proveedor autorizado de e-file del IRS</h3>
        <p>Para conectarte a internet necesitas un proveedor de servicio que haga de intermediario. Con los taxes pasa lo mismo: muchas oficinas dependen de otra empresa para enviar tu declaración.</p>
        <p>Nosotros somos proveedor autorizado de e-file del IRS: transmitimos tu declaración directamente al IRS, sin intermediarios.</p>
        <div class="irs-pro">
          <b>¿Eres preparador de impuestos?</b>
          <span>Tú también puedes transmitir tus declaraciones al IRS a través de nosotros.</span>
          <a class="btn btn-navy" href="#contacto">Quiero transmitir con ustedes</a>
        </div>
      </div>
      <div class="card">
        <div class="ic">🪪</div>
        <h3>ITIN con Agentes de Aceptación Certificados del IRS</h3>
        <p>Si solicitas el número ITIN por tu cuenta, tienes que enviar tus documentos originales al IRS por correo, como el pasaporte, y se pueden perder.</p>
        <p>Contamos con Agentes de Aceptación Certificados (CAA) del IRS: revisamos y certificamos tus documentos aquí en la oficina y tú no tienes que mandar los originales.</p>
        <ul>
          <li>Solicitud del ITIN nueva o renovación.</li>
          <li>Tus documentos no salen de nuestras manos: no van al IRS.</li><li>¿No puedes venir? Nos los envías por correo a la oficina, los certificamos y te los devolvemos.</li>
          <li>Te acompañamos hasta que llega tu número.</li>
        </ul>
        <a class="btn btn-acc" href="/solicitud/?serv=itin">Solicitar mi ITIN</a>
      </div>
    </div>
  </div>
</section>

<section class="dmvt" id="dmv">
  <div class="wrap">
    <div class="dmvt-in">
      <div>
        <div class="kicker">Traducciones para el DMV</div>
        <h2>Traductor aprobado por el DMV de Nevada.</h2>
        <p>Para sacar la licencia de manejo, la Driver Authorization Card o la tarjeta de identificación en Nevada, el DMV exige que todo documento que no esté en inglés venga traducido por un traductor aprobado por el DMV.</p>
        <p>Nuestro fundador, Eliam Marrero Bernal, es traductor aprobado por el DMV de Nevada. Y como el DMV no está aceptando nuevos traductores, somos de los pocos que pueden hacerlo.</p>
        <div class="irs-btns"><a class="btn btn-acc" href="/solicitud/?serv=trad">Traducir mis documentos</a><a class="btn btn-ghost" href="https://dmv.nv.gov/translators.htm" target="_blank" rel="noopener">Verlo en el sitio del DMV</a></div>
      </div>
      <ul>
        <li>Actas de nacimiento, pasaportes y documentos de identidad.</li>
        <li>Licencias de manejo de otros países.</li>
        <li>Traducción completa y escrita a máquina, con fecha, firma, nuestro número de traductor del DMV y la certificación en la misma hoja, como la exige el DMV.</li><li>Sin un número de traductor válido, el DMV rechaza la traducción en la oficina.</li>
        <li>Atención en Las Vegas, North Las Vegas, Henderson, Paradise, Pahrump y Moapa Valley / Mesquite.</li>
      </ul>
    </div>
  </div>
</section>

<section class="about" id="nosotros">
  <div class="wrap">
    <img src="<?php echo esc_url(get_theme_file_uri('img/eliam.jpg')); ?>" alt="Eliam Marrero Bernal atendiendo clientes en la oficina" style="border-radius:22px;border:1px solid var(--line)">
    <div>
      <div class="kicker">Quiénes somos</div>
      <h2>Nacimos en el barrio. Hoy atendemos a todo el mundo.</h2>
      <p class="lead">Eliam Marrero Bernal fundó Marrero Bernal &amp; Associates en 2008 con una idea simple: que un cubano, un mexicano o un salvadoreño recién llegado a Las Vegas pudiera resolver su seguro, sus taxes y sus papeles con alguien que le hablara claro y en su idioma.</p>
      <p class="lead" style="margin-top:14px">Hoy somos una agencia independiente con contratos con varias compañías de primer nivel, preparadores de impuestos y un equipo que conoce a cada cliente por su nombre. Lo que ofrecemos no es un producto: es que tengas tu problema resuelto, vengas a la oficina o nos escribas desde el otro lado del mundo.</p>
      <div class="creds"><span>Agencia independiente</span><span>LUTCF · FSCP · CSP</span><span><span data-seg="tot.mba">23K</span>+ seguidores en redes</span><span>Licencia NV · CA · AZ</span><span>The American College</span><span>Español · English</span></div>
    </div>
  </div>
</section>

<section style="background:var(--cream)">
  <div class="wrap">
    <div class="kicker">Cómo funciona</div>
    <h2>Resolver un trámite no tiene que ser un día perdido.</h2>
    <img class="simg" style="object-position:50% 15%" src="<?php echo esc_url(get_theme_file_uri('img/tramites.jpg')); ?>" alt="Clienta firmando sus documentos en la oficina" width="1280" height="720" loading="lazy">
    <div class="steps">
      <div class="step"><h3>Nos cuentas</h3><p>Por teléfono, WhatsApp o en la oficina. Sin cita para la mayoría de los trámites.</p></div>
      <div class="step"><h3>Te decimos qué traer</h3><p>Una lista corta y clara de documentos. Si falta algo, te ayudamos a conseguirlo.</p></div>
      <div class="step"><h3>Lo hacemos contigo</h3><p>Cotizamos, llenamos y revisamos todo delante de ti, en tu idioma.</p></div>
      <div class="step"><h3>Seguimos ahí</h3><p>Reclamos, renovaciones, cambios y preguntas: la misma oficina, la misma gente.</p></div>
    </div>
  </div>
</section>

<section class="contact" id="contacto">
  <div class="wrap">
    <div class="cinfo">
      <div class="kicker">Contacto</div>
      <h2>Ven, llama o escribe.</h2>
      <a class="big" href="tel:+18888772583">888-877-2583</a><div style="font-size:14px;color:var(--mut);margin:-4px 0 10px">888-87-SALUD · llamadas y WhatsApp · gratis desde cualquier estado</div>
      <a class="wa" href="https://wa.me/18888772583" target="_blank" rel="noopener">💬 WhatsApp 888-877-2583</a>
      <div id="vonageClick2callme" style="margin-top:12px"></div>
      <p style="margin-top:16px"><b style="color:var(--ink)">3455 W Craig Rd, Suite D</b><br>North Las Vegas, NV 89032</p>
      <p>Lunes a viernes, 9:00 AM – 5:00 PM<br>Sábados y domingos cerrado</p>
      <div class="map"><iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=3455+W+Craig+Rd+Ste+D,+North+Las+Vegas,+NV+89032&output=embed" title="Mapa"></iframe></div>
    </div>
    <form method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
      <input type="hidden" name="action" value="mba_contacto"><?php wp_nonce_field('mba_contacto','mba_n'); ?><input type="text" name="empresa" style="display:none" tabindex="-1" autocomplete="off">
      <b style="font-family:Fraunces,serif;font-size:22px">Pide tu cotización gratis</b>
      <input name="nombre" placeholder="Nombre" required>
      <input name="telefono" placeholder="Teléfono o WhatsApp" required>
      <input type="email" name="correo" placeholder="Correo (opcional)">
      <select name="servicio"><option>¿Qué necesitas?</option><option>Seguro de auto</option><option>Seguro de casa o renters</option><option>Seguro de vida</option><option>Medicare Advantage</option><option>Obamacare (Nevada Health Link)</option><option>Protección de dispositivos</option><option>Seguro de negocio</option><option>Workers' compensation</option><option>Contabilidad y nómina</option><option>Taxes</option><option>Notaría o traducción</option><option>Licencia o LLC</option><option>Otro</option></select>
      <textarea name="mensaje" placeholder="Cuéntanos brevemente"></textarea>
      <button class="btn btn-navy" type="submit" style="justify-self:start">Enviar</button>
      <small>Respondemos el mismo día hábil. Nunca compartimos tus datos.</small>
      <?php if (isset($_GET['enviado'])): ?><div class="ok">✅ Recibido. Te contactamos el mismo día hábil.</div><?php elseif (isset($_GET['error'])): ?><div class="ok" style="background:#fdecec;color:#8a1f1f">No se pudo enviar. Llámanos al 888-877-2583.</div><?php endif; ?>
    </form>
  </div>
</section>


<?php get_footer(); ?>
