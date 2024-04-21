# Name, Date, Assignment Name/Number: Joe Huffer, 4/21/2024, Module 6.2 'Setup'
# Citation: None 

import mysql.connector                                                                  # Import the MySQL connector
from mysql.connector import Error                                                       # Import the Error class from the MySQL connector

# Configuration for MySQL connection
config = {
    "user": "movies_user",                                                              # The username for the MySQL account
    "password": "popcorn",                                                              # The password for the MySQL account
    "host": "127.0.0.1",                                                                # The host to connect to the MySQL server
    "database": "movies",                                                               # The database to connect to
    "raise_on_warnings": True                                                           # Raise an exception on warnings
}

# Attempt to connect to the MySQL database using the configuration above
try:    
    db = mysql.connector.connect(**config)                                              # Connect to the MySQL server using the configuration
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(   # Print a message to confirm the connection
        config["user"], config["host"], config["database"]                              # Print the username, host, and database name
    ))
    input("\nPress any key to continue...")                                             # Wait for user input before continuing
    
# Handle errors during connection attempt
except mysql.connector.Error as err:                                                    # Catch any errors that occur
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:                   # Check if the error is due to invalid credentials
        print("The supplied username or password are invalid")                          # Print an error message
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:                        # Check if the error is due to a missing database
        print("The specified database does not exist")                                  # Print an error message
    else:                                                                               # If the error is not one of the above
        print(err)                                                                      # Print the error message

# Ensure the database connection is closed after the operation is complete
finally:                                                                                # Code to run after the try block, regardless of the outcome
    if db.is_connected():                                                               # Check if the database connection is still open
        db.close()                                                                      # Close the database connection   