package com.marrerobernalmedia.elhome;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;
import android.widget.FrameLayout;
import androidx.activity.OnBackPressedCallback;
import com.getcapacitor.BridgeActivity;
import com.getcapacitor.BridgeWebChromeClient;

// App de Android TV de El Home de la Risa.
// 1) Pantalla completa de verdad para el video (Capacitor la trae apagada): el video va directo a la pantalla,
//    sin pasar por la página, y así no parpadea (TCL, 17-nov-2026).
// 2) Botón Atrás del control: primero sale del video, después retrocede dentro de la app (show → lista → Inicio)
//    y solo cierra la app desde Inicio.
public class MainActivity extends BridgeActivity {

    private View videoView = null;
    private android.webkit.WebChromeClient.CustomViewCallback videoCallback = null;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        final WebView web = getBridge() != null ? getBridge().getWebView() : null;
        if (web != null) {
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
