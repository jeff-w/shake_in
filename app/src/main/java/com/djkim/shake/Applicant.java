package com.djkim.shake;

import android.support.annotation.NonNull;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

/**
 * Created by dongjoonkim on 7/18/15.
 */
public class Applicant {
    private String firstName;
    private String lastName;
    private String emailAddress;
    private long phoneNumber;
    private String school;
    private String education;
    private float gpa;
    private String skillsAndProjects;

    public Applicant(String fn, String ln, String ea, String sc, float gp, String sap) {
        firstName = fn;
        lastName = ln;
        emailAddress = ea;
        school = sc;
        gpa = gp;
        skillsAndProjects = sap;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getEmailAddress() {
        return emailAddress;
    }

    public long getPhoneNumber() {
        return phoneNumber;
    }

    public String getSchool() {
        return school;
    }

    public String getEducation() {
        return education;
    }

    public float getGpa() {
        return gpa;
    }

    public String getSkillsAndProjects() {
        return skillsAndProjects;
    }

    public static ArrayList<Applicant> applicantList() {
        ArrayList<Applicant> returnList = new ArrayList<Applicant>();
        Applicant DJ = new Applicant("DJ", "Kim", "djkim@shakein.com", "UCLA", 4.0f, "C++, C, Java, Android Programming");
        returnList.add(DJ);
        Applicant Jeffrey = new Applicant("Jeffrey", "Wong", "jeffrey@shakein.com", "UCLA", 2.3f, "I really don't know how to do anything");
        returnList.add(Jeffrey);
        Applicant Kevin = new Applicant("Kevin", "Lu", "kevinluissohot@shakein.com", "What is school?", 0.1f, "I am so funny");
        returnList.add(Kevin);
        return returnList;
    }
}
