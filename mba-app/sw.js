// App de Marrero Bernal: guarda la pantalla principal para que abra aunque falle la red.
// Siempre intenta primero la red, así los cambios se ven enseguida.
const C = 'mba-app-v8';
const SHELL = ['./', 'index.html', 'logo.svg', 'logo-es.svg', 'manifest.webmanifest', 'icons/icon-192.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(C).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(k => Promise.all(k.filter(x => x !== C).map(x => caches.delete(x)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const r = e.request; if (r.method !== 'GET' || new URL(r.url).origin !== location.origin) return;
  // La página se pide siempre fresca al servidor (el iPad se quedaba con la copia vieja, 18-nov-2026)
  const req = (r.mode === 'navigate' || /\/(index\.html)?$/.test(new URL(r.url).pathname)) ? new Request(r.url, { cache: 'no-cache', credentials: 'same-origin' }) : r;
  e.respondWith(fetch(req).then(res => { if (res.ok) { const cp = res.clone(); caches.open(C).then(c => c.put(r, cp)); } return res; }).catch(() => caches.match(r).then(m => m || caches.match('./'))));
});
