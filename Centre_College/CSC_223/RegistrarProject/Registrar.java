import java.util.*;
import java.io.*;

public class Registrar{

	BinarySearchTree<Course> theClasses;
	
	public Registrar() {
		theClasses = new BinarySearchTree<Course>();
	}
	
	public void readCourses(String fileName) throws FileNotFoundException{
		String Id;
		int Maximum;
		String courseTitle = "";
		//We used this forum post: http://stackoverflow.com/questions/6082586/how-to-read-a-text-file-using-scanner-in-java as a guide to using the Scanner to read .txt files.
		File inputFile = new File(fileName);
		Scanner in = new Scanner(inputFile);
		while (in.hasNextLine()){
			String courseInfo = in.nextLine();
			Id = courseInfo.getNext();
			Maximum = courseInfo.nextInt();
			while (courseInfo.hasNext()){
				courseTitle += courseInfo.getNext();
			}
			addCourse(Id, Maximum, courseTitle);
		}
	}
		

	public void addCourse(String courseId, int max, String title) {
		Course newCourse = Course(courseId, max, title);
		theClasses.add(newCourse);
	}
	
	public void deleteCourse(Course toBeRemoved) {
		theClasses.remove(toBeRemoved);
	}
	
	public void printStudentsByCourse(String courseId) {
		Course c = new Course(courseId,1,"Dummy");
		Course c2 = theClasses.get(c);
		System.out.println(c2.getEnrolled());
	}
	
	public void printEnrollments() {
		theClasses.reset(1);
		int numClasses = theClasses.size();
		Course c;
		for (int i =0; i < numClasses; i++) {
			c = theClasses.getNext(1);
			System.out.println("" + c.getTitle() + " " + c.getEnrolled().size());
		}
	}
	
	void registerStudent(String firstName, String lastName, int nCourses) {
		//Precondition: User input is correct and accurate.
		Scanner inputCourse;
		for(int i = 0; i < nCourses; i++){
			System.out.println("Enter the course id for the course to add");
			inputCourse = new Scanner(System.in);
			String inputId = inputCourse.nextLine();
			addStudentToCourse(firstName, lastName, inputId);
		}
			
	}
	
	public void addStudentToCourse(String firstName, String lastName, String courseId){
		//Precondition: Course exists.
		Student studentToAdd = new Student(firstName, lastName);
		Course dummyCourse = new Course(courseId, 1, "dummy");
		Course toAddCourse = theClasses.get(dummyCourse);
		toAddCourse.addStudent(studentToAdd);
	}
	public void dropStudentFromCourse(String firstName, String lastName, String courseId){
		//Preconditoin: Course exists and student in course.
		Student studentToDrop = new Student(firstName, lastName);
		Course dummyCourse = new Course(courseId, 1, "dummy");
		Course toDropCourse = theClasses.get(dummyCourse);
		toDropCourse.removeStudent(studentToDrop);
	}
}
