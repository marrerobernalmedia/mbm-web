import Foundation
import Capacitor
import WebKit
import OneSignalFramework

// Avisos de estreno con OneSignal nativo (en la app de iPhone la web no puede usar los avisos del navegador).
// La web (nativo.js) llama iniciar({appId}) con el ID de OneSignal que ya usa la web; se guarda para arrancar
// OneSignal desde el primer instante en las próximas aperturas.
@objc(MbmAvisosPlugin)
public class MbmAvisosPlugin: CAPPlugin, CAPBridgedPlugin {
    public let identifier = "MbmAvisosPlugin"
    public let jsName = "MbmAvisos"
    public let pluginMethods: [CAPPluginMethod] = [
        CAPPluginMethod(name: "iniciar", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "estado", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "pedir", returnType: CAPPluginReturnPromise),
        CAPPluginMethod(name: "etiqueta", returnType: CAPPluginReturnPromise)
    ]
    private static let clave = "mbm_onesignal_app_id"
    private static var iniciado = false

    // Audio en el idioma de la app: el reproductor de YouTube lleva hl=en cuando la app está en inglés; dentro de su
    // marco se escoge la pista de audio en ese idioma si el video la tiene (igual que en la app de TV; Eliam, 18-nov-2026).
    private static let audioJS = #"""
    (function(){if(!/(^|\.)youtube(-nocookie)?\.com$/.test(location.hostname))return;if(!/^\/embed\//.test(location.pathname))return;
    var want=(new URLSearchParams(location.search).get('hl')||'').slice(0,2).toLowerCase();if(!want)return;
    function meta(t){for(var k in t){var v=t[k];if(v&&typeof v==='object'&&typeof v.id==='string'&&('isDefault' in v))return v;}return {};}
    var done={};setInterval(function(){try{var p=document.getElementById('movie_player');if(!p||!p.getAvailableAudioTracks)return;
    var vd=p.getVideoData&&p.getVideoData();var vid=vd&&vd.video_id;if(!vid||done[vid])return;
    var av=p.getAvailableAudioTracks()||[];if(!av.length)return;
    var cur=(meta(p.getAudioTrack()).id||'').slice(0,2).toLowerCase();if(cur===want){done[vid]=1;return;}
    var t=av.find(function(x){return (meta(x).id||'').slice(0,2).toLowerCase()===want;});
    if(!t){done[vid]=1;return;}if(p.setAudioTrack(t))done[vid]=1;}catch(e){}},700);})();
    """#

    override public func load() {
        DispatchQueue.main.async {
            guard let web = self.bridge?.webView else { return }
            web.configuration.userContentController.addUserScript(
                WKUserScript(source: MbmAvisosPlugin.audioJS, injectionTime: .atDocumentStart, forMainFrameOnly: false))
        }
        if let id = UserDefaults.standard.string(forKey: MbmAvisosPlugin.clave), !id.isEmpty {
            arrancar(id)
        }
    }

    private func arrancar(_ id: String) {
        if MbmAvisosPlugin.iniciado { return }
        MbmAvisosPlugin.iniciado = true
        DispatchQueue.main.async {
            OneSignal.initialize(id, withLaunchOptions: nil)
        }
    }

    @objc func iniciar(_ call: CAPPluginCall) {
        guard let id = call.getString("appId"), !id.isEmpty else { call.reject("Falta appId"); return }
        UserDefaults.standard.set(id, forKey: MbmAvisosPlugin.clave)
        arrancar(id)
        call.resolve()
    }

    @objc func estado(_ call: CAPPluginCall) {
        DispatchQueue.main.async {
            if !MbmAvisosPlugin.iniciado { call.resolve(["permiso": false, "suscrito": false]); return }
            call.resolve([
                "permiso": OneSignal.Notifications.permission,
                "suscrito": OneSignal.User.pushSubscription.optedIn
            ])
        }
    }

    @objc func pedir(_ call: CAPPluginCall) {
        DispatchQueue.main.async {
            if !MbmAvisosPlugin.iniciado { call.resolve(["permiso": false]); return }
            if OneSignal.Notifications.permission {
                OneSignal.User.pushSubscription.optIn()
                call.resolve(["permiso": true])
                return
            }
            OneSignal.Notifications.requestPermission({ ok in
                call.resolve(["permiso": ok])
            }, fallbackToSettings: true)
        }
    }

    // Etiqueta en OneSignal (p. ej. grabacion_cuero_t1 = confirmada) para avisar solo a quienes reservaron
    @objc func etiqueta(_ call: CAPPluginCall) {
        guard let k = call.getString("clave"), let v = call.getString("valor") else { call.reject("Faltan datos"); return }
        DispatchQueue.main.async {
            if MbmAvisosPlugin.iniciado { OneSignal.User.addTag(key: k, value: v) }
            call.resolve()
        }
    }
}
