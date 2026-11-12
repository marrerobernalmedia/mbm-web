// Avisos de OneSignal (si no carga, la app sigue funcionando)
try { importScripts("https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.sw.js"); } catch (e) {}
// El Home de la Risa — service worker: siempre intenta la red primero (así ve lo nuevo) y usa la copia guardada sin conexión
const CACHE = "elhome-v52";
self.addEventListener("install", e => { self.skipWaiting(); e.waitUntil(caches.open(CACHE).then(c => c.addAll(["./", "./index.html", "./data.js", "./manifest.webmanifest", "./icons/icon-192.png"]))); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); });
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  const u = new URL(e.request.url);
  if (u.origin !== location.origin) return;
  const fresh = /\.(html|js|webmanifest)(\?|$)/.test(u.pathname + u.search) || u.pathname.endsWith("/");
  e.respondWith(fetch(e.request, fresh ? { cache: "no-cache" } : {}).then(r => { const c = r.clone(); caches.open(CACHE).then(x => x.put(e.request, c)); return r; })
    .catch(() => caches.match(e.request).then(m => m || caches.match("./index.html"))));
});
