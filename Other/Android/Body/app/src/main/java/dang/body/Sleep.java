package dang.body;

import android.support.v4.util.CircularArray;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.concurrent.TimeUnit;

/**
 * Created by Daniel on 6/12/2017.
 * TODO: Add Sleep this week so far, and Sleep this Month so far.
 */

public class Sleep {
    double daySleep;
    MovingAverageArray weekMA, monthMA, threeMonthMA, sixMonthMA, nineMonthMA, yearMA;
    long lastUpdated;

    public Sleep() {
        this.daySleep = 0.0;
        this.weekMA = new MovingAverageArray(7);
        this.monthMA = new MovingAverageArray(30);
        this.threeMonthMA = new MovingAverageArray(91);
        this.sixMonthMA = new MovingAverageArray(182);
        this.nineMonthMA = new MovingAverageArray(273);
        this.yearMA = new MovingAverageArray(365);
        this.lastUpdated = -1;
    }

    public void addSleep(double amntSleep) {
        this.lastUpdated = TimeUnit.MILLISECONDS.toDays(Calendar.getInstance().getTimeInMillis());
        this.daySleep = amntSleep;
        this.weekMA.add(amntSleep);
        this.monthMA.add(amntSleep);
        this.threeMonthMA.add(amntSleep);
        this.sixMonthMA.add(amntSleep);
        this.nineMonthMA.add(amntSleep);
        this.yearMA.add(amntSleep);
    }

    public double[] getMovingAverages(){
        double WMA, MMA, TMMA, SMMA, NMMA, YMA;
        WMA = this.weekMA.calculateAverage();
        MMA = this.monthMA.calculateAverage();
        TMMA = this.threeMonthMA.calculateAverage();
        SMMA = this.sixMonthMA.calculateAverage();
        NMMA = this.nineMonthMA.calculateAverage();
        YMA = this.yearMA.calculateAverage();
        double[] rtnList = {WMA, MMA, TMMA, SMMA, NMMA, YMA};
        return rtnList;
    }

    public double getDaySleep(){
        double rtnVal = -1.0;
        if(this.lastUpdated == TimeUnit.MILLISECONDS.toDays(Calendar.getInstance().getTimeInMillis())){
            rtnVal = this.daySleep;
        }
        return rtnVal;
    }
}
