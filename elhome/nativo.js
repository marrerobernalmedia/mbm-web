// Puente con la app de iPhone/iPad (Capacitor). En el navegador y en la app de Android no hace nada.
// Mismo archivo en elhome/nativo.js y recta/nativo.js: si cambias uno, copia el otro.
(() => {
  const C = window.Capacitor;
  if (!C || !C.isNativePlatform || !C.isNativePlatform()) return;
  document.documentElement.classList.add("app-nativa");

  // Dentro de la app no se ofrece "instalar la app" ni "pantalla de inicio" (la página ya lo hace cuando está instalada)
  const mm = window.matchMedia.bind(window);
  window.matchMedia = q => /display-mode:\s*standalone/.test(q)
    ? { matches: true, media: q, onchange: null, addEventListener() {}, removeEventListener() {}, addListener() {}, removeListener() {}, dispatchEvent() { return false; } }
    : mm(q);
  const st = document.createElement("style");
  st.textContent = 'html.app-nativa a[href*="marrerobernalmedia.com/apps"],html.app-nativa #appBtn,html.app-nativa #instBtn{display:none!important}';
  document.head.appendChild(st);

  // Compartir con el menú del iPhone
  const Share = C.Plugins && C.Plugins.Share;
  if (Share) navigator.share = d => Share.share({ title: d && d.title, text: d && d.text, url: d && d.url, dialogTitle: d && d.title }).then(() => {});

  // Avisos de estreno: en la app van por OneSignal nativo (plugin MbmAvisos), no por los avisos del navegador.
  // Se imita la parte de la API web de OneSignal que usa index.html, así la página no cambia.
  const Av = C.Plugins && C.Plugins.MbmAvisos, appId = window.ONESIGNAL_APP_ID;
  const est = { permiso: false, suscrito: false }, ls = [];
  const avisar = () => ls.forEach(f => { try { f(); } catch (e) {} });
  const leer = () => Av ? Av.estado().then(r => { est.permiso = !!r.permiso; est.suscrito = !!r.suscrito; avisar(); }).catch(() => {}) : Promise.resolve();
  const pedir = () => Av ? Av.pedir().then(leer).catch(() => {}) : Promise.resolve();
  const OS = {
    init: async () => {},
    Notifications: { get permission() { return est.permiso; }, requestPermission: pedir, addEventListener: (e, f) => ls.push(f) },
    User: { addTag: (k, v) => { if (Av && Av.etiqueta) Av.etiqueta({ clave: String(k), valor: String(v) }).catch(() => {}); }, PushSubscription: { get optedIn() { return est.suscrito; }, optIn: pedir, addEventListener: (e, f) => ls.push(f) } }
  };
  const cola = [];
  Object.defineProperty(cola, "push", { writable: false, value: fn => { try { const r = fn(OS); if (r && r.catch) r.catch(() => {}); } catch (e) {} return 0; } });
  try { Object.defineProperty(window, "OneSignalDeferred", { configurable: false, get: () => cola, set: () => {} }); } catch (e) {}
  if (Av && appId) Av.iniciar({ appId }).then(leer).catch(() => {});
  document.addEventListener("visibilitychange", () => { if (!document.hidden) leer(); });
})();
