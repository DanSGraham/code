package dang.alfredassistant;

import android.content.Intent;
import android.speech.RecognizerIntent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    protected Intent speechRecognizerIntent;
    private SpeechRecognizerManager mSpeechRecognizerManager;
    private static final String TAG = "MainActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mSpeechRecognizerManager = new SpeechRecognizerManager(this);

    }

    public void OnResult(ArrayList<String> commands){

    }
}
