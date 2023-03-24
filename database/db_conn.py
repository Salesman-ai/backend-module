import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path
from logger.log import database_log 

config_path = Path('./config.cfg')
load_dotenv(dotenv_path=config_path)

def generate_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASS"),
            host=os.environ.get("POSTGRES_HOST"),
            port=os.environ.get("POSTGRES_PORT")
        )
    except Exception as error:
        database_log.error(error)
    finally:
        return conn