import sqlite3
import csv

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Open the CSV file and read data
with open('user_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
        INSERT INTO users (name, email, age)
        VALUES (?, ?, ?)
        ''', (row['name'], row['email'], row['age']))

# Commit the changes and close the connection
conn.commit()
conn.close()