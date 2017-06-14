package dang.food;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Daniel on 6/12/2017.
 */

public class Food {

    public HashMap<String, Double> nutrients;
    public String foodGroup;
    public double mass;
    public double costPerGram;
    public static final String APIKEY="AFC2Sauy5464490EsyZHCUekMYI1iuc7Hzi1Wd9x";

    public Food(String nameOfFood){
        //Search the UDSDA Database for the food and nutrition profile
        //If found update the nutrients profile to be for standard mass of food




    }

    public void updateMass(double mass){
        //Update the mass of food and corresponding nutrients
    }

    public void updateCost(double cost){
        //Update the cost of the food item per gram.
    }

    public void add(Food foodToAdd){
        for(Map.Entry<String, Double> entry : foodToAdd.nutrients.entrySet()){
            String key = entry.getKey();
            Double value = entry.getValue();
            this.nutrients.put(key, (this.nutrients.get(key) + value));
        }
    }


}
