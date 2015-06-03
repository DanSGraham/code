//import ch06.lists.*
public class Course implements Comparable<Course>{
	
	String courseId;
	String Title;
	int max;
	RefSortedList<Student> enrolled;
	
	public Course(String id, int maxEnroll, String courseTitle){
		
		max = maxEnroll;
		courseId = id;
		Title = courseTitle;
		enrolled = new RefSortedList<Student>();
		
	}
	
	public String getId(){
		return courseId;
	}
	
	public String getTitle(){
		return Title;
	}
	
	public int getMax(){
		return max;
	}
	
	public RefSortedList<Student> getEnrolled(){
		return enrolled;
	}
	
	
	public boolean addStudent(Student newStudent){
		if (enrolled.size() < max){
		enrolled.add(newStudent);
		return true;
	}
	else{
		System.out.println("ERROR: Course Student Limit Reached!");
		return false;
	}
	}
	
	public boolean removeStudent(Student oldStudent){
		return enrolled.remove(oldStudent);
	}
	
	public boolean equals(Object o){
		Course otherCourse = (Course) o;
		return (this.getId() == otherCourse.getId());
	}
	
	public int compareTo(Course compareCourse){
		return(this.getId().compareTo(compareCourse.getId()));
	}
	
	public String toString(){
		return( getTitle() + ":\n" + getEnrolled());
	}
	
	public static void main(String[] args){
		/*The expected output of this test method should be :
		 * Philosophy of Alien Cultures:
		 * List:
		 * David Neil
		 * David Newton
		 * 
		 * 
		 * -------Testing Compare and Equals---------
		 * 
		 * -value
		 * +value
		 * 0
		 * false
		 * true
		 * 
		 * 
		 * ----------Testing Remove-------
		 * 
		 * Philosophy of Alien Cultures:
		 * List:
		 * David Newton*/
		 
		Student test1, test2, test3, test4;
		test1 = new Student("David", "Newton");
		test2 = new Student("David", "Neil");
		test3 = new Student("Daniel", "Newton");
		test4 = new Student("Thomas", "Becker");
		Course testC1, testC2, testC3;
		testC1 = new Course("CHE361", 3, "Inorganic Chemistry");
		testC2 = new Course("PHI800", 2, "Philosophy of Alien Cultures");
		testC3 = new Course("ART100",3,  "Coloring inside the Lines");
		testC1.addStudent(test3);
		testC2.addStudent(test1);
		testC2.addStudent(test2);
		testC3.addStudent(test4);
		System.out.println(testC2);
		System.out.println();
		System.out.println();
		System.out.println("-------Testing Compare and Equals-------");
		System.out.println();
		System.out.println();
		System.out.println(testC1.compareTo(testC2));
		System.out.println(testC2.compareTo(testC3));
		System.out.println(testC1.compareTo(testC1));
		System.out.println(testC1.equals(testC2));
		System.out.println(testC1.equals(testC1));
		System.out.println();
		System.out.println();
		System.out.println("-------Testing Remove-------");
		System.out.println();
		testC2.removeStudent(test2);
		System.out.println(testC2);
		
		//Testing gave expected output.
	}
}
