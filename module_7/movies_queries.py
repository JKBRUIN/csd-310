#CSD 310
#Module 7 Assignment 7.2
#Jeremiah Kellam
#4/16/2023

"""
Create a new file under the module_7 directory and name it movies_queries.py.
    
Write the code to connect to your MySQL movies database.
    Refer to the previous assignment for code structure.
    You can basically copy/paste the code we used in the previous assignment, assuming you were able to get it to work.

Write four queries, in one Python file.The output from your queries should match the example below, including descriptions of output and format.
        
        
-- DISPLAYING Studio RECORDS --
Studio ID: 
Studio Name:

Studio ID: 
Studio Name:

Studio ID: 
Studio Name:


-- DISPLAYING Genre RECORDS --
Genre ID: 
Genre Name:

Genre ID: 
Genre Name:

Genre ID: 
Genre Name:

-- DISPLAYING Short Film RECORDS --
Film Name:
Runtime:

Film Name:
Runtime:


-- DISPLAYING Director RECORDS in Order --
Film Name:
Director:

Film Name:
Director:

Film Name:
Director:


Here are the queries:
The first and second query is to select all the fields for the studio and genre tables.

The third query is to select the movie names for those movies that have a run time of less than two hours.

The fourth query is to get a list of film names, and directors ordered by director.
    Run the script and take a screenshot of the results. Copy screenshot into a Word document.
"""

#Citations:
#       8. Errors and Exceptions. (n.d.). Python Documentation. 
#           https://docs.python.org/3/tutorial/errors.html#handling-exceptions

#       8. Compound statements. (n.d.). Python Documentation. 
#           https://docs.python.org/3/reference/compound_stmts.html#the-with-statement

#       Vishal. (2021). Python Select from MySQL Table. PYnative. 
#           https://pynative.com/python-mysql-select-query-to-fetch-data/

#       RealPython. (2023). Python “for” Loops (Definite Iteration). realpython.com. 
#           https://realpython.com/python-for-loop/

#       Python String Formatting. (n.d.). 
#           https://www.w3schools.com/python/python_string_formatting.asp



import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    with mysql.connector.connect(**config) as db:
        print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"],config["host"],config["database"]))
        input("\n\n Press any key to continue...")

        # Create a cursor object
        cursor = db.cursor()

        # Query 1
        cursor.execute("SELECT * FROM studio")
        print("-- DISPLAYING Studio RECORDS --")
        for studio in cursor.fetchall():
            print(f"Studio ID: {studio[0]}")
            print(f"Studio Name: {studio[1]}\n")

        # Query 2
        cursor.execute("SELECT * FROM genre")
        print("-- DISPLAYING Genre RECORDS --")
        for genre in cursor.fetchall():
            print(f"Genre ID: {genre[0]}")
            print(f"Genre Name: {genre[1]}\n")

        # Query 3
        cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
        print("-- DISPLAYING Short Film RECORDS --")
        for film in cursor.fetchall():
            print(f"Film Name: {film[0]}")
            print(f"Runtime: {film[1]}\n")

        # Query 4
        cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
        print("-- DISPLAYING Director RECORDS in Order --")
        for film in cursor.fetchall():
            print(f"Film Name: {film[0]}")
            print(f"Director: {film[1]}\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    db.close()