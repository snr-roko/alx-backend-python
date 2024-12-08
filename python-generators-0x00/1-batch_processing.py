seed = __import__('seed')
# A generator function that batch streams data from the database by size
def stream_users_in_batches(batch_size):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM user_data;")
        
        while True:
            chunk = cursor.fetchmany(batch_size)
            if not chunk:
                break
            yield chunk
    except Exception as e:
        print("Error retrieving data: ", e)
    finally:
        cursor.close
        connection.close()

# A function that filters each batch for users over the age of 25
def batch_processing(batch_size):
    generator = stream_users_in_batches(batch_size=batch_size)
    
    for chunk in generator:
        for user_data in chunk:
            if user_data[3] > 25:
                print(
                    {
                        'user_id': user_data[0],
                        'name': user_data[1],
                        'email': user_data[2],
                        'age': user_data[3]
                    }
            )