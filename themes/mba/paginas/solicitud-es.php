<?php /* solicitud (es) — GENERADO por tools/build_mba_paginas.py */
ob_start(); get_header(); echo mba_pag_fix(ob_get_clean(), 'es', 'solicitud', 'request'); ?>
<main class="subpage">
<section class="sub sol"><div class="wrap">
  <div id="sol-app" data-lang="es" data-ajax="<?php echo esc_url(admin_url('admin-ajax.php')); ?>"></div>
  <noscript><p>Para pedir tu cotización llámanos o escríbenos por WhatsApp al 888-877-2583.</p></noscript>
</div></section>
<script>
(function(){
// ---------- idioma
const app=document.getElementById('sol-app');if(!app)return;
const L=app.dataset.lang==='en'?'en':'es';
const T=(es,en)=>L==='es'?es:en;
// ---------- opciones comunes
const YN=[['si','Sí','Yes'],['no','No','No']];
const O=(...a)=>a.map(x=>Array.isArray(x)?x:[x[0]||x,x,x]);
const opt=(list)=>list.map(x=>typeof x==='string'?[x,x,x]:x);
// ---------- campos: [id, es, en, tipo, opciones|null, flags]  flags: r=requerido, w=ancho, o=opcional visible
const F=(id,es,en,type='text',opts=null,fl='')=>({id,es,en,type,opts:opts&&opt(opts),req:fl.includes('r'),wide:fl.includes('w'),opc:fl.includes('o')});
const SEGURO_ACTUAL=[
  F('aseg','¿Tienes seguro ahora?','Do you have insurance now?','select',YN),
  F('cia','Compañía actual','Current company'),
  F('vence','¿Cuándo vence?','When does it expire?','date'),
];
const SERV={
 auto:{g:'seg',ic:'🚗',es:'Auto',en:'Auto',
  rep:[
   {id:'veh',es:'Vehículo',en:'Vehicle',max:4,f:[
     F('anio','Año','Year','number',null,'r'),F('marca','Marca','Make','text',null,'r'),F('modelo','Modelo','Model','text',null,'r'),
     F('vin','VIN','VIN','text',null,'o'),
     F('prop','¿Financiado o pagado?','Financed or paid off?','select',[['fin','Financiado','Financed'],['lease','Arrendado (lease)','Leased'],['pag','Pagado','Paid off']]),
     F('uso','Uso','Use','select',[['pers','Personal','Personal'],['trab','Ir al trabajo','Commute'],['neg','Negocio','Business'],['app','Uber, Lyft o entregas','Rideshare or delivery']]),
     F('millas','Millas al año (aprox.)','Miles per year (approx.)','number')]},
   {id:'cond',es:'Conductor',en:'Driver',max:5,f:[
     F('nom','Nombre completo','Full name','text',null,'r'),F('nac','Fecha de nacimiento','Date of birth','date',null,'r'),
     F('civil','Estado civil','Marital status','select',[['sol','Soltero/a','Single'],['cas','Casado/a','Married'],['otro','Otro','Other']]),
     F('lic','Licencia de','License from','select',[['nv','Nevada','Nevada'],['us','Otro estado','Another state'],['ext','Otro país','Another country'],['no','No tiene','None']]),
     F('licnum','Número de licencia','License number','text',null,'o'),
     F('anios','Años manejando en EE. UU.','Years driving in the U.S.','number'),
     F('inc','¿Accidentes o multas en 3 años?','Accidents or tickets in 3 years?','select',YN),
     F('incdet','Si los hubo, cuéntanos','If so, tell us','text',null,'w')]}],
  f:[...SEGURO_ACTUAL,
   F('cob','Cobertura que buscas','Coverage you want','select',[['min','La mínima del estado','State minimum'],['full','Completa (full cover)','Full coverage'],['ns','No sé, aconséjenme','Not sure, advise me']]),
   F('viv','¿Tu vivienda es propia o rentada?','Do you own or rent your home?','select',[['prop','Propia','Own'],['rent','Rentada','Rent']])]},
 casa:{g:'seg',ic:'🏠',es:'Casa o condominio',en:'Home or condo',
  f:[F('dir','Dirección de la propiedad','Property address','text',null,'rw'),
   F('tipo','Tipo','Type','select',[['casa','Casa','House'],['condo','Condominio','Condo'],['town','Townhouse','Townhouse'],['movil','Casa móvil','Mobile home']],'r'),
   F('uso','Uso','Use','select',[['vivo','Vivo ahí','I live there'],['rento','La rento a otros','I rent it out'],['vac','Vacacional','Vacation home']]),
   F('anio','Año de construcción','Year built','number'),F('pies','Pies cuadrados','Square feet','number'),
   F('techo','Año del techo','Roof year','number'),
   F('hip','¿Tiene hipoteca?','Is there a mortgage?','select',YN),
   F('compra','¿La estás comprando ahora?','Are you buying it now?','select',YN),F('cierre','Fecha de cierre','Closing date','date',null,'o'),
   F('pisc','¿Piscina o trampolín?','Pool or trampoline?','select',YN),F('perro','¿Perros? (raza)','Dogs? (breed)'),
   F('alarma','¿Alarma o cámaras?','Alarm or cameras?','select',YN),
   F('recl','¿Reclamos en 5 años?','Claims in 5 years?','select',YN),...SEGURO_ACTUAL]},
 renters:{g:'seg',ic:'🔑',es:'Renters',en:'Renters',
  f:[F('dir','Dirección donde vives','Address where you live','text',null,'rw'),
   F('tipo','Tipo de vivienda','Home type','select',[['apto','Apartamento','Apartment'],['casa','Casa','House'],['cuarto','Cuarto','Room']]),
   F('valor','Valor de tus pertenencias','Value of your belongings','select',[['15','Hasta $15,000','Up to $15,000'],['30','$15,000 – $30,000','$15,000 – $30,000'],['50','$30,000 – $50,000','$30,000 – $50,000'],['mas','Más de $50,000','Over $50,000']]),
   F('perro','¿Perros? (raza)','Dogs? (breed)'),F('recl','¿Reclamos en 5 años?','Claims in 5 years?','select',YN)]},
 vida:{g:'seg',ic:'❤️',es:'Vida',en:'Life',
  f:[F('quien','¿Para quién?','For whom?','select',[['yo','Para mí','Myself'],['cony','Mi cónyuge','My spouse'],['hijo','Un hijo','A child'],['otro','Otro familiar','Another relative']],'r'),
   F('nac','Fecha de nacimiento del asegurado','Insured\'s date of birth','date'),
   F('fuma','¿Fuma?','Smoker?','select',YN),
   F('monto','Monto que buscas','Amount you want','select',[['100','Hasta $100,000','Up to $100,000'],['250','$100,000 – $250,000','$100,000 – $250,000'],['500','$250,000 – $500,000','$250,000 – $500,000'],['mas','Más de $500,000','Over $500,000'],['ns','No sé','Not sure']]),
   F('tipo','Tipo','Type','select',[['term','A término (por años)','Term'],['ent','Vida entera','Whole life'],['ns','No sé, aconséjenme','Not sure, advise me']])],
  nota:['Las preguntas de salud te las hace el especialista por teléfono.','Health questions are asked by the specialist over the phone.']},
 recre:{g:'seg',ic:'🏍️',es:'Moto, RV o bote',en:'Motorcycle, RV or boat',
  f:[F('tipo','Tipo','Type','select',[['moto','Motocicleta','Motorcycle'],['rv','RV o casa rodante','RV or motorhome'],['bote','Bote o jet ski','Boat or jet ski'],['atv','ATV u off-road','ATV or off-road'],['clas','Auto clásico','Classic car']],'r'),
   F('anio','Año','Year','number'),F('marca','Marca y modelo','Make and model'),F('valor','Valor aproximado','Approximate value')]},
 mexico:{g:'seg',ic:'🇲🇽',es:'Auto para México',en:'Auto for Mexico',
  f:[F('veh','Vehículo (año, marca, modelo)','Vehicle (year, make, model)','text',null,'rw'),F('valor','Valor aproximado','Approximate value'),
   F('ida','Fecha de entrada','Entry date','date'),F('vuelta','Fecha de salida','Exit date','date'),F('dest','Destino','Destination')]},
 negocio:{g:'seg',ic:'💼',es:'Seguro de negocio',en:'Business insurance',
  f:[F('nom','Nombre del negocio','Business name','text',null,'r'),F('act','¿A qué se dedica?','What does it do?','text',null,'r'),
   F('estr','Estructura','Structure','select',[['llc','LLC','LLC'],['corp','Corporación','Corporation'],['solo','Dueño único','Sole proprietor'],['ns','No sé','Not sure']]),
   F('anios','Años operando','Years in business','number'),F('emp','Número de empleados','Number of employees','number'),
   F('nomina','Nómina anual aprox.','Approx. annual payroll'),F('ventas','Ventas anuales aprox.','Approx. annual sales'),
   F('cobs','¿Qué necesitas?','What do you need?','checks',[['gl','Responsabilidad general','General liability'],['wc','Workers\' comp','Workers\' comp'],['auto','Auto comercial','Commercial auto'],['prop','Propiedad','Property'],['bono','Bonos','Bonds'],['ns','No sé','Not sure']],'w'),
   F('cert','¿Necesitas un certificado para un contrato?','Need a certificate for a contract?','select',YN),F('limite','¿Para qué fecha?','By what date?','date',null,'o')]},
 obamacare:{g:'sal',ic:'🩺',es:'Obamacare (Nevada Health Link)',en:'Obamacare (Nevada Health Link)',
  f:[F('pers','Personas en el hogar','People in household','number',null,'r'),F('edades','Edades','Ages'),
   F('ingreso','Ingreso anual aprox. del hogar','Approx. annual household income'),F('zip','Código postal','ZIP code')]},
 taxes:{g:'tax',ic:'🧾',es:'Taxes personales',en:'Personal taxes',
  f:[F('anio','Año(s) a declarar','Tax year(s)','text',null,'r'),
   F('civil','Estado civil','Filing status','select',[['sol','Soltero/a','Single'],['cas','Casado/a','Married'],['cab','Cabeza de familia','Head of household']]),
   F('dep','Dependientes','Dependents','number'),
   F('ing','Tipo de ingreso','Type of income','checks',[['w2','Empleo (W-2)','Job (W-2)'],['1099','Cuenta propia (1099)','Self-employed (1099)'],['neg','Negocio','Business'],['renta','Rentas','Rental'],['ext','Del extranjero','Foreign']],'w'),
   F('nuevo','¿Primera vez con nosotros?','First time with us?','select',YN),F('itin','¿Necesitas ITIN?','Need an ITIN?','select',YN)]},
 taxneg:{g:'tax',ic:'📊',es:'Taxes de negocio, contabilidad y nómina',en:'Business taxes, bookkeeping and payroll',
  f:[F('nom','Nombre del negocio','Business name','text',null,'r'),
   F('estr','Estructura','Structure','select',[['llc','LLC','LLC'],['corp','Corporación','Corporation'],['solo','Dueño único','Sole proprietor'],['ns','No sé','Not sure']]),
   F('nec','¿Qué necesitas?','What do you need?','checks',[['tax','Taxes anuales','Annual taxes'],['book','Contabilidad mensual','Monthly bookkeeping'],['pay','Nómina','Payroll'],['sales','Sales tax','Sales tax']],'w'),
   F('emp','Número de empleados','Number of employees','number')]},
 itin:{g:'tax',ic:'🪪',es:'ITIN',en:'ITIN',
  f:[F('cuantos','¿Para cuántas personas?','For how many people?','number',null,'r'),
   F('tipo','¿Nuevo o renovación?','New or renewal?','select',[['nuevo','Nuevo','New'],['ren','Renovación','Renewal']]),
   F('pas','¿Pasaporte vigente?','Valid passport?','select',YN)]},
 llc:{g:'tax',ic:'📑',es:'LLC y licencias',en:'LLC and licenses',
  f:[F('nec','¿Qué necesitas?','What do you need?','checks',[['llc','Crear una LLC','Form an LLC'],['lic','Licencia de negocio','Business license'],['ein','EIN','EIN']],'w'),
   F('act','Tipo de negocio','Type of business'),F('nombre','Nombre que quieres usar','Name you want to use')]},
 trad:{g:'doc',ic:'📝',es:'Traducciones',en:'Translations',
  f:[F('doc','Documento','Document','select',[['lic','Licencia de conducir (para el DMV)','Driver\'s license (for the DMV)'],['nac','Acta de nacimiento','Birth certificate'],['mat','Acta de matrimonio','Marriage certificate'],['dip','Diplomas o notas','Diplomas or transcripts'],['otro','Otro','Other']],'r'),
   F('idioma','De qué idioma a cuál','From which language to which'),F('pag','Número de páginas','Number of pages','number'),
   F('para','¿Para qué lo necesitas?','What is it for?','select',[['dmv','DMV','DMV'],['inm','Inmigración','Immigration'],['corte','Corte','Court'],['otro','Otro','Other']]),
   F('limite','¿Para qué fecha?','By what date?','date')]},
 notaria:{g:'doc',ic:'✒️',es:'Notaría',en:'Notary',
  f:[F('doc','¿Qué documento?','What document?','text',null,'r'),F('firmas','¿Cuántas firmas?','How many signatures?','number'),
   F('fecha','¿Para qué fecha?','By what date?','date')]},
};
const GRUPOS=[['seg','Seguros','Insurance'],['sal','Salud','Health'],['tax','Taxes y negocios','Taxes and business'],['doc','Documentos','Documents']];
const CONTACTO=[
 F('nombre','Nombre','First name','text',null,'r'),F('apellido','Apellido','Last name','text',null,'r'),
 F('tel','Teléfono','Phone','tel',null,'r'),F('correo','Correo','Email','email'),
 F('dir','Dirección','Street address','text',null,'w'),
 F('ciudad','Ciudad','City'),F('zip','Código postal','ZIP code','text',null,'r'),
 F('nac','Fecha de nacimiento','Date of birth','date'),
 F('hora','Mejor hora para llamarte','Best time to call you','select',[['man','Mañana','Morning'],['tar','Tarde','Afternoon'],['cual','Cualquiera','Any time']]),
 F('cliente','¿Ya eres cliente?','Already a client?','select',YN),
];
// ---------- estado
const S={paso:1,sel:[],c:{},d:{},wa:true,ok:false,enviado:false,t0:Date.now()};
const $=s=>app.querySelector(s);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function campo(f,ns,val){
  const id=ns+'.'+f.id, lab=esc(T(f.es,f.en))+(f.opc?' <em>('+T('opcional','optional')+')</em>':'')+(f.req?' *':'');
  let h;
  if(f.type==='select') h=`<select data-k="${id}" ${f.req?'data-r':''}><option value="">—</option>${f.opts.map(o=>`<option value="${o[0]}" ${val===o[0]?'selected':''}>${esc(T(o[1],o[2]))}</option>`).join('')}</select>`;
  else if(f.type==='checks') h=`<div class="q-opts">${f.opts.map(o=>`<label><input type="checkbox" data-k="${id}" value="${o[0]}" ${(val||[]).includes(o[0])?'checked':''}>${esc(T(o[1],o[2]))}</label>`).join('')}</div>`;
  else h=`<input type="${f.type}" data-k="${id}" value="${esc(val||'')}" ${f.req?'data-r':''} ${f.type==='tel'?'inputmode="tel" autocomplete="tel"':''} ${f.type==='number'?'inputmode="numeric"':''}>`;
  return `<div class="q-f ${f.wide?'q-w':''}"><label>${lab}</label>${h}</div>`;
}
const get=(o,k)=>k.split('.').reduce((a,p)=>a==null?a:a[p],o);
function set(o,k,v){const p=k.split('.');let a=o;p.slice(0,-1).forEach(x=>a=a[x]??=(/^\d+$/.test(x)?{}:{}));a[p.at(-1)]=v}
function render(){
  if(S.enviado){app.innerHTML=`<div class="q-spanel q-done"><div class="q-ok">✓</div><h1>${T('Recibimos tu solicitud.','We received your request.')}</h1>
   <p class="lead" style="margin:0 auto">${T('Un especialista de Marrero Bernal Agency te contactará con opciones de varias compañías. Si es urgente, llámanos o escríbenos por WhatsApp al 888-877-2583.','A Marrero Bernal Agency specialist will contact you with options from several companies. If it is urgent, call or WhatsApp us at 888-877-2583.')}</p></div>`;app.scrollIntoView({block:'start'});return}
  const bar=`<div class="q-ssteps">${[1,2,3,4].map(i=>`<i class="${i<=S.paso?'q-on':''}"></i>`).join('')}</div>`;
  let h='';
  if(S.paso===1){
    h=`<div class="kicker">${T('Paso 1 de 4','Step 1 of 4')}</div><h1>${T('¿Qué necesitas?','What do you need?')}</h1><p class="lead">${T('Marca todo lo que quieras cotizar o solicitar. Puedes escoger varios.','Select everything you want a quote or help with. You can choose several.')}</p>${bar}<div class="q-spanel">`+
      GRUPOS.map(g=>`<div class="q-grp">${T(g[1],g[2])}</div><div class="q-tiles">${Object.entries(SERV).filter(([k,s])=>s.g===g[0]).map(([k,s])=>`<button type="button" class="q-tile ${S.sel.includes(k)?'q-on':''}" data-s="${k}"><span>${s.ic}</span>${esc(T(s.es,s.en))}</button>`).join('')}</div>`).join('')+
      `<p class="q-fine">${T('Para Medicare, llámanos al 888-877-2583: lo atendemos por separado.','For Medicare, call us at 888-877-2583: we handle it separately.')}</p></div>`;
  } else if(S.paso===2){
    h=`<div class="kicker">${T('Paso 2 de 4','Step 2 of 4')}</div><h1>${T('Sobre ti','About you')}</h1><p class="lead">${T('Para saber a quién contactar.','So we know who to contact.')}</p>${bar}<div class="q-spanel"><div class="q-srow">${CONTACTO.map(f=>campo(f,'c',S.c[f.id])).join('')}</div>
      <label class="q-chk" style="margin-top:14px"><input type="checkbox" id="wa" ${S.wa?'checked':''}>${T('Ese teléfono tiene WhatsApp','That phone has WhatsApp')}</label></div>`;
  } else if(S.paso===3){
    h=`<div class="kicker">${T('Paso 3 de 4','Step 3 of 4')}</div><h1>${T('Los detalles','The details')}</h1><p class="lead">${T('Mientras más completo, más rápido te respondemos. Lo que no sepas, déjalo en blanco.','The more complete, the faster we answer. Leave blank whatever you don\'t know.')}</p>${bar}<div class="q-spanel">`+
      S.sel.map(k=>{const s=SERV[k],d=S.d[k]??={};
        const reps=(s.rep||[]).map(r=>{const arr=d[r.id]??=[{}];
          return arr.map((it,i)=>`<div class="q-rep"><b>${T(r.es,r.en)} ${i+1}</b>${arr.length>1?`<button type="button" class="q-x" data-del="${k}.${r.id}.${i}">${T('Quitar','Remove')}</button>`:''}<div class="q-srow">${r.f.map(f=>campo(f,`d.${k}.${r.id}.${i}`,it[f.id])).join('')}</div></div>`).join('')+
            (arr.length<r.max?`<button type="button" class="q-add" data-add="${k}.${r.id}">+ ${T('Añadir otro '+r.es.toLowerCase(),'Add another '+r.en.toLowerCase())}</button>`:'');}).join('');
        return `<div class="q-blk"><h2><span>${s.ic}</span>${esc(T(s.es,s.en))}</h2>${reps}<div class="q-srow">${s.f.map(f=>campo(f,`d.${k}`,d[f.id])).join('')}</div>${s.nota?`<p class="q-fine">${T(...s.nota)}</p>`:''}</div>`}).join('')+
      `<div class="q-blk"><div class="q-f q-w"><label>${T('¿Algo más que debamos saber?','Anything else we should know?')}</label><textarea data-k="c.nota">${esc(S.c.nota||'')}</textarea></div></div></div>`;
  } else {
    h=`<div class="kicker">${T('Paso 4 de 4','Step 4 of 4')}</div><h1>${T('Revisa y envía','Review and send')}</h1><p class="lead">${T('No te damos un precio automático: un especialista revisa tu caso y te contacta con opciones.','We don\'t give an automatic price: a specialist reviews your case and contacts you with options.')}</p>${bar}<div class="q-spanel"><div class="q-sum">${esc(resumen())}</div>
      <label class="q-chk" style="margin-top:16px"><input type="checkbox" id="ok" ${S.ok?'checked':''}>${T('Autorizo a Marrero Bernal & Associates a contactarme por llamada, mensaje de texto o WhatsApp sobre esta solicitud.','I authorize Marrero Bernal & Associates to contact me by call, text message or WhatsApp about this request.')}</label>
      <p class="q-fine">${T('Nunca pedimos tu Seguro Social por este formulario. Tus datos van solo a nuestra oficina.','We never ask for your Social Security number on this form. Your information goes only to our office.')}</p></div>`;
  }
  h+=`<div class="q-msg" id="msg"></div><div class="q-snav">${S.paso>1?`<button type="button" class="q-sbtn q-g" id="atras">← ${T('Atrás','Back')}</button>`:''}<button type="button" class="q-sbtn q-p" id="sig">${S.paso<4?T('Continuar','Continue')+' →':T('Enviar solicitud','Send request')}</button></div>`;
  app.innerHTML=h;if(S.movido)app.scrollIntoView({block:'start'});S.movido=true;
}
function leer(){
  app.querySelectorAll('[data-k]').forEach(el=>{const k=el.dataset.k;
    if(el.type==='checkbox'){const cur=get(S,k)||[];const nx=cur.filter(v=>v!==el.value);if(el.checked)nx.push(el.value);set(S,k,nx)}
    else set(S,k,el.value.trim())});
  const wa=$('#wa');if(wa)S.wa=wa.checked;const ok=$('#ok');if(ok)S.ok=ok.checked;
}
function validar(){
  if(S.paso===1&&!S.sel.length)return T('Escoge al menos un servicio.','Choose at least one service.');
  let bad=0;app.querySelectorAll('[data-r]').forEach(el=>{const v=!el.value.trim();el.classList.toggle('q-bad',v);if(v)bad++});
  if(bad)return T('Faltan los campos marcados con *.','Fields marked * are missing.');
  if(S.paso===2&&S.c.tel.replace(/\D/g,'').length<10)return T('Revisa el teléfono: faltan dígitos.','Check the phone number: digits are missing.');
  if(S.paso===4&&!S.ok)return T('Marca la casilla de autorización para enviar.','Check the authorization box to send.');
  return '';
}
function val(f,v){if(v==null||v===''||(Array.isArray(v)&&!v.length))return null;
  if(f.opts){const m=x=>{const o=f.opts.find(o=>o[0]===x);return o?o[1]:x};return Array.isArray(v)?v.map(m).join(', '):m(v)}return v}
function resumen(){ // siempre en español: es lo que lee la oficina
  const out=[];const linea=(f,v)=>{const x=val(f,v);if(x!=null)out.push(`  ${f.es}: ${x}`)};
  out.push('SERVICIOS: '+S.sel.map(k=>SERV[k].es).join(' · '));
  out.push('IDIOMA DEL CLIENTE: '+(L==='es'?'Español':'Inglés'));
  out.push('','CONTACTO');CONTACTO.forEach(f=>linea(f,S.c[f.id]));out.push('  WhatsApp: '+(S.wa?'Sí':'No'));
  S.sel.forEach(k=>{const s=SERV[k],d=S.d[k]||{};out.push('',s.es.toUpperCase());
    (s.rep||[]).forEach(r=>(d[r.id]||[]).forEach((it,i)=>{out.push(` ${r.es} ${i+1}`);r.f.forEach(f=>{const x=val(f,it[f.id]);if(x!=null)out.push(`    ${f.es}: ${x}`)})}));
    s.f.forEach(f=>linea(f,d[f.id]))});
  if(S.c.nota)out.push('','NOTA DEL CLIENTE','  '+S.c.nota);
  return out.join('\n');
}
function enviar(btn){
  const c=S.c,datos={servicios:S.sel.map(k=>SERV[k].es),claves:S.sel,idioma:L,whatsapp:S.wa,
    nombre:c.nombre,apellido:c.apellido,telefono:c.tel,correo:c.correo||'',direccion:c.dir||'',ciudad:c.ciudad||'',zip:c.zip||'',
    nacimiento:c.nac||'',hora:val(CONTACTO.find(f=>f.id==='hora'),c.hora)||'',cliente:c.cliente||'',resumen:resumen(),
    origen:/[?&]app=1/.test(location.search)||window.matchMedia('(display-mode: standalone)').matches?'app':'web',seg:Math.round((Date.now()-S.t0)/1000)};
  btn.disabled=true;btn.textContent=T('Enviando…','Sending…');
  const fd=new FormData();fd.append('action','mba_solicitud');fd.append('datos',JSON.stringify(datos));fd.append('empresa','');
  fetch(app.dataset.ajax,{method:'POST',body:fd,credentials:'same-origin'}).then(r=>r.json()).then(j=>{if(!j||!j.success)throw 0;S.enviado=true;render()})
   .catch(()=>{btn.disabled=false;btn.textContent=T('Enviar solicitud','Send request');$('#msg').textContent=T('No se pudo enviar. Inténtalo otra vez o llámanos al 888-877-2583.','It could not be sent. Try again or call us at 888-877-2583.')});
}
app.addEventListener('click',e=>{
  const t=e.target.closest('button');if(!t)return;
  if(t.dataset.s){const k=t.dataset.s;S.sel=S.sel.includes(k)?S.sel.filter(x=>x!==k):[...S.sel,k];t.classList.toggle('q-on');return}
  if(t.dataset.add){leer();get(S.d,t.dataset.add).push({});render();return}
  if(t.dataset.del){leer();const p=t.dataset.del.split('.');get(S.d,p.slice(0,2).join('.')).splice(+p[2],1);render();return}
  if(t.id==='atras'){leer();S.paso--;render();return}
  if(t.id==='sig'){leer();const m=validar();if(m){$('#msg').textContent=m;return}
    if(S.paso<4){S.paso++;render()}else enviar(t)}
});
(new URLSearchParams(location.search).get('serv')||'').split(',').forEach(k=>{if(SERV[k]&&!S.sel.includes(k))S.sel.push(k)});
render();
})();
</script>

</main>
<?php ob_start(); get_footer(); echo mba_pag_fix(ob_get_clean(), 'es', 'solicitud', 'request'); ?>
