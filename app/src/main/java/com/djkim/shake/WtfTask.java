package com.djkim.shake;

import android.net.http.AndroidHttpClient;
import android.os.AsyncTask;
import android.widget.EditText;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.json.JSONObject;
import org.xml.sax.XMLReader;

import java.net.URL;

import javax.xml.parsers.SAXParserFactory;

/**
 * Created by jfwong on 7/18/15.
 */
public class WtfTask extends AsyncTask<String, Integer, Void> {
    private Exception exception;


    protected Void doInBackground(String... strs) {
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

            HttpClient httpClient = AndroidHttpClient.newInstance("Android");
            HttpPost httpPost = new HttpPost(url.toURI());

            json = jsonObject.toString();

            StringEntity se = new StringEntity(json);
            httpPost.setEntity(se);
            httpPost.setHeader("Accept", "application/json");
            httpPost.setHeader("Content-type", "application/json");

            HttpResponse httpResponse = httpClient.execute(httpPost);
        } catch (Exception e) {
            this.exception = e;
        }
        return null;
    }

    protected void onProgressUpdate(Integer... progress) {
        System.out.println(progress);
    }



    protected void onPostExecute(Long feed) {
        System.out.println(feed);
    }
}