### SEED.PY STRUCTURE
A python script that seed.py:

Set up the MySQL database, ALX_prodev with the table user_data with the following fields:
user_id(Primary Key, UUID, Indexed)
name (VARCHAR, NOT NULL)
email (VARCHAR, NOT NULL)
age (DECIMAL,NOT NULL)

Populate the database with the sample data from this user_data.csv
Prototypes:
def connect_db() :- connects to the mysql database server
def create_database(connection):- creates the database ALX_prodev if it does not exist
def connect_to_prodev() connects the the ALX_prodev database in MYSQL
def create_table(connection):- creates a table user_data if it does not exists with the required fields
def insert_data(connection, data):- inserts data in the database if it does not exist

__0-main.py__ is used to implement the script

### 0-stream_users.py 

A generator function is created to retrieve data one by one from the database.

__1-main.py__ is used to implement the script

### 1-batch.py structure
A generator functions for retrieving data in batches from the database user_data table and use another function to filter for ages more than 25.

__2-main.py__ is used to implement the script