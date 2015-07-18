package com.djkim.shake;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

/**
 * Created by dongjoonkim on 7/17/15.
 */
public class RecruiterSignupActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.recruiter_signup_page);
    }

    // TODO: Check if all of the fields are filled out and send all of the data to the server and get the USER_ID
    public void recruiterJoinNowClicked(View view) {
        Intent shakeIntent = new Intent(this, RecruiterShakeActivity.class);
        startActivity(shakeIntent);
        finish();
    }
}
