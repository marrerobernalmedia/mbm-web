import Foundation
import Capacitor
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

    override public func load() {
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
