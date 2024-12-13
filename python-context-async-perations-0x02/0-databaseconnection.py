import sqlite3


class DatabaseConnection:

    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        print("Database connection created")
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Error occurred: ", exc_value)
        self.connection.close()
        print("Database connection closed")


with DatabaseConnection('users.db') as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)

