#!/usr/bin/env python3
"""Páginas propias de marrerobernal.com (Medicare, Obamacare/Nevada Health Link, Medicaid de Nevada,
protección de dispositivos) en español e inglés, y redirecciones 301 de las páginas viejas de Elementor.
Lo llama tools/build_mba_theme.py al final; también se puede correr solo: python3 tools/build_mba_paginas.py
Escribe themes/mba/paginas.php, themes/mba/paginas/*.php y añade CSS al final de themes/mba/style.css."""
import json, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
out = root / 'themes/mba'
(out / 'paginas').mkdir(parents=True, exist_ok=True)

TEL = '<a href="tel:+18888772583">888-877-2583</a>'
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
    <div class="sub-cta"><a class="btn btn-acc" href="tel:+18888772583">Llamar al 888-877-2583</a><a class="btn btn-ghost" href="#contacto">Revisar mi plan</a></div>
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
    <div class="sub-cta"><a class="btn btn-acc" href="tel:+18888772583">Call 888-877-2583</a><a class="btn btn-ghost" href="#contacto">Review my plan</a></div>
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
    <div class="sub-cta"><a class="btn btn-acc" href="tel:+18888772583">Llamar al 888-877-2583</a><a class="btn btn-ghost" href="#contacto">Quiero que me llamen</a></div>
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
    <div class="sub-cta"><a class="btn btn-acc" href="tel:+18888772583">Call 888-877-2583</a><a class="btn btn-ghost" href="#contacto">Have us call me</a></div>
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
    <div class="sub-cta"><a class="btn btn-acc" href="https://accessnevada.nv.gov/public/landing-page" target="_blank" rel="noopener">Ir a Access Nevada</a><a class="btn btn-ghost" href="tel:+18888772583">Tengo una pregunta</a></div>
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
    <div class="sub-cta"><a class="btn btn-acc" href="https://accessnevada.nv.gov/public/landing-page" target="_blank" rel="noopener">Go to Access Nevada</a><a class="btn btn-ghost" href="tel:+18888772583">I have a question</a></div>
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
    <div class="sub-cta"><a class="btn btn-acc" href="{FARMERS_DEV}" target="_blank" rel="noopener">Ver planes e inscribirme</a><a class="btn btn-ghost" href="tel:+18888772583">Llamar al 888-877-2583</a></div>
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
    <div class="sub-cta"><a class="btn btn-acc" href="{FARMERS_DEV}" target="_blank" rel="noopener">See plans and enroll</a><a class="btn btn-ghost" href="tel:+18888772583">Call 888-877-2583</a></div>
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
    <div class="sub-cta"><a class="btn btn-acc" href="/#contacto">Pide una consulta</a><a class="btn btn-ghost" href="tel:+18888772583">Llamar al 888-877-2583</a></div>
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
    <div class="sub-cta"><a class="btn btn-acc" href="/en/#contacto">Request a consultation</a><a class="btn btn-ghost" href="tel:+18888772583">Call 888-877-2583</a></div>
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

# ---------------------------------------------------------------- páginas por servicio (auto, casa, taxes, ITIN, traducciones, notary)
# Solo datos que ya están en el sitio o en el formulario de solicitud, más los requisitos públicos del estado o del IRS.
def _pag(lang, kicker, h1, lead, ctas, alt, cuerpo, faq, legal, med=False):
    es = lang == 'es'
    b = ''.join(f'<a class="btn {c}" href="{h}">{t}</a>' for c, h, t in ctas)
    q = ''.join(f'\n  <details class="sub-faq"><summary>{a}</summary><p>{r}</p></details>' for a, r in faq)
    lg = ''.join(f'\n    <p>{x}</p>' for x in legal)
    return f'''
<section class="sub-hero"><div class="wrap">
  <div>
    <div class="kicker">{kicker}</div>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="sub-cta">{b}</div>
  </div>
  <img class="mimg" src="IMG" alt="{alt}" width="1280" height="720">
</div></section>
<section class="sub"><div class="wrap">{cuerpo}
  <h2>{'Preguntas frecuentes' if es else 'Frequently asked questions'}</h2>{q}
  <div class="sub-legal">{lg}
  </div>
</div></section>'''

_TEL = ('btn-ghost', 'tel:+18888772583', 'Llamar al 888-877-2583')
_TELEN = ('btn-ghost', 'tel:+18888772583', 'Call 888-877-2583')
_LEGSEG = 'Marrero Bernal &amp; Associates es una agencia de seguros independiente con licencia en Nevada, California y Arizona. Los seguros se ofrecen a través de las compañías con las que la agencia mantiene contrato; cada póliza la emite la compañía correspondiente. La disponibilidad de coberturas varía por compañía y por estado.'
_LEGSEGEN = 'Marrero Bernal &amp; Associates is an independent insurance agency licensed in Nevada, California and Arizona. Insurance is offered through the companies the agency is contracted with; each policy is issued by the corresponding company. Coverage availability varies by company and state.'
_LEGTAX = 'No somos abogados y no ofrecemos asesoría legal. Las fechas y los requisitos los fija el IRS y pueden cambiar.'
_LEGTAXEN = 'We are not attorneys and do not give legal advice. Dates and requirements are set by the IRS and may change.'

def _faqs(faq): return [[re.sub(r'<[^>]+>', '', a), re.sub(r'<[^>]+>', '', r)] for a, r in faq]

# ---- auto
_fa = [('¿Cuánto cuesta la cotización?', 'Nada. La cotización no tiene costo ni compromiso.'),
       ('¿Con qué compañías cotizan el auto?', 'Con Farmers, Progressive, Travelers, Liberty Mutual, Mercury, National General y Bristol West. Te mostramos las opciones y tú decides.'),
       ('Mi licencia es de otro país o todavía no tengo licencia. ¿Puedo pedir la cotización?', 'Sí. En la solicitud nos dices de dónde es tu licencia y el especialista revisa qué compañías aplican a tu caso.'),
       ('¿Atienden fuera de Nevada?', 'Tenemos licencia de seguros en Nevada, California y Arizona.'),
       ('¿Y después de comprar la póliza?', 'Seguimos contigo: reclamos, renovaciones, cambios y preguntas, en la misma oficina y con la misma gente.')]
_faen = [('How much does the quote cost?', 'Nothing. The quote is free, with no obligation.'),
       ('Which companies do you quote auto with?', 'Farmers, Progressive, Travelers, Liberty Mutual, Mercury, National General and Bristol West. We show you the options and you decide.'),
       ('My license is from another country, or I do not have one yet. Can I request a quote?', 'Yes. In the request you tell us where your license is from and the specialist checks which companies fit your case.'),
       ('Do you serve clients outside Nevada?', 'We hold insurance licenses in Nevada, California and Arizona.'),
       ('What about after I buy the policy?', 'We stay with you: claims, renewals, changes and questions, at the same office with the same people.')]
P['auto'] = dict(
    es=dict(slug='seguro-de-auto', img='familia.jpg', faq=_faqs(_fa),
        title='Seguro de auto en Las Vegas con varias compañías · Marrero Bernal & Associates',
        desc='Cotiza tu seguro de auto en español con Farmers, Progressive, Travelers, Liberty Mutual, Mercury, National General y Bristol West. Qué exige Nevada y qué tener a mano. Cotización sin costo.',
        html=_pag('es', 'Seguros personales · Auto', 'Seguro de auto con varias compañías, explicado en español.',
            'Somos una agencia independiente: cotizamos tu auto con varias compañías de primer nivel y te mostramos las opciones para que escojas. La cotización no cuesta y la pides en cinco minutos.',
            [('btn-acc', '/solicitud/?serv=auto', 'Cotizar mi auto'), _TEL], 'Familia frente a su casa en Las Vegas con su auto en la entrada', '''
  <div class="sub-grid">
    <div class="sub-card"><b>7 compañías</b><p>Farmers, Progressive, Travelers, Liberty Mutual, Mercury, National General y Bristol West.</p></div>
    <div class="sub-card"><b>Paquetes</b><p>Auto + casa o auto + renters en una sola cotización.</p></div>
    <div class="sub-card"><b>Más que autos</b><p>Motocicleta, RV, bote y jet ski, ATV, autos clásicos y seguro para manejar en México.</p></div>
    <div class="sub-card"><b>NV · CA · AZ</b><p>Licencia de seguros en Nevada, California y Arizona.</p></div>
  </div>
  <h2>Lo mínimo que exige Nevada</h2>
  <p>Para manejar en Nevada la ley exige seguro de responsabilidad civil con estos mínimos: <b>$25,000</b> por persona lesionada, <b>$50,000</b> por accidente y <b>$20,000</b> por daños a la propiedad de otros. Ese seguro paga los daños que tú causas a los demás; no paga tu carro.</p>
  <p>Lo que la gente llama «full cover» añade colisión y comprensivo, que sí cubren tu vehículo. Si el carro está financiado o arrendado, el banco normalmente lo exige. En la solicitud puedes pedir la mínima, la completa, o decirnos que te aconsejemos.</p>
  <h2>Ten esto a mano</h2>
  <ul class="sub-list">
    <li>Año, marca y modelo de cada vehículo, y el VIN si lo tienes.</li>
    <li>Si está financiado, arrendado o pagado, para qué lo usas y las millas que haces al año.</li>
    <li>Nombre, fecha de nacimiento y licencia de cada conductor de la casa.</li>
    <li>Accidentes o multas de los últimos 3 años.</li>
    <li>Tu seguro actual, si tienes: la compañía y cuándo vence.</li>
  </ul>
  <h2>Cómo trabajamos</h2>
  <ol class="sub-steps">
    <li><b>Nos cuentas.</b> Llenas la solicitud en línea, llamas, escribes por WhatsApp o vienes a la oficina.</li>
    <li><b>Cotizamos.</b> Un especialista revisa tu caso con varias compañías.</li>
    <li><b>Tú decides.</b> Te explicamos cada opción en tu idioma, sin letra pequeña.</li>
    <li><b>Seguimos ahí.</b> Reclamos, renovaciones y cambios, con la misma gente.</li>
  </ol>''', _fa, [_LEGSEG, 'Los mínimos de responsabilidad civil los fija el estado de Nevada y pueden cambiar.'])),
    en=dict(slug='auto-insurance', img='familia.jpg', faq=_faqs(_faen),
        title='Auto insurance in Las Vegas with several companies · Marrero Bernal & Associates',
        desc='Get your auto insurance quote in English or Spanish with Farmers, Progressive, Travelers, Liberty Mutual, Mercury, National General and Bristol West. What Nevada requires and what to have ready. Free quote.',
        html=_pag('en', 'Personal insurance · Auto', 'Auto insurance with several companies, explained clearly.',
            'We are an independent agency: we quote your auto with several top companies and show you the options so you can choose. The quote is free and takes five minutes to request.',
            [('btn-acc', '/en/request/?serv=auto', 'Quote my auto'), _TELEN], 'Family in front of their Las Vegas home with their car in the driveway', '''
  <div class="sub-grid">
    <div class="sub-card"><b>7 companies</b><p>Farmers, Progressive, Travelers, Liberty Mutual, Mercury, National General and Bristol West.</p></div>
    <div class="sub-card"><b>Bundles</b><p>Auto + home or auto + renters in a single quote.</p></div>
    <div class="sub-card"><b>More than cars</b><p>Motorcycle, RV, boat and jet ski, ATV, classic cars and insurance to drive in Mexico.</p></div>
    <div class="sub-card"><b>NV · CA · AZ</b><p>Insurance licenses in Nevada, California and Arizona.</p></div>
  </div>
  <h2>The minimum Nevada requires</h2>
  <p>To drive in Nevada the law requires liability insurance with these minimums: <b>$25,000</b> per injured person, <b>$50,000</b> per accident and <b>$20,000</b> for damage to other people's property. That insurance pays for the damage you cause to others; it does not pay for your car.</p>
  <p>What people call “full coverage” adds collision and comprehensive, which do cover your vehicle. If the car is financed or leased, the lender usually requires it. In the request you can ask for the minimum, full coverage, or tell us to advise you.</p>
  <h2>Have this ready</h2>
  <ul class="sub-list">
    <li>Year, make and model of each vehicle, and the VIN if you have it.</li>
    <li>Whether it is financed, leased or paid off, how you use it and the miles you drive per year.</li>
    <li>Name, date of birth and license of each driver in the household.</li>
    <li>Accidents or tickets in the last 3 years.</li>
    <li>Your current insurance, if any: the company and when it expires.</li>
  </ul>
  <h2>How we work</h2>
  <ol class="sub-steps">
    <li><b>You tell us.</b> Fill out the online request, call, WhatsApp us or come to the office.</li>
    <li><b>We quote.</b> A specialist reviews your case with several companies.</li>
    <li><b>You decide.</b> We explain each option in your language, with no fine print.</li>
    <li><b>We stay with you.</b> Claims, renewals and changes, with the same people.</li>
  </ol>''', _faen, [_LEGSEGEN, 'Liability minimums are set by the State of Nevada and may change.'])))

