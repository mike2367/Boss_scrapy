
import pymysql 
from schedule import every, run_pending, repeat
import time


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
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]

            cursor.execute(f"SELECT * FROM {table_name}")
            records = cursor.fetchall()
            print(f"Records in {table_name}:")
            for record in records:
                print(record)
            print("*********************************************************************************")
            print(f"Table: {table_name}, Record count: {count}")
    except pymysql.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@repeat(every().day.at("00:00"))
def run_bodd_spider():
    import subprocess
    try:
        subprocess.run(['scrapy', 'crawl', 'Bossspider'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the 'Bossspider' spider: {e}")


if __name__ == "__main__":
    run_bodd_spider()
    print("*********************************************************************************")
    search_boss_db()
    while True:
        run_pending()
        time.sleep(1)
