package com.djkim.shake;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.ArrayList;

/**
 * Created by dongjoonkim on 7/18/15.
 */
public class PickApplicantsActivity extends Activity {
    private ArrayList<Applicant> applicantList = Applicant.applicantList();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.pick_applicants);

        ApplicantsAdapter adapter = new ApplicantsAdapter(this, applicantList);
        // Attach the adapter to a ListView
        ListView listView = (ListView) findViewById(R.id.lv);
        listView.setAdapter(adapter);
    }
}
