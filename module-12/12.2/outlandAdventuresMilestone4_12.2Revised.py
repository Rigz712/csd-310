import mysql.connector
from mysql.connector import errorcode

# Alfa team group project 5/8/2024 Milestone 3 Assignment 11.1
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
        show_equipment_sales(cursor,"Equipment Sales Report")
        show_booking_trends(cursor,"Booking Trends Report")
        show_old_equipment(cursor,"Report of Equipment older than 5 years")

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

def show_equipment_sales(cursor,title):
    #method to execute query and output results

    #inner join query
    cursor.execute("select ItemDescription, COUNT(*), SupplyPricetoBuy, NOW() from Supply where supplystatus = 'bought' group by ItemDescription, SupplyPricetoBuy")
    # get results
    supplies = cursor.fetchall()

    print("\n -- {} --".format(title))

    #interate over results to display
    for supply in supplies:
        print("Item: {}\nNumber sold: {}\nPrice to buy: {}\nDate and Time Report was Ran: {}\n".format(supply[0], supply[1], supply[2], supply[3]))

def show_booking_trends(cursor,title):
    #method to execute query and output results

    #inner join query
    cursor.execute("select Destination, YEAR(DepartureDate), MONTH(DepartureDate), Count(*), NOW() from Trips Group by Destination, YEAR(DepartureDate), MONTH(DepartureDate) Order by Destination, YEAR(DepartureDate), MONTH(DepartureDate)")
    # get results
    trips = cursor.fetchall()

    print("\n -- {} --".format(title))

    #interate over results to display
    for trip in trips:
        print("Location: {}\nDeparture Year: {}\nDeparture Month: {}\nNumber of Bookings: {}\nDate and Time Report was Ran: {}\n".format(trip[0], trip[1], trip[2], trip[3], trip[4]))

def show_old_equipment(cursor,title):
    #method to execute query and output results

    #inner join query
    cursor.execute("select SuppliesID, ItemDescription, AcquiredDate, NOW() from Supply WHERE YEAR(CURDATE()) - YEAR(AcquiredDate) > 5")
    # get results
    supplies = cursor.fetchall()

    print("\n -- {} --".format(title))

    #interate over results to display
    for supply in supplies:
        print("Supply ID: {}\nItem Description: {}\nAcquired Date: {}\nDate and Time Report was Ran: {}\n".format(supply[0], supply[1], supply[2], supply[3]))

main()