package com.djkim.shake;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Spinner;

/**
 * Created by dongjoonkim on 7/17/15.
 */
public class ApplicantSignupActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.applicant_signup_page);
    }

    public void applicantJoinNowClicked(View view) {

        String fn = ((EditText)findViewById(R.id.applicant_first_name)).getText().toString();
        String ln = ((EditText)findViewById(R.id.applicant_last_name)).getText().toString();
        String pw = ((EditText)findViewById(R.id.applicant_password)).getText().toString();
        String ea = ((EditText)findViewById(R.id.applicant_email_address)).getText().toString();
        String pn = ((EditText)findViewById(R.id.applicant_phone_number)).getText().toString();
        String sc = ((EditText)findViewById(R.id.applicant_school)).getText().toString();
        String ed = ((Spinner)findViewById(R.id.applicant_education_level)).getSelectedItem().toString();
        String gp = ((EditText)findViewById(R.id.applicant_gpa)).getText().toString();
        String sk = ((EditText)findViewById(R.id.applicant_skills_and_projects)).getText().toString();
        String u = "http://172.21.129.192:9000/applicantSignup";

        String[] args = {"applicant", u, fn, ln, pw, ea, pn, sc, ed, gp, sk};
        try {
            new WtfTask().execute(args);
        }
        catch(Exception e){
            Log.e("error", e.getMessage());
        }

        Intent shakeIntent = new Intent(this, ApplicantShakeActivity.class);
        startActivity(shakeIntent);
        finish();
    }
}
