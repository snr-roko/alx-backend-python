seed = __import__('seed')

def stream_user_ages():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT age FROM user_data;")
        
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

def calculate_average_age():
    total_ages = 0
    count = 0
    for age in stream_user_ages():
        print(age[0])
        total_ages += age[0]
        count += 1
    average_age = total_ages / count
    print(f"Average age of users: {average_age}") 

calculate_average_age()
