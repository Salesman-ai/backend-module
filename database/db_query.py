from db_conn import generate_connection
import psycopg2

def check_connection():
    conn =  generate_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print(f"Connection established to: {data}")
    conn.close()

def insert_price(data):
    sql = """INSERT INTO ..."""
    conn = None
    try:
        conn =  generate_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (data,))
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()