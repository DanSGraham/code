import java.io.*;
import java.util.*;


public class QuickSort {
	Integer[] initialArray, sortedArray;
	
	public QuickSort(String filename) throws NumberFormatException, IOException{
		BufferedReader in;
		
		String nextLine;
		int arraySize;
		
		//Initialization Step
		in = new BufferedReader(new FileReader(filename));
		
		arraySize = Integer.parseInt(in.readLine());
		initialArray = new Integer[arraySize];
		sortedArray = new Integer[arraySize];
		
		
		//Read in the text into an initial array.
		nextLine = in.readLine();
		
		int arrayPos = 0;
		while(nextLine != null){
			initialArray[arrayPos] = Integer.parseInt(nextLine);
			arrayPos ++;
			nextLine = in.readLine();
			System.out.println("TEST");
		}
		
		//Sort the initial array with quicksort to sortedArray
		sortedArray = recurseSort(initialArray);
		
		
	}
	
	
	//Code from http://stackoverflow.com/questions/80476/how-can-i-concatenate-two-arrays-in-java
	public Integer[] concat(Integer[] a, Integer[] b) {
		   int aLen = a.length;
		   int bLen = b.length;
		   Integer[] c= new Integer[aLen+bLen];
		   System.arraycopy(a, 0, c, 0, aLen);
		   System.arraycopy(b, 0, c, aLen, bLen);
		   return c;
		}
	
	
	private Integer[] recurseSort(Integer[] integersList){
		
		
		if (integersList.length <= 1){
			return integersList;
		}
		else{
		System.out.println(integersList.length);	
			 ArrayList <Integer> smallerOrEqual, largerList;
			 Integer[] smallerSorted, largerSorted;
			 
			 smallerOrEqual = new ArrayList<Integer>();
			 largerList = new ArrayList<Integer>();
			 
			 int pivot = integersList[integersList.length - 1];
			 for (int i = 0; i < integersList.length - 1; i++){
				 if(integersList[i] > pivot){
					 largerList.add(integersList[i]);
				 }
				 else{
					 smallerOrEqual.add(integersList[i]);
				 }
				}
				 smallerOrEqual.add(pivot);
			 
			 smallerSorted = recurseSort(smallerOrEqual.toArray(new Integer[smallerOrEqual.size()]));
			 largerSorted  = recurseSort(largerList.toArray(new Integer[largerList.size()]));
			 return concat(smallerSorted, largerSorted);
			 }
	}
	
	public static void main(String[] args){
		try {
			QuickSort example = new QuickSort(args[0]);
			System.out.println(example.sortedArray);
		} catch (NumberFormatException | IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}
}