# ---- casa
_fc = [('¿Con qué compañías cotizan la casa?', 'Con Farmers, Foremost, Progressive, Mercury, National General, Homeowners of America y Lemonade.'),
       ('Estoy comprando una casa. ¿Cuándo pido el seguro?', 'Apenas tengas la dirección y la fecha de cierre. Ponlas en la solicitud para tener la póliza lista a tiempo; el banco suele pedir la prueba de seguro antes del cierre.'),
       ('¿El seguro de casa cubre inundación y terremoto?', 'Normalmente no: son seguros aparte. Los cotizamos también; pídelos en la solicitud, en «Otros seguros».'),
       ('Rento donde vivo. ¿Qué seguro me toca?', 'El de renters, que cubre tus pertenencias. En la solicitud nos dices qué tipo de vivienda es y el valor aproximado de tus cosas.'),
       ('Tengo una propiedad que rento a otros. ¿La pueden asegurar?', 'Sí, con un seguro de landlord. Dinos en la solicitud que la rentas a otros.')]
_fcen = [('Which companies do you quote home insurance with?', 'Farmers, Foremost, Progressive, Mercury, National General, Homeowners of America and Lemonade.'),
       ('I am buying a house. When should I request the insurance?', 'As soon as you have the address and the closing date. Put them in the request so the policy is ready on time; the lender usually asks for proof of insurance before closing.'),
       ('Does home insurance cover flood and earthquake?', 'Usually not: those are separate policies. We quote them too; ask for them in the request under “Other insurance”.'),
       ('I rent where I live. Which insurance do I need?', 'Renters insurance, which covers your belongings. In the request you tell us the type of home and the approximate value of your things.'),
       ('I own a property I rent out. Can you insure it?', 'Yes, with landlord insurance. Tell us in the request that you rent it out.')]
P['casa'] = dict(
    es=dict(slug='seguro-de-casa', img='familia.jpg', faq=_faqs(_fc),
        title='Seguro de casa, condominio y renters en Las Vegas · Marrero Bernal & Associates',
        desc='Cotiza en español tu seguro de casa, condominio, casa móvil, renters o landlord con Farmers, Foremost, Progressive, Mercury, National General, Homeowners of America y Lemonade. Cotización sin costo.',
        html=_pag('es', 'Seguros personales · Casa', 'Seguro de casa, condominio y renters, con varias compañías.',
            'Seas dueño o rentes, cotizamos tu vivienda con varias compañías de primer nivel y te explicamos en español qué cubre cada opción. Si estás comprando casa, la dejamos lista para el cierre.',
            [('btn-acc', '/solicitud/?serv=casa', 'Cotizar mi casa'), ('btn-ghost', '/solicitud/?serv=renters', 'Cotizar renters')], 'Familia frente a su casa en Las Vegas', '''
  <div class="sub-grid">
    <div class="sub-card"><b>7 compañías</b><p>Farmers, Foremost, Progressive, Mercury, National General, Homeowners of America y Lemonade.</p></div>
    <div class="sub-card"><b>Dueños</b><p>Casa, condominio, townhouse, casa móvil y casa de vacaciones.</p></div>
    <div class="sub-card"><b>Renters y landlord</b><p>Para quien renta donde vive y para quien renta su propiedad a otros.</p></div>
    <div class="sub-card"><b>Aparte</b><p>Inundación, terremoto y umbrella se cotizan como seguros separados.</p></div>
  </div>
  <h2>Ten esto a mano</h2>
  <ul class="sub-list">
    <li>La dirección de la propiedad y qué tipo es: casa, condominio, townhouse o casa móvil.</li>
    <li>Año de construcción, pies cuadrados y año del techo.</li>
    <li>Si tiene hipoteca; y si la estás comprando, la fecha de cierre.</li>
    <li>Si hay piscina, trampolín, perros (la raza), alarma o cámaras.</li>
    <li>Reclamos de los últimos 5 años y tu seguro actual, si tienes.</li>
  </ul>
  <h2>Junta la casa con el auto</h2>
  <p>Puedes pedir el paquete de auto + casa o auto + renters en la misma solicitud, y el especialista los cotiza juntos. <a href="/seguro-de-auto/">Ver seguro de auto →</a></p>
  <h2>Cómo trabajamos</h2>
  <ol class="sub-steps">
    <li><b>Nos cuentas.</b> Llenas la solicitud en línea, llamas, escribes por WhatsApp o vienes a la oficina.</li>
    <li><b>Cotizamos.</b> Un especialista revisa tu caso con varias compañías.</li>
    <li><b>Tú decides.</b> Te explicamos cada opción en tu idioma.</li>
    <li><b>Seguimos ahí.</b> Reclamos, renovaciones y cambios, con la misma gente.</li>
  </ol>''', _fc, [_LEGSEG])),
    en=dict(slug='home-insurance', img='familia.jpg', faq=_faqs(_fcen),
        title='Home, condo and renters insurance in Las Vegas · Marrero Bernal & Associates',
        desc='Get a quote in English or Spanish for home, condo, mobile home, renters or landlord insurance with Farmers, Foremost, Progressive, Mercury, National General, Homeowners of America and Lemonade. Free quote.',
        html=_pag('en', 'Personal insurance · Home', 'Home, condo and renters insurance, with several companies.',
            'Whether you own or rent, we quote your home with several top companies and explain what each option covers. If you are buying a house, we have it ready for closing.',
            [('btn-acc', '/en/request/?serv=casa', 'Quote my home'), ('btn-ghost', '/en/request/?serv=renters', 'Quote renters')], 'Family in front of their Las Vegas home', '''
  <div class="sub-grid">
    <div class="sub-card"><b>7 companies</b><p>Farmers, Foremost, Progressive, Mercury, National General, Homeowners of America and Lemonade.</p></div>
    <div class="sub-card"><b>Owners</b><p>House, condo, townhouse, mobile home and vacation home.</p></div>
    <div class="sub-card"><b>Renters and landlord</b><p>For those who rent where they live and those who rent their property to others.</p></div>
    <div class="sub-card"><b>Separate</b><p>Flood, earthquake and umbrella are quoted as separate policies.</p></div>
  </div>
  <h2>Have this ready</h2>
  <ul class="sub-list">
    <li>The property address and its type: house, condo, townhouse or mobile home.</li>
    <li>Year built, square feet and roof year.</li>
    <li>Whether there is a mortgage; and if you are buying it, the closing date.</li>
    <li>Whether there is a pool, trampoline, dogs (the breed), an alarm or cameras.</li>
    <li>Claims in the last 5 years and your current insurance, if any.</li>
  </ul>
  <h2>Bundle home and auto</h2>
  <p>You can request the auto + home or auto + renters bundle in the same request, and the specialist quotes them together. <a href="/en/auto-insurance/">See auto insurance →</a></p>
  <h2>How we work</h2>
  <ol class="sub-steps">
    <li><b>You tell us.</b> Fill out the online request, call, WhatsApp us or come to the office.</li>
    <li><b>We quote.</b> A specialist reviews your case with several companies.</li>
    <li><b>You decide.</b> We explain each option in your language.</li>
    <li><b>We stay with you.</b> Claims, renewals and changes, with the same people.</li>
  </ol>''', _fcen, [_LEGSEGEN])))

# ---- taxes
_PORTAL = 'https://marrerobernal.securefilepro.com/portal/#/login'
_ft = [('¿Tengo que vivir en Nevada?', 'No. Preparamos los taxes de clientes en cualquier estado de EE. UU. y de estadounidenses que viven en otros países.'),
       ('¿Cómo les mando mis documentos?', 'Por el portal seguro de clientes o por correo a la oficina: 3455 W Craig Rd Ste D, North Las Vegas, NV 89032. También puedes traerlos en persona.'),
       ('¿Qué pasa si el IRS me manda una carta?', 'Tu declaración va protegida con Protection Plus, por escrito: hasta $1,000,000 en servicios de defensa si recibes una carta, una auditoría o una consulta del IRS o del estado.'),
       ('No tengo Seguro Social. ¿Puedo declarar?', 'Sí, con un número ITIN. Contamos con Agentes de Aceptación Certificados del IRS para solicitarlo, y también preparamos tu declaración.'),
       ('¿También hacen los taxes de mi negocio?', 'Sí, y además la contabilidad, la nómina y el sales tax.')]
_ften = [('Do I have to live in Nevada?', 'No. We prepare taxes for clients in any U.S. state and for Americans living in other countries.'),
       ('How do I send you my documents?', 'Through the secure client portal or by mail to the office: 3455 W Craig Rd Ste D, North Las Vegas, NV 89032. You can also bring them in person.'),
       ('What if the IRS sends me a letter?', 'Your return is protected with Protection Plus, in writing: up to $1,000,000 in defense services if you receive a letter, an audit or an inquiry from the IRS or the state.'),
       ('I do not have a Social Security number. Can I file?', 'Yes, with an ITIN. We have IRS Certifying Acceptance Agents to apply for it, and we also prepare your return.'),
       ('Do you also do my business taxes?', 'Yes, as well as bookkeeping, payroll and sales tax.')]
