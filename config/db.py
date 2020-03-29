import psycopg2
from psycopg2 import pool
import traceback
import os
import logging

# Database connection
def connect_db(app):
    try: 
        print("Establishing connection..")
        app.config['postgreSQL_pool'] = psycopg2.pool.SimpleConnectionPool(1, 20,
            user = os.getenv("DATABASE_USER"),
            password = os.getenv("DATABASE_PASS"),
            host = "127.0.0.1",
            port = os.getenv("DATABASE_PORT"),
            database = os.getenv("DATABASE_NAME")
        )
    except Exception:
        logging.error(traceback.format_exc())
        logging.error('Failed to set db connection pool for {0}')
        print("Database connection error")


