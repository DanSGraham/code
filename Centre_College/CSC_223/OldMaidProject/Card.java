public class Card {
    private int rank;
    private int suit;

    public Card (int r, int s){  // 1 to 13 for rank ; 1 to 4 for Hearts Spades Diamonds and Clubs
		rank = r;
		suit = s;
    }

    public String toString() {
		String rankString = "";
		String suitString = "";
			switch(rank) {
				case 1: 
					rankString = "Ace";
					break;
				case 2:
					rankString = "Two";
					break;
				case 3: 
					rankString = "Three";
					break;
				case 4:
					rankString = "Four";
					break;
				case 5: 
					rankString = "Five";
					break;
				case 6:
					rankString = "Six";
					break;
				case 7: 
					rankString = "Seven";
					break;
				case 8:
					rankString = "Eight";
					break;
				case 9: 
					rankString = "Nine";
					break;
				case 10:
					rankString = "Ten";
					break;
				case 11: 
					rankString = "Jack";
					break;
				case 12:
					rankString = "Queen";
					break;
				case 13:
					rankString = "King";
					break;
				}
			switch (suit){
				case 1:
					suitString = "Hearts";
					break; 
				case 2:
					suitString = "Spades";
					break;
				case 3:
					suitString = "Diamonds";
					break;
				case 4: 
					suitString = "Clubs";
					break;
				}
			return rankString + " of " + suitString;
	// returns a string like "Ace of Hearts"
}
    public boolean equals(Object c) {
		Card newCard = (Card) c;
		if (((rank == newCard.rank) && (!(rank == 12 && suit == 2) && !(newCard.rank == 12 && newCard.suit == 2)) || ((rank == 12 && suit == 2) && (newCard.rank == 12 && newCard.suit == 2)))){ 
			return true;
		}
		else{
			return false;
		}
	}
    	//this will be used for finding pairs to discard
		//the Queen of spades should not equal any other card, others are equal if they have the same rank
	
   

    public static void main(String[] arg) {
    	//you may hae to adjust if your representation is different
    	/* This should output:
    	 * Six of Hearts
    	 * Six of Diamonds
    	 * Queen of Diamonds
    	 * Queen of Spades
    	 * false
    	 * false
    	 * true*/
    	
	Card c1 = new Card(6,1);
	Card c2 = new Card(6,3);
	Card c3 = new Card(12,3);
	Card c4 = new Card(12,2);
	System.out.println(c1);
	System.out.println(c2);
	System.out.println(c3);
	System.out.println(c4);
	System.out.println(c3.equals(c4));
	System.out.println(c4.equals(c3));
	System.out.println(c1.equals(c2));
	
	//Further Testing. Print whole deck of cards.
	
	for (int i = 0, j = 13; i <= 52; i++, j++){
		int newRank = i % 13 + 1 ;
		int newSuit = j / 13;
		Card c5 = new Card(newRank, newSuit);
		System.out.println(c5);
	}
	//Works as expected and prints a whole deck. Only issue is the final line: "Ace of ", however this is due to the suit division by 13 is 5 for the final value, and not because of my class being incorrect.
    }
}