P['taxes'] = dict(
    es=dict(slug='taxes', img='tramites.jpg', faq=_faqs(_ft),
        title='Preparación de taxes en español, en la oficina o a distancia · Marrero Bernal & Associates',
        desc='Preparamos tus taxes personales y de negocio en español, en North Las Vegas o a distancia para todo EE. UU. y el extranjero. E-file directo al IRS y protección Protection Plus por escrito.',
        html=_pag('es', 'Impuestos · Taxes', 'Tus taxes, directo al IRS y protegidos por escrito.',
            'Preparamos tu declaración personal o de negocio en español, en la oficina de North Las Vegas o a distancia, vivas donde vivas. Somos proveedor autorizado de e-file del IRS: la transmitimos nosotros, sin intermediarios.',
            [('btn-acc', '/solicitud/?serv=taxes', 'Empezar mis taxes'), ('btn-ghost', _PORTAL, 'Subir mis documentos')], 'Persona firmando documentos de impuestos junto a una laptop y una calculadora', '''
  <div class="sub-grid">
    <div class="sub-card"><b>E-file directo</b><p>Somos proveedor autorizado de e-file del IRS. Tu declaración va de nuestra oficina al IRS.</p></div>
    <div class="sub-card destacado"><b>Protection Plus</b><p>Hasta $1,000,000 en servicios de defensa si recibes una carta, auditoría o consulta del IRS o del estado.</p></div>
    <div class="sub-card"><b>A distancia</b><p>Para clientes en cualquier estado y estadounidenses en el extranjero, por el portal seguro o por correo.</p></div>
    <div class="sub-card"><b>ITIN aquí mismo</b><p>Agentes de Aceptación Certificados del IRS: no mandas tu pasaporte original. <a href="/itin/">Ver ITIN →</a></p></div>
  </div>
  <h2>Qué incluye Protection Plus</h2>
  <ul class="sub-list">
    <li>Evaluación profesional de tu caso y respuesta preparada por expertos.</li>
    <li>Representación ante el IRS o el estado.</li>
    <li>Ayuda para restaurar tu identidad si te la roban.</li>
  </ul>
  <h2>Ten esto a mano</h2>
  <p>En la solicitud te preguntamos lo básico; después te damos una lista corta y clara de los documentos de tu caso.</p>
  <ul class="sub-list">
    <li>El año o los años que vas a declarar.</li>
    <li>Tu estado civil y cuántos dependientes tienes.</li>
    <li>De dónde vienen tus ingresos: empleo (W-2), cuenta propia (1099), negocio, rentas o ingresos del extranjero.</li>
    <li>Si es tu primera vez con nosotros y si necesitas un ITIN.</li>
  </ul>
  <h2>Cómo trabajamos a distancia</h2>
  <ol class="sub-steps">
    <li><b>Nos mandas tus documentos.</b> Por el portal seguro de clientes o por correo a la oficina.</li>
    <li><b>Te explicamos todo.</b> Por teléfono o videollamada, en tu idioma.</li>
    <li><b>Transmitimos.</b> Tu declaración sale directo al IRS.</li>
  </ol>
  <h2>Si tienes un negocio</h2>
  <p>Preparamos la declaración del negocio y llevamos la contabilidad, la nómina y el sales tax durante el año. <a href="/contabilidad-y-nomina/">Ver contabilidad y nómina →</a></p>
  <p>¿Eres preparador de impuestos? Puedes transmitir tus declaraciones al IRS a través de nosotros. <a href="/#contacto">Escríbenos →</a></p>''', _ft, [_LEGTAX, 'Protection Plus es un servicio de terceros; aplican sus términos y condiciones.'])),
    en=dict(slug='taxes', img='tramites.jpg', faq=_faqs(_ften),
        title='Tax preparation in English and Spanish, at the office or remotely · Marrero Bernal & Associates',
        desc='We prepare your personal and business taxes in North Las Vegas or remotely for all of the U.S. and abroad. Direct IRS e-file and Protection Plus coverage in writing.',
        html=_pag('en', 'Taxes', 'Your taxes, straight to the IRS and protected in writing.',
            'We prepare your personal or business return at our North Las Vegas office or remotely, wherever you live. We are an authorized IRS e-file provider: we transmit it ourselves, with no middleman.',
            [('btn-acc', '/en/request/?serv=taxes', 'Start my taxes'), ('btn-ghost', _PORTAL, 'Upload my documents')], 'Person signing tax documents next to a laptop and a calculator', '''
  <div class="sub-grid">
    <div class="sub-card"><b>Direct e-file</b><p>We are an authorized IRS e-file provider. Your return goes from our office to the IRS.</p></div>
    <div class="sub-card destacado"><b>Protection Plus</b><p>Up to $1,000,000 in defense services if you receive a letter, audit or inquiry from the IRS or the state.</p></div>
    <div class="sub-card"><b>Remote</b><p>For clients in any state and Americans abroad, through the secure portal or by mail.</p></div>
    <div class="sub-card"><b>ITIN right here</b><p>IRS Certifying Acceptance Agents: you do not mail your original passport. <a href="/en/itin/">See ITIN →</a></p></div>
  </div>
  <h2>What Protection Plus includes</h2>
  <ul class="sub-list">
    <li>A professional evaluation of your case and a response prepared by experts.</li>
    <li>Representation before the IRS or the state.</li>
    <li>Help restoring your identity if it is stolen.</li>
  </ul>
  <h2>Have this ready</h2>
  <p>The request asks for the basics; afterwards we give you a short, clear list of the documents for your case.</p>
  <ul class="sub-list">
    <li>The tax year or years you are filing.</li>
    <li>Your filing status and how many dependents you have.</li>
    <li>Where your income comes from: a job (W-2), self-employment (1099), a business, rentals or foreign income.</li>
    <li>Whether it is your first time with us and whether you need an ITIN.</li>
  </ul>
  <h2>How we work remotely</h2>
  <ol class="sub-steps">
    <li><b>You send us your documents.</b> Through the secure client portal or by mail to the office.</li>
    <li><b>We explain everything.</b> By phone or video call, in your language.</li>
    <li><b>We transmit.</b> Your return goes straight to the IRS.</li>
  </ol>
  <h2>If you have a business</h2>
  <p>We prepare the business return and keep the books, payroll and sales tax during the year. <a href="/en/bookkeeping-payroll/">See bookkeeping and payroll →</a></p>
  <p>Are you a tax preparer? You can transmit your returns to the IRS through us. <a href="/en/#contacto">Write to us →</a></p>''', _ften, [_LEGTAXEN, 'Protection Plus is a third-party service; its terms and conditions apply.'])))

# ---- ITIN
_fi = [('¿Tengo que mandar mi pasaporte original al IRS?', 'No. Nuestros Agentes de Aceptación Certificados revisan y certifican tus documentos aquí, y los originales no van al IRS.'),
       ('No puedo ir a la oficina. ¿Se puede a distancia?', 'Sí. Nos envías los documentos por correo a la oficina, los certificamos y te los devolvemos.'),
       ('¿Hacen renovaciones?', 'Sí: solicitud nueva o renovación.'),
       ('¿El ITIN me da permiso de trabajo?', 'No. El ITIN es un número del IRS para declarar impuestos; no cambia tu estatus migratorio ni autoriza a trabajar.'),
       ('¿Cuánto tarda en llegar?', 'El tiempo lo pone el IRS y cambia según la época del año. Te acompañamos hasta que llega tu número.')]
_fien = [('Do I have to mail my original passport to the IRS?', 'No. Our Certifying Acceptance Agents review and certify your documents here, and the originals do not go to the IRS.'),
       ('I cannot come to the office. Can it be done remotely?', 'Yes. You mail the documents to our office, we certify them and send them back to you.'),
       ('Do you handle renewals?', 'Yes: new applications and renewals.'),
       ('Does an ITIN give me a work permit?', 'No. An ITIN is an IRS number for filing taxes; it does not change your immigration status or authorize you to work.'),
       ('How long does it take to arrive?', 'The IRS sets the timing and it changes with the time of year. We stay with you until your number arrives.')]
P['itin'] = dict(
    es=dict(slug='itin', img='tramites.jpg', faq=_faqs(_fi),
        title='Número ITIN con Agentes de Aceptación Certificados del IRS · Marrero Bernal & Associates',
        desc='Solicita o renueva tu ITIN en español con Agentes de Aceptación Certificados (CAA) del IRS: certificamos tus documentos en la oficina y no mandas tu pasaporte original. También a distancia.',
        html=_pag('es', 'Impuestos · ITIN', 'Tu ITIN sin mandar el pasaporte original al IRS.',
            'Si pides el ITIN por tu cuenta, tienes que enviar tus documentos originales al IRS por correo, y se pueden perder. Contamos con Agentes de Aceptación Certificados (CAA) del IRS: revisamos y certificamos tus documentos aquí mismo.',
            [('btn-acc', '/solicitud/?serv=itin', 'Solicitar mi ITIN'), _TEL], 'Persona firmando una solicitud junto a una carpeta de trámites', '''
  <div class="sub-grid">
    <div class="sub-card"><b>Tus originales, contigo</b><p>Los certificamos en la oficina. No van al IRS.</p></div>
    <div class="sub-card"><b>Nuevo o renovación</b><p>Hacemos la solicitud nueva y la renovación.</p></div>
    <div class="sub-card"><b>A distancia</b><p>¿No puedes venir? Nos los envías por correo, los certificamos y te los devolvemos.</p></div>
    <div class="sub-card"><b>Hasta el final</b><p>Te acompañamos hasta que llega tu número.</p></div>
  </div>
  <h2>Qué es el ITIN</h2>
  <p>Es el número que da el IRS a quien tiene que declarar impuestos, o aparecer en una declaración, y no puede obtener un número de Seguro Social. Se pide con el formulario W-7, por lo general junto con la declaración de impuestos, que también preparamos. <a href="/taxes/">Ver taxes →</a></p>
  <h2>Ten esto a mano</h2>
  <ul class="sub-list">
    <li>Para cuántas personas es.</li>
    <li>Si es una solicitud nueva o una renovación.</li>
    <li>Si tienes pasaporte vigente. Si no lo tienes, dínoslo y te decimos qué otros documentos sirven.</li>
  </ul>
  <h2>Cómo trabajamos</h2>
  <ol class="sub-steps">
    <li><b>Nos cuentas.</b> Llenas la solicitud en línea, llamas o escribes por WhatsApp.</li>
    <li><b>Te decimos qué traer.</b> Una lista corta y clara para tu caso.</li>
    <li><b>Certificamos tus documentos.</b> En la oficina, o por correo si estás lejos.</li>
    <li><b>Enviamos la solicitud</b> y seguimos contigo hasta que llega el número.</li>
  </ol>''', _fi, [_LEGTAX, 'El IRS decide sobre cada solicitud de ITIN.'])),
    en=dict(slug='itin', img='tramites.jpg', faq=_faqs(_fien),
        title='ITIN with IRS Certifying Acceptance Agents · Marrero Bernal & Associates',
        desc='Apply for or renew your ITIN with IRS Certifying Acceptance Agents (CAA): we certify your documents at the office and you do not mail your original passport. Also available remotely.',
        html=_pag('en', 'Taxes · ITIN', 'Your ITIN without mailing your original passport to the IRS.',
            'If you apply for an ITIN on your own, you have to mail your original documents to the IRS, and they can get lost. We have IRS Certifying Acceptance Agents (CAA): we review and certify your documents right here.',
            [('btn-acc', '/en/request/?serv=itin', 'Apply for my ITIN'), _TELEN], 'Person signing an application next to a folder of paperwork', '''
  <div class="sub-grid">
    <div class="sub-card"><b>Your originals stay with you</b><p>We certify them at the office. They do not go to the IRS.</p></div>
    <div class="sub-card"><b>New or renewal</b><p>We handle new applications and renewals.</p></div>
    <div class="sub-card"><b>Remote</b><p>Cannot come in? Mail them to us, we certify them and send them back.</p></div>
    <div class="sub-card"><b>To the finish</b><p>We stay with you until your number arrives.</p></div>
  </div>
  <h2>What an ITIN is</h2>
  <p>It is the number the IRS issues to people who must file taxes, or be listed on a return, and cannot get a Social Security number. You apply with Form W-7, usually together with your tax return, which we also prepare. <a href="/en/taxes/">See taxes →</a></p>
  <h2>Have this ready</h2>
  <ul class="sub-list">
    <li>How many people it is for.</li>
    <li>Whether it is a new application or a renewal.</li>
    <li>Whether you have a valid passport. If you do not, tell us and we will tell you which other documents work.</li>
  </ul>
  <h2>How we work</h2>
  <ol class="sub-steps">
    <li><b>You tell us.</b> Fill out the online request, call or WhatsApp us.</li>
    <li><b>We tell you what to bring.</b> A short, clear list for your case.</li>
    <li><b>We certify your documents.</b> At the office, or by mail if you are far away.</li>
    <li><b>We submit the application</b> and stay with you until the number arrives.</li>
  </ol>''', _fien, [_LEGTAXEN, 'The IRS decides on each ITIN application.'])))

# ---- traducciones
_DMV = 'https://dmv.nv.gov/translators.htm'
_fr = [('¿El DMV acepta sus traducciones?', 'Sí. Nuestro fundador, Eliam Marrero Bernal, es traductor aprobado por el DMV de Nevada, y cada traducción lleva nuestro número de traductor. Puedes verlo en la lista del sitio del DMV.'),
       ('¿Qué documentos traducen?', 'Actas de nacimiento y de matrimonio, pasaportes, documentos de identidad, licencias de manejo de otros países, diplomas y notas, entre otros.'),
       ('¿Cómo les hago llegar el documento?', 'En la oficina o a distancia. Pide la traducción en línea y te decimos cómo enviarlo.'),
       ('¿Cuánto demora y cuánto cuesta?', 'Depende del documento y del número de páginas. Dinos para qué fecha lo necesitas y te respondemos el mismo día hábil.'),
       ('¿Qué pasa si la traducción no lleva número de traductor?', 'El DMV la rechaza en la oficina. Por eso la nuestra lleva la fecha, la firma, el número de traductor y la certificación en la misma hoja.')]
