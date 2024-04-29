# Name, Date, Assignment Name/Number: Joe Huffer, 4/21/2024, Module 6.2 'Setup'
# Citation: https://www.tutorialspoint.com/python_data_access/python_mysql_cursor_object.htm, https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html, https://realpython.com/python-f-strings/, 

import mysql.connector

def main():                                                                                                 # Define the main function
    config = {                                                                                              # Configuration settings for MySQL connection - cleaning this up from last assignment and moving note here.
        "user": "movies_user",                                                                              # The username for the MySQL account
        "password": "popcorn",                                                                              # The password for the MySQL account
        "host": "127.0.0.1",                                                                                # The host to connect to the MySQL server
        "database": "movies",                                                                               # The database to connect to
        "raise_on_warnings": True                                                                           # Raise an exception on warnings
    }

    # Establish a connection to the MySQL database using the configuration
    db = mysql.connector.connect(**config)                                                                  # Connect to the MySQL server using the configuration - https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    
    # Create a cursor object using the connection   
    cursor = db.cursor()                                                                                    # Create a cursor object using the connection.  https://www.tutorialspoint.com/python_data_access/python_mysql_cursor_object.htm.  A cursor object is an instance which you can execute SQL queries. It is used to manage the context of a fetch operation. Cursors created from the same connection are not isolated, i.e., any changes done to the database by a cursor are immediately visible by the other cursors.

    # Query 1: Select all fields from the studio table
    print("\n-- DISPLAYING Studio RECORDS --")                                                              # Display the message "DISPLAYING Studio RECORDS". \n = newline character.
    cursor.execute("SELECT * FROM studio")                                                                  # Execute the SQL query to select all fields from the studio table.  cursor.execute() method executes the SQL query given in the parameter. 
    for studio in cursor.fetchall():                                                                        # Iterate over the records returned by the query.  for studio, in cursor - fetchall():  The fetchall() method fetches all rows from the last executed statement. Returns a list of tuples, each tuple is a value for each field in the row.
        print(f"Studio ID: {studio[0]}\nStudio Name: {studio[1]}\n")                                        # Print the Studio ID and Studio Name for each record in the studio table.  f-string formatting.  https://realpython.com/python-f-strings/.  Studio ID and Studio Name are the first and second fields in the studio table, so we're printing studio[0] (field 1) and studio[1] (field 2).

    # Query 2: Select all fields from the genre table
    print("\n-- DISPLAYING Genre RECORDS --")                                                               # Display the message "DISPLAYING Genre RECORDS". \n = newline character.
    cursor.execute("SELECT * FROM genre")                                                                   # Execute the SQL query to select all fields from the genre table.  cursor.execute() method executes the SQL query given in the parameter. 
    for genre in cursor.fetchall():                                                                         # Iterate over the records returned by the query.  for genre, in cursor - fetchall():  See line 25.
        print(f"Genre ID: {genre[0]}\nGenre Name: {genre[1]}\n")

    # Query 3: Select movie names with a runtime less than two hours
    print("\n-- DISPLAYING Short Film RECORDS --")                                                          # Display the message "DISPLAYING Short Film RECORDS". \n = newline character.
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")                     # Execute the SQL query to select movie names with a runtime less than two hours.  cursor.execute() method executes the SQL query given in the parameter.
    for film_name, film_runtime in cursor.fetchall():                                                       # Iterate over the records returned by the query.  for film_name, film_runtime in cursor - fetchall():  See line 25.
        print(f"Film Name: {film_name}\nRuntime: {film_runtime}\n")                                         # Print the Film Name and Runtime for each record in the film table. 

    # Query 4: Get a list of film names and directors grouped by director
    print("\n-- DISPLAYING Director RECORDS In Order --")                                                   # Display the message "DISPLAYING DIRECTOR RECORDS IN ORDER". \n = newline character.
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director, film_name")           # Execute the SQL query to get a list of film names and directors grouped by director.  cursor.execute() method executes the SQL query given in the parameter.
    for film_name, film_director in cursor.fetchall():                                                      # Iterate over the records returned by the query.  for film_name, film_director in cursor - fetchall():  See line 25.
        print(f"Film Name: {film_name}\nDirector: {film_director}\n")                                       # Print the Film Name and Director for each record in the film table. My output shows Alien as the first movie and Gladiator as second - screenshot has them reversed in blackboard.  Not sure if I should attempt to reverse mine or not, leaving it for now @Prof Sue.
    
    # Close the cursor and the connection
    cursor.close()                                                                                          # Close the cursor object
    db.close()                                                                                              # Close the database connection

if __name__ == "__main__":                                                                                  # if the script is being run directly __name__ will be equal to __main__
    main()                                                                                                  # main() function is called