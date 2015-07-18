package com.djkim.shake;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;


public class MainActivity extends Activity {
    final String PREFS_NAME = "prefs_file";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_page);
    }


    public void joinNowClicked(View view) {
        Intent signUpIntent = new Intent(this, SignupActivity.class);
        startActivity(signUpIntent);
    }

    public void signInClicked(View view) {
        Intent loginIntent = new Intent(this, LoginActivity.class);
        startActivity(loginIntent);
    }
}