_fren = [('Does the DMV accept your translations?', 'Yes. Our founder, Eliam Marrero Bernal, is a Nevada DMV-approved translator, and every translation carries our translator number. You can see it on the list on the DMV website.'),
       ('Which documents do you translate?', 'Birth and marriage certificates, passports, identity documents, driver licenses from other countries, diplomas and transcripts, among others.'),
       ('How do I get the document to you?', 'At the office or remotely. Request the translation online and we will tell you how to send it.'),
       ('How long does it take and what does it cost?', 'It depends on the document and the number of pages. Tell us the date you need it by and we will answer the same business day.'),
       ('What if a translation has no translator number?', 'The DMV rejects it at the counter. That is why ours carries the date, the signature, the translator number and the certification on the same page.')]
P['traducciones'] = dict(
    es=dict(slug='traducciones', img='tramites.jpg', faq=_faqs(_fr),
        title='Traducciones para el DMV de Nevada y traducciones certificadas · Marrero Bernal & Associates',
        desc='Traductor aprobado por el DMV de Nevada. Traducimos actas de nacimiento, pasaportes, licencias de otros países y más, con número de traductor y certificación. En la oficina o a distancia.',
        html=_pag('es', 'Trámites · Traducciones', 'Traducciones que el DMV de Nevada sí acepta.',
            'Para sacar la licencia de manejo, la Driver Authorization Card o la tarjeta de identificación en Nevada, el DMV exige que todo documento que no esté en inglés venga traducido por un traductor aprobado. Nuestro fundador, Eliam Marrero Bernal, lo es.',
            [('btn-acc', '/solicitud/?serv=trad', 'Traducir mis documentos'), ('btn-ghost', _DMV, 'Verlo en el sitio del DMV')], 'Persona revisando y firmando documentos sobre un escritorio', '''
  <div class="sub-grid">
    <div class="sub-card"><b>Traductor aprobado</b><p>Y como el DMV no está aceptando nuevos traductores, somos de los pocos que pueden hacerlo.</p></div>
    <div class="sub-card"><b>Como la exige el DMV</b><p>Completa, escrita a máquina, con fecha, firma, número de traductor y certificación en la misma hoja.</p></div>
    <div class="sub-card"><b>Más que el DMV</b><p>Traducciones certificadas para inmigración, corte y otros trámites.</p></div>
    <div class="sub-card"><b>En la oficina o a distancia</b><p>Las Vegas, North Las Vegas, Henderson, Paradise, Pahrump y Moapa Valley / Mesquite.</p></div>
  </div>
  <h2>Qué traducimos</h2>
  <ul class="sub-list">
    <li>Actas de nacimiento y de matrimonio.</li>
    <li>Pasaportes y documentos de identidad.</li>
    <li>Licencias de manejo de otros países.</li>
    <li>Diplomas y notas.</li>
  </ul>
  <h2>Ten esto a mano</h2>
  <ul class="sub-list">
    <li>Qué documento es y cuántas páginas tiene.</li>
    <li>De qué idioma a cuál.</li>
    <li>Para qué lo necesitas: DMV, inmigración, corte u otro trámite.</li>
    <li>Para qué fecha lo necesitas.</li>
  </ul>
  <h2>Si también necesitas notarizar</h2>
  <p>Lo hacemos en la misma oficina. <a href="/notary-public/">Ver el servicio de notary public →</a></p>''', _fr, ['Los requisitos de las traducciones para licencias e identificaciones los fija el DMV de Nevada y pueden cambiar. No somos abogados y no ofrecemos asesoría legal.'])),
    en=dict(slug='translations', img='tramites.jpg', faq=_faqs(_fren),
        title='Nevada DMV translations and certified translations · Marrero Bernal & Associates',
        desc='Nevada DMV-approved translator. We translate birth certificates, passports, foreign driver licenses and more, with translator number and certification. At the office or remotely.',
        html=_pag('en', 'Paperwork · Translations', 'Translations the Nevada DMV accepts.',
            'To get a driver license, a Driver Authorization Card or an ID card in Nevada, the DMV requires every document not in English to be translated by an approved translator. Our founder, Eliam Marrero Bernal, is one.',
            [('btn-acc', '/en/request/?serv=trad', 'Translate my documents'), ('btn-ghost', _DMV, 'See it on the DMV website')], 'Person reviewing and signing documents at a desk', '''
  <div class="sub-grid">
    <div class="sub-card"><b>Approved translator</b><p>And since the DMV is not accepting new translators, we are among the few who can do it.</p></div>
    <div class="sub-card"><b>The way the DMV requires</b><p>Complete, typed, with date, signature, translator number and certification on the same page.</p></div>
    <div class="sub-card"><b>Beyond the DMV</b><p>Certified translations for immigration, court and other paperwork.</p></div>
    <div class="sub-card"><b>At the office or remotely</b><p>Las Vegas, North Las Vegas, Henderson, Paradise, Pahrump and Moapa Valley / Mesquite.</p></div>
  </div>
  <h2>What we translate</h2>
  <ul class="sub-list">
    <li>Birth and marriage certificates.</li>
    <li>Passports and identity documents.</li>
    <li>Driver licenses from other countries.</li>
    <li>Diplomas and transcripts.</li>
  </ul>
  <h2>Have this ready</h2>
  <ul class="sub-list">
    <li>What the document is and how many pages it has.</li>
    <li>From which language to which.</li>
    <li>What you need it for: DMV, immigration, court or other paperwork.</li>
    <li>The date you need it by.</li>
  </ul>
  <h2>If you also need a notarization</h2>
  <p>We do it at the same office. <a href="/en/notary/">See the notary public service →</a></p>''', _fren, ['Translation requirements for licenses and IDs are set by the Nevada DMV and may change. We are not attorneys and do not give legal advice.'])))

# ---- notary public (en el texto en español se dice «notary public» y «notarizar», nunca «notario»)
_fn = [('¿Qué tengo que traer?', 'Una identificación oficial vigente con foto y el documento completo, sin firmar: se firma delante del notary public.'),
       ('¿Tienen que venir todas las personas que firman?', 'Sí. Cada persona que firma tiene que presentarse con su identificación.'),
       ('¿Me pueden explicar o redactar el documento?', 'No. Un notary public que no es abogado no puede dar asesoría legal ni decirte qué documento necesitas. Si tienes dudas legales, consulta a un abogado.'),
       ('¿Necesito cita?', 'Para la mayoría de los trámites no. Si quieres asegurar la hora, agenda tu cita en línea o llámanos.'),
       ('Mi documento está en español. ¿Lo pueden traducir?', 'Sí, hacemos traducciones certificadas en la misma oficina.')]
_fnen = [('What do I need to bring?', 'A valid government-issued photo ID and the complete document, unsigned: you sign it in front of the notary public.'),
       ('Do all the signers have to come?', 'Yes. Each person signing must appear with their ID.'),
       ('Can you explain or draft the document for me?', 'No. A notary public who is not an attorney cannot give legal advice or tell you which document you need. If you have legal questions, consult an attorney.'),
       ('Do I need an appointment?', 'Not for most paperwork. If you want to secure a time, book your appointment online or call us.'),
       ('My document is in Spanish. Can you translate it?', 'Yes, we do certified translations at the same office.')]
_AVISO = '<b>Aviso:</b> No soy abogado en el estado de Nevada. No tengo licencia para dar asesoría legal. No puedo aceptar honorarios por dar asesoría legal.'
_AVISOEN = '<b>Notice:</b> I am not an attorney in the State of Nevada. I am not licensed to give legal advice. I may not accept fees for giving legal advice.'
P['notary'] = dict(
    es=dict(slug='notary-public', img='tramites.jpg', faq=_faqs(_fn),
        title='Notary public en español en North Las Vegas · Marrero Bernal & Associates',
        desc='Notariza tus documentos en español o inglés en nuestra oficina de North Las Vegas. Qué traer, quién tiene que venir y cómo agendar. También traducciones certificadas.',
        html=_pag('es', 'Trámites · Notary public', 'Notariza tus documentos, atendido en español.',
            'Servicio de notary public en nuestra oficina de North Las Vegas, en español e inglés. Y si el documento hay que traducirlo, lo hacemos aquí mismo.',
            [('btn-acc', '/solicitud/?serv=notaria', 'Pedir el servicio'), ('btn-ghost', '/citas/', 'Agendar una cita')], 'Persona firmando un documento sobre un escritorio', f'''
  <div class="sub-alert">{_AVISO}</div>
  <h2>Qué traer</h2>
  <ul class="sub-list">
    <li>Una identificación oficial vigente con foto de cada persona que firma.</li>
    <li>El documento completo y <b>sin firmar</b>: se firma delante del notary public.</li>
    <li>Todas las personas que firman tienen que presentarse.</li>
  </ul>
  <h2>Dinos esto al pedirlo</h2>
  <ul class="sub-list">
    <li>Qué documento es.</li>
    <li>Cuántas firmas lleva.</li>
    <li>Para qué fecha lo necesitas.</li>
  </ul>
  <h2>Dónde y cuándo</h2>
  <p>3455 W Craig Rd, Suite D, North Las Vegas, NV 89032. Lunes a viernes, de 9:00 AM a 5:00 PM. Para la mayoría de los trámites no hace falta cita; si prefieres asegurar la hora, <a href="/citas/">agéndala en línea</a>.</p>
  <h2>Si también necesitas traducir</h2>
  <p>Hacemos traducciones certificadas y traducciones para el DMV de Nevada. <a href="/traducciones/">Ver traducciones →</a></p>''', _fn, ['El notary public verifica la identidad de quien firma y presencia la firma; no revisa ni garantiza el contenido del documento. No somos abogados y no ofrecemos asesoría legal.'])),
    en=dict(slug='notary', img='tramites.jpg', faq=_faqs(_fnen),
        title='Notary public in North Las Vegas, in English and Spanish · Marrero Bernal & Associates',
        desc='Get your documents notarized in English or Spanish at our North Las Vegas office. What to bring, who has to come and how to book. Certified translations too.',
        html=_pag('en', 'Paperwork · Notary public', 'Get your documents notarized, in your language.',
            'Notary public service at our North Las Vegas office, in English and Spanish. And if the document needs to be translated, we do that right here.',
            [('btn-acc', '/en/request/?serv=notaria', 'Request the service'), ('btn-ghost', '/en/appointments/', 'Book an appointment')], 'Person signing a document at a desk', f'''
  <div class="sub-alert">{_AVISOEN}</div>
  <h2>What to bring</h2>
  <ul class="sub-list">
    <li>A valid government-issued photo ID for each person signing.</li>
    <li>The complete document, <b>unsigned</b>: you sign it in front of the notary public.</li>
    <li>Every person signing must appear.</li>
  </ul>
  <h2>Tell us this when you request it</h2>
  <ul class="sub-list">
    <li>What the document is.</li>
    <li>How many signatures it needs.</li>
    <li>The date you need it by.</li>
  </ul>
  <h2>Where and when</h2>
  <p>3455 W Craig Rd, Suite D, North Las Vegas, NV 89032. Monday to Friday, 9:00 AM to 5:00 PM. Most paperwork needs no appointment; if you prefer to secure a time, <a href="/en/appointments/">book it online</a>.</p>
  <h2>If you also need a translation</h2>
  <p>We do certified translations and translations for the Nevada DMV. <a href="/en/translations/">See translations →</a></p>''', _fnen, ['The notary public verifies the identity of the signer and witnesses the signature; it does not review or guarantee the content of the document. We are not attorneys and do not give legal advice.'])))

