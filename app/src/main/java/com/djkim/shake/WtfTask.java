package com.djkim.shake;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.net.http.AndroidHttpClient;
import android.os.AsyncTask;
import android.widget.EditText;
import android.widget.Toast;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.json.JSONObject;
import org.xml.sax.XMLReader;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;

import javax.xml.parsers.SAXParserFactory;

/**
 * Created by jfwong on 7/18/15.
 */
public class WtfTask extends AsyncTask<String, Integer, HttpResponse> {
    private Exception exception;
    private String userID;
    private String desc;

    protected HttpResponse doInBackground(String... strs) {
        HttpResponse resp = null;
        try {
            URL url = new URL(strs[1]);
            String json = "";
            JSONObject jsonObject = new JSONObject();

            if(strs[0].equals("login")){
                String em = strs[2];
                String pw = strs[3];

                jsonObject.accumulate("emailAddress", em);
                jsonObject.accumulate("password", pw);
            }
            else if(strs[0].equals("applicant")){
                jsonObject.accumulate("firstName", strs[2]);
                jsonObject.accumulate("lastName", strs[3]);
                jsonObject.accumulate("password", strs[4]);
                jsonObject.accumulate("emailAddress", strs[5]);
                jsonObject.accumulate("phoneNumber", strs[6]);
                jsonObject.accumulate("school", strs[7]);
                jsonObject.accumulate("eduLevel", strs[8]);
                jsonObject.accumulate("GPA", strs[9]);
                jsonObject.accumulate("skills", strs[10]);
            }
            else if(strs[0].equals("recruiter")){
                jsonObject.accumulate("firstName", strs[2]);
                jsonObject.accumulate("lastName", strs[3]);
                jsonObject.accumulate("password", strs[4]);
                jsonObject.accumulate("emailAddress", strs[5]);
                jsonObject.accumulate("phoneNumber", strs[6]);
                jsonObject.accumulate("company", strs[7]);
            }
            else if(strs[0].equals("recruiterShake")){
                jsonObject.accumulate("latitude", strs[2]);
                jsonObject.accumulate("longitude", strs[3]);
            }
            else if(strs[0].equals("applicantShake")){
                jsonObject.accumulate("latitude", strs[2]);
                jsonObject.accumulate("longitude", strs[3]);
            }

            HttpClient httpClient = AndroidHttpClient.newInstance("Android");
            HttpPost httpPost = new HttpPost(url.toURI());

            json = jsonObject.toString();

            StringEntity se = new StringEntity(json);
            httpPost.setEntity(se);
            httpPost.setHeader("Accept", "application/json");
            httpPost.setHeader("Content-type", "application/json");

            resp = httpClient.execute(httpPost);
        } catch (Exception e) {
            this.exception = e;
        }
        return resp;
    }

    protected void onProgressUpdate(Integer... progress) {

    }



    protected void onPostExecute(HttpResponse resp) {
        try {
            StringBuilder builder = new StringBuilder();
            HttpEntity e = resp.getEntity();
            if (e != null) {
                InputStream inputStream = e.getContent();
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
                for (String line = null; (line = bufferedReader.readLine()) != null; ) {
                    builder.append(line).append("\n");
                }
                JSONObject jsonObject = new JSONObject(builder.toString());

                userID = jsonObject.getString("userID");
                desc = jsonObject.getString("desc");
            }
        }
        catch(Exception e){
            //lol
        }
    }

    public String getDesc() {
        return desc;
    }
}