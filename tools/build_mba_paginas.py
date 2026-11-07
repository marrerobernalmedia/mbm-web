#!/usr/bin/env python3
"""Páginas propias de marrerobernal.com (Medicare, Obamacare/Nevada Health Link, Medicaid de Nevada,
protección de dispositivos) en español e inglés, y redirecciones 301 de las páginas viejas de Elementor.
Lo llama tools/build_mba_theme.py al final; también se puede correr solo: python3 tools/build_mba_paginas.py
Escribe themes/mba/paginas.php, themes/mba/paginas/*.php y añade CSS al final de themes/mba/style.css."""
import json, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
out = root / 'themes/mba'
(out / 'paginas').mkdir(parents=True, exist_ok=True)

TEL = '<a href="tel:+18338772583">833-877-2583</a>'
FARMERS_DEV = 'https://www.farmers.com/electronic-device-insurance/?Agent_Code=67249W%2430306E%248833H2&amp;Source_Indicator=AP'

# ---------------------------------------------------------------- contenido
P = {}

P['medicare'] = dict(
    es=dict(slug='medicare', img='medicare.jpg',
        title='Medicare Advantage en español · Marrero Bernal & Associates',
        desc='Te ayudamos a comparar planes Medicare Advantage y de medicinas en tu condado, en español. Fechas de inscripción, qué revisar y cómo trabajamos. North Las Vegas.',
        html=f'''
<section class="sub-hero med"><div class="wrap">
  <div>
    <div class="kicker">Seguros de salud · Medicare</div>
    <h1>Medicare Advantage y planes de medicinas, explicados en español.</h1>
    <p class="lead">Si tienes 65 años o más, o tienes Medicare por discapacidad, te ayudamos a comparar los planes que ofrecemos en tu condado y a entender qué cubre cada uno antes de decidir.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="tel:+18338772583">Llamar al 833-877-2583</a><a class="btn btn-ghost" href="#contacto">Revisar mi plan</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Pareja mayor revisando su plan de salud en casa" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <h2>Fechas que importan</h2>
  <div class="sub-grid">
    <div class="sub-card"><b>Inscripción anual</b><p>Del 15 de octubre al 7 de diciembre. Puedes cambiar de plan y el cambio empieza el 1 de enero.</p></div>
    <div class="sub-card"><b>Si ya tienes Medicare Advantage</b><p>Del 1 de enero al 31 de marzo puedes cambiar a otro plan Medicare Advantage o volver a Medicare Original, una sola vez.</p></div>
    <div class="sub-card"><b>Cuando cumples 65</b><p>Tienes un período de 7 meses: los 3 meses antes de tu cumpleaños, el mes del cumpleaños y los 3 meses después.</p></div>
    <div class="sub-card"><b>Períodos especiales</b><p>Una mudanza, perder la cobertura del trabajo o tener Medicaid, entre otros casos, te pueden abrir un período para cambiar fuera de esas fechas.</p></div>
  </div>
  <h2>Con quién trabajamos</h2>
  <p>Tenemos contrato para Medicare Advantage con <b>Alignment Health, Humana, SCAN y UnitedHealthcare</b>. Revisamos contigo los planes de estas compañías disponibles en tu condado.</p>
  <h2>Qué revisamos contigo</h2>
  <ul class="sub-list">
    <li>Que tus médicos y hospitales estén en la red del plan.</li>
    <li>Que tus medicinas estén cubiertas y cuánto pagarías por ellas.</li>
    <li>La prima, el deducible y el máximo que pagarías de tu bolsillo en el año.</li>
    <li>Los beneficios adicionales que incluyen algunos planes, como dental, visión o audición. Varían según el plan y el condado.</li>
    <li>Si tienes ingresos limitados, te decimos dónde pedir Ayuda Adicional (Extra Help) para las medicinas y los Programas de Ahorros de Medicare.</li>
  </ul>
  <h2>Cómo trabajamos</h2>
  <ol class="sub-steps">
    <li><b>Hablamos.</b> Por teléfono, por WhatsApp o en la oficina de North Las Vegas.</li>
    <li><b>Comparamos.</b> Revisamos los planes que ofrecemos en tu condado con tus médicos y tus medicinas.</li>
    <li><b>Tú decides.</b> Sin presión: la decisión es tuya.</li>
    <li><b>Seguimos contigo.</b> Atención en español durante todo el año, no solo en temporada.</li>
  </ol>
  <div class="sub-legal">
    <p>No ofrecemos todos los planes disponibles en su área. Actualmente representamos 4 organizaciones que ofrecen 38 productos en su área. Comuníquese con Medicare.gov, al 1-800-MEDICARE (TTY 1-877-486-2048) o con su Programa Estatal de Asistencia sobre Seguros de Salud (SHIP) para obtener información sobre todas sus opciones. En Nevada, el SHIP es el Medicare Assistance Program (MAP): 1-800-307-4444.</p>
    <p>Al llamar, hablará con un agente de seguros con licencia. Marrero Bernal &amp; Associates es una agencia de seguros independiente y no está afiliada ni respaldada por el gobierno de EE. UU. ni por el programa federal Medicare. Las coberturas, primas y beneficios varían según el plan y el condado.</p>
  </div>
</div></section>'''),
    en=dict(slug='medicare', img='medicare.jpg',
        title='Medicare Advantage help in Spanish and English · Marrero Bernal & Associates',
        desc='We help you compare the Medicare Advantage and drug plans we offer in your county, in Spanish or English. Enrollment dates, what to check and how we work. North Las Vegas.',
        html=f'''
<section class="sub-hero med"><div class="wrap">
  <div>
    <div class="kicker">Health insurance · Medicare</div>
    <h1>Medicare Advantage and drug plans, explained clearly.</h1>
    <p class="lead">If you are 65 or older, or have Medicare because of a disability, we help you compare the plans we offer in your county and understand what each one covers before you decide.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="tel:+18338772583">Call 833-877-2583</a><a class="btn btn-ghost" href="#contacto">Review my plan</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Older couple reviewing their health plan at home" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <h2>Dates that matter</h2>
  <div class="sub-grid">
    <div class="sub-card"><b>Annual Enrollment</b><p>October 15 to December 7. You can change plans and the change starts January 1.</p></div>
    <div class="sub-card"><b>If you already have Medicare Advantage</b><p>From January 1 to March 31 you can switch to another Medicare Advantage plan or go back to Original Medicare, one time.</p></div>
    <div class="sub-card"><b>When you turn 65</b><p>You have a 7-month window: the 3 months before your birthday, your birthday month and the 3 months after.</p></div>
    <div class="sub-card"><b>Special periods</b><p>Moving, losing employer coverage or having Medicaid, among other cases, can open a period to change outside those dates.</p></div>
  </div>
  <h2>Who we work with</h2>
  <p>We are appointed for Medicare Advantage with <b>Alignment Health, Humana, SCAN and UnitedHealthcare</b>. We review the plans from these companies available in your county.</p>
  <h2>What we review with you</h2>
  <ul class="sub-list">
    <li>That your doctors and hospitals are in the plan's network.</li>
    <li>That your medications are covered and what you would pay for them.</li>
    <li>The premium, the deductible and the most you would pay out of pocket in a year.</li>
    <li>Extra benefits some plans include, such as dental, vision or hearing. They vary by plan and county.</li>
    <li>If your income is limited, we tell you where to apply for Extra Help with drug costs and the Medicare Savings Programs.</li>
  </ul>
  <h2>How we work</h2>
  <ol class="sub-steps">
    <li><b>We talk.</b> By phone, WhatsApp or at our North Las Vegas office.</li>
    <li><b>We compare.</b> We check the plans we offer in your county against your doctors and medications.</li>
    <li><b>You decide.</b> No pressure: the decision is yours.</li>
    <li><b>We stay with you.</b> Service all year round, not just during enrollment season.</li>
  </ol>
  <div class="sub-legal">
    <p>We do not offer every plan available in your area. Currently we represent 4 organizations which offer 38 products in your area. Please contact Medicare.gov, 1-800-MEDICARE (TTY 1-877-486-2048), or your local State Health Insurance Program (SHIP) to get information on all of your options. In Nevada, the SHIP is the Medicare Assistance Program (MAP): 1-800-307-4444.</p>
    <p>By calling, you will speak with a licensed insurance agent. Marrero Bernal &amp; Associates is an independent insurance agency and is not connected with or endorsed by the U.S. government or the federal Medicare program. Coverage, premiums and benefits vary by plan and county.</p>
  </div>
</div></section>'''))

