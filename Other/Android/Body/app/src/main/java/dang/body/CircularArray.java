package dang.body;

/**
 * Created by Daniel on 6/12/2017.
 */

public class CircularArray<E> {
        int size;
        int current;
        E[] circularArray;

    public CircularArray(int sizeOfArray){
        this.size = sizeOfArray;
        this.current = 0;
        this.circularArray = (E[]) new Object[sizeOfArray];
        }

    public void add(E data){
        this.current = (this.current % this.size);
        this.circularArray[this.current] = data;
        this.current += 1;
        }

}
