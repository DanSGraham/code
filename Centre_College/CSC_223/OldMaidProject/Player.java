import java.util.Random;
import ch06.lists.*;

public class Player {

    private String name;
    private List2<Card> hand = new List2<Card>();
    private Random rand = new Random();

    public Player(String aName){
		name = aName;

    }
    public String toString(){
		String format = name + "\n" + hand;
		return format;
	}
	    
    public String getName(){
		return name;

    }
    
    public boolean equals(Object p){
		Player compareP = (Player) p;
		if(getName() == compareP.getName()){
			return true;
		}
		else{
			return false;
		}
	}

   
    public int getHandSize() {
		return hand.size();
    }

    public void addCard(Card c){
		hand.add(c);
    }
    
    public Card getCard(int i){
		return hand.getAtIndex(i);
    	
    }
    
    public void DiscardDup(){//I recieved help from Colin Wurster and Adrienne on this segment.
		int startingSize = this.getHandSize();
		Card addCard;
		Card compareCard;
		hand.reset();
		List2<Card> handCopy = new List2<Card>();
		for(int k = 0; k < startingSize; k++){
			addCard = hand.getNext();
			handCopy.add(addCard);
		}
		hand.reset();
		for(int k = 0; k < startingSize; k++){
			compareCard = handCopy.getNext();
			hand.removePairs(compareCard);
		}
}	
    
    
    
    public void playOneTurn(Player p){
		if(p.hasCardLeft() && this.hasCardLeft()){
			int cardToSelect = rand.nextInt(p.getHandSize());
			Card cardToAdd = p.getCard(cardToSelect);
			System.out.println(this.getName() + " chooses the " + cardToAdd + "\n");
			hand.add(cardToAdd);
			DiscardDup();
		}
    	// the current player finds out how many cards the opponent has and selects a random location
    	// and asks for that card from the other player
    	// that card is added to the player's hand and then the player checks if that made a pair
    	// the pair is removed if necessary
	}
    	
	
    
    
    public boolean hasCardLeft(){
		if (hand.size() > 0){
			return true;
		}
		else{
			return false;
		}
	// returns true or false depending on whether the player still has some cards left in the hand
}
   

//TESTING.
/* Should Return:
 * Bobby
 * List:
 * 		CARDS
 * Bobby
 * List:
 * 		CARDS WITHOUT PAIRS
 * Susie
 * List:
 * 		CARDS
 * Bobby:
 * List:
 * 		CARDS with one added
 * Susie
 * List:
 * 		Cards with the one added to Bobby removed
 * 
 * Bobby:
 * List:
 * 		CARDS with one added
 * Susie
 * List:
 * 		Cards with the one added to Bobby removed
 * */

    public static void main(String[] arg){
	Player p1 = new Player("Bobby");
	p1.addCard(new Card(6,1));
	p1.addCard(new Card(6,2));
	p1.addCard(new Card(7,2));
	p1.addCard(new Card(13,3));
	p1.addCard(new Card(2,3));
	p1.addCard(new Card(2,4));
	p1.addCard(new Card(13,2));
	p1.addCard(new Card(4,3));
	p1.addCard(new Card(9,3));
	p1.addCard(new Card(11,1));
	p1.addCard(new Card(1,2));
	p1.addCard(new Card(8,1));
	p1.addCard(new Card(8,2));
	System.out.println(p1);
	p1.DiscardDup();
	System.out.println(p1);
	
	Player p2 = new Player("Susie");
	p2.addCard(new Card(13,4));
	p2.addCard(new Card(12,2));
	p2.addCard(new Card(7,4));
	p2.addCard(new Card(11,4));
	p2.addCard(new Card(8,4));
	p2.addCard(new Card(10,4));
	System.out.println(p2);
	p1.playOneTurn(p2);
	System.out.println(p1);
	System.out.println(p2);
	p2.playOneTurn(p1);
	System.out.println(p1);
	System.out.println(p2);
    }
}
