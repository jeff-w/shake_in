package com.djkim.shake;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.util.ArrayList;

/**
 * Created by dongjoonkim on 7/18/15.
 */
public class ApplicantsAdapter extends ArrayAdapter<Applicant>
{
    public ApplicantsAdapter(Context context, ArrayList<Applicant> applicants) {
        super(context, 0, applicants);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        Applicant applicant = getItem(position);

        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.applicant_item, parent, false);
        }

        TextView tvName = (TextView) convertView.findViewById(R.id.name);
        TextView tvEmail = (TextView) convertView.findViewById(R.id.email_address);
        TextView tvSchool = (TextView) convertView.findViewById(R.id.school);
        TextView tvgpa = (TextView) convertView.findViewById(R.id.gpa);
        TextView tvSkillsAndProjects = (TextView) convertView.findViewById(R.id.skills_and_projects);

        // Populate the data into the template view using the data object
        tvName.setText(applicant.getFirstName() + " " + applicant.getLastName());
        tvEmail.setText(applicant.getEmailAddress());
        tvSchool.setText(applicant.getSchool());
        tvgpa.setText("GPA: " + String.valueOf(applicant.getGpa()));
        tvSkillsAndProjects.setText(applicant.getSkillsAndProjects());

        // Return the completed view to render on screen
        return convertView;
    }
}
