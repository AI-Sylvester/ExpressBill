package com.posapp.id;

import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebSettings;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    // Wait until WebView is ready
    WebView webView = (WebView) this.bridge.getWebView();
    if (webView != null) {
      WebSettings webSettings = webView.getSettings();
      webSettings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
    }
  }
}
