package dang.exercise;

import java.util.ArrayList;

/**
 * Created by Daniel on 6/13/2017.
 */

public class CustomExercise {

    public String name;
    public ArrayList<ArrayList<Double>> sets;
    public ArrayList<Double> rep;

    public CustomExercise(String name){
        this.name = name;
        this.rep = new ArrayList<Double>();
        this.sets = new ArrayList<>();
    }

    public void addRep(Double val){
        this.rep.add(val);
    }

    public void addSet(){
        this.sets.add(this.rep);
        this.rep.clear();
    }

    public ArrayList<ArrayList<Double>> getSets(){
        return this.sets;
    }

}
