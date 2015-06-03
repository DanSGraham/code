package com.danielgraham.originalintelligentinsults;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import com.danielgraham.originalintelligentinsults.MainActivity;
import com.danielgraham.originalintelligentinsults.InsultsDatabase;
import com.danielgraham.originalintelligentinsults.SettingsActivity;
import com.danielgraham.originalintelligentinsults.R;

import android.support.v7.app.ActionBarActivity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnLongClickListener;
import android.widget.TextView;

public class MainActivity extends ActionBarActivity {
	
	//ALL PUBLICALLY ACCESSABLE ITEMS NEED TO GO HERE
		public List<String> selectedTypes, insultTypes;
		public List<String[][]> selectedCategories, insultCategories;
		
		public void initializeLists(){
				//INITIALIZE ALL ITEMS HERE!
				insultTypes = new ArrayList<String>();
				insultCategories = new ArrayList<String[][]>();
				selectedTypes = new ArrayList<String>();
				selectedCategories = new ArrayList<String[][]>();
				insultTypes.add("Noun");
				insultTypes.add("Verb");
				insultTypes.add("Phrase");
				insultCategories.add(InsultsDatabase.shakespeare);
				insultCategories.add(InsultsDatabase.science);
				insultCategories.add(InsultsDatabase.english);
				insultCategories.add(InsultsDatabase.biblical);
			}
		
	    public static int randInt(int min, int max){

	        Random rand = new Random();

	        int randomNum = rand.nextInt((max-min) +1) + min;

	        return randomNum;
	    }
	    
	    public String returnInsultType(List<String> types){
	    	if (types.size() == 0){
	    		return "VOID";
	    	}
	    	int typeInt = randInt(0, types.size() - 1);
	    	return types.get(typeInt);	
	    }
	    	
	    public String[][] returnInsultCategory(String type, List<String[][]> category){
	    	if (type == "VOID"){
	    		return new String[][]{
	    				{"Please Select An Insult Type!@@TAG@@-DSG"},
	    				{"Please Select An Insult Type!@@TAG@@-DSG"},
	    				{"Please Select An Insult Type!@@TAG@@-DSG"},
	    				{"Please Select An Insult Type!@@TAG@@-DSG"}
	    		};
	    	}
	    	if (category.size() == 0){
	    		return new String[][] {
	    				{"Please Select An Insult Category!@@TAG@@-DSG"},
	    				{"Please Select An Insult Category!@@TAG@@-DSG"},
	    				{"Please Select An Insult Category!@@TAG@@-DSG"},
	    				{"Please Select An Insult Category!@@TAG@@-DSG"}
	    		};
	    	}
	    	int emptyCat = 0;
	    	
	    	for (String[][] cat: category){
	    		if ((type == "Noun" && cat[1].length == 0) || (type == "Verb" && cat[2].length == 0) || (type == "Phrase" && cat[3].length == 0)){
	    			emptyCat = emptyCat + 1;
	    		}
	    	}
	    	if(emptyCat == category.size()){
	    		return new String[][]{
						{"No insults met your requirements! Change settings to get insults!@@TAG@@-DSG"},
						{"No insults met your requirements! Change settings to get insults!@@TAG@@-DSG"},
						{"No insults met your requirements! Change settings to get insults!@@TAG@@-DSG"},
						{"No insults met your requirements! Change settings to get insults!@@TAG@@-DSG"}
					};
	    	}
	    	while (true){
	    		int catInt = randInt(0,category.size() - 1);
	    		String[][] tempCat = category.get(catInt);
	    		if (!((type == "Noun" && tempCat[1].length == 0) || (type == "Verb" && tempCat[2].length == 0) || (type == "Phrase" && tempCat[3].length == 0))){
	    			return tempCat;
	    		}
	    	
	    		}
	    	}
	    
	    public String returnInsult(String typeIns, String[][] catIns){
	    	if (typeIns.equals("Noun")){
	    		int insIntN = randInt(0, catIns[1].length - 1);
	    		return catIns[1][insIntN];
	    	}
	    	if (typeIns.equals("Verb")){
	    		int insIntV = randInt(0, catIns[2].length - 1);
	    		return catIns[2][insIntV];
	    	}
	    	if (typeIns.equals("Phrase")){
	    		int insIntP = randInt(0, catIns[3].length - 1);
	    		return catIns[3][insIntP];
	    		}
	    	else{
	    		return "Please Select at least one Insult Type!@@TAG@@-DSG";
	    	}
	    }
	    
	    public void updateSelectedLists(){
	    	selectedTypes.clear();
	    	selectedCategories.clear();
	    	SharedPreferences allPreferences = PreferenceManager.getDefaultSharedPreferences(getBaseContext());
	    	for(String type : insultTypes){
	    		if (allPreferences.getBoolean(type,true)){
	    			selectedTypes.add(type);
	    		}
	    	}
	    	for (String[][] cat: insultCategories){
	    		if (allPreferences.getBoolean(cat[0][0], true)){
	    			selectedCategories.add(cat);
	    		}
	    	}
	    }
	    
	    public void openSettings(){
	    	Intent myIntent = new Intent(MainActivity.this, SettingsActivity.class);
	    	startActivity(myIntent); 
	    }
	    
	    public void showInsult(View view){
	    	 String selType = returnInsultType(selectedTypes);
	         String[][] selCategory = returnInsultCategory(selType, selectedCategories);
	         String insult = returnInsult(selType, selCategory);
	    	 TextView newInsult = (TextView)findViewById(R.id.newInsult);
	    	 TextView author = (TextView)findViewById(R.id.insultAuthor);
	         newInsult.setText(insult.substring(0,insult.indexOf("@@TAG@@")));
	         author.setText(insult.substring(insult.indexOf("@@TAG@@") + 7));
	         
	    }    
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
        View homepage = findViewById(R.id.insultsHomepage);
        initializeLists();
        updateSelectedLists();
        homepage.setOnLongClickListener(new OnLongClickListener() {
            public boolean onLongClick(View arg0) {
            	//HERE WE USE Intent to start preference activity.
            	openSettings();
                return true;                         
            }
        });
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

    @Override
    public void onResume() {
        super.onResume();  // Always call the superclass method first

        updateSelectedLists();
    }
    
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
		if (id == R.id.action_settings) {
			openSettings();
			return true;
		}
		return super.onOptionsItemSelected(item);
	}
}
