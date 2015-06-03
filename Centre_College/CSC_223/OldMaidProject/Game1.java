import java.util.Random;
//import ch06.lists.*;

public class Game{
	RefUnsortedList<Player> playerList = new RefUnsortedList();
	Deck gameDeck;
	
	public Game(String players){
		//Precondition:
			//The players are seperated by commas
		String [] playerArray = players.split(", ");
		for(int i = 0; i < playerArray.length; i++){
			playerList.add(new Player(playerArray[i]));
		}
		gameDeck = new Deck();
		gameDeck.shuffle();
		gameDeck.shuffle();
		Card dealt = gameDeck.deal();
		while( dealt != null){
			playerList.reset();
			for(int i = 0; i < playerList.size(); i++){
				if (dealt != null){
					Player currPlayer = playerList.getNext();
					currPlayer.addCard(dealt);
					dealt = gameDeck.deal();
				}
			}
		}
		playerList.reset();
		for(int i = 0; i < playerList.size(); i++){
			Player currPlayer2 = playerList.getNext();
			currPlayer2.DiscardDup();
		}
	}
				
	public Player playGame(){
		playerList.reset();
		RefUnsortedList<Player> winnerList = new RefUnsortedList<Player>();
		Player player2 = playerList.getNext();
		if (player2.getHandSize() == 0){
			winnerList.add(player2);
		}
		Player player1;
		while(playerList.size() > winnerList.size() + 1){
			while(winnerList.contains(player2)){
				player2 = playerList.getNext();
			}
			player1 = player2;
			player2 = playerList.getNext();
			System.out.println(player1);
			System.out.println(player2);
			player1.playOneTurn(player2);
			System.out.println(player1);
			System.out.println(player2);
			if(player1.getHandSize() == 0){
				winnerList.add(player1);
			}
			if(playerList.size() > winnerList.size() + 1){
				if (player2.getHandSize() == 0){
					winnerList.add(player2);
					player2 = playerList.getNext();
				}
			}
		}
		return playerList.getNext();
	}
			
					
		
	
	public static void main(String[] args){
		Game test1 = new Game("Daniel Graham, Colin Wurster, TJ Vance");
		System.out.println(test1.playGame());
	}
}
	
