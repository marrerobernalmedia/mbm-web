package com.marrerobernalmedia.recta;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.InputMethodManager;
import android.webkit.JavascriptInterface;
import android.content.Context;
import android.webkit.WebView;
import android.widget.FrameLayout;
import androidx.activity.OnBackPressedCallback;
import androidx.webkit.WebViewCompat;
import androidx.webkit.WebViewFeature;
import java.util.HashSet;
import java.util.Arrays;
import com.getcapacitor.BridgeActivity;
import com.getcapacitor.BridgeWebChromeClient;

// App de Android TV de Recta Al Pecho.
// 1) Pantalla completa de verdad para el video (Capacitor la trae apagada): el video va directo a la pantalla,
//    sin pasar por la página, y así no parpadea (TCL, 17-nov-2026).
// 2) Botón Atrás del control: primero sale del video, después retrocede dentro de la app (serie → lista → Inicio)
//    y solo cierra la app desde Inicio.
public class MainActivity extends BridgeActivity {

    // Insiste 60 s por video: YouTube a veces entrega la lista de audios después de arrancar, o vuelve al original
    private static final String AUDIO_JS =
        "(function(){if(!/^\\/embed\\//.test(location.pathname))return;" +
        "var want=(new URLSearchParams(location.search).get('hl')||'').slice(0,2).toLowerCase();if(!want)return;" +
        "function meta(t){for(var k in t){var v=t[k];if(v&&typeof v==='object'&&typeof v.id==='string'&&('isDefault' in v))return v;}return {};}" +
        "function lang(t){var m=meta(t);var id=(m.id||'').slice(0,2).toLowerCase();if(id)return id;return /english|ingl/i.test(m.name||'')?'en':'';}" +
        "var st={},last='';setInterval(function(){try{var p=document.getElementById('movie_player');if(!p||!p.getAvailableAudioTracks)return;" +
        "var vd=p.getVideoData&&p.getVideoData();var vid=vd&&vd.video_id;if(!vid)return;" +
        "if(vid!==last){last=vid;st[vid]={t:Date.now()};}var s=st[vid];if(Date.now()-s.t>60000)return;" +
        "if(lang(p.getAudioTrack())===want)return;" +
        "var av=p.getAvailableAudioTracks()||[];var t=av.find(function(x){return lang(x)===want;});" +
        "if(t)p.setAudioTrack(t);}catch(e){}},600);})();";

    private View videoView = null;
    private android.webkit.WebChromeClient.CustomViewCallback videoCallback = null;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        final WebView web = getBridge() != null ? getBridge().getWebView() : null;
        if (web != null) {
            // Teclado en pantalla: la página lo pide al entrar al cuadro de búsqueda (en el TV no sale solo)
            web.addJavascriptInterface(new Object() {
                @JavascriptInterface
                public void teclado() {
                    runOnUiThread(() -> {
                        web.requestFocus();
                        InputMethodManager imm = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
                        if (imm != null) imm.showSoftInput(web, InputMethodManager.SHOW_FORCED);
                    });
                }
            }, "MBMNative");
            // Audio en inglés: si la app está en inglés (el reproductor lleva hl=en), dentro del reproductor de YouTube
            // se escoge la pista de audio en inglés cuando el video la tiene (Eliam, 17-nov-2026)
            if (WebViewFeature.isFeatureSupported(WebViewFeature.DOCUMENT_START_SCRIPT)) {
                try {
                    WebViewCompat.addDocumentStartJavaScript(web, AUDIO_JS, new HashSet<>(Arrays.asList(
                        "https://www.youtube.com", "https://www.youtube-nocookie.com")));
                } catch (Exception e) {}
            }
            web.setWebChromeClient(new BridgeWebChromeClient(getBridge()) {
                @Override
                public void onShowCustomView(View view, CustomViewCallback callback) {
                    if (videoView != null) { callback.onCustomViewHidden(); return; }
                    videoView = view;
                    videoCallback = callback;
                    view.setBackgroundColor(Color.BLACK);
                    ViewGroup decor = (ViewGroup) getWindow().getDecorView();
                    decor.addView(view, new FrameLayout.LayoutParams(
                        ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
                    view.requestFocus();
                }

                @Override
                public void onHideCustomView() {
                    if (videoView == null) return;
                    ViewGroup decor = (ViewGroup) getWindow().getDecorView();
                    decor.removeView(videoView);
                    videoView = null;
                    if (videoCallback != null) { try { videoCallback.onCustomViewHidden(); } catch (Exception e) {} }
                    videoCallback = null;
                    web.requestFocus();
                    // Al salir de la pantalla completa también se cierra el reproductor y se vuelve a la página
                    web.evaluateJavascript("try{window.MBP&&window.MBP.close()}catch(e){}", null);
                }
            });
        }

        getOnBackPressedDispatcher().addCallback(this, new OnBackPressedCallback(true) {
            @Override
            public void handleOnBackPressed() {
                WebView w = getBridge() != null ? getBridge().getWebView() : null;
                if (videoView != null && w != null) {
                    // Sale de la pantalla completa (la página cierra el reproductor)
                    w.evaluateJavascript("try{document.exitFullscreen&&document.exitFullscreen()}catch(e){}", null);
                    return;
                }
                if (w != null && w.canGoBack()) {
                    w.goBack();
                } else {
                    setEnabled(false);
                    getOnBackPressedDispatcher().onBackPressed();
                    setEnabled(true);
                }
            }
        });
    }
}