P['obamacare'] = dict(
    es=dict(slug='obamacare-nevada', img='salud.jpg',
        title='Obamacare en Nevada (Nevada Health Link) con broker certificado · Marrero Bernal & Associates',
        desc='Somos broker certificado de Nevada Health Link. Te ayudamos en español a comparar planes, ver si calificas para ayuda con el pago e inscribirte. Inscripción abierta hasta el 15 de enero.',
        html='''
<section class="sub-hero"><div class="wrap">
  <div>
    <div class="kicker">Seguros de salud · Nevada Health Link</div>
    <h1>Obamacare en Nevada, con un broker certificado que te habla en español.</h1>
    <p class="lead">Somos broker certificado de Nevada Health Link, el mercado de seguros médicos del estado. Te ayudamos a comparar los planes, a ver si calificas para ayuda con el pago y a inscribirte.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="tel:+18338772583">Llamar al 833-877-2583</a><a class="btn btn-ghost" href="#contacto">Quiero que me llamen</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Familia revisando opciones de seguro médico con una agente" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <div class="sub-alert"><b>La inscripción abierta para 2027 ya empezó y termina el 15 de enero de 2027.</b> Para tener cobertura desde el 1 de enero, inscríbete a más tardar el 31 de diciembre.</div>
  <div class="sub-grid">
    <div class="sub-card"><b>Más de 130 planes</b><p>De nueve compañías en Nevada Health Link, más planes dentales.</p></div>
    <div class="sub-card"><b>Ayuda con el pago</b><p>Según Nevada Health Link, cerca de 8 de cada 10 inscritos califica para ahorros que bajan la prima o lo que paga de su bolsillo.</p></div>
    <div class="sub-card"><b>Planes Battle Born</b><p>Los planes del estado de Nevada, pensados para primas más bajas, con Health Plan of Nevada, Anthem y SilverSummit (Ambetter).</p></div>
    <div class="sub-card"><b>El mismo precio</b><p>La prima es la misma si te inscribes con un broker certificado o por tu cuenta. La diferencia es que alguien te explica y te acompaña.</p></div>
  </div>
  <h2>Ten esto a mano</h2>
  <ul class="sub-list">
    <li>Un estimado de los ingresos de tu hogar para 2027.</li>
    <li>Quiénes van en tu declaración de impuestos.</li>
    <li>Los documentos de estatus migratorio de quienes piden cobertura.</li>
    <li>Tus médicos y tus medicinas, para buscar un plan que los incluya.</li>
  </ul>
  <h2>Fuera de la inscripción abierta</h2>
  <p>Solo puedes inscribirte si tienes un evento que califique, como perder otra cobertura, mudarte, casarte o tener un bebé. Normalmente tienes 60 días desde ese evento. Llámanos y lo revisamos.</p>
  <p>Si tus ingresos son bajos, puede que califiques para Medicaid: <a href="/medicaid-nevada/">así se solicita</a>. Si vives fuera de Nevada, te orientamos hacia el mercado de tu estado.</p>
  <div class="sub-legal">
    <p>Marrero Bernal &amp; Associates es una agencia de seguros independiente y broker certificado de Nevada Health Link. No somos Nevada Health Link ni una agencia del gobierno. Los planes, las primas y la ayuda con el pago dependen de tus ingresos, tu condado y tu hogar. También puedes inscribirte directamente en NevadaHealthLink.com o al 1-800-547-2927.</p>
  </div>
</div></section>'''),
    en=dict(slug='obamacare-nevada', img='salud.jpg',
        title='Obamacare in Nevada (Nevada Health Link) with a certified broker · Marrero Bernal & Associates',
        desc='We are a Nevada Health Link certified broker. We help you compare plans, see if you qualify for financial help and enroll, in English or Spanish. Open enrollment runs through January 15.',
        html='''
<section class="sub-hero"><div class="wrap">
  <div>
    <div class="kicker">Health insurance · Nevada Health Link</div>
    <h1>Obamacare in Nevada, with a certified broker who speaks your language.</h1>
    <p class="lead">We are a certified broker with Nevada Health Link, the state's health insurance marketplace. We help you compare plans, see if you qualify for financial help and enroll.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="tel:+18338772583">Call 833-877-2583</a><a class="btn btn-ghost" href="#contacto">Have us call me</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Family reviewing health insurance options with an agent" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <div class="sub-alert"><b>Open enrollment for 2027 is underway and ends January 15, 2027.</b> For coverage starting January 1, enroll by December 31.</div>
  <div class="sub-grid">
    <div class="sub-card"><b>130+ plans</b><p>From nine companies on Nevada Health Link, plus dental plans.</p></div>
    <div class="sub-card"><b>Help paying</b><p>According to Nevada Health Link, about 8 in 10 enrollees qualify for savings that lower their premium or out-of-pocket costs.</p></div>
    <div class="sub-card"><b>Battle Born State Plans</b><p>Nevada's state plans, designed for lower premiums, with Health Plan of Nevada, Anthem and SilverSummit (Ambetter).</p></div>
    <div class="sub-card"><b>Same price</b><p>Your premium is the same whether you enroll with a certified broker or on your own. The difference is someone explains it and stays with you.</p></div>
  </div>
  <h2>Have this ready</h2>
  <ul class="sub-list">
    <li>An estimate of your household income for 2027.</li>
    <li>Who is on your tax return.</li>
    <li>Immigration status documents for those requesting coverage.</li>
    <li>Your doctors and medications, to find a plan that includes them.</li>
  </ul>
  <h2>Outside open enrollment</h2>
  <p>You can only enroll with a qualifying life event, such as losing other coverage, moving, getting married or having a baby. You usually have 60 days from that event. Call us and we will review it.</p>
  <p>If your income is low, you may qualify for Medicaid: <a href="/en/medicaid-nevada/">here is how to apply</a>. If you live outside Nevada, we point you to your state's marketplace.</p>
  <div class="sub-legal">
    <p>Marrero Bernal &amp; Associates is an independent insurance agency and a Nevada Health Link certified broker. We are not Nevada Health Link or a government agency. Plans, premiums and financial help depend on your income, county and household. You can also enroll directly at NevadaHealthLink.com or 1-800-547-2927.</p>
  </div>
</div></section>'''))

