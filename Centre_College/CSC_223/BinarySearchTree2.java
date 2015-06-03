//John Daniel
//Daniel Graham

//import ch08.trees.*;
//import support.*;
import java.util.Random;
import java.lang.Math;

public class BinarySearchTree2<T extends Comparable<T>>extends BinarySearchTree<T>{

    public BinarySearchTree2(){
	super();
    }

    public int height(){
	if(root!=null){
	    return recHeight(root);
	}
	else{
	    System.out.println("height() called on empty tree");
	    return -1;
	}
    }

    private int recHeight(BSTNode<T> t){
	if(t.getLeft()==null&&t.getRight()==null){
	    return 0;
	}

	if(t.getLeft()==null){
	    return recHeight(t.getRight())+1;
	}
	if(t.getRight()==null){
	    return recHeight(t.getLeft())+1;
	}
	if(recHeight(t.getLeft())>recHeight(t.getRight())){
	    return recHeight(t.getLeft())+1;
	}
	else{
	    return recHeight(t.getRight())+1;
	}
    }

    public static BinarySearchTree2<Integer> buildIntTree(int size){
	int[] used=new int[size*2+1];
	BinarySearchTree2<Integer> test=new BinarySearchTree2<Integer>();
	Random rand=new Random();
	for(int i=0;i<(size*2);i++){
	    used[i]=0;
	}
	for(int i=1;i<=size;i++){
	    int r=rand.nextInt(size*2);
	    while(used[r]!=0){
		r=rand.nextInt(size*2);
	    }
	    used[r]=1;
	    test.add(r);
	    //System.out.println(r);
	}
	return test;
    }   

    public static double avgSize(int size){
	double sum = 0.000;
	double N = 200.000;
	int[] vals=new int[1001]; //this array is used to keep track of number of arrays for the histogram
					// ignore for exp 2
	for(int i=0;i<=1000;i++){  //sets all locations in array equal to zero
	    vals[i]=0;
	}
	for(int j = 0; j<N; j++){
	    int n=buildIntTree(size).height();
	    vals[n]+=1; //everytime a tree of n size appears, is tallied in the array
	    sum+=n;
	}
	for(int k=0;k<1001;k++){
	    if(vals[k]!=0){
		System.out.println(k+" :"+vals[k]); //prints all values of array
	    }
	}
	return(sum/N);
    }
	   
	
	

    public static void main(String[] args){
		for ( int j = 0; j<20; j++){
		    System.out.println("Avg T Size of 1000 Nodes+ : "+(avgSize(1000)));
        }
	for(int i=0;i< 6;i++){
	    int n=(int)(25*Math.pow(2,i));
	    System.out.println("Avg T Size "+n+": "+(avgSize(n)));
        }
  //comment out for exp 2 and also comment out stuff in avgSize class, unucomment for loop to run for exp 2 (note the the second to lsat one takes like 5 minutes to run and the last one takes like 15 just message me if you want my data for those 2)

    }

}

