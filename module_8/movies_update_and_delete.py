# CSD 310
# Module 8 Assignment 8.2
# Jeremiah Kellam
# 4/18/2023

# Citations:
# Python MySQL Insert Into. (n.d.). https://www.w3schools.com/python/python_mysql_insert.asp

# Python SQL query string formatting. (n.d.). Stack Overflow. https://stackoverflow.com/questions/5243596/python-sql-query-string-formatting

#Python MySQL Update Table. (n.d.). https://www.w3schools.com/python/python_mysql_update.asp

"""
Create a new file under the module_8 directory and name it movies_update_and_delete.py. --> Done
Using the example code I provided, connect to the movies database. --> Done
Using the example code I have provided, call the python function to display the selected fields and the associated Label. --> Done
show_films(cursor, "DISPLAYING FILMS") --> Done - Query #1
Insert a new record into the film table using a film of your choice. (Easier if you use a studio already in use..) --> Done - INSERT FILM
Using the example code I have provided, call the python function to display the selected fields and the associated Label. --> Done - Query #2
Using the example code I have provided, update the film Alien to being a Horror film. --> Done - UPDATE FILM
Using the example code I have provided, call the python function to display the selected fields and the associated Label. --> Done - Query #3
Using the example code I have provided, delete the movie Gladiator. --> Done - DELETE FILM
Using the example code I have provided, call the python function to display the selected fields and the associated Label. --> Done - Query #4
Hint: If you run this script more than once, you'll have multiple additions.. and you won't be able to access the film you deleted earlier.. in order to get a pristine output, you'll need to run that db_init_2022.sql file again (it drops the tables), then run your update and delete script.
Take a screen shot of the results or copy the output, and paste into a Word document. --> Done.
Make sure your output matches the expected output (this is gradable.) --> DONE. """



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
        input("\n\n Press any key to continue...\n")

        # Create a cursor object
        cursor = db.cursor()

        # Query 1 show_films(cursor, "DISPLAYING FILMS")
        cursor.execute("SELECT film_name, film_director, genre_name, studio_name FROM film JOIN genre ON film.genre_id = genre.genre_id JOIN studio ON film.studio_id = studio.studio_id")
        print("\n-- DISPLAYING FILMS --")
        for film in cursor.fetchall():
            print(f"Film Name: {film[0]}")
            print(f"Director: {film[1]}")
            print(f"Genre Name ID: {film[2]}")
            print(f"Studio Name: {film[3]}\n")

        # INSERT film - Jurassic Park, 1993, 127 minutes, Steven Spielberg - Universal Pictures - SciFi
        cursor.execute("""INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
        VALUES('Jurassic Park', '1993', '127', 'Steven Spielberg',
        (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'),
        (SELECT genre_id FROM genre WHERE genre_name = 'SciFi'));""")

        # Query 2 show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
        cursor.execute("SELECT film_name, film_director, genre_name, studio_name FROM film JOIN genre ON film.genre_id = genre.genre_id JOIN studio ON film.studio_id = studio.studio_id")
        print("\n-- DISPLAYING FILMS AFTER INSERT--")
        for film in cursor.fetchall():
            print(f"Film Name: {film[0]}")
            print(f"Director: {film[1]}")
            print(f"Genre Name ID: {film[2]}")
            print(f"Studio Name: {film[3]}\n")

        # UPDATE Alien to Horror Genre
        cursor.execute("UPDATE film \
        SET genre_id = 1 \
        WHERE film_name = 'Alien';")

        # Query 3 show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")
        cursor.execute("SELECT film_name, film_director, genre_name, studio_name FROM film JOIN genre ON film.genre_id = genre.genre_id JOIN studio ON film.studio_id = studio.studio_id")
        print("\n-- DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror --")
        for film in cursor.fetchall():
            print(f"Film Name: {film[0]}")
            print(f"Director: {film[1]}")
            print(f"Genre Name ID: {film[2]}")
            print(f"Studio Name: {film[3]}\n")

        # DELETE Gladiator from FILM
        cursor.execute("""DELETE FROM film
        WHERE film_name = 'Gladiator';""")

        # Query 4 show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
        cursor.execute("SELECT film_name, film_director, genre_name, studio_name FROM film JOIN genre ON film.genre_id = genre.genre_id JOIN studio ON film.studio_id = studio.studio_id")
        print("\n-- DISPLAYING FILMS AFTER DELETE --")
        for film in cursor.fetchall():
            print(f"Film Name: {film[0]}")
            print(f"Director: {film[1]}")
            print(f"Genre Name ID: {film[2]}")
            print(f"Studio Name: {film[3]}\n")

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