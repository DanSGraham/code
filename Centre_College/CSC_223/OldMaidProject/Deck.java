import java.util.Random;

public class Deck {
    private Card[] deck = new Card[51];
    private int index = 0;  //next card to be deal
    private Random rand = new Random();

    public Deck() {
		//I copied this code from the test code on my Card class, with a few minor adjustments.
		for (int i = 0, j = 13; i < 52; i++, j++){
			int newRank = i % 13 + 1 ;
			int newSuit = j / 13;
			if (i < 50){
				Card c5 = new Card(newRank, newSuit);
				deck[i] = c5;
			}
			else if (i > 50){
				Card c5 = new Card(newRank, newSuit);
				deck[i-1] = c5;
			}
		}			
	// construct a deck containing all the cards except the Queen of Clubs
	}

    public void shuffle(){
		for (int i = 0; i < 51; i ++){
			int newPosition = rand.nextInt(51);
			Card cardToSwap = deck[i];
			deck[i] = deck[newPosition];
			deck[newPosition] = cardToSwap;
		}
		index = 0;
	}
	//shuffle all the cards and set the index to 0

    public Card deal(){
		if(hasMoreCards()){
			index++;
			return deck[index - 1];
		}
		else{
			return null;
		}
	}
	
    // if there are any more cards left in the deck, return the next one and increment index
    //return null when all the cards have been dealt
	

    public boolean hasMoreCards(){
		if (index < 51){
			return true;
		}
		else{ 
			return false;
		}
	}
	//return true if there are more cards left in the deck, else false

    public static void main(String[] arg){
	Deck myDeck = new Deck();
	    myDeck.shuffle();
	    while (myDeck.hasMoreCards())
			System.out.println(myDeck.deal());
    }
    }
