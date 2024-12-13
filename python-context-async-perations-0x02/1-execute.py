import sqlite3

class ExecuteQuery:
    def __init__(self, query, placeholder):
        self.query = query
        self.placeholder = placeholder
        self.db = "users.db"        
        
    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        print("Database connected successfully")
        self.result = None
        try:
            self.cursor.execute(self.query, self.placeholder)
        except sqlite3.OperationalError as e:
            self.result = f"SQL Error Occured: {e}"
        else:
            self.result = self.cursor.fetchall()
        
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
        print("Database connection closed")


with ExecuteQuery("SELECT * FROM users WHERE age > ?", 25) as query_result:
    print(query_result)