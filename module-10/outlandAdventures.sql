
CREATE DATABASE IF NOT EXISTS outland_adventures;
USE outland_adventures;

-- drop database user if exists 
--DROP USER IF EXISTS 'adventures_user'@'localhost';


-- create adventures_user and grant them all privileges to the movies database 
CREATE USER 'adventures_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'outland';

-- grant all privileges to the movies database to user movies_user on localhost 
GRANT ALL PRIVILEGES ON outland_adventures.* TO 'adventures_user'@'localhost';

CREATE TABLE IF NOT EXISTS EMPLOYEE (
    EmployeeID INT PRIMARY KEY,
    Role varchar(50),
	EmployeeContactInfo varchar (255),
	EmployeeName varchar(100)
	);

CREATE TABLE IF NOT EXISTS Trips (
	TripID INT PRIMARY KEY,
	Destination varchar(100),
	TripCost DOUBLE (7,2),
	DepartureDate DATE,
	ArrivalDate Date,
	EmployeeID INT,
	CustomerID INTEGER
	);

CREATE TABLE IF NOT EXISTS Supply (
	SuppliesID INT PRIMARY KEY,
	ItemDescription varchar(100),
	SupplyPricetoBuy DOUBLE(7,2),
	SupplyPricetoRent DOUBLE(7,2),
	AcquiredDate DATE,
	SupplyStatus varchar(9),
	-- values of available, rented, or bought
	TripID INT
	);

CREATE TABLE IF NOT EXISTS Customer (
	CustomerID INT PRIMARY KEY,
	CustomerName varchar(50),
	CustomerContactInfo varchar(255)
	);
	
INSERT INTO EMPLOYEE values (1,'Owner','phone: 123','Blythe Timmerson');
INSERT INTO EMPLOYEE values (2,'Owner','phone: 132','Jim Ford');
INSERT INTO EMPLOYEE values (3,'Guide','phone: 1456','John ‘Mac’MacNell');
INSERT INTO EMPLOYEE values (4,'Guide','phone: 1956','D.B. ‘Duke’ Marland');
INSERT INTO EMPLOYEE values (5,'Supplies/Inventory','phone: 5956','Dimitrios Stravopolous');
INSERT INTO EMPLOYEE values (6,'Website','phone: 8856','Mei Wong');

INSERT INTO Trips values (1,'Africa',799.99,'2024-01-15','2024-01-25',3,1);
INSERT INTO Trips values (2,'Asia',999.99,'2024-01-17','2024-01-28',4,2);
INSERT INTO Trips values (2,'Asia',999.99,'2024-01-17','2024-01-28',4,3);
INSERT INTO Trips values (3,'Southern Europe',699.99,'2024-02-10','2024-02-18',3,3);
INSERT INTO Trips values (4,'Southern Europe',699.99,'2024-02-10','2024-02-18',3,4);
INSERT INTO Trips values (5,'Southern Europe',699.99,'2024-02-10','2024-02-18',3,5);

INSERT INTO Supply values (1,'Tents',99.99,19.95,'2014-05-07','available',null);
INSERT INTO Supply values (2,'Tents',99.99,19.95,'2023-08-17','rented',2);
INSERT INTO Supply values (3,'Backpacks',40.99,9.95,'2022-04-25','bought',3);
INSERT INTO Supply values (4,'Bedroll',30.99,8.95,'2024-01-01','rented',4);
INSERT INTO Supply values (5,'Cookpots',50.99,15.75,'2021-09-16','bought',1);
INSERT INTO Supply values (6,'Waterskin',10.99,5.95,'2022-08-18','rented',1);

INSERT INTO Customer VALUES (1,'Miles Franklin', 'Contact Info 13544');
INSERT INTO Customer VALUES (2,'Clara Bowman', 'Contact Info 277456');
INSERT INTO Customer VALUES (3,'Theodore Snyder', 'Contact Info 55443');
INSERT INTO Customer VALUES (4,'Lucy Mendoza', 'Contact Info 881634');
INSERT INTO Customer VALUES (5,'Elijah Hart', 'Contact Info 65855');
INSERT INTO Customer VALUES (6,'Sophie Lamb', 'Contact Info 63321');