# ---- vida
_fv = [('¿Qué tipos de seguro de vida cotizan?', 'A término (por un número de años), vida entera y vida universal. Si no sabes cuál te conviene, márcalo en la solicitud y el especialista te aconseja.'),
       ('¿Me van a hacer preguntas de salud en el formulario?', 'No. Las preguntas de salud te las hace el especialista por teléfono.'),
       ('¿Puedo asegurar a mi cónyuge o a un hijo?', 'Sí. En la solicitud nos dices para quién es: para ti, tu cónyuge, un hijo u otro familiar.'),
       ('¿Cuánto cuesta la cotización?', 'Nada. La cotización no tiene costo ni compromiso.')]
_fven = [('Which types of life insurance do you quote?', 'Term (for a number of years), whole life and universal life. If you are not sure which fits you, say so in the request and the specialist will advise you.'),
       ('Will the form ask me health questions?', 'No. Health questions are asked by the specialist over the phone.'),
       ('Can I insure my spouse or a child?', 'Yes. In the request you tell us who it is for: yourself, your spouse, a child or another relative.'),
       ('How much does the quote cost?', 'Nothing. The quote is free, with no obligation.')]
P['vida'] = dict(
    es=dict(slug='seguro-de-vida', img='familia.jpg', faq=_faqs(_fv),
        title='Seguro de vida en español: a término, vida entera y universal · Marrero Bernal & Associates',
        desc='Cotiza tu seguro de vida en español: a término, vida entera o vida universal, para ti, tu cónyuge o tus hijos. Un especialista te explica las opciones. Cotización sin costo.',
        html=_pag('es', 'Seguros personales · Vida', 'Seguro de vida, explicado en tu idioma.',
            'Para que tu familia no quede desprotegida. Te explicamos en español la diferencia entre un seguro a término y uno permanente, y cotizamos el monto que necesitas.',
            [('btn-acc', '/solicitud/?serv=vida', 'Cotizar seguro de vida'), _TEL], 'Familia con dos hijos frente a su casa', '''
  <div class="sub-grid">
    <div class="sub-card"><b>A término</b><p>Te cubre por un número de años.</p></div>
    <div class="sub-card"><b>Vida entera</b><p>Cobertura permanente.</p></div>
    <div class="sub-card"><b>Vida universal</b><p>Otra forma de cobertura permanente. Te explicamos cómo funciona.</p></div>
    <div class="sub-card"><b>¿No sabes cuál?</b><p>Márcalo en la solicitud y el especialista te aconseja.</p></div>
  </div>
  <h2>Ten esto a mano</h2>
  <ul class="sub-list">
    <li>Para quién es el seguro: para ti, tu cónyuge, un hijo u otro familiar.</li>
    <li>La fecha de nacimiento de la persona asegurada y si fuma.</li>
    <li>El monto que buscas, o dinos que no lo sabes.</li>
  </ul>
  <p>Las preguntas de salud no van en el formulario: te las hace el especialista por teléfono.</p>
  <h2>Cómo trabajamos</h2>
  <ol class="sub-steps">
    <li><b>Nos cuentas.</b> Llenas la solicitud en línea, llamas, escribes por WhatsApp o vienes a la oficina.</li>
    <li><b>Te llamamos.</b> Un especialista revisa tu caso contigo.</li>
    <li><b>Tú decides.</b> Te explicamos cada opción, sin presión.</li>
    <li><b>Seguimos ahí.</b> La misma oficina y la misma gente.</li>
  </ol>''', _fv, [_LEGSEG, 'La aprobación, la cobertura y la prima dependen de la compañía aseguradora y de cada persona.'])),
    en=dict(slug='life-insurance', img='familia.jpg', faq=_faqs(_fven),
        title='Life insurance: term, whole and universal life · Marrero Bernal & Associates',
        desc='Get a life insurance quote in English or Spanish: term, whole life or universal life, for you, your spouse or your children. A specialist explains the options. Free quote.',
        html=_pag('en', 'Personal insurance · Life', 'Life insurance, explained in your language.',
            'So your family is not left unprotected. We explain the difference between term and permanent insurance and quote the amount you need.',
            [('btn-acc', '/en/request/?serv=vida', 'Quote life insurance'), _TELEN], 'Family with two children in front of their home', '''
  <div class="sub-grid">
    <div class="sub-card"><b>Term</b><p>Covers you for a number of years.</p></div>
    <div class="sub-card"><b>Whole life</b><p>Permanent coverage.</p></div>
    <div class="sub-card"><b>Universal life</b><p>Another form of permanent coverage. We explain how it works.</p></div>
    <div class="sub-card"><b>Not sure which?</b><p>Say so in the request and the specialist will advise you.</p></div>
  </div>
  <h2>Have this ready</h2>
  <ul class="sub-list">
    <li>Who the insurance is for: yourself, your spouse, a child or another relative.</li>
    <li>The insured person's date of birth and whether they smoke.</li>
    <li>The amount you are looking for, or tell us you are not sure.</li>
  </ul>
  <p>Health questions are not in the form: the specialist asks them over the phone.</p>
  <h2>How we work</h2>
  <ol class="sub-steps">
    <li><b>You tell us.</b> Fill out the online request, call, WhatsApp us or come to the office.</li>
    <li><b>We call you.</b> A specialist reviews your case with you.</li>
    <li><b>You decide.</b> We explain each option, with no pressure.</li>
    <li><b>We stay with you.</b> The same office and the same people.</li>
  </ol>''', _fven, [_LEGSEGEN, 'Approval, coverage and premium depend on the insurance company and on each person.'])))

# ---- negocio / workers' comp
_fb = [('¿Estoy obligado a tener workers\' comp?', 'En Nevada, si tienes uno o más empleados, sí: la ley lo exige. En construcción, aunque el trabajo sea corto.'),
       ('Trabajo solo. ¿Para qué lo quiero?', 'Porque muchos contratistas generales, dueños de obra y clientes no dan el trabajo sin un certificado de seguro.'),
       ('Me piden un certificado de seguro para un contrato. ¿Me lo dan?', 'Sí. Te lo enviamos cuando te lo pidan, para que no pierdas el trabajo. En la solicitud nos dices para qué fecha lo necesitas.'),
       ('¿Qué pasa si no tengo la cobertura?', 'El estado puede multarte hasta con $15,000 y ordenar que cierres el negocio hasta tener el seguro, y pagas tú los costos de cualquier accidente de trabajo.'),
       ('¿Qué otros seguros de negocio cotizan?', 'Responsabilidad civil, auto comercial, propiedad comercial, bonos y paquetes por industria.')]
_fben = [('Am I required to have workers\' comp?', 'In Nevada, if you have one or more employees, yes: the law requires it. In construction, even for a short job.'),
       ('I work alone. Why would I need it?', 'Because many general contractors, project owners and clients will not give you the job without a certificate of insurance.'),
       ('I am asked for a certificate of insurance for a contract. Do you provide it?', 'Yes. We send it when you are asked for it, so you do not lose the job. In the request you tell us the date you need it by.'),
       ('What if I do not have coverage?', 'The state can fine you up to $15,000 and order your business closed until you have insurance, and you pay the costs of any workplace accident.'),
       ('What other business insurance do you quote?', 'General liability, commercial auto, commercial property, bonds and industry packages.')]
P['negocio'] = dict(
    es=dict(slug='seguro-de-negocio', img='workers.jpg', faq=_faqs(_fb),
        title='Workers\' compensation y seguro de negocio en Nevada · Marrero Bernal & Associates',
        desc='Workers\' comp, responsabilidad civil, auto comercial y propiedad para tu negocio, cotizados en español. Certificados de seguro cuando te los pidan. Cotización sin costo.',
        html=_pag('es', 'Para tu negocio · Seguros comerciales', 'Workers\' comp y seguro de negocio, en español.',
            'En Nevada, si tienes uno o más empleados, la ley te obliga a tener seguro de compensación al trabajador. Te lo cotizamos en español, junto con el resto de los seguros del negocio, y te mandamos los certificados cuando te los pidan.',
            [('btn-acc', '/solicitud/?serv=negocio', 'Cotizar mi negocio'), _TEL], 'Contratista con casco dándole la mano a una agente de seguros en una obra', '''
  <div class="sub-grid">
    <div class="sub-card"><b>Obligatorio en Nevada</b><p>Con uno o más empleados. En construcción, aunque el trabajo sea corto.</p></div>
    <div class="sub-card destacado"><b>Multas de hasta $15,000</b><p>Sin cobertura, el estado puede multarte y ordenar que cierres hasta tener el seguro.</p></div>
    <div class="sub-card"><b>Certificados</b><p>Si un contratista o un cliente te pide el certificado de seguro, te lo enviamos.</p></div>
    <div class="sub-card"><b>Todo el negocio</b><p>Responsabilidad civil, auto comercial, propiedad y paquetes por industria.</p></div>
  </div>
  <h2>Industrias que atendemos</h2>
  <p>Construcción, limpieza, jardinería, restaurantes, transporte y camiones, salones y barberías, y tiendas.</p>
  <h2>Ten esto a mano</h2>
  <ul class="sub-list">
    <li>El nombre del negocio, a qué se dedica y su estructura (LLC, corporación o dueño único).</li>
    <li>Años operando y número de empleados.</li>
    <li>La nómina anual y las ventas anuales aproximadas.</li>
    <li>Qué necesitas: responsabilidad general, workers' comp, auto comercial, propiedad o bonos.</li>
    <li>Si necesitas un certificado para un contrato, y para qué fecha.</li>
  </ul>
  <h2>La nómina y el seguro, en el mismo lugar</h2>
  <p>El workers' comp se calcula sobre la nómina. Como también llevamos la contabilidad, la nómina y los taxes del negocio, todo cuadra en un mismo lugar. <a href="/contabilidad-y-nomina/">Ver contabilidad y nómina →</a></p>
  <p>¿Vas a abrir tu negocio? <a href="/llc-y-licencias/">Ver LLC y licencias →</a></p>''', _fb, [_LEGSEG, 'Fuente de los requisitos: División de Relaciones Industriales de Nevada. Las coberturas y las primas dependen de la aseguradora, la industria y la nómina.'])),
    en=dict(slug='business-insurance', img='workers.jpg', faq=_faqs(_fben),
        title='Workers\' compensation and business insurance in Nevada · Marrero Bernal & Associates',
        desc='Workers\' comp, general liability, commercial auto and property for your business, in English or Spanish. Certificates of insurance when you are asked for them. Free quote.',
        html=_pag('en', 'For your business · Commercial insurance', 'Workers\' comp and business insurance, in your language.',
            'In Nevada, if you have one or more employees, the law requires workers\' compensation insurance. We quote it, along with the rest of your business insurance, and send certificates when you are asked for them.',
            [('btn-acc', '/en/request/?serv=negocio', 'Quote my business'), _TELEN], 'Contractor in a hard hat shaking hands with an insurance agent at a job site', '''
  <div class="sub-grid">
    <div class="sub-card"><b>Required in Nevada</b><p>With one or more employees. In construction, even for a short job.</p></div>
    <div class="sub-card destacado"><b>Fines up to $15,000</b><p>Without coverage, the state can fine you and order you closed until you have insurance.</p></div>
    <div class="sub-card"><b>Certificates</b><p>If a contractor or client asks for a certificate of insurance, we send it.</p></div>
    <div class="sub-card"><b>The whole business</b><p>General liability, commercial auto, property and industry packages.</p></div>
  </div>
  <h2>Industries we serve</h2>
  <p>Construction, cleaning, landscaping, restaurants, transportation and trucking, salons and barbershops, and retail stores.</p>
  <h2>Have this ready</h2>
  <ul class="sub-list">
    <li>The business name, what it does and its structure (LLC, corporation or sole proprietor).</li>
    <li>Years in business and number of employees.</li>
    <li>Approximate annual payroll and annual sales.</li>
    <li>What you need: general liability, workers' comp, commercial auto, property or bonds.</li>
    <li>Whether you need a certificate for a contract, and by what date.</li>
  </ul>
  <h2>Payroll and insurance in the same place</h2>
  <p>Workers' comp is based on payroll. Since we also handle the business's bookkeeping, payroll and taxes, everything lines up in one place. <a href="/en/bookkeeping-payroll/">See bookkeeping and payroll →</a></p>
  <p>Opening a business? <a href="/en/llc-and-licenses/">See LLC and licenses →</a></p>''', _fben, [_LEGSEGEN, 'Source of the requirements: Nevada Division of Industrial Relations. Coverage and premiums depend on the carrier, the industry and the payroll.'])))