P['medicaid'] = dict(
    es=dict(slug='medicaid-nevada', img='medicaid.jpg',
        title='Medicaid de Nevada: cómo solicitarlo · Marrero Bernal & Associates',
        desc='Te orientamos en español sobre Medicaid y Nevada Check Up: quién puede calificar, cómo solicitar en Access Nevada y qué hacer si no calificas.',
        html='''
<section class="sub-hero"><div class="wrap">
  <div>
    <div class="kicker">Seguros de salud · Medicaid</div>
    <h1>Medicaid de Nevada: te explicamos cómo solicitarlo.</h1>
    <p class="lead">Medicaid y Nevada Check Up son programas del estado para personas y familias con ingresos limitados. No vendemos Medicaid ni hacemos la solicitud: te orientamos en español para que sepas si puedes calificar y dónde solicitar.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="https://accessnevada.nv.gov/public/landing-page" target="_blank" rel="noopener">Ir a Access Nevada</a><a class="btn btn-ghost" href="tel:+18338772583">Tengo una pregunta</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Madre con su hijo en la recepción de una clínica" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <h2>Quién puede calificar</h2>
  <p>Depende de los ingresos y del tamaño del hogar, y de los requisitos de estatus migratorio. En general, el estado revisa casos de niños, embarazadas, adultos con ingresos limitados y personas mayores, ciegas o con discapacidad. Las reglas las fija el estado y la decisión es de la División de Servicios Sociales de Nevada.</p>
  <h2>Cómo se solicita</h2>
  <div class="sub-grid">
    <div class="sub-card"><b>En línea</b><p>En <a href="https://accessnevada.nv.gov/public/landing-page" target="_blank" rel="noopener">Access Nevada</a>. Tiene una herramienta para saber si calificas antes de solicitar.</p></div>
    <div class="sub-card"><b>Por teléfono</b><p>División de Servicios Sociales de Nevada: (775) 684-0800, de 7:00 AM a 5:00 PM.</p></div>
    <div class="sub-card"><b>En papel</b><p>Con el formulario "Application for Health Insurance" del estado, que se envía por correo.</p></div>
  </div>
  <h2>Si no calificas o pierdes Medicaid</h2>
  <p>Puedes buscar un plan de Nevada Health Link, muchas veces con ayuda para pagar la prima. Perder Medicaid abre un período especial para inscribirte. Somos broker certificado: <a href="/obamacare-nevada/">te ayudamos con eso</a>.</p>
  <div class="sub-alert"><b>Cuidado con las estafas.</b> El estado no te llama para pedirte datos de tu historial médico, de tus beneficios o de tus medicinas. Si recibes una llamada así, cuelga.</div>
  <div class="sub-legal">
    <p>Marrero Bernal &amp; Associates es una agencia de seguros independiente. No somos una agencia del gobierno, no decidimos quién califica para Medicaid y no presentamos solicitudes de Medicaid. La información de esta página es orientativa; confirma siempre con la División de Servicios Sociales de Nevada.</p>
  </div>
</div></section>'''),
    en=dict(slug='medicaid-nevada', img='medicaid.jpg',
        title='Nevada Medicaid: how to apply · Marrero Bernal & Associates',
        desc='Guidance in English and Spanish on Medicaid and Nevada Check Up: who may qualify, how to apply on Access Nevada and what to do if you do not qualify.',
        html='''
<section class="sub-hero"><div class="wrap">
  <div>
    <div class="kicker">Health insurance · Medicaid</div>
    <h1>Nevada Medicaid: we explain how to apply.</h1>
    <p class="lead">Medicaid and Nevada Check Up are state programs for people and families with limited income. We do not sell Medicaid or file the application: we guide you so you know if you may qualify and where to apply.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="https://accessnevada.nv.gov/public/landing-page" target="_blank" rel="noopener">Go to Access Nevada</a><a class="btn btn-ghost" href="tel:+18338772583">I have a question</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Mother with her child at a clinic front desk" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <h2>Who may qualify</h2>
  <p>It depends on income, household size and immigration status requirements. In general, the state reviews cases for children, pregnant women, adults with limited income, and people who are older, blind or have a disability. The state sets the rules and the Nevada Division of Social Services makes the decision.</p>
  <h2>How to apply</h2>
  <div class="sub-grid">
    <div class="sub-card"><b>Online</b><p>At <a href="https://accessnevada.nv.gov/public/landing-page" target="_blank" rel="noopener">Access Nevada</a>. It has a tool to check if you qualify before applying.</p></div>
    <div class="sub-card"><b>By phone</b><p>Nevada Division of Social Services: (775) 684-0800, 7:00 AM to 5:00 PM.</p></div>
    <div class="sub-card"><b>On paper</b><p>With the state's "Application for Health Insurance" form, sent by mail.</p></div>
  </div>
  <h2>If you do not qualify or lose Medicaid</h2>
  <p>You can look for a Nevada Health Link plan, often with help paying the premium. Losing Medicaid opens a special period to enroll. We are a certified broker: <a href="/en/obamacare-nevada/">we can help with that</a>.</p>
  <div class="sub-alert"><b>Watch out for scams.</b> The state does not call you to ask about your medical records, benefits or prescriptions. If you get a call like that, hang up.</div>
  <div class="sub-legal">
    <p>Marrero Bernal &amp; Associates is an independent insurance agency. We are not a government agency, we do not decide who qualifies for Medicaid and we do not submit Medicaid applications. This page is for guidance only; always confirm with the Nevada Division of Social Services.</p>
  </div>
</div></section>'''))

