import ch06.lists.*

public class PlayerList extends RefUnsortedList<Player>{
	public Player loser;
	
	public PlayerList(){
		super();
		}
		
	public void removeWinners(){
		//Precondition: The List is not empty
		PlayerList tempList = new PlayerList();
		for(int i = 0; i < size(); i++){
			Player toAdd = this.getNext();
			tempList.add(toAdd);
		}
		tempList.reset();
		for(int k = 0; k < tempList.size(); k++){
			Player checkPlayer = tempList.getNext();
			if(!checkPlayer.hasCardLeft()){
				remove(checkPlayer);
			}
		}
	}
	
	public boolean gameOver(){
		reset();
		if(size() == 1){
			loser = getNext();
			return true;
		}
		else{
			return false;
		}
	}
	
	public Player getLoser(){
		//Precondition: There is a loser;
		return loser;
	}
}
		
			
		
		
	
