package dang.alfredassistant;

import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.speech.SpeechRecognizer;
import android.util.Log;
import android.widget.Toast;

import java.util.Dictionary;
import java.util.HashMap;

/**
 * Created by Daniel on 6/11/2017.
 */

public class SpeechRecognizerManager {
    private static final String KWS_SEARCH = "wakeup";
    private static final String WAKE_UP_PHRASE = "Hello Alfred";
    private android.speech.SpeechRecognizer offlineGSpeechRecognizer;
    protected Intent offlineGSpeechRecognizerIntent;
    private android.speech.SpeechRecognizer onlineGSpeechRecognizer;
    protected Intent onlineGSpeechRecognizerIntent;
    private static final String TAG = SpeechRecognizerManager.class.getSimpleName();
    private Context currContext;
    protected Boolean offlineListening;
    protected Boolean delibCalledStop;

    public SpeechRecognizerManager(Context context){
        this.currContext = context;
        offlineListening = false;
        initOfflineGRecognizer();
        //initOnlineGRecognizer();
    }

    private void restartOfflineListen(){
        if (offlineListening == true) {
            delibCalledStop = true;
            offlineGSpeechRecognizer.stopListening();
            offlineListening = false;
        }
        offlineGSpeechRecognizer.startListening(offlineGSpeechRecognizerIntent);
        offlineListening = true;
        delibCalledStop = true;


    }
    private void initOfflineGRecognizer(){


        offlineGSpeechRecognizer = android.speech.SpeechRecognizer
                .createSpeechRecognizer(currContext);
        offlineGSpeechRecognizerIntent = new Intent (
                RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        offlineGSpeechRecognizerIntent.putExtra(
                RecognizerIntent.EXTRA_PARTIAL_RESULTS, true);
        offlineGSpeechRecognizerIntent.putExtra(
                RecognizerIntent.EXTRA_PREFER_OFFLINE, true);
        offlineGSpeechRecognizerIntent.putExtra(
                RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        Toast.makeText(currContext, "2", Toast.LENGTH_SHORT).show();
        offlineGSpeechRecognizer.setRecognitionListener(new OfflineGoogleRecognitionListener());
        restartOfflineListen();
    }

    protected class OfflineGoogleRecognitionListener implements
            android.speech.RecognitionListener {

        private final String TAG = OfflineGoogleRecognitionListener.class.getSimpleName();
        private HashMap<String, String> keywordsDict = new HashMap<String, String>();

        @Override
        public void onReadyForSpeech(Bundle params) {

        }

        @Override
        public void onBeginningOfSpeech() {

        }

        @Override
        public void onRmsChanged(float rmsdB) {

        }

        @Override
        public void onBufferReceived(byte[] buffer) {
            Toast.makeText(currContext, "5", Toast.LENGTH_SHORT).show();

        }

        @Override
        public void onEndOfSpeech() {
            Toast.makeText(currContext, "ENDSPEECH", Toast.LENGTH_SHORT).show();
            restartOfflineListen();
        }

        @Override
        public void onError(int error) {
            if (!delibCalledStop) {
                Toast.makeText(currContext, "ERR: " + error, Toast.LENGTH_SHORT).show();
            }
            restartOfflineListen();
        }

        @Override
        public void onResults(Bundle results) {


            String text = results.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION).get(0);
            Toast.makeText(currContext, "You said: " + text, Toast.LENGTH_SHORT).show();
            restartOfflineListen();
        }

        @Override
        public void onPartialResults(Bundle partialResults) {
            if (partialResults == null){
                restartOfflineListen();
                return;
            }

            String text = partialResults.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION).get(0);
            Toast.makeText(currContext, "You said: " + text, Toast.LENGTH_SHORT).show();
            restartOfflineListen();
            /**
            if (text.contains(WAKE_UP_PHRASE)) {
                Toast.makeText(currContext, "You said: " + text, Toast.LENGTH_SHORT).show();
            }**/
        }

        @Override
        public void onEvent(int eventType, Bundle params) {

        }

        public void addKeyphrase(String Key, String Value){
            keywordsDict.put(Key, Value);
        }
    }
}
