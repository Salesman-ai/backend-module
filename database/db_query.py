from db_conn import generate_connection
import psycopg2
from logger.log import log

def check_connection():
    conn = None
    try:
        conn =  generate_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        log.info(f"Connection established to: {data}")
    except (Exception, psycopg2.DatabaseError) as error:
        log.error(error)
    finally:
        if conn is not None:
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
        log.info(f"Data: {data} inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        log.error(error)
    finally:
        if conn is not None:
            conn.close()