P['dispositivos'] = dict(
    es=dict(slug='proteccion-de-dispositivos', img='dispositivos.jpg',
        title='Protección de teléfonos y electrónicos desde $16.99 al mes · Marrero Bernal & Associates',
        desc='Pantalla rota, derrames, fallas, pérdida o robo. Protección de dispositivos de Farmers para los teléfonos de la casa y tus electrónicos, desde $16.99 al mes. Aplican términos.',
        html=f'''
<section class="sub-hero"><div class="wrap">
  <div>
    <div class="kicker">Seguros personales · Dispositivos</div>
    <h1>Protección para tus teléfonos y tus equipos electrónicos.</h1>
    <p class="lead">Pantalla rota, un derrame, un robo o un equipo que deja de funcionar. Con la protección de dispositivos de Farmers cubres los teléfonos de la casa y tus electrónicos con un plan mensual, sin contrato a largo plazo.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="{FARMERS_DEV}" target="_blank" rel="noopener">Ver planes e inscribirme</a><a class="btn btn-ghost" href="tel:+18338772583">Llamar al 833-877-2583</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Familia en casa con teléfono, laptop, tableta y televisor" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <div class="sub-grid planes">
    <div class="sub-card"><b>Móvil</b><div class="precio">$16.99<small>/mes</small></div><p>Hasta 4 teléfonos de la casa. Daño accidental, pantalla rota, fallas, pérdida y robo.</p></div>
    <div class="sub-card"><b>Hogar</b><div class="precio">$19.99<small>/mes</small></div><p>Los electrónicos de la casa: televisores LED y LCD, computadoras, tabletas, consolas, audífonos, relojes inteligentes y equipos del hogar inteligente. Daño accidental y fallas; no cubre pérdida ni robo.</p></div>
    <div class="sub-card destacado"><b>Total</b><div class="precio">$34.99<small>/mes</small></div><p>Las dos cosas: hasta 4 teléfonos y los electrónicos de la casa en un solo plan.</p></div>
  </div>
  <p class="sub-nota">Precios sin impuestos ni cargos.</p>
  <h2>Cómo funciona</h2>
  <ul class="sub-list">
    <li>Cada reclamo lleva un deducible que depende del equipo y del tipo de reclamo.</li>
    <li>Los teléfonos quedan cubiertos desde la inscripción; los electrónicos del hogar, a los 30 días.</li>
    <li>Según el caso, reparan, reemplazan o reembolsan el equipo.</li>
    <li>Los equipos tienen que estar funcionando bien cuando te inscribes.</li>
    <li>Puedes cancelar cuando quieras.</li>
  </ul>
  <div class="sub-legal">
    <p>Aplican términos, límites y exclusiones. Programa ofrecido a clientes de Farmers y administrado por Likewize Device Protection, LLC; Likewize Agency, LLC es el agente con licencia. El seguro de pérdida y robo lo emite Universal Underwriters Insurance Company, que no está afiliada a Farmers Insurance Group. Precios vigentes en noviembre de 2026; pueden cambiar. Lee el contrato antes de inscribirte.</p>
  </div>
</div></section>'''),
    en=dict(slug='device-protection', img='dispositivos.jpg',
        title='Phone and electronics protection from $16.99 a month · Marrero Bernal & Associates',
        desc='Cracked screens, spills, breakdowns, loss or theft. Farmers device protection for your household phones and electronics, from $16.99 a month. Terms apply.',
        html=f'''
<section class="sub-hero"><div class="wrap">
  <div>
    <div class="kicker">Personal insurance · Devices</div>
    <h1>Protection for your phones and electronics.</h1>
    <p class="lead">A cracked screen, a spill, a theft or a device that stops working. With Farmers device protection you cover your household phones and electronics with a monthly plan and no long-term contract.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="{FARMERS_DEV}" target="_blank" rel="noopener">See plans and enroll</a><a class="btn btn-ghost" href="tel:+18338772583">Call 833-877-2583</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Family at home with a phone, laptop, tablet and TV" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <div class="sub-grid planes">
    <div class="sub-card"><b>Mobile</b><div class="precio">$16.99<small>/mo</small></div><p>Up to 4 household phones. Accidental damage, cracked screens, breakdowns, loss and theft.</p></div>
    <div class="sub-card"><b>Home</b><div class="precio">$19.99<small>/mo</small></div><p>Your home electronics: LED and LCD TVs, computers, tablets, game consoles, headphones, smartwatches and smart home devices. Accidental damage and breakdowns; no loss or theft.</p></div>
    <div class="sub-card destacado"><b>Total</b><div class="precio">$34.99<small>/mo</small></div><p>Both: up to 4 phones and your home electronics in one plan.</p></div>
  </div>
  <p class="sub-nota">Prices exclude taxes and fees.</p>
  <h2>How it works</h2>
  <ul class="sub-list">
    <li>Each claim has a deductible that depends on the device and the type of claim.</li>
    <li>Phones are covered from enrollment; home electronics after 30 days.</li>
    <li>Depending on the case, the device is repaired, replaced or reimbursed.</li>
    <li>Devices must be in good working condition when you enroll.</li>
    <li>You can cancel anytime.</li>
  </ul>
  <div class="sub-legal">
    <p>Terms, limits and exclusions apply. Program offered to Farmers customers and administered by Likewize Device Protection, LLC; Likewize Agency, LLC is the licensed agent. Loss and theft insurance is underwritten by Universal Underwriters Insurance Company, which is not affiliated with Farmers Insurance Group. Prices as of November 2026; subject to change. Read the contract before enrolling.</p>
  </div>
</div></section>'''))

