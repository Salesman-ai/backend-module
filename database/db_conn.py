import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path

config_path = Path('./config.cfg')
load_dotenv(dotenv_path=config_path)

def generate_connection():
    conn = psycopg2.connect(
        dbname=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASS"),
        host=os.environ.get("POSTGRES_HOST"),
        port=os.environ.get("POSTGRES_PORT")
    )
    return conn