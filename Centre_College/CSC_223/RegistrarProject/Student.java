import java.util.*;

public class Student implements Comparable<Student>{
	String firstName;
	String lastName;
	
	public Student(String fName, String lName){
		
		firstName = fName;
		lastName = lName;
		
	}
	
	public String getFirstName(){
		return firstName;
	}
	
	public String getLastName(){
		return lastName;
	}
	
	public boolean equals(Object other){
		
		Student castOther = (Student) other;
		return (this.getFirstName() == castOther.getFirstName() 
				&& this.getLastName() == castOther.getLastName());
			}
	public int compareTo(Student castOther){
		
		if (this.getLastName() == castOther.getLastName()){
			return (this.getFirstName().compareTo(castOther.getFirstName()));
		}
		else{
			return (this.getLastName().compareTo(castOther.getLastName()));
		}
	}
	public String toString(){
			
			return (this.getFirstName() + " " + this.getLastName());
		}
		
	public static void main(String[] args){
		/* The output of this testing should be as follows:
		 * 1
		 * 1
		 * 1
		 * 0
		 * -1
		 * false
		 * David Newton
		 * */
		Student test1, test2, test3, test4;
		test1 = new Student("David", "Newton");
		test2 = new Student("David", "Neil");
		test3 = new Student("Daniel", "Newton");
		test4 = new Student("Thomas", "Becker");
		System.out.println(test1.compareTo(test2));
		System.out.println(test1.compareTo(test3));
		System.out.println(test1.compareTo(test4));
		System.out.println(test1.compareTo(test1));
		System.out.println(test3.compareTo(test1));
		System.out.println(test1.equals(test3));
		System.out.println(test1);
		
		/* The output was:
		 * 14
		 * 8
		 * 12
		 * 0
		 * -8
		 * false
		 * David Newton
		 * 
		 * This differed because the String compareTo returns the difference in the ascii values not only positive or negative difference.
		 * We can use the methods as is however, because when we check our compareTo, we will check positive or negative which was successfully returned.*/
	}
		
	}

