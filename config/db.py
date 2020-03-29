import psycopg2
from psycopg2 import pool
import os

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
        print(os.getenv("DATABASE_USER"))
    except: 
        print("Error while establishing database connection")


