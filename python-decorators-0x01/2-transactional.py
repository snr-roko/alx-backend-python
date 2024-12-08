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

# A decorator function that commits or rollbacks connections when database manipulation is successful or unsuccessful
def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = kwargs.get('conn')  
        if not conn:
            raise ValueError("No database connection provided")
            
        try:
            result = func(*args, **kwargs)
            conn.commit() 
            print("Transaction committed successfully")
            return result
        except Exception as e:
            conn.rollback() 
            print("Transaction rolled back due to error:", e)
            raise  
    return wrapper  

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')