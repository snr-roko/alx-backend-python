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

query_cache = {}

def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            query = kwargs['query']
            result = query_cache.setdefault(query, func(*args, **kwargs))
            return result
        except Exception as e:
            print("Query Error Occured: ", e)
            raise
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")