#!/usr/bin/env python3
import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # 🔁 Replace with your MySQL username
            password="META_physical"    # 🔁 Replace with your MySQL password
        )

        cursor = connection.cursor()

        # Attempt to create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL Server: {err}")

    finally:
        # Ensure clean exit
        try:
            cursor.close()
            connection.close()
        except:
            pass

if __name__ == "__main__":
    create_database()