# ---- LLC y licencias
_fl = [('¿Qué hacen exactamente?', 'Te formamos la LLC, sacamos la licencia de negocio, tramitamos el EIN y el registro estatal, y dejamos el seguro listo.'),
       ('¿Cuántas visitas hacen falta?', 'La idea es resolverlo en una sola visita: LLC, licencia y seguro.'),
       ('Después de abrir, ¿quién me lleva los impuestos y la nómina?', 'Nosotros, si quieres: contabilidad, nómina, sales tax y los taxes del negocio.'),
       ('¿Dan asesoría legal?', 'No. No somos abogados y no ofrecemos asesoría legal. Si necesitas decidir qué estructura legal te conviene, consulta a un abogado.')]
_flen = [('What exactly do you do?', 'We form your LLC, get the business license, handle the EIN and state registration, and set up the insurance.'),
       ('How many visits does it take?', 'The idea is to get it done in a single visit: LLC, license and insurance.'),
       ('After I open, who handles my taxes and payroll?', 'We can: bookkeeping, payroll, sales tax and the business taxes.'),
       ('Do you give legal advice?', 'No. We are not attorneys and do not give legal advice. If you need to decide which legal structure suits you, consult an attorney.')]
P['llc'] = dict(
    es=dict(slug='llc-y-licencias', img='negocio.jpg', faq=_faqs(_fl),
        title='Crear una LLC, licencia de negocio y EIN en Nevada · Marrero Bernal & Associates',
        desc='Abre tu negocio en español: formamos tu LLC, sacamos la licencia de negocio, el EIN y el registro estatal, y dejamos el seguro listo en una sola visita.',
        html=_pag('es', 'Para tu negocio · LLC y licencias', 'Abre tu negocio: LLC, licencia y seguro en una sola visita.',
            'Te formamos la LLC, sacamos la licencia de negocio, tramitamos el EIN y el registro estatal, y dejamos el seguro listo. En español, en la oficina de North Las Vegas.',
            [('btn-acc', '/solicitud/?serv=llc', 'Empezar mi negocio'), _TEL], 'Dueño de una panadería en su local', '''
  <div class="sub-grid">
    <div class="sub-card"><b>Creación de LLC</b><p>Formamos la compañía con el nombre que quieres usar.</p></div>
    <div class="sub-card"><b>Licencia de negocio</b><p>Sacamos la licencia para que puedas operar.</p></div>
    <div class="sub-card"><b>EIN y registro estatal</b><p>El número del negocio ante el IRS y el registro ante el estado.</p></div>
    <div class="sub-card"><b>Seguro listo</b><p>Workers' comp y responsabilidad civil, para empezar asegurado. <a href="/seguro-de-negocio/">Ver seguros →</a></p></div>
  </div>
  <h2>Ten esto a mano</h2>
  <ul class="sub-list">
    <li>Qué necesitas: crear la LLC, la licencia de negocio, el EIN, o todo.</li>
    <li>A qué se va a dedicar el negocio.</li>
    <li>El nombre que quieres usar.</li>
  </ul>
  <h2>Y después de abrir</h2>
  <p>Llevamos la contabilidad, la nómina, el sales tax y los taxes del negocio durante el año. <a href="/contabilidad-y-nomina/">Ver contabilidad y nómina →</a></p>''', _fl, ['No somos abogados y no ofrecemos asesoría legal. Los requisitos y las tarifas de registro y de licencias los fijan el estado, el condado y la ciudad, y pueden cambiar.'])),
    en=dict(slug='llc-and-licenses', img='negocio.jpg', faq=_faqs(_flen),
        title='Form an LLC, business license and EIN in Nevada · Marrero Bernal & Associates',
        desc='Open your business: we form your LLC, get the business license, the EIN and state registration, and set up the insurance in a single visit. In English or Spanish.',
        html=_pag('en', 'For your business · LLC and licenses', 'Open your business: LLC, license and insurance in one visit.',
            'We form your LLC, get the business license, handle the EIN and state registration, and set up the insurance. At our North Las Vegas office.',
            [('btn-acc', '/en/request/?serv=llc', 'Start my business'), _TELEN], 'Bakery owner at his shop', '''
  <div class="sub-grid">
    <div class="sub-card"><b>LLC formation</b><p>We form the company with the name you want to use.</p></div>
    <div class="sub-card"><b>Business license</b><p>We get the license so you can operate.</p></div>
    <div class="sub-card"><b>EIN and state registration</b><p>The business's IRS number and its registration with the state.</p></div>
    <div class="sub-card"><b>Insurance ready</b><p>Workers' comp and general liability, so you start out insured. <a href="/en/business-insurance/">See insurance →</a></p></div>
  </div>
  <h2>Have this ready</h2>
  <ul class="sub-list">
    <li>What you need: forming the LLC, the business license, the EIN, or all of it.</li>
    <li>What the business will do.</li>
    <li>The name you want to use.</li>
  </ul>
  <h2>After you open</h2>
  <p>We keep the books, payroll, sales tax and business taxes during the year. <a href="/en/bookkeeping-payroll/">See bookkeeping and payroll →</a></p>''', _flen, ['We are not attorneys and do not give legal advice. Registration and license requirements and fees are set by the state, county and city, and may change.'])))

# ---- privacidad
def _priv(es):
    T = lambda a, b: a if es else b
    S = [
     (T('Quiénes somos', 'Who we are'), T('<p>Marrero Bernal &amp; Associates y Marrero Bernal Agency LLC, 3455 W Craig Rd, Suite D, North Las Vegas, NV 89032. Teléfono y WhatsApp: 888-877-2583.</p>', '<p>Marrero Bernal &amp; Associates and Marrero Bernal Agency LLC, 3455 W Craig Rd, Suite D, North Las Vegas, NV 89032. Phone and WhatsApp: 888-877-2583.</p>')),
     (T('Qué datos recogemos', 'What we collect'), T('''<ul class="sub-list">
    <li><b>Lo que tú nos das</b> en la solicitud en línea, el formulario de contacto, el chat y las citas: nombre, teléfono, correo, dirección, fecha de nacimiento y los datos del servicio que pides (por ejemplo, tu vehículo o tu propiedad).</li>
    <li><b>De dónde llegaste</b> al sitio (por ejemplo, Google o Facebook), para saber qué anuncios funcionan.</li>
    <li><b>Datos de uso</b> del sitio, por medio de Google Analytics y del píxel de Meta: páginas vistas y si se envió una solicitud. Al píxel de Meta no le enviamos lo que escribes en los formularios.</li>
  </ul>
  <p>En los formularios del sitio no pedimos números de Seguro Social o ITIN, ni datos bancarios. Los documentos de tus taxes se suben por el portal seguro de clientes (SecureFilePro), y los pagos en línea los procesa GoDaddy Payments; no guardamos tu tarjeta en este sitio.</p>''', '''<ul class="sub-list">
    <li><b>What you give us</b> in the online request, the contact form, the chat and appointments: name, phone, email, address, date of birth and the details of the service you ask for (for example, your vehicle or your property).</li>
    <li><b>How you reached</b> the site (for example, Google or Facebook), so we know which ads work.</li>
    <li><b>Usage data</b> through Google Analytics and the Meta pixel: pages viewed and whether a request was sent. We do not send what you type in forms to the Meta pixel.</li>
  </ul>
  <p>The site's forms do not ask for Social Security or ITIN numbers or for bank information. Your tax documents are uploaded through the secure client portal (SecureFilePro), and online payments are processed by GoDaddy Payments; we do not store your card on this site.</p>''')),
     (T('Para qué los usamos', 'How we use it'), T('<p>Para contactarte sobre lo que pediste, preparar tu cotización o tu trámite, confirmar y recordarte tus citas, y mejorar el sitio.</p>', '<p>To contact you about what you requested, prepare your quote or your paperwork, confirm and remind you of appointments, and improve the site.</p>')),
     (T('Con quién los compartimos', 'Who we share it with'), T('''<p><b>No vendemos tus datos.</b> Los compartimos solo con:</p>
  <ul class="sub-list">
    <li>Las compañías de seguros con las que cotizamos lo que pediste, y las agencias ante las que hacemos tu trámite (por ejemplo, el IRS).</li>
    <li>Los proveedores que operan nuestras herramientas: el sistema de clientes y mensajería (HighLevel / LeadConnector), el alojamiento del sitio, Google Analytics y Meta.</li>
    <li>Las autoridades, cuando la ley lo exige.</li>
  </ul>''', '''<p><b>We do not sell your data.</b> We share it only with:</p>
  <ul class="sub-list">
    <li>The insurance companies we quote your request with, and the agencies we file your paperwork with (for example, the IRS).</li>
    <li>The providers that run our tools: the client and messaging system (HighLevel / LeadConnector), the site's hosting, Google Analytics and Meta.</li>
    <li>Authorities, when the law requires it.</li>
  </ul>''')),
     (T('Mensajes de texto y WhatsApp', 'Text messages and WhatsApp'), T('''<p>Si nos autorizas en un formulario, te contactamos por llamada, mensaje de texto o WhatsApp sobre tu solicitud y tus citas. La frecuencia de los mensajes varía. Pueden aplicar tarifas de mensajes y datos de tu compañía telefónica. Responde <b>STOP</b> para dejar de recibir mensajes de texto y <b>HELP</b> para ayuda. Dar tu autorización no es condición para comprar ningún servicio.</p>
  <p>No compartimos ni vendemos tu número de teléfono ni tu autorización para recibir mensajes con terceros para fines de mercadeo.</p>''', '''<p>If you authorize us in a form, we contact you by call, text message or WhatsApp about your request and your appointments. Message frequency varies. Message and data rates from your carrier may apply. Reply <b>STOP</b> to stop receiving text messages and <b>HELP</b> for help. Consent is not a condition of purchasing any service.</p>
  <p>We do not share or sell your phone number or your consent to receive messages with third parties for marketing purposes.</p>''')),
     (T('Cookies y medición', 'Cookies and measurement'), T('<p>El sitio usa cookies de Google Analytics y de Meta para contar visitas y medir anuncios, y guarda en tu navegador el idioma que escogiste. Puedes bloquear las cookies en tu navegador; el sitio sigue funcionando.</p>', '<p>The site uses Google Analytics and Meta cookies to count visits and measure ads, and stores your language choice in your browser. You can block cookies in your browser; the site keeps working.</p>')),
     (T('Tus opciones', 'Your choices'), T('<p>Puedes pedirnos ver, corregir o borrar los datos que tenemos de ti, o que dejemos de contactarte: llámanos o escríbenos por WhatsApp al 888-877-2583, o ven a la oficina. Hay datos que la ley nos obliga a conservar, como los de las declaraciones de impuestos y las pólizas.</p>', '<p>You can ask us to see, correct or delete the data we hold about you, or to stop contacting you: call or WhatsApp us at 888-877-2583, or come to the office. Some data we are required by law to keep, such as tax return and policy records.</p>')),
    ]
    body = ''.join(f'\n  <h2>{h}</h2>\n  {c}' for h, c in S)
    return ('\n<section class="sub"><div class="wrap">\n  <div class="kicker">' + T('Privacidad', 'Privacy') + '</div>\n  <h1>' + T('Política de privacidad', 'Privacy policy') + '</h1>\n  <p class="lead">'
            + T('Qué datos recogemos en marrerobernal.com, para qué los usamos y con quién los compartimos.', 'What data we collect at marrerobernal.com, how we use it and who we share it with.') + '</p>' + body
            + '\n  <div class="sub-legal"><p>' + T('Vigente desde el 13 de noviembre de 2026. Si cambiamos esta política, publicamos aquí la nueva versión.', 'Effective November 13, 2026. If we change this policy, we will post the new version here.') + '</p></div>\n</div></section>')
