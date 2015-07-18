package com.djkim.shake;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.widget.Toast;

/**
 * Created by dongjoonkim on 7/18/15.
 */
public class RecruiterShakeActivity extends Activity {
    private SensorManager mSensorManager;

    private float xAccel;
    private float yAccel;
    private float zAccel;

    private float xPreviousAccel;
    private float yPreviousAccel;
    private float zPreviousAccel;

    private boolean firstUpdate = true;

    private final float shakeThreshold = 10.0f;

    private boolean shakeInitiated = false;

    private double longitude;
    private double latitude;

    private final SensorEventListener mSensorEventListener = new SensorEventListener() {
        @Override
        public void onSensorChanged(SensorEvent event) {
            updateAccelParameters(event.values[0], event.values[1], event.values[2]);
            if ((!shakeInitiated) && isAccelerationChanged()) {
                shakeInitiated = true;
            } else if ((shakeInitiated) && isAccelerationChanged()) {
                executeShakeAction();
            } else if ((shakeInitiated) && (!isAccelerationChanged())) {
                shakeInitiated = false;
            }
        }

        @Override
        public void onAccuracyChanged(Sensor sensor, int accuracy) {

        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.recruiter_shake_page);

        mSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        mSensorManager.registerListener(mSensorEventListener, mSensorManager
                        .getDefaultSensor(Sensor.TYPE_ACCELEROMETER),
                SensorManager.SENSOR_DELAY_NORMAL);

        GPSTracker gpsTracker = new GPSTracker(this);
        if (gpsTracker.getIsGPSTrackingEnabled())
        {
            longitude = gpsTracker.getLongitude();
            latitude = gpsTracker.getLatitude();
        }
        else
        {
            Toast.makeText(this, "Location tracking is not available", Toast.LENGTH_SHORT).show();
        }
    }

    /* Store the acceleration values given by the sensor */
    private void updateAccelParameters(float xNewAccel, float yNewAccel, float zNewAccel) {
        if (firstUpdate) {
            xPreviousAccel = xNewAccel;
            yPreviousAccel = yNewAccel;
            zPreviousAccel = zNewAccel;
            firstUpdate = false;
        } else {
            xPreviousAccel = xAccel;
            yPreviousAccel = yAccel;
            zPreviousAccel = zAccel;
        }
        xAccel = xNewAccel;
        yAccel = yNewAccel;
        zAccel = zNewAccel;
    }

    private boolean isAccelerationChanged() {
        float deltaX = Math.abs(xPreviousAccel - xAccel);
        float deltaY = Math.abs(yPreviousAccel - yAccel);
        float deltaZ = Math.abs(zPreviousAccel - zAccel);
        return (deltaX > shakeThreshold && deltaY > shakeThreshold)
                || (deltaX > shakeThreshold && deltaZ > shakeThreshold)
                || (deltaY > shakeThreshold && deltaZ > shakeThreshold);
    }

    private void executeShakeAction() {
        Toast.makeText(this, "" + latitude + " " + longitude, Toast.LENGTH_SHORT).show();
        shakeInitiated = false;
        mSensorManager.unregisterListener(mSensorEventListener);
        Intent pickApplicantsIntent = new Intent(this, PickApplicantsActivity.class);
        startActivity(pickApplicantsIntent);

        //POST with lat/long


        finish();
    }
}
