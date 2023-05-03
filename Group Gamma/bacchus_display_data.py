#Group Gamma 
#Julian Gomez Jr., Zachary Mazairz, Jeremiah Kellam, Emily Wojan
#CSD 310
#Module 10 Assignment
#May 2, 2023

"""The purpose of this program is to enable access to the MySQL Bacchus
database and query the MySQL bacchus database to display all data in the
tables."""

#Necessary python imports.
import mysql.connector
from mysql.connector import errorcode

#For connecting to the Bacchus database.
config = {
	"user": "bacchus_user",
	"password": "gamma",
	"host": "127.0.0.1",
	"database": "bacchus",
	"raise_on_warnings": True
}

db = mysql.connector.connect(**config)

#Used to create a cursor on the connection.
cursor = db.cursor()

#For displaying Supplier Records.
query = ("SELECT * from supplier")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Supplier RECORDS--")

for row in result:
	print("Supplier ID:",row[0])
    
	print("Supplier Name:",row[1])
    
	print("Street Address:", row[2])
	
	print("City", row[3])
	
	print("State:", row[4])
    
	print("Country:", row[5])
    
	print("Zip Code:", row[6])
    
	print("First Name of Contact:", row[7])
    
	print("Last Name of Contact:", row[8])
    
	print("Phone Number:", row[9])
    
	print("Email Address:", row[10])
	
	print(" ")
    

#For displaying Supplies Records.
query = ("SELECT * from supplies")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Supplies RECORDS--")

for row in result:
	print("Supply ID:",row[0])
    
	print("Item Name:",row[1])
    
	print("Item Description:", row[2])
    
	print("Units On Hand:", row[3])
    
	print("Supplier ID:", row[4])
   
	print(" ")
	
#For displaying Supply Order Records.
query = ("SELECT * from supply_order")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Supply Order RECORDS--")

for row in result:
	print("Supplier Order ID:",row[0])
    
	print("Total Cost:",row[1])
    
	print("Order_Date:", row[2])
    
	print("Tracking Number:", row[3])
    
	print("Estimated Delivery Date:", row[4])
    
	print("Actual Delivery Date:", row[5])
    
	print("Supplier ID:", row[6])
	
	print(" ")

#For displaying Supply Order Details Records.
query = ("SELECT * from supply_order_details")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Supply Order Details RECORDS--")

for row in result:
	print("Supplier Order Details ID:",row[0])
    
	print("Units Ordered:",row[1])
    
	print("Unit Price:", row[2])
    
	print("Supply ID:", row[3])
    
	print("Supply Order ID:", row[4])
	
	print(" ")
	
#For displaying Wine Records.
query = ("SELECT * from wine")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Wine RECORDS--")

for row in result:
	print("Wine ID:", row[0])
    
	print("Wine Name:", row[1])
	
	print("Wine Description:", row[2])
    
	print("Units On Hand:", row[3])
    
	print("Cost Per Unit:", row[4])
	
	print(" ")
	
#For displaying Distributor Records.
query = ("SELECT * from distributor")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Distributor RECORDS--")

for row in result:
	print("Distributor ID:",row[0])
    
	print("Distributor_Name:",row[1])
    
	print("Street Address:", row[2])
	
	print("City", row[3])
	
	print("State:", row[4])
    
	print("Country:", row[5])
    
	print("Zip Code:", row[6])
    
	print("First Name of Contact:", row[7])
    
	print("Last Name of Contact:", row[7])
    
	print("Phone Number:", row[8])
    
	print("Email Address:", row[9])
	
	print("Wine ID:", row[10]);
	
	print(" ")
	
#For displaying Wine Order Records.
query = ("SELECT * from wine_order")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Wine Order RECORDS--")

for row in result:
	print("Wine ID:",row[0])
    
	print("Total Cost:",row[1])
    
	print("Order Date:", row[2])
    
	print("Tracking Number:", row[3])
    
	print("Estimated Delivery Date:", row[4])
    
	print("Actual Delivery Date:", row[5])
    
	print("Distributor ID:", row[6])
	
	print(" ")
	
#For displaying Wine Order Details Records.
query = ("SELECT * from wine_order_details")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Wine Order Details RECORDS--")

for row in result:
	print("Wine Order Details ID:",row[0])
    
	print("Units Ordered:",row[1])
    
	print("Sales Price:", row[2])
    
	print("Wine ID:", row[3])
    
	print("Wine Order ID:", row[4])
	
	print(" ")
	
#For displaying Employees Records.
query = ("SELECT * from employees")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Employees RECORDS--")

for row in result:
	print("Employee ID:",row[0])
    
	print("First Name:",row[1])
    
	print("Last Name:", row[2])
    
	print("Date Of Birth", row[3])
    
	print("Phone Number:", row[4])
    
	print("Email Address:", row[5])
    
	print("Street Address:", row[6])
	
	print("City", row[7])
	
	print("State:", row[8])
	
	print("Country:", row[9])
	
	print("Zip Code:", row[10])
    
	print("Hire Date:", row[11])
    
	print("Job Title:", row[12])
	
	print("Hourly Wage:", row[13])
	
	print("Employee Status:", row[14])
	
	print(" ")
	
#For displaying Timcards Records.
query = ("SELECT * from timecards")

cursor.execute(query)

result=cursor.fetchall()

print("--DISPLAYING Timcards RECORDS--")

for row in result:
	print("Timecard ID:",row[0])
    
	print("Date Posted:",row[1])
    
	print("Hours Worked Monthly", row[2])
    
	print("PTO Hours", row[3])
    
	print("Unpaid Time Taken:", row[4])
    
	print("Total Hours Worked:", row[5])
	
	print("Employee ID:", row[6])
	
	print(" ")	


cursor.close() #Used to close the cursor


db.close() #USed to close the connection.
