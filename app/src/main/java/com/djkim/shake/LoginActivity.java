package com.djkim.shake;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.net.MalformedURLException;
import java.net.URL;

public class LoginActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login_page);
    }

    public void signinButtonClicked(View view) {
        EditText email = (EditText)findViewById(R.id.login_id);
        EditText password = (EditText)findViewById(R.id.login_password);
        String emailAddress = email.getText().toString();
        String pass = password.getText().toString();
        String u = "http://172.21.129.192:9000/login";
        String[] args = {"login", u, emailAddress, pass};

        try {
            WtfTask wtfTask = new WtfTask();
            String userType = wtfTask.getDesc();

            Intent applicantIntent = new Intent(this, ApplicantShakeActivity.class);
            startActivity(applicantIntent);
            finish();
        }
        catch(Exception e){
            Toast.makeText(this, "Invalid login credential!", Toast.LENGTH_SHORT).show();
        }
    }

}