P['contabilidad'] = dict(
    es=dict(slug='contabilidad-y-nomina', img='contabilidad.jpg',
        title='Contabilidad, nómina y sales tax para negocios en Nevada · Marrero Bernal & Associates',
        desc='Nómina con las planillas 941 y 940, W-2 y 1099, los reportes de Nevada (DETR y Modified Business Tax), declaraciones de sales tax y contabilidad mensual. En español, en la oficina o a distancia.',
        html='''
<section class="sub-hero"><div class="wrap">
  <div>
    <div class="kicker">Para tu negocio · Contabilidad y nómina</div>
    <h1>Tu nómina, tus libros y tus declaraciones, al día con el IRS y con Nevada.</h1>
    <p class="lead">Calculamos la nómina de tus empleados, presentamos las planillas federales y estatales a tiempo, declaramos el impuesto sobre las ventas y llevamos la contabilidad del negocio. Tú te ocupas de trabajar; nosotros, de que no te llegue una multa.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="/#contacto">Pide una consulta</a><a class="btn btn-ghost" href="tel:+18338772583">Llamar al 833-877-2583</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Dueña de un negocio revisando su contabilidad y nómina con un contador" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <h2>Nómina (payroll)</h2>
  <ul class="sub-list">
    <li>Cálculo de cada pago con sus retenciones federales: impuesto sobre el ingreso, Seguro Social y Medicare, y talón de pago para cada empleado.</li>
    <li><b>Formulario 941</b> cada trimestre, con los depósitos de impuestos de nómina al IRS.</li>
    <li><b>Formulario 940</b> una vez al año, el impuesto federal de desempleo (FUTA).</li>
    <li><b>W-2 y W-3</b> para tus empleados y para el Seguro Social al cierre del año.</li>
    <li><b>1099-NEC</b> para los contratistas a los que les pagas.</li>
    <li>Registro de cada empleado nuevo ante el estado.</li>
  </ul>
  <h2>Lo que pide Nevada</h2>
  <p>Nevada no cobra impuesto estatal sobre el sueldo, pero el negocio que tiene empleados sí tiene obligaciones con el estado:</p>
  <ul class="sub-list">
    <li><b>Seguro de desempleo (DETR):</b> el reporte de salarios y la contribución de cada trimestre.</li>
    <li><b>Modified Business Tax (MBT):</b> la declaración trimestral ante el Departamento de Impuestos de Nevada, que se presenta aunque no toque pagar.</li>
    <li><b>Workers' compensation:</b> la ley lo exige desde el primer empleado. Lo cotizamos con varias compañías y se calcula sobre la misma nómina que llevamos. <a href="/#workers-comp">Ver seguro de workers' comp →</a></li>
  </ul>
  <h2>Impuesto sobre las ventas (sales tax)</h2>
  <ul class="sub-list">
    <li>Declaraciones de ventas y uso de Nevada por My Nevada Tax, con la frecuencia que el estado le asigna a tu negocio, mensual o trimestral.</li>
    <li>Desde 2026 vencen el día 20 del mes siguiente al período.</li>
    <li>Se presentan aunque ese período no hayas vendido nada; una declaración que falta también trae multa.</li>
  </ul>
  <h2>Contabilidad (bookkeeping)</h2>
  <ul class="sub-list">
    <li>Registro de ingresos y gastos, y conciliación de las cuentas del banco y las tarjetas cada mes.</li>
    <li>Estado de ganancias y pérdidas para que sepas cómo va el negocio.</li>
    <li>Los libros listos para la declaración de impuestos del negocio al final del año, que también preparamos.</li>
  </ul>
  <h2>El calendario que llevamos por ti</h2>
  <div class="sub-grid">
    <div class="sub-card"><b>Cada pago</b><p>Nómina, retenciones y talones de pago.</p></div>
    <div class="sub-card"><b>Cada mes o trimestre</b><p>Sales tax de Nevada, el día 20 del mes siguiente.</p></div>
    <div class="sub-card"><b>Cada trimestre</b><p>Formulario 941, reporte del DETR y Modified Business Tax: hasta el último día del mes siguiente al trimestre.</p></div>
    <div class="sub-card destacado"><b>Cada año</b><p>Formulario 940, W-2, W-3 y 1099-NEC antes del 31 de enero.</p></div>
  </div>
  <div class="sub-legal">
    <p>Las fechas, tasas y requisitos los fijan el IRS, el Departamento de Empleo, Capacitación y Rehabilitación de Nevada (DETR) y el Departamento de Impuestos de Nevada, y pueden cambiar. Los confirmamos para cada negocio al empezar.</p>
  </div>
</div></section>'''),
    en=dict(slug='bookkeeping-payroll', img='contabilidad.jpg',
        title='Bookkeeping, payroll and sales tax for Nevada businesses · Marrero Bernal & Associates',
        desc='Payroll with Forms 941 and 940, W-2s and 1099s, Nevada filings (DETR and Modified Business Tax), sales tax returns and monthly bookkeeping. In English or Spanish, at the office or remotely.',
        html='''
<section class="sub-hero"><div class="wrap">
  <div>
    <div class="kicker">For your business · Bookkeeping and payroll</div>
    <h1>Your payroll, your books and your filings, up to date with the IRS and Nevada.</h1>
    <p class="lead">We run your employees' payroll, file your federal and state returns on time, file your sales tax and keep your business books. You run your business; we make sure no penalty letter shows up.</p>
    <div class="sub-cta"><a class="btn btn-acc" href="/en/#contacto">Request a consultation</a><a class="btn btn-ghost" href="tel:+18338772583">Call 833-877-2583</a></div>
  </div>
  <img class="mimg" src="IMG" alt="Business owner reviewing her books and payroll with an accountant" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">
  <h2>Payroll</h2>
  <ul class="sub-list">
    <li>Every paycheck calculated with its federal withholding (income tax, Social Security and Medicare), plus a pay stub for each employee.</li>
    <li><b>Form 941</b> every quarter, with your payroll tax deposits to the IRS.</li>
    <li><b>Form 940</b> once a year, the federal unemployment tax (FUTA).</li>
    <li><b>W-2s and W-3</b> for your employees and the Social Security Administration at year end.</li>
    <li><b>1099-NEC</b> for the contractors you pay.</li>
    <li>New-hire reporting to the state.</li>
  </ul>
  <h2>What Nevada requires</h2>
  <p>Nevada has no state income tax on wages, but a business with employees still has state obligations:</p>
  <ul class="sub-list">
    <li><b>Unemployment insurance (DETR):</b> the quarterly wage report and contribution.</li>
    <li><b>Modified Business Tax (MBT):</b> the quarterly return to the Nevada Department of Taxation, filed even when nothing is owed.</li>
    <li><b>Workers' compensation:</b> required by law from your first employee. We quote it with several carriers, and it's based on the same payroll we run. <a href="/en/#workers-comp">See workers' comp insurance →</a></li>
  </ul>
  <h2>Sales tax</h2>
  <ul class="sub-list">
    <li>Nevada sales and use tax returns through My Nevada Tax, on the schedule the state assigns your business, monthly or quarterly.</li>
    <li>Since 2026 they are due on the 20th of the month after the period.</li>
    <li>They must be filed even if you had no sales that period; a missing return also brings a penalty.</li>
  </ul>
  <h2>Bookkeeping</h2>
  <ul class="sub-list">
    <li>Income and expenses recorded, and bank and card accounts reconciled every month.</li>
    <li>A profit and loss statement so you know how the business is doing.</li>
    <li>Books ready for the year-end business tax return, which we also prepare.</li>
  </ul>
  <h2>The calendar we keep for you</h2>
  <div class="sub-grid">
    <div class="sub-card"><b>Every payday</b><p>Payroll, withholding and pay stubs.</p></div>
    <div class="sub-card"><b>Every month or quarter</b><p>Nevada sales tax, due the 20th of the following month.</p></div>
    <div class="sub-card"><b>Every quarter</b><p>Form 941, DETR report and Modified Business Tax: by the last day of the month after the quarter.</p></div>
    <div class="sub-card destacado"><b>Every year</b><p>Form 940, W-2s, W-3 and 1099-NECs by January 31.</p></div>
  </div>
  <div class="sub-legal">
    <p>Due dates, rates and requirements are set by the IRS, the Nevada Department of Employment, Training and Rehabilitation (DETR) and the Nevada Department of Taxation, and may change. We confirm them for each business when we start.</p>
  </div>
</div></section'''+'''>'''))

