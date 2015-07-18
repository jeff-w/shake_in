package com.djkim.shake;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

/**
 * Created by dongjoonkim on 7/17/15.
 */
public class SignupActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.signup_page);
    }

    public void recruiterButtonClicked(View view) {
        Intent recruiterIntent = new Intent(this, RecruiterSignupActivity.class);
        startActivity(recruiterIntent);
    }

    public void applicantButtonClicked(View view) {
        Intent applicantIntent = new Intent(this, ApplicantSignupActivity.class);
        startActivity(applicantIntent);
    }
}
