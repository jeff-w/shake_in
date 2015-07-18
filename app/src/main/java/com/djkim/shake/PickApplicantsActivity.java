package com.djkim.shake;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
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
            public void onItemClick(AdapterView<?>adapter,View v, final int position, long id){
                new AlertDialog.Builder(PickApplicantsActivity.this)
                        .setTitle("Delete entry")
                        .setMessage("Are you sure you want to delete this candidate from the pool?")
                        .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int which) {
                                // continue with delete
                                Toast.makeText(PickApplicantsActivity.this, applicantList.get(position).getFirstName() + " " + applicantList.get(position).getLastName() + " has been removed from the applicant pool.", Toast.LENGTH_SHORT).show();
                                applicantList.remove(position);
                                resetListView();
                            }
                        })
                        .setNegativeButton(android.R.string.no, new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int which) {
                                // do nothing
                            }
                        })
                        .setIcon(android.R.drawable.ic_dialog_alert)
                        .show();
            }


        });
        listView.setAdapter(adapter);
    }

    private void resetListView() {
        listView.setAdapter(adapter);
    }
}
