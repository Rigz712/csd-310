# Name, Date, Assignment Name/Number: Joe Huffer, 4/21/2024, Module 6.2 'Setup'
# Citation: https://stackoverflow.com/questions/5686882/what-does-s-means-here (<-- % Placeholder before inserting values), Notes/Screenshots from Blackboard, Previous Cursor Notes from Module 7.2.

import mysql.connector

# Define the connection to the database
config = {                                                                                                                                              # Configuration settings for MySQL connection.
    "user": "movies_user",                                                                                                                              # The username for the MySQL account
    "password": "popcorn",                                                                                                                              # The password for the MySQL account
    "host": "127.0.0.1",                                                                                                                                # The host to connect to the MySQL server
    "database": "movies",                                                                                                                               # The database to connect to
    "raise_on_warnings": True                                                                                                                           # Raise an exception on warnings
    }

def show_films(cursor, title):                                                                                                                          # Define a function to display films
    print("\n-- {} --".format(title))                                                                                                                   # Display the title of the section - Next line is query, 1) SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name', 2) From film, 3) INNER JOIN genre ON film.genre_id = genre.genre_id, 4) INNER JOIN studio ON film.studio_id = studio.studio_id, 5) ORDER BY film_name
    query = """ 
    SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name'
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    ORDER BY film_name
    """
    cursor.execute(query)                                                                                                                               # Execute the query
    films = cursor.fetchall()                                                                                                                           # Fetch all the records
    for film in films:                                                                                                                                  # Iterate over the records
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))                                   # Print the film details: film name, director, genre, studio name, new line, and format starting at item 1 in the list.

# Main routine
db = mysql.connector.connect(**config)                                                                                                                  # Connect to the database - copied from module 7.2
cursor = db.cursor()                                                                                                                                    # Create a cursor object - copied from module 7.2

# Show initial state of films
show_films(cursor, "DISPLAYING FILMS")                                                                                                                  # Show the films

# Insert a new film record
insert_query = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s)"       # Insert into film table - film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id as columns, VALUES as placeholders. %s is a placeholder for the values to be inserted.
cursor.execute(insert_query, ("New Film", "2024", 120, "New Director", 1, 1))                                                                           # Execute the insert query with the values for the new film, see line above.
db.commit()                                                                                                                                             # Commit 

# Show films after insert
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")                                                                                                     # Show the films

# Update the film 'Alien' to be a Horror film
update_query = "UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien'"                          # Update the film genre to Horror Update film table, set genre_id to the genre_id from the genre table where the genre_name is Horror, where the film_name is Alien.
cursor.execute(update_query)                                                                                                                            # Execute the update query
db.commit()                                                                                                                                             # Commit

# Show films after update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")                                                                                                     # Show the films after update

# Delete the movie 'Gladiator'
delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"                                                                                         # Delete from the film table where the film_name is Gladiator
cursor.execute(delete_query)                                                                                                                            # Execute the delete query
db.commit()                                                                                                                                             # Commit

# Show films after delete
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")                                                                                                     # Show the films after delete

# Clean up
cursor.close()                                                                                                                                          # Close the cursor
db.close()                                                                                                                                              # Close the database connection