# Páginas viejas de Elementor → destino (301). Las de seguros van a los cotizadores de Farmers con el código de agente.
FQ = 'https://esales.farmers.com/fastquote?Lob={}&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032'
REDIR = {
    'insurance': '/#personal', 'insurance-2': FQ.format('autoHome'), 'vehicle-insurance': FQ.format('Auto'),
    'home-insurance': FQ.format('Home'), 'life': FQ.format('Lifec'), 'business-insurance-2': FQ.format('Business'),
    'health': '/obamacare-nevada/', 'travel': '/#personal', 'personal': '/#personal', 'business': '/#negocios',
    'taxes': '/#irs', 'taxes-2': '/#irs', 'business-taxes': '/#negocios', 'business-licenses': '/#negocios',
    'about-us': '/#nosotros', 'contact': '/#contacto', 'blog': '/', 'immigration': '/', 'payroll': '/contabilidad-y-nomina/',
    'dmv': '/#dmv', 'translations': '/#dmv', 'notary': '/#contacto', 'media': 'https://marrerobernalmedia.com/',
    # Artículos del blog viejo (2023), enviados a la papelera el 6-nov-2026 por orden de Eliam
    'do-you-want-to-avoid-paying-taxes-today-on-your-first-61000-per-year': '/#irs',
    'the-advance-of-the-child-tax-credit-a-double-edged-weapon': '/#irs',
    'new-taxes-when-using-services-like-zelle-venmo-and-cash-app': '/#irs',
    'what-you-need-to-know-when-buying-health-insurance': '/obamacare-nevada/',
    'when-can-i-apply-for-affordable-health-insurance': '/obamacare-nevada/',
    'full-cover-is-never-full-cover': '/#personal',
    'do-i-have-the-correct-auto-insurance': '/#personal',
    'what-business-insurances-do-i-need': '/#negocios',
    'how-to-start-your-own-business': '/#negocios',
    'i-have-an-idea': '/#negocios',
    'who-do-you-work-for': '/',
    'growing-your-money-tree': '/',
    'compound-interest-the-mary-poppins-way': '/',
    'you-can-avoid-paying-taxes': '/#irs',
    'new-tax-changes-for-2021': '/#irs',
    'income': '/#irs',
    'earned-or-not-that-is-the-question': '/#irs',
    'nothing-is-certain-except-death-and-taxes': '/#irs',
    'fun-fun-and-more-fun': '/',
    'to-each-his-own': '/',
    'if-its-about-spending-less': '/',
    'how-to-pay-bills-and-die-while-doing-it': '/',
    'are-you-saving-for-a-rainy-day': '/',
    'hello-world': '/',
}

