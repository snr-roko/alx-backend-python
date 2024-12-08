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
            
@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 

#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)