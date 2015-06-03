package com.daniel.intelligentinsults;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;
import java.util.Random;


public class ShowInsult extends ActionBarActivity {

    public static int randInt(int min, int max){

        Random rand = new Random();

        int randomNum = rand.nextInt((max-min) +1) + min;

        return randomNum;
    }
    private String[] insults = {"ur dumb", "fartsniffer"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        int firstInsultNum = randInt(0,1);
        String insult = insults[firstInsultNum];
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_show_insult);

        TextView newInsult = (TextView)findViewById(R.id.newInsult);
        newInsult.setText(insult);

    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.show_insult, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
    public void getNewInsult(View view){
        int firstInsultNum = randInt(0,1);
        String insult = insults[firstInsultNum];
        TextView newInsult = (TextView)findViewById(R.id.newInsult);
        newInsult.setText(insult);
    }


}
