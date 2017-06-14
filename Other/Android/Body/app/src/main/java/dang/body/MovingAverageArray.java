package dang.body;

import java.util.Arrays;
import java.util.Calendar;
import java.util.concurrent.TimeUnit;

/**
 * Created by Daniel on 6/12/2017.
 */

public class MovingAverageArray extends CircularArray<Double> {

    final static double SKIPPED_VAL = -1.0;
    long lastDay;
    long currDay;

    public MovingAverageArray(int sizeOfArray){
        super(sizeOfArray);
        Arrays.fill(this.circularArray, SKIPPED_VAL);
        lastDay = -1;
    }

    public double calculateAverage(){
        int totalNum = -1;
        double sum = 0;
        for(int i=0; i < this.size; i++){
            if(((double) this.circularArray[i]) != SKIPPED_VAL){
                totalNum++;
                sum += (double) this.circularArray[i];
            }
        }
        return (sum / totalNum);
    }

    public void add(double data){
        if(lastDay == -1){
            lastDay = TimeUnit.MILLISECONDS.toDays(Calendar.getInstance().getTimeInMillis());
        }
        currDay = TimeUnit.MILLISECONDS.toDays(Calendar.getInstance().getTimeInMillis());
        for(int i=1; i < (currDay - lastDay); i++){
            super.add(SKIPPED_VAL);
        }
        super.add(data);
        lastDay = currDay;
    }

}
