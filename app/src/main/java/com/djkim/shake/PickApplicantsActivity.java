package com.djkim.shake;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

/**
 * Created by dongjoonkim on 7/18/15.
 */
public class PickApplicantsActivity extends Activity {
    private ArrayList<Applicant> applicantList = Applicant.applicantList();
    private ApplicantsAdapter adapter;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.pick_applicants);

        adapter = new ApplicantsAdapter(this, applicantList);
        // Attach the adapter to a ListView
        listView = (ListView) findViewById(R.id.lv);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener(){
            @Override
            public void onItemClick(AdapterView<?>adapter,View v, int position, long id){
                applicantList.remove(position);
                resetListView();
                Toast.makeText(PickApplicantsActivity.this, "" + position, Toast.LENGTH_SHORT).show();
            }


        });
        listView.setAdapter(adapter);
    }

    private void resetListView() {
        listView.setAdapter(adapter);
    }
}
