seed = __import__('seed')
# A generator function that reads data from the user_data database
def stream_users():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM user_data;")
        
        while True:
            chunk = cursor.fetchone()
            if not chunk:
                break
            yield chunk
    except Exception as e:
        print("Error retrieving data: ", e)
    finally:
        cursor.close
        connection.close()