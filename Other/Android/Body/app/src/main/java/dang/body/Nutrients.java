package dang.body;

import java.util.HashMap;

/**
 * Created by Daniel on 6/12/2017.
 * TODO: Connect with Food Application.
 */

public class Nutrients {

    int calories;
    //Macronutrients in g.
    double protein, carbohydrates, dietary_fiber, added_sugar, fat;

    //Macronutrient Breakdown
    double saturated_fat, monounsaturated_fat, polyunsaturated_fat, linoleic_acid,
        a_linolenic_acid, omega_3_epa, omega_3_dha, cholesterol;
    //Micronutrients in g
    //Minerals
    double calcium, iron, magnesium, phosphorus, potassium,
            sodium, zinc, copper, manganese, selenium;

    //Vitamins
    double vitamin_a, vitamin_e, vitamin_d, vitamin_c, thiamin, riboflavin,
        niacin, vitamin_b6, vitamin_b12, choline, vitamin_k, folate;

    HashMap<String, Double> nutrientMap;



    public Nutrients(){

    }

}