# ---------------------------------------------------------------- plantillas
for key, pair in P.items():
    for lang, d in pair.items():
        other = pair['en' if lang == 'es' else 'es']
        html = d['html'].replace('src="IMG"', 'src="<?php echo esc_url(get_theme_file_uri(\'img/' + d['img'] + '\')); ?>"')
        hdr = "get_header('en')" if lang == 'en' else 'get_header()'
        ftr = "get_footer('en')" if lang == 'en' else 'get_footer()'
        php = f"""<?php /* {key} ({lang}) — GENERADO por tools/build_mba_paginas.py */
ob_start(); {hdr}; echo mba_pag_fix(ob_get_clean(), '{lang}', '{d['slug']}', '{other['slug']}'); ?>
<main class="subpage">{html}
</main>
<?php ob_start(); {ftr}; echo mba_pag_fix(ob_get_clean(), '{lang}', '{d['slug']}', '{other['slug']}'); ?>
"""
        (out / 'paginas' / f"{key}-{lang}.php").write_text(php)

routes = {}
for key, pair in P.items():
    routes[pair['es']['slug'] + '|es'] = dict(file=f'{key}-es', title=pair['es']['title'], desc=pair['es']['desc'], img=pair['es']['img'], pair='/en/' + pair['en']['slug'] + '/', self='/' + pair['es']['slug'] + '/')
    routes[pair['en']['slug'] + '|en'] = dict(file=f'{key}-en', title=pair['en']['title'], desc=pair['en']['desc'], img=pair['en']['img'], pair='/' + pair['es']['slug'] + '/', self='/en/' + pair['en']['slug'] + '/')

J = lambda o: json.dumps(o, ensure_ascii=False)
import hashlib
RWV = hashlib.md5(','.join(sorted(routes)).encode()).hexdigest()[:8]  # cambia sola cuando hay rutas nuevas → vuelve a generar las reglas de WP
php = """<?php
/** Páginas propias (Medicare, Obamacare, Medicaid, dispositivos) y redirecciones de páginas viejas.
 *  GENERADO por tools/build_mba_paginas.py — no editar a mano. */
if (!defined('ABSPATH')) exit;

function mba_pag_routes() { static $r = null; if ($r === null) $r = json_decode(""" + "'" + J(routes).replace("\\", "\\\\").replace("'", "\\'") + "'" + """, true); return $r; }
function mba_pag() { $s = get_query_var('mba_pag'); if (!$s) return null; $k = $s . '|' . (get_query_var('mba_pl') ?: 'es'); $r = mba_pag_routes(); return isset($r[$k]) ? $r[$k] + ['lang' => get_query_var('mba_pl') ?: 'es'] : null; }

add_filter('query_vars', function ($v) { $v[] = 'mba_pag'; $v[] = 'mba_pl'; return $v; });
add_action('init', function () {
  foreach (mba_pag_routes() as $k => $r) {
    [$slug, $lang] = explode('|', $k);
    $re = ($lang === 'en' ? '^en/' : '^') . preg_quote($slug, '#') . '/?$';
    add_rewrite_rule($re, 'index.php?mba_pag=' . $slug . '&mba_pl=' . $lang, 'top');
  }
  if (get_option('mba_pag_rw') !== '""" + RWV + """') { flush_rewrite_rules(false); update_option('mba_pag_rw', '""" + RWV + """'); }
});
add_filter('redirect_canonical', fn($r) => mba_pag() ? false : $r);
add_action('wp', function () { global $wp_query; if (mba_pag()) { $wp_query->is_404 = false; $wp_query->is_home = false; status_header(200); remove_action('wp_head', 'rel_canonical'); } });
add_filter('template_include', function ($t) { $p = mba_pag(); if ($p) { $f = get_theme_file_path('paginas/' . $p['file'] . '.php'); if (file_exists($f)) return $f; } return $t; }, 1001);
add_filter('pre_get_document_title', function ($t) { $p = mba_pag(); return $p ? $p['title'] : $t; }, 30);
add_filter('language_attributes', function ($a) { $p = mba_pag(); return $p ? 'lang="' . $p['lang'] . '"' : $a; }, 30);
add_filter('body_class', function ($c) { $p = mba_pag(); if ($p) { $c[] = 'subpagina'; if ($p['lang'] === 'en') $c[] = 'lang-en'; } return $c; });
add_action('wp_head', function () {
  $p = mba_pag(); if (!$p) return;
  $self = home_url($p['self']); $pair = home_url($p['pair']);
  [$es, $en] = $p['lang'] === 'es' ? [$self, $pair] : [$pair, $self];
  echo '<meta name="description" content="' . esc_attr($p['desc']) . '"><link rel="canonical" href="' . esc_url($self) . '">'
    . '<link rel="alternate" hreflang="es" href="' . esc_url($es) . '"><link rel="alternate" hreflang="en" href="' . esc_url($en) . '"><link rel="alternate" hreflang="x-default" href="' . esc_url($es) . '">'
    . '<meta property="og:type" content="website"><meta property="og:site_name" content="Marrero Bernal & Associates"><meta property="og:locale" content="' . ($p['lang'] === 'en' ? 'en_US' : 'es_US') . '">'
    . '<meta property="og:url" content="' . esc_url($self) . '"><meta property="og:title" content="' . esc_attr($p['title']) . '"><meta property="og:description" content="' . esc_attr($p['desc']) . '">'
    . '<meta property="og:image" content="' . esc_url(get_theme_file_uri('img/' . $p['img'])) . '"><meta name="twitter:card" content="summary_large_image">' . "\\n";
}, 5);

/** Cabecera y pie dentro de una subpágina: las anclas (#personal…) vuelven a la portada del idioma y las banderas llevan a la página par. */
function mba_pag_fix($h, $lang, $self, $other) {
  $home = $lang === 'en' ? home_url('/en/') : home_url('/');
  $h = preg_replace('/href="#(?!")/', 'href="' . esc_url($home) . '#', $h);
  if ($lang === 'en') $h = str_replace('<a class="logo" href="' . esc_url(home_url('/')) . '"', '<a class="logo" href="' . esc_url($home) . '"', $h);
  $es = $lang === 'es' ? home_url('/' . $self . '/') : home_url('/' . $other . '/');
  $en = $lang === 'en' ? home_url('/en/' . $self . '/') : home_url('/en/' . $other . '/');
  $h = preg_replace('/href="[^"]*"(\\s+hreflang="es")/', 'href="' . esc_url($es) . '"$1', $h);
  $h = preg_replace('/href="[^"]*"(\\s+hreflang="en")/', 'href="' . esc_url($en) . '"$1', $h);
  return $h;
}

/** Páginas viejas del sitio de Elementor → 301 a su destino actual (no se borra nada en WordPress). */
add_action('template_redirect', function () {
  $map = json_decode(""" + "'" + J(REDIR).replace("\\", "\\\\").replace("'", "\\'") + "'" + """, true);
  $path = trim(parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH) ?? '', '/');
  if (!isset($map[$path]) && preg_match('#^\\d{4}/\\d{2}/\\d{2}/([^/]+)$#', $path, $mm)) $path = $mm[1];
  if (isset($map[$path])) { $to = $map[$path]; if ($to[0] === '/') $to = home_url($to); wp_redirect($to, 301, 'Marrero Bernal & Associates'); exit; }
}, 1);
/** …y salen del sitemap. */
add_filter('wp_sitemaps_posts_query_args', function ($a, $type) {
  if ($type !== 'page') return $a;
  $ids = [];
  foreach (array_keys(json_decode(""" + "'" + J(REDIR).replace("\\", "\\\\").replace("'", "\\'") + "'" + """, true)) as $s) { $pg = get_page_by_path($s); if ($pg) $ids[] = $pg->ID; }
  $a['post__not_in'] = array_merge($a['post__not_in'] ?? [], $ids); return $a;
}, 10, 2);
add_action('init', function () {
  if (!function_exists('wp_register_sitemap_provider')) return;
  wp_register_sitemap_provider('paginas', new class extends WP_Sitemaps_Provider {
    public function __construct() { $this->name = 'paginas'; $this->object_type = 'paginas'; }
    public function get_url_list($page_num, $subtype = '') { return array_map(fn($r) => ['loc' => home_url($r['self'])], array_values(mba_pag_routes())); }
    public function get_max_num_pages($subtype = '') { return 1; }
  });
});
"""
(out / 'paginas.php').write_text(php)

