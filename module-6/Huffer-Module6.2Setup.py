# Name, Date, Assignment Name/Number: Joe Huffer, 4/21/2024, Module 6.2 'Setup'
# Citation: None 

import mysql.connector

def main():
    # Configuration settings for MySQL connection
    config = {
        "user": "movies_user",  # The username for the MySQL account
        "password": "popcorn",  # The password for the MySQL account
        "host": "127.0.0.1",  # The host to connect to the MySQL server
        "database": "movies",  # The database to connect to
        "raise_on_warnings": True  # Raise an exception on warnings
    }

    # Establish a connection to the MySQL database using the configuration
    db = mysql.connector.connect(**config)
    
    # Create a cursor object using the connection
    cursor = db.cursor()

    # Query 1: Select all fields from the studio table
    print("\n-- DISPLAYING STUDIO RECORDS --")
    cursor.execute("SELECT * FROM studio")
    for studio in cursor.fetchall():
        print(f"Studio ID: {studio[0]}, Studio Name: {studio[1]}")

    # Query 2: Select all fields from the genre table
    print("\n-- DISPLAYING GENRE RECORDS --")
    cursor.execute("SELECT * FROM genre")
    for genre in cursor.fetchall():
        print(f"Genre ID: {genre[0]}, Genre Name: {genre[1]}")

    # Query 3: Select movie names with a runtime less than two hours
    print("\n-- DISPLAYING SHORT FILM RECORDS --")
    cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120")
    for film in cursor.fetchall():
        print(f"Film Name: {film[0]}")

    # Query 4: Get a list of film names and directors grouped by director
    print("\n-- DISPLAYING DIRECTOR RECORDS IN ORDER --")
    cursor.execute("SELECT film_director, GROUP_CONCAT(film_name) FROM film GROUP BY film_director")
    for record in cursor.fetchall():
        print(f"Director: {record[0]}, Films: {record[1]}")

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()                                                                # Close the database connection   