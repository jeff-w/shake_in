package com.djkim.shake;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

/**
 * Created by dongjoonkim on 7/17/15.
 */
public class RecruiterSignupActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.recruiter_signup_page);
    }

    public void recruiterJoinNowClicked(View view) {

        String em = ((EditText)findViewById(R.id.recruiter_email_address)).getText().toString();
        String pw = ((EditText)findViewById(R.id.recruiter_password)).getText().toString();
        String fn = ((EditText)findViewById(R.id.recruiter_first_name)).getText().toString();
        String ln = ((EditText)findViewById(R.id.recruiter_last_name)).getText().toString();
        String pn = ((EditText)findViewById(R.id.recruiter_phone_number)).getText().toString();
        String cp = ((EditText)findViewById(R.id.recruiter_company)).getText().toString();
        String u = "http://172.21.129.192:9000/recruiterSignup";

        String[] args = {"recruiter", u, em, pw, fn, ln, pn, cp};
        try {
            WtfTask wtfTask = new WtfTask();
            wtfTask.execute(args);
            Intent shakeIntent = new Intent(this, RecruiterShakeActivity.class);
            startActivity(shakeIntent);
            finish();
        }
        catch(Exception e){
            Log.e("error", e.getMessage());
        }
    }
}