# CSS de las subpáginas (se añade al final de style.css)
CSS = '''
/* ---- subpáginas (build_mba_paginas.py) ---- */
.subpage .sub-hero{background:var(--cream);padding:56px 0}.subpage .sub-hero.med{background:var(--navy);color:#fff}.subpage .sub-hero .wrap{display:grid;grid-template-columns:1.1fr 1fr;gap:44px;align-items:center}
@media(max-width:900px){.subpage .sub-hero .wrap{grid-template-columns:1fr}}
.subpage h1{font-family:Fraunces,serif;font-size:clamp(30px,4.4vw,48px);line-height:1.08;margin:8px 0 16px;text-wrap:balance}
.subpage .sub-hero .mimg{margin:0}.subpage .sub-cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}.subpage .sub-hero.med .btn-ghost{background:transparent;color:#fff;border-color:#4a5a75}
.subpage .sub{padding:50px 0 70px}.subpage .sub .wrap{max-width:900px}.subpage .sub h2{font-family:Fraunces,serif;font-size:28px;margin:40px 0 14px}.subpage .sub p{line-height:1.65;font-size:16px}
.sub-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin:18px 0}
.sub-card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 20px}.sub-card b{display:block;font-size:17px;margin-bottom:6px}.sub-card p{margin:0;font-size:15px!important;color:var(--mut)}
.sub-card .precio{font-family:Fraunces,serif;font-size:34px;font-weight:700;color:var(--navy);margin:2px 0 8px}.sub-card .precio small{font-size:15px;color:var(--mut);font-family:Inter,sans-serif}
.sub-card.destacado{border:2px solid var(--acc)}
.sub-list{padding-left:20px;display:grid;gap:8px;line-height:1.55}.sub-steps{padding-left:20px;display:grid;gap:10px;line-height:1.55}
.sub-alert{background:#fff6e2;border:1px solid #f0d699;border-radius:14px;padding:16px 18px;margin:8px 0 18px;line-height:1.55}
.sub-nota{font-size:13px!important;color:var(--mut)}
.sub-legal{margin-top:40px;padding-top:20px;border-top:1px solid var(--line)}.sub-legal p{font-size:13px!important;color:var(--mut);line-height:1.55}
'''
st = (out / 'style.css').read_text()
st = st.split('/* ---- subpáginas (build_mba_paginas.py) ---- */')[0].rstrip() + '\n' + CSS
(out / 'style.css').write_text(st)

# Portada en inglés: los enlaces a subpáginas apuntan a /en/…
slugmap = {'/' + P[k]['es']['slug'] + '/': '/en/' + P[k]['en']['slug'] + '/' for k in P}
for f in ('front-page-en.php', 'footer-en.php', 'header-en.php'):
    fp = out / f
    if fp.exists():
        t = fp.read_text()
        for a, b in slugmap.items(): t = t.replace(f'href="{a}"', f'href="{b}"')
        fp.write_text(t)

# functions.php carga paginas.php
fn = (out / 'functions.php').read_text()
if "paginas.php" not in fn:
    fn = fn.rstrip() + "\nrequire_once __DIR__ . '/paginas.php';\n"
    (out / 'functions.php').write_text(fn)
print('páginas generadas:', ', '.join(sorted(r['self'] for r in routes.values())))
