/*********** Data Science, Algorithms and Advanced Software Engineering
 ============ Johnson Temilola ====== [2019/07/16] ====================
 * 
 */


package course;

import java.util.*;

public class Course {
    private static final Comparator Comparator = null;
	private String courseName; //Name of course
    private int numberOfStudents; //Declare array
    private String courseLecturer; //Number of students allowed in course
    
    //constructors
	public Course(String courseName, int numberOfStudents, String courseLecturer) {
		super();
		this.courseName = courseName;
		this.numberOfStudents = numberOfStudents;
		this.courseLecturer = courseLecturer;
	}
    
	public Course(String string, Object object) {
		// TODO Auto-generated constructor stub
	}

	public Course(String string) {
		// TODO Auto-generated constructor stub
	}

	// get and set methods for data fields
	public String getCourseName() {
		return courseName;
	}

	public void setCourseName(String courseName) {
		this.courseName = courseName;
	}

	public int getNumberOfStudents() {
		return numberOfStudents;
	}

	public void setNumberOfStudents(int numberOfStudents) {
		this.numberOfStudents = numberOfStudents;
	}

	public String getCourseLecturer() {
		return courseLecturer;
	}

	public void setCourseLecturer(String courseLecturer) {
		this.courseLecturer = courseLecturer;
	}

	// toString method
	public String toString() {
	       return "CourseName : "+courseName+" Number of Students : "+numberOfStudents+" Course Lecturer: "+courseLecturer;
	}
	
	// Comparator class for the course name
	public static Comparator<Course> courseNameComparator = new Comparator<Course>() {

		public int compare(Course c1, Course c2) {
			String cs1 = c1.getCourseName();
			String cs2 = c2.getCourseName();

			// to ascending order
			return cs1.compareTo(cs2);
		}
	};
	
	
	public static Comparator<Course> studentsComparator = new Comparator<Course>() {

		   public int compare(Course c1, Course c2) {

		   int sort1 = c1.getNumberOfStudents();
		   int sort2 = c2.getNumberOfStudents();

		   // for the ascending order
		   return sort1 - sort2;

		}
	};
	
	public static void main(String[] args) {
	       ArrayList<Course> courses1 = new ArrayList<Course>();
	       courses1.add(new Course("PHP", 10, "Micheal"));
	       courses1.add(new Course("C++", 20, "Dorris"));
	       courses1.add(new Course("Python", 5, "Victor"));
	       courses1.add(new Course("SAP", 2, "Angel"));
	       courses1.add(new Course("C#", 15, "Sandra"));
	       
	       for(Course c: courses1) {
	           System.out.println(c);
	       }
	
	       // sort list according to numberOfStudents
	       System.out.println();
	       Collections.sort(courses1, Course.studentsComparator);
	       for(Course c: courses1) {
	    	   System.out.println(c);
	       }
	       
	       // swap element position 1 of list at position 2
	       System.out.println();
	       Collections.swap(courses1, 0, 1);
	       for(Course c: courses1) {
	           System.out.println(c);
	       }
	       
	       // create arrayList for courses2
	       // using addAll method for courses2 list
	       System.out.println();
	       ArrayList<Course> courses2 = new ArrayList<Course>();
	       courses2.addAll(courses1);
	       for(Course c: courses2) {
	           System.out.println(c);
	       }
	       
	       // add two elements to courses2 
	       System.out.println();
	       courses2.add(new Course("Java 101",55, "Dr. P Green"));
	       courses2.add(new Course("Advanced Programming", 93, "Prof. M Milton"));
	       for(Course c: courses2) {
	           System.out.println(c);
	       }
	       
	       // sort in alphabetical order to the course name
	       System.out.println();
	       Collections.sort(courses2, Course.courseNameComparator);
	       for(Course c: courses2) {
	           System.out.println(c);
	       }
	       
	       // Search for the course “Java 101”
	       for(int i = 0; i<courses2.size(); i++) {
	    	   if(courses2.get(i).getCourseName().equals("Java 101")) {
	    		   System.out.println("Java 101 found on index " + i);
	    		   break;
	    	   }
	      
	       // to determine whether courses1 and courses 2 have any elements in common
	       System.out.println();
	       boolean isCommon = Collections.disjoint(courses1, courses2);
	       System.out.println("There is No Common elements! : "+isCommon);
	       System.out.println();
	       
	       // to get the course with the most and least students
	       Collections.sort(courses2, Course.studentsComparator);
	       System.out.println("Course with minimum no of students : ");
	       System.out.println(courses2.get(0));
	       System.out.println("Course with maximum no of students : ");
	       System.out.println(courses2.get(courses2.size()-1));
	   }
	}
}
	       
	       
	