P['privacidad'] = dict(
    es=dict(slug='privacidad', img='og.jpg', title='Política de privacidad · Marrero Bernal & Associates',
        desc='Qué datos recoge marrerobernal.com, para qué se usan, con quién se comparten y cómo dejar de recibir mensajes.', html=_priv(True)),
    en=dict(slug='privacy', img='og.jpg', title='Privacy policy · Marrero Bernal & Associates',
        desc='What data marrerobernal.com collects, how it is used, who it is shared with and how to stop receiving messages.', html=_priv(False)))

# Páginas viejas de Elementor → destino (301). Las de seguros van al formulario propio de solicitud.
FQ = 'https://esales.farmers.com/fastquote?Lob={}&Source_Indicator=AP&State_Code=NV&Agent_Code=67249W%2430306E%248833H2&Zip_Code=89032'
REDIR = {
    'insurance': '/#personal', 'insurance-2': '/solicitud/?serv=auto,casa', 'vehicle-insurance': '/seguro-de-auto/',
    'home-insurance': '/seguro-de-casa/', 'life': '/seguro-de-vida/', 'business-insurance-2': '/seguro-de-negocio/',
    'health': '/obamacare-nevada/', 'travel': '/#personal', 'personal': '/#personal', 'business': '/#negocios',
    'taxes-2': '/taxes/', 'business-taxes': '/#negocios', 'business-licenses': '/llc-y-licencias/',
    'about-us': '/#nosotros', 'contact': '/#contacto', 'blog': '/', 'immigration': '/', 'payroll': '/contabilidad-y-nomina/',
    'dmv': '/traducciones/', 'translations': '/traducciones/', 'notary': '/notary-public/', 'media': 'https://marrerobernalmedia.com/',
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
    'hello-world': '/', 'privacy-policy': '/privacidad/',
}

# ---------------------------------------------------------------- solicitud en línea (formulario por pasos → CRM)
# El formulario vive en maquetas/mba/solicitud.js y solicitud.css; aquí solo se monta la página en los dos idiomas.
SOL_JS = (root / 'maquetas/mba/solicitud.js').read_text()
def _sol(lang):
    return ('\n<section class="sub sol"><div class="wrap">\n'
            '  <a class="gstars" href="https://g.page/r/CRuuvSm15kNDEAI" target="_blank" rel="noopener"><b>★★★★★</b> ' + ('4.9 en Google · 27 reseñas' if lang == 'es' else '4.9 on Google · 27 reviews') + '</a>\n'
            '  <div id="sol-app" data-lang="' + lang + '" data-ajax="<?php echo esc_url(admin_url(\'admin-ajax.php\')); ?>"></div>\n'
            '  <noscript><p>' + ('Para pedir tu cotización llámanos o escríbenos por WhatsApp al 888-877-2583.' if lang == 'es' else 'To request your quote, call or WhatsApp us at 888-877-2583.') + '</p></noscript>\n'
            '</div></section>\n<script>\n' + SOL_JS + '</script>\n')
P['solicitud'] = dict(
    es=dict(slug='solicitud', img='tramites.jpg',
        title='Cotiza o solicita un servicio en línea · Marrero Bernal & Associates',
        desc='Pide tu cotización de seguro de auto, casa, vida o negocio, o solicita taxes, ITIN, traducciones y notary public. Un especialista te contacta con opciones de varias compañías.',
        html=_sol('es')),
    en=dict(slug='request', img='tramites.jpg',
        title='Get a quote or request a service online · Marrero Bernal & Associates',
        desc='Request your auto, home, life or business insurance quote, or ask for taxes, ITIN, translations and notary. A specialist contacts you with options from several companies.',
        html=_sol('en')))

# ---------------------------------------------------------------- citas en línea (calendario del CRM)
def _cita(lang):
    es = lang == 'es'
    return ('\n<section class="sub sol"><div class="wrap" style="max-width:860px">\n'
            '  <div class="kicker">' + ('Citas' if es else 'Appointments') + '</div>\n'
            '  <h1 style="font-family:Fraunces,serif;margin:6px 0 10px">' + ('Agenda tu cita en la oficina' if es else 'Book your appointment at the office') + '</h1>\n'
            '  <p class="lead" style="margin:0 0 18px">' + ('Escoge el día y la hora. Atendemos citas lunes, martes, jueves y viernes de 9:00 AM a 4:00 PM, excepto feriados. Si prefieres, llámanos o escríbenos por WhatsApp al 888-877-2583.' if es else 'Pick a day and time. Appointments are Monday, Tuesday, Thursday and Friday from 9:00 AM to 4:00 PM, except holidays. If you prefer, call or WhatsApp us at 888-877-2583.') + '</p>\n'
            '  <p style="margin:0 0 18px;padding:12px 14px;border-radius:12px;background:#fff;border:1px solid #e4dfd3"><b>' + ('Dinos para qué es la cita.' if es else 'Tell us what the appointment is for.') + '</b> ' + ('Al llenar tus datos, escribe en la casilla «Additional information» el motivo: taxes, seguro de auto, ITIN, traducción, notary public u otro. Así te atendemos con todo listo.' if es else 'When you enter your details, use the “Additional information” box to tell us the reason: taxes, auto insurance, ITIN, translation, notary or other. That way we have everything ready for you.') + '</p>\n'
            '  <iframe src="https://api.leadconnectorhq.com/widget/booking/J9VOKpFkhYtqSUi4Lbrn" style="width:100%;min-height:720px;border:none;overflow:hidden;background:#fff;border-radius:16px" scrolling="no" id="J9VOKpFkhYtqSUi4Lbrn_cita" title="' + ('Calendario de citas' if es else 'Appointment calendar') + '"></iframe>\n'
            '  <script src="https://link.msgsndr.com/js/form_embed.js" type="text/javascript"></script>\n'
            '</div></section>\n')
