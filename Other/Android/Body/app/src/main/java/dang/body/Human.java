package dang.body;

/**
 * Created by Daniel on 6/11/2017.
 */

public class Human {
    Nutrients myNutrients;
    Sleep mySleep;
    Exercise myExercise;


    double weight;  //In lbs
    double height;  //In Feet

    public Human(){

        /** Arrays formatted:
         * [Day, Week Rolling Average, Month Rolling Average, 3, 6, 9, 12 Month Rolling Averages,
         *  Week Total so far, Month total so far]
         *
         *  Week starts on Sunday.
         */
        this.myNutrients = new Food[10];
        this.mySleep = new Sleep();

        /** Arrays formatted:
         * [Day1, Day2, Day3, Day4, Day5, Day6, Day7]
         * Likely store as other.
         */
        this.exerciseArray = new Exercise[10];


        this.weight = 0.0;
        this.height = 0.0;
    }

    public void sleep(double amountOfSleep){
        this.mySleep.addSleep(amountOfSleep);
    }
}
