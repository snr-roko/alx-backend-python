import mysql.connector
import csv
def connect_db():
    try: 
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="######"
    ) 
        return connection
    except mysql.connector.Error:
        print("Database connection failed")
        return None

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    connection.commit()

def connect_to_prodev():
    try: 
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MrRoko@0405",
        database="ALX_prodev"
    ) 
        return connection
    except mysql.connector.Error:
        print("Database connection failed")
        return None

# creating database tables
def create_table(connection):
    cursor = connection.cursor()
    try: 
        cursor.execute("""CREATE TABLE IF NOT EXISTS user_data(
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age INT NOT NULL);""")
    except Exception as e:
        print("Error creating Tables: ", e)
    else:
        connection.commit()
    finally:
        cursor.close()


# Inserting values into the database tables
def insert_data(connection, file_path):
    cursor = connection.cursor()
    
    try:
        with open(file_path, 'r') as file:
            csvfile = csv.reader(file, quotechar='"', skipinitialspace=True)
            next(csvfile)  # Skip header
            
            for line in csvfile:
                print(line)
                cursor.execute("INSERT INTO user_data(user_id, name, email, age) VALUES (UUID(), %s, %s, %s);", (line[0], line[1], int(line[2])))
        
        connection.commit()
            
    except Exception as e:
        connection.rollback()
        print(e)
    finally:
        cursor.close()
   