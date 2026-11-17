package com.marrerobernalmedia.elhome;

import android.os.Bundle;
import android.webkit.WebView;
import androidx.activity.OnBackPressedCallback;
import com.getcapacitor.BridgeActivity;

// Botón Atrás del control remoto: retrocede dentro de la app (show → lista → Inicio).
// Solo cierra la app cuando ya no hay a dónde volver (Inicio).
public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getOnBackPressedDispatcher().addCallback(this, new OnBackPressedCallback(true) {
            @Override
            public void handleOnBackPressed() {
                WebView w = getBridge() != null ? getBridge().getWebView() : null;
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
