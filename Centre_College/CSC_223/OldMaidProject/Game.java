import java.util.Random;
import ch06.lists.*;

public class Game{
	PlayerList playerList = new PlayerList();
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
		System.out.println(playerList + "\n");
		playerList.reset();
		for(int i = 0; i < playerList.size(); i++){
			Player currPlayer2 = playerList.getNext();
			currPlayer2.DiscardDup();
		}
		System.out.println(playerList + "\n");
		playerList.removeWinners();
	}
	

				
	public String play(){
		boolean endGame = !playerList.gameOver();
		Player player2 = playerList.getNext();
		Player player1;
		System.out.println("Begin Game \n");
		while(endGame){
			for( int i = 0; i < playerList.size(); i++){
				player1 = player2;
				player2 = playerList.getNext();
				player1.playOneTurn(player2);
				System.out.println(player1 + "\n");
				}
				playerList.removeWinners();
				endGame = !playerList.gameOver();
				player2 = playerList.getNext();
			}
		return playerList.getLoser().getName();
	}
			
					
		
	
	public static void main(String[] args){
		//Names are seperated by ", " for games with multple players.
		Game test1 = new Game("Daniel Graham, Batman");
		System.out.println(test1.play() + " is the Loser! :(" );
	}
}
	
