import asyncio
import aiosqlite

async def async_fetch_users():
    print("async_fetch_users function started")
    try:
        db = await aiosqlite.connect('users.db')
        print("Database Connected successfully")
    except Exception as e:
        print(f"Database Connection Error: {e}")
        return
    else:
        try:
            cursor = await db.execute("SELECT * FROM users;")
        except Exception as e:
            print(f"Database Execution Error: {e}")
            return
        else:
            users = await cursor.fetchall()
            await cursor.close()
            return users
    finally:
        await db.close()
        print("Database closed successfully")

async def async_fetch_older_users():
    print("async_fetch_older_users function started")
    try:
        db = await aiosqlite.connect('users.db')
        print("Database Connected successfully")
    except Exception as e:
        print(f"Database Connection Error: {e}")
        return
    else:
        try:
            cursor = await db.execute("SELECT * FROM users WHERE ? > 40;", ("age", ))
        except Exception as e:
            print(f"Database Execution Error: {e}")
            return
        else:
            users = await cursor.fetchall()
            await cursor.close()
            return users
    finally:
        await db.close()
        print("Database closed successfully")

async def fetch_concurrently():
    task_one = asyncio.create_task(async_fetch_users())
    task_two = asyncio.create_task(async_fetch_older_users())

    results = await asyncio.gather(task_one, task_two)

    return results

if __name__ == "__main__" :
    print(asyncio.run(fetch_concurrently()))