P['citas'] = dict(
    es=dict(slug='citas', img='tramites.jpg',
        title='Agenda tu cita · Marrero Bernal & Associates',
        desc='Agenda en línea tu cita en la oficina de Marrero Bernal & Associates en North Las Vegas: lunes, martes, jueves y viernes de 9 a 4.',
        html=_cita('es')),
    en=dict(slug='appointments', img='tramites.jpg',
        title='Book your appointment · Marrero Bernal & Associates',
        desc='Book your appointment online at the Marrero Bernal & Associates office in North Las Vegas: Monday, Tuesday, Thursday and Friday, 9 to 4.',
        html=_cita('en')))

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
    routes[pair['es']['slug'] + '|es'] = dict(file=f'{key}-es', title=pair['es']['title'], desc=pair['es']['desc'], img=pair['es']['img'], faq=pair['es'].get('faq', []), pair='/en/' + pair['en']['slug'] + '/', self='/' + pair['es']['slug'] + '/')
    routes[pair['en']['slug'] + '|en'] = dict(file=f'{key}-en', title=pair['en']['title'], desc=pair['en']['desc'], img=pair['en']['img'], faq=pair['en'].get('faq', []), pair='/' + pair['es']['slug'] + '/', self='/en/' + pair['en']['slug'] + '/')

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
  $ld = [['@context' => 'https://schema.org', '@type' => 'WebPage', 'url' => $self, 'name' => $p['title'], 'description' => $p['desc'], 'inLanguage' => $p['lang'],
    'isPartOf' => ['@type' => 'WebSite', 'url' => home_url('/'), 'name' => 'Marrero Bernal & Associates'], 'publisher' => ['@id' => home_url('/#agencia')]]];
  if (!empty($p['faq'])) $ld[] = ['@context' => 'https://schema.org', '@type' => 'FAQPage', 'mainEntity' => array_map(fn($q) => ['@type' => 'Question', 'name' => $q[0], 'acceptedAnswer' => ['@type' => 'Answer', 'text' => $q[1]]], $p['faq'])];
  foreach ($ld as $x) echo '<script type="application/ld+json">' . wp_json_encode($x, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . '</script>';
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

/** Solicitud en línea (formulario por pasos de /solicitud/ y /en/request/).
 *  Va al CRM por la dirección guardada en Ajustes → Generales («Solicitudes web → CRM»). Si no hay dirección o el CRM no responde,
 *  la solicitud completa queda guardada en WordPress (menú «Solicitudes web») para que no se pierda. El correo de aviso no lleva los datos. */
add_action('init', function () {
  register_post_type('mba_solicitud', ['labels' => ['name' => 'Solicitudes web', 'singular_name' => 'Solicitud web'], 'public' => false, 'show_ui' => true, 'show_in_rest' => false,
    'exclude_from_search' => true, 'capability_type' => 'page', 'supports' => ['title', 'editor'], 'menu_icon' => 'dashicons-clipboard', 'menu_position' => 25]);
});
add_action('admin_init', function () {
  register_setting('general', 'mba_ghl_webhook', ['type' => 'string', 'sanitize_callback' => function ($v) { $v = esc_url_raw(trim((string) $v), ['https']); return $v; }, 'default' => '']);
  add_settings_field('mba_ghl_webhook', 'Solicitudes web → CRM', function () {
    echo '<input type="url" class="regular-text code" name="mba_ghl_webhook" value="' . esc_attr(get_option('mba_ghl_webhook', '')) . '" placeholder="https://…">'
      . '<p class="description">Dirección de entrada (inbound webhook) de HighLevel. Si está vacía, las solicitudes se guardan solo aquí, en «Solicitudes web».</p>';
  }, 'general');
});
add_action('wp_ajax_nopriv_mba_solicitud', 'mba_solicitud');
add_action('wp_ajax_mba_solicitud', 'mba_solicitud');
function mba_solicitud() {
  $d = json_decode(wp_unslash($_POST['datos'] ?? ''), true);
  if (!is_array($d) || !empty($_POST['empresa'])) wp_send_json_error(null, 400);
  $ipk = 'mba_sol_' . md5($_SERVER['REMOTE_ADDR'] ?? '');
  $n = (int) get_transient($ipk); if ($n >= 8) wp_send_json_error(null, 429); set_transient($ipk, $n + 1, HOUR_IN_SECONDS);
  $s = fn($k, $max = 120) => mb_substr(sanitize_text_field((string) ($d[$k] ?? '')), 0, $max);
  $nombre = $s('nombre'); $apellido = $s('apellido'); $tel = preg_replace('/\\\\D/', '', $s('telefono', 30));
  $servs = array_slice(array_filter(array_map('sanitize_text_field', (array) ($d['servicios'] ?? []))), 0, 20);
  $resumen = mb_substr(sanitize_textarea_field((string) ($d['resumen'] ?? '')), 0, 12000);
  if (!$nombre || strlen($tel) < 10 || !$servs || (int) ($d['seg'] ?? 0) < 5) wp_send_json_error(null, 400);
  if (strlen($tel) === 10) $tel = '1' . $tel;
  $lista = implode(', ', $servs);
  $fuente = strtolower($s('fuente', 80)); $fcat = 'directo';
  foreach (['facebook' => 'facebook|fb\\.|fbclid', 'instagram' => 'instagram', 'google' => 'google', 'whatsapp' => 'whatsapp|wa\\.me', 'youtube' => 'youtube|youtu\\.be', 'tiktok' => 'tiktok', 'bing' => 'bing'] as $k => $re) if (preg_match("/$re/", $fuente)) { $fcat = $k; break; }
  if ($fcat === 'directo' && $fuente && $fuente !== 'directo') $fcat = 'otro';
  $esapp = ($d['origen'] ?? '') === 'app'; if ($esapp) $fcat = 'app';
  $claves = array_slice(array_filter(array_map(fn($c) => preg_replace('/[^a-z]/', '', (string) $c), (array) ($d['claves'] ?? []))), 0, 20);
  $eti = array_merge(['solicitud-web'], array_map(fn($c) => 'serv-' . $c, $claves), [($d['idioma'] ?? '') === 'en' ? 'idioma-ingles' : 'idioma-espanol', 'fuente-' . $fcat, $s('cliente', 4) === 'si' ? 'cliente-existente' : 'prospecto-nuevo']);
  $resumen .= "\n\nORIGEN\n  Llegó por: " . ucfirst($fcat) . ($fuente && $fuente !== $fcat ? " ($fuente)" : '');
  // Cuándo llamará la oficina (lun-vie 9 a 5, hora de Las Vegas), para que el texto de confirmación no prometa de más.
  $lv = new DateTime('now', new DateTimeZone('America/Los_Angeles')); $dw = (int) $lv->format('N'); $hr = (int) $lv->format('G');
  $fer = ['2026-11-26', '2026-12-25', '2027-01-01', '2027-01-18', '2027-02-15', '2027-05-31', '2027-06-18', '2027-07-05', '2027-09-06', '2027-10-11', '2027-11-11', '2027-11-25', '2027-12-24'];
  $habil = fn($x) => (int) $x->format('N') <= 5 && !in_array($x->format('Y-m-d'), $fer, true);
  $sig = clone $lv; do { $sig->modify('+1 day'); } while (!$habil($sig));
  $man = (clone $lv)->modify('+1 day')->format('Y-m-d') === $sig->format('Y-m-d'); $n = (int) $sig->format('N');
  $des = [1 => 'el lunes', 2 => 'el martes', 3 => 'el miércoles', 4 => 'el jueves', 5 => 'el viernes']; $den = [1 => 'on Monday', 2 => 'on Tuesday', 3 => 'on Wednesday', 4 => 'on Thursday', 5 => 'on Friday'];
  $prox = [$man ? 'mañana' : $des[$n], $man ? 'tomorrow' : $den[$n]];
  if ($habil($lv) && $hr < 12) { $cu = ['hoy', 'today']; }
  elseif ($habil($lv) && $hr < 15) { $cu = ['hoy o ' . $prox[0], 'today or ' . $prox[1]]; }
  else { $cu = $prox; }
  $msgconf = ($d['idioma'] ?? '') === 'en'
    ? "Hi $nombre, we received your request at Marrero Bernal & Associates. A specialist will contact you {$cu[1]} (office hours: Mon-Fri, 9 to 5). To write to us, use WhatsApp at 888-877-2583; if it is urgent, call that same number."
    : "Hola $nombre, recibimos tu solicitud en Marrero Bernal & Associates. Un especialista te contactará {$cu[0]} (atendemos de lunes a viernes, de 9 a 5). Para escribirnos, usa WhatsApp al 888-877-2583; si es urgente, llama a ese mismo número.";
  $payload = ['first_name' => $nombre, 'last_name' => $apellido, 'phone' => '+' . $tel, 'email' => sanitize_email((string) ($d['correo'] ?? '')),
    'address1' => $s('direccion', 200), 'city' => $s('ciudad'), 'postal_code' => $s('zip', 12), 'date_of_birth' => $s('nacimiento', 10),
    'servicios' => $lista, 'idioma' => ($d['idioma'] ?? '') === 'en' ? 'Inglés' : 'Español', 'whatsapp' => !empty($d['whatsapp']) ? 'Sí' : 'No',
    'mejor_hora' => $s('hora', 40), 'ya_cliente' => $s('cliente', 4), 'resumen' => $resumen, 'origen' => $esapp ? 'App' : 'marrerobernal.com', 'fuente' => $fcat, 'fuente_detalle' => $fuente, 'etiquetas' => implode(',', $eti), 'servicio_principal' => $servs[0] ?? '',
    'mensaje_confirmacion' => $msgconf,
    'fecha' => wp_date('Y-m-d H:i')];
  delete_transient('mba_parc_' . $tel);
  $hook = get_option('mba_ghl_webhook', ''); $crm = false;
  if ($hook) {
    $r = wp_remote_post($hook, ['timeout' => 12, 'headers' => ['Content-Type' => 'application/json'], 'body' => wp_json_encode($payload)]);
    $crm = !is_wp_error($r) && (int) wp_remote_retrieve_response_code($r) < 300;
  }
  $id = wp_insert_post(['post_type' => 'mba_solicitud', 'post_status' => 'private', 'post_title' => trim("$nombre $apellido") . ' — ' . $lista,
    'post_content' => $crm ? 'Enviada al CRM el ' . wp_date('Y-m-d H:i') . '. Los datos están en HighLevel.' : $resumen]);
  if (!$crm && !$id) wp_send_json_error(null, 500);
  $to = get_option('mba_contacto_email', get_option('admin_email'));
  wp_mail($to, "Solicitud web: $lista — $nombre", "Entró una solicitud nueva desde " . $payload['origen'] . ".\\n\\nCliente: $nombre $apellido\\nServicios: $lista\\n\\n"
    . ($crm ? "Los datos completos están en HighLevel." : "Los datos completos están en WordPress → Solicitudes web.") . "\\n\\nFecha: " . wp_date('Y-m-d H:i'));
  wp_send_json_success();
}

/** Solicitud a medias: al terminar el paso 2 se guarda el contacto 30 minutos. Si en ese tiempo no envía el formulario completo,
 *  pasa al CRM marcada como incompleta (tipo = incompleta) para que la oficina lo llame. Si lo completa, no se envía nada. */
add_action('wp_ajax_nopriv_mba_solicitud_parcial', 'mba_solicitud_parcial');
add_action('wp_ajax_mba_solicitud_parcial', 'mba_solicitud_parcial');
function mba_solicitud_parcial() {
  $d = json_decode(wp_unslash($_POST['datos'] ?? ''), true);
  if (!is_array($d) || !empty($_POST['empresa'])) wp_send_json_error(null, 400);
  $ipk = 'mba_solp_' . md5($_SERVER['REMOTE_ADDR'] ?? '');
  $n = (int) get_transient($ipk); if ($n >= 6) wp_send_json_error(null, 429); set_transient($ipk, $n + 1, HOUR_IN_SECONDS);
  $s = fn($k, $max = 120) => mb_substr(sanitize_text_field((string) ($d[$k] ?? '')), 0, $max);
  $nombre = $s('nombre'); $tel = preg_replace('/\\D/', '', $s('telefono', 30));
  $servs = array_slice(array_filter(array_map('sanitize_text_field', (array) ($d['servicios'] ?? []))), 0, 20);
  if (!$nombre || strlen($tel) < 10 || !$servs || (int) ($d['seg'] ?? 0) < 5) wp_send_json_error(null, 400);
  if (strlen($tel) === 10) $tel = '1' . $tel;
  $fuente = strtolower($s('fuente', 80)); $fcat = 'directo';
  foreach (['facebook' => 'facebook|fb\\.|fbclid', 'instagram' => 'instagram', 'google' => 'google', 'whatsapp' => 'whatsapp|wa\\.me', 'youtube' => 'youtube|youtu\\.be', 'tiktok' => 'tiktok', 'bing' => 'bing'] as $k => $re) if (preg_match("/$re/", $fuente)) { $fcat = $k; break; }
  if ($fcat === 'directo' && $fuente && $fuente !== 'directo') $fcat = 'otro';
  $claves = array_slice(array_filter(array_map(fn($c) => preg_replace('/[^a-z]/', '', (string) $c), (array) ($d['claves'] ?? []))), 0, 20);
  $en = ($d['idioma'] ?? '') === 'en'; $lista = implode(', ', $servs);
  $eti = array_merge(['solicitud-incompleta'], array_map(fn($c) => 'serv-' . $c, $claves), [$en ? 'idioma-ingles' : 'idioma-espanol', 'fuente-' . $fcat, $s('cliente', 4) === 'si' ? 'cliente-existente' : 'prospecto-nuevo']);
  $payload = ['tipo' => 'incompleta', 'first_name' => $nombre, 'last_name' => $s('apellido'), 'phone' => '+' . $tel, 'email' => sanitize_email((string) ($d['correo'] ?? '')),
    'servicios' => $lista, 'idioma' => $en ? 'Inglés' : 'Español', 'whatsapp' => !empty($d['whatsapp']) ? 'Sí' : 'No', 'mejor_hora' => $s('hora', 40), 'ya_cliente' => $s('cliente', 4),
    'resumen' => "SOLICITUD INCOMPLETA\\nDejó sus datos de contacto y no terminó el formulario. Llamar para completar la solicitud.\\n\\nSERVICIOS: $lista\\nIDIOMA DEL CLIENTE: " . ($en ? 'Inglés' : 'Español')
      . "\\nMejor hora para llamar: " . ($s('hora', 40) ?: 'no dijo') . "\\nWhatsApp: " . (!empty($d['whatsapp']) ? 'Sí' : 'No') . "\\n\\nORIGEN\\n  Llegó por: " . ucfirst($fcat),
    'origen' => 'marrerobernal.com (solicitud incompleta)', 'fuente' => $fcat, 'fuente_detalle' => $fuente, 'etiquetas' => implode(',', $eti), 'servicio_principal' => $servs[0] ?? '', 'fecha' => wp_date('Y-m-d H:i')];
  set_transient('mba_parc_' . $tel, $payload, 2 * DAY_IN_SECONDS);
  wp_clear_scheduled_hook('mba_parcial_enviar', [$tel]);
  wp_schedule_single_event(time() + 30 * MINUTE_IN_SECONDS, 'mba_parcial_enviar', [$tel]);
  wp_send_json_success();
}
add_action('mba_parcial_enviar', function ($tel) {
  $p = get_transient('mba_parc_' . $tel); if (!is_array($p)) return;
  delete_transient('mba_parc_' . $tel);
  $hook = get_option('mba_ghl_webhook', ''); if (!$hook) return;
  wp_remote_post($hook, ['timeout' => 12, 'headers' => ['Content-Type' => 'application/json'], 'body' => wp_json_encode($p)]);
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
.sub-faq{background:#fff;border:1px solid var(--line);border-radius:14px;padding:0 18px;margin:10px 0}.sub-faq summary{cursor:pointer;font-weight:600;padding:15px 0;line-height:1.4}.sub-faq p{margin:0 0 16px;color:var(--mut)}
.sub-legal{margin-top:40px;padding-top:20px;border-top:1px solid var(--line)}.sub-legal p{font-size:13px!important;color:var(--mut);line-height:1.55}
'''
st = (out / 'style.css').read_text()
CSS += (root / 'maquetas/mba/solicitud.css').read_text()
st = st.split('/* ---- subpáginas (build_mba_paginas.py) ---- */')[0].rstrip() + '\n' + CSS
(out / 'style.css').write_text(st)

# Portada en inglés: los enlaces a subpáginas apuntan a /en/…
slugmap = {'/' + P[k]['es']['slug'] + '/': '/en/' + P[k]['en']['slug'] + '/' for k in P}
for f in ('front-page-en.php', 'footer-en.php', 'header-en.php'):
    fp = out / f
    if fp.exists():
        t = fp.read_text()
        for a, b in slugmap.items(): t = t.replace(f'href="{a}"', f'href="{b}"').replace(f'href="{a}?', f'href="{b}?')
        fp.write_text(t)

# functions.php carga paginas.php
fn = (out / 'functions.php').read_text()
if "paginas.php" not in fn:
    fn = fn.rstrip() + "\nrequire_once __DIR__ . '/paginas.php';\n"
    (out / 'functions.php').write_text(fn)
print('páginas generadas:', ', '.join(sorted(r['self'] for r in routes.values())))
