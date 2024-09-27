# Start Generation Here
import pymysql 

def search_boss_db():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='boss'
        )
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT * FROM {table_name}")
            records = cursor.fetchall()
            print(f"Records in {table_name}:")
            for record in records:
                print(record)
    except pymysql.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    
search_boss_db()
