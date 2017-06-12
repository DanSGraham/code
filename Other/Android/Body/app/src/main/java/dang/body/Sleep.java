package dang.body;

import java.util.ArrayList;

/**
 * Created by Daniel on 6/12/2017.
 */

public class Sleep {
    ArrayList<Double> sleepHours;

    public Sleep(){
        this.sleepHours = new ArrayList<Double>();
    }

    public void addSleep(double amntSleep){
        this.sleepHours.add(amntSleep);
    }

    public double getDay(int dayBack){
        double rtnVal = 0;
        if (dayBack < this.sleepHours.size()){
            rtnVal = this.sleepHours.get(this.sleepHours.size() - 1 - dayBack);
        }
        return rtnVal;
    }

    public double getLastNight(){
        return getDay(0);
    }

    public double weekMA(){
        double sum = 0.0;
        for(int i = 0; i < 7; i++){
            sum += getDay(i);
        }
        return (sum / 7.0);
    }

    public double monthMA(){
        double sum = 0.0;
        for(int i = 0; i < 30; i++){
            sum += getDay(i);
        }
        return (sum / 30.0);
    }

    public double threeMonthMA(){
        double sum = 0.0;
        for(int i = 0; i < 91; i++){
            sum += getDay(i);
        }
        return (sum / 91.0);
    }

    public double sixMonthMA(){
        double sum = 0.0;
        for(int i = 0; i < 183; i++){
            sum += getDay(i);
        }
        return (sum / 183.0);
    }

    public double nineMonthMA(){
        double sum = 0.0;
        for(int i = 0; i < 274; i++){
            sum += getDay(i);
        }
        return (sum / 274.0);
    }

    public double twelveMonthMA(){
        double sum = 0.0;
        for(int i = 0; i < 365; i++){
            sum += getDay(i);
        }
        return (sum / 365.0);
    }
}
