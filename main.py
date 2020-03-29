from flask import Flask, g, jsonify, request, escape
from flask_cors import cross_origin
import os
import psycopg2
from psycopg2 import pool
import logging
app = Flask(__name__)
from config import db
from dotenv import load_dotenv
load_dotenv()

#Establishing postgres database connection
db.connect_db(app);

def get_db():
    if 'db' not in g:
        g.db = app.config['postgreSQL_pool'].getconn()
    return g.db

#connection close hack
@app.teardown_appcontext
def close_conn(e):
    db = g.pop('db', None)
    if db is not None:
        app.config['postgreSQL_pool'].putconn(db)

# Default endpoint
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

# sample GET API endpoint
@app.route('/sample_get', methods=['GET'])
@cross_origin(origins='*')
def sample_get():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("select * from employees;")
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)

