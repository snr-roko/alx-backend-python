import sqlite3
import functools
import time

#### decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Query: ", args[0])
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print("Query Error: ", e)
            return None  
            
        try:
            with open('query-loggings.txt', 'a') as file:
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {args[0]}\n")
        except Exception as e:
            print("Query Completed, File Appending error")
        else:
            print("Query Completed, Query logged into file, query-loggings.txt")
        
        return result
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users("SELECT * FROM users")
print(users)