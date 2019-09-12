/*************** DATA SCIENCE, ALGORITHMS AND ADVANCED SOFTWARE ENGINEERING - [TASK 7] ********************
 * ************* JOHNSON TEMILOLA  - [2019/07/16] ************
 *  
 *  A program that can be used by a bookstore clerk. 
 *  The program should allow the clerk to:
 *  enter new books into the database
 *  update book information
 *  delete books from the database
 *  search the database to find a specific book
 *  
 *  The program should perform the function that the user selects
 *  The program should present the user with the following menu:
    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    0. Exit
 *  
 */

import java.sql.*;
import java.util.Scanner;

public class BookStoreClerk {

	public static void main ( String[] args) {

		try (
				// Allocate a database 'Connection' object
				Connection conn = DriverManager . getConnection (
						"jdbc:mysql://localhost:3306/ebookstore?useSSL=false" , "root" , "deoltedb" );

				// Allocate a 'Statement' object in the Connection
				Statement stmt = conn . createStatement ();
				) {

			System.out.println("****** WELCOME TO THE BOOK STORE DATABASE ********\n---------- ENTER MENU OPTION ----------- ");
			System.out.println("1. Enter book");
			System.out.println("2. Update book");
			System.out.println("3. Delete book");
			System.out.println("4. Search books");
			System.out.println("0. exit");
			Scanner in = new Scanner(System.in);

			String choice = in.nextLine();
			int choice_Int = Integer.parseInt(choice);

			// Add book to the 'books' table in the database 'ebookstore'
			while (choice_Int != 0){
				if(choice_Int == 1) {
					
					System.out.println("PLEASE ENTER THE BOOK TITLE: ");
					String new_Title = in.nextLine();
					System.out.println("PLEASE ENTER THE BOOK AUTHOR: ");
					String new_Author = in.nextLine();
					System.out.println("PLEASE ENTER THE BOOK QUANTITY(as an integer)IN THE STORE: ");
					String new_Qty = in.nextLine();

					String sqlInsert = "insert into books (Title, Author, Qty) values ("							
							+ "'" + new_Title + "', "
							+ "'" + new_Author + "', "
							+ new_Qty + ")";

					// Execute a SQL UPDATE via executeUpdate()
					// which returns an int indicating the number of rows affected
					System.out.println ("The SQL query is: " + sqlInsert);
					int countInserted = stmt.executeUpdate(sqlInsert);
					System.out.println ("******* " + countInserted + " RECORDS INSERTED.***********\n");
                    
					// a SELECT to check the records inserted.
					String strSelect = "select * from books" ;
					System.out.println ("The SQL query is: " + strSelect);
					
				}

				// update the book details from database
				if(choice_Int == 2) {
					System.out.println("PLEASE ENTER THE BOOK TITLE TO UPDATE: ");
					String update_Title = in.nextLine();

					System.out.println("PLEASE ENTER THE UPDATED QUNATITY (as an integer) OF THIS BOOK IN-STORE: ");
					String updated_Qty = in.nextLine();

					String sqlUpdate = "update books set Qty = "
							+ updated_Qty +
							" where Title = '" + update_Title + "' ";

					// Execute a SQL UPDATE via executeUpdate()
					// which returns an int indicating the number of rows affected
					System.out.println ("The SQL query is: " + sqlUpdate);
					int countUpdated = stmt.executeUpdate( sqlUpdate );
					System.out.println("****** " + countUpdated + " RECORDS AFFECTED.*******");
					
					// a SELECT to check the UPDATE.
					String strUpdated = "select * from books where title = " + update_Title;
					System.out.println("The SQL query is: " + strUpdated);
				}

				// delete book from table 'books' in the database 'ebookstore'
				if(choice_Int == 3) {
					System.out.println("PLEASE ENTER THE TITLE OF BOOK TO DELETE: ");
					String delete_Title = in.nextLine();

					String sqlDelete = "delete from books where Title = '" + delete_Title + "'";

					// Execute a SQL UPDATE via executeUpdate()
					// which returns an int indicating the number of rows affected
					
					System.out.println ("The SQL query is: " + sqlDelete);
					int countDeleted = stmt.executeUpdate(sqlDelete);
					System.out.println("****** " + countDeleted + " RECORDS DELETED *******\n");
					
					// a SELECT to check the deleted book.
					String strDeleted = "select * from books where Title = " + delete_Title;
					System.out.println("The SQL query is: " + strDeleted);
				}

				// search book from the table 'books' in database 'ebookstore
				if(choice_Int == 4) {
					System.out.println("PLEASE ENTER THE TITLE OF BOOK TO SEARCH: ");
					String search_Title = in.nextLine();
										
					String sqlSearch = "select * from books where Title = '" + search_Title + "'";					
					// Execute a SQL Search via executeQuery()
					System.out.println ("The SQL query is: " + sqlSearch);
					
					ResultSet rset = stmt.executeQuery(sqlSearch);
					System.out.println ( "********* THE RECORDS ARE ************: " );

					int rowCount = 0;
					// Move the cursor to the next row, and then return false if there's no more row
					while(rset.next()) {
						int id = rset.getInt("id");
						String title = rset . getString ( "Title" );
						String author = rset . getString ( "Author" );
						int qty = rset . getInt ( "Qty" );
						System . out . println (id + ", " + title + ", " + author + ", " + qty );
						++ rowCount ;
					}
					System . out . println ("THE TOTAL NUMBER OF RECORDS = " + rowCount );
				}

				System.out.println(" -----------:  PLEASE MAKE ANOTHER CHOICE BELOW -----------: ");
				System.out.println("1. Enter book");
				System.out.println("2. Update book");
				System.out.println("3. Delete book");
				System.out.println("4. Search books");
				System.out.println("0. exit");

				choice = in.nextLine();
				choice_Int = Integer.parseInt(choice);
			}

			in.close();

		}
		catch ( SQLException ex ) {
			ex.printStackTrace ();
		}
		
	}
}