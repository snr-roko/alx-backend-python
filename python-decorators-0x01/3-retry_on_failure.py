import time
import sqlite3 
import functools

# A decorator function that opens a database connection, completes function actions and closes connection afterwards
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect('users.db')
        except sqlite3.Error as e:
            print("Database Connection Error: ", e)
            return None
        else:
            try:
                print("Database Connected Successfully")
                kwargs['conn'] = conn
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print("Query Error:", e)
                return None
            finally:
                conn.close()
                print("Database Connection Closed Successfully")
    return wrapper

# A decorator function that retries functions for a number of time when there are errors 
def retry_on_failure(retries, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for retry in range(retries):
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    print("Query Error Occured: ", e)
                    if retry == 2:
                        raise
                    time.sleep(delay)
                else:
                    return result
                    
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)