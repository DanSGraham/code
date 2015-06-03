import ch06.lists.*;

public class List2<T> extends ArrayUnsortedList<T> {
  
    public List2(){
	super();}
 
    public List2(int origCap){
	super(origCap);
    }

    public int count(T element){
		if (element != null){
			reset();
			int numCount = 0;
			for(int i = 0; i < size(); i++){
				T compareItem = this.getNext();
				if (compareItem.equals(element)){
					numCount++;
				}
			}
			return numCount;
		}
		else{
			return 0;
		}
	// returns the number of items in the list which equal element
    }
    
    public void removePairs(T element){
		int matches = count(element);
		for (int i = 0; i < (matches/2); i++){
			remove(element);
			remove(element);
		}
// remove any pairs that equal element
    }
    
    public T getAtIndex(int index) throws IndexOutOfBoundsException{
		T item = this.list[index];
		T toReturn = item;
		remove(item);
		return toReturn;
	}		
    	//if index does not correspond to item in the list throus IndexOutOfBoundsException
    	// else remove and return the item at location index
    	// since unordered, just replace the item with the last one and decrement the number of elements
    
         

    public static void main(String[] arg){
		//Test should return:
		/*Six of Spades
		 * Six of Clubs
		 * Six of Hearts
		 * Seven of Spades
		 * Ten of Spades
		 * 3
		 * Six of Hearts
		 * Seven of Spades
		 * Ten of Spades
		 * */
	List2<Card> myList = new List2<Card>();
	myList.add(new Card(6,2));
	myList.add(new Card(6,4));
	myList.add(new Card(6,1));
	myList.add(new Card(7,2));
	myList.add(new Card(10,2));
	System.out.println(myList);
	System.out.println(myList.count(new Card(6,3)));
	myList.removePairs(new Card(6,3));
//add some testing with the queens so that the queen of spades is not removed
	System.out.println(myList);
	
	/* Further Testing.
	 * Should create a larger deck. I anticipate it to return a count one less than number of queens 
	 * but used in the remove method, should be fine. As long as the queen of spades does not need to be counted, it works.
	 * */
	
	myList.add(new Card(12, 1));
	myList.add(new Card(12, 2));
	myList.add(new Card(12, 3));
	myList.add(new Card(12, 4));
	myList.add(new Card(13, 1));
	myList.add(new Card(13, 3));
	myList.add(new Card(1, 1));
	myList.add(new Card(1, 2));
	myList.add(new Card(1, 4));
	myList.add(new Card(7, 1));
	System.out.println(myList.getAtIndex(8));
	System.out.println(myList.count(new Card(12,3)));
	myList.removePairs(new Card(12,3));
	System.out.println(myList.count(new Card(1,3)));
	myList.removePairs(new Card(1,3));
	System.out.println(myList.count(new Card(7,3)));
	myList.removePairs(new Card(7,3));
	System.out.println(myList);

	//The testing produced the expected result. The only possible mistake would be the counting of the queen of spades, 
	//however to change this would require change to the equals function or making the count method much more complex.
	
    }
}

