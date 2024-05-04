import mysql.connector
from mysql.connector import errorcode

# Alfa team group project 5/3/2024 Milestone 2 Assignment 10.1
config = {
    "user": "adventures_user",
    "password": "outland",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

def main():
    try:
        db = mysql.connector.connect(**config)

        print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

        input("\n\n Press any key to continue...")

        cursor = db.cursor()
        show_employees(cursor,"DISPLAYING EMPLOYEES")
        show_trips(cursor,"DISPLAYING TRIPS")
        show_supplies(cursor,"DISPLAYING SUPPLIES")
        show_customers(cursor,"DISPLAYING CUSTOMERS")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist")

        else:
            print(err)
    except Exception as error:
        print("Error other than database connection occured: ", error)

    finally:
        db.close()

def show_employees(cursor,title):
    #method to execute query and output results

    #inner join query
    cursor.execute("select EmployeeID, Role, EmployeeContactInfo, EmployeeName from Employee ")
    # get results
    employees = cursor.fetchall()

    print("\n -- {} --".format(title))

    #interate over results to display
    for employee in employees:
        print("EmployeeID: {}\nRole: {}\nContact Info: {}\nName: {}\n".format(employee[0], employee[1], employee[2], employee[3]))

def show_trips(cursor,title):
    #method to execute query and output results

    #inner join query
    cursor.execute("select TripID, Destination, TripCost, DepartureDate, ArrivalDate, EmployeeID, CustomerID from Trips ")
    # get results
    trips = cursor.fetchall()

    print("\n -- {} --".format(title))

    #interate over results to display
    for trip in trips:
        print("TripID: {}\nDestination: {}\nTrip Cost: {}\nDeparture Date: {}\nArrival Date: {}\nEmployeeID: {}\nCustomerID: {}\n".format(trip[0], trip[1], trip[2], trip[3], trip[4], trip[5], trip[6]))

def show_supplies(cursor,title):
    #method to execute query and output results

    #inner join query
    cursor.execute("select SuppliesID, ItemDescription, SupplyPricetoBuy, SupplyPricetoRent, AcquiredDate, SupplyStatus, TripID from Supply ")
    # get results
    supplies = cursor.fetchall()

    print("\n -- {} --".format(title))

    #interate over results to display
    for supply in supplies:
        print("SupplyID: {}\nItem Description: {}\nSupply Price to Buy: {}\nSupply Price to Rent: {}\nAcquired Date: {}\nSupply Status: {}\nTripID: {}\n".format(supply[0], supply[1], supply[2], supply[3], supply[4], supply[5], supply[6]))
        
def show_customers(cursor,title):
    #method to execute query and output results

    #inner join query
    cursor.execute("select CustomerID, CustomerName, CustomerContactInfo from Customer ")
    # get results
    customers = cursor.fetchall()

    print("\n -- {} --".format(title))

    #interate over results to display
    for customer in customers:
        print("CustomerID: {}\nCustomer Name: {}\nCustomer Contact Info: {}\n".format(customer[0], customer[1], customer[2]))

main()
