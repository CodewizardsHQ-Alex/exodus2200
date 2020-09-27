from flask import Flask, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

def create_tables():
    cur = mysql.connection.cursor()
    s = cur.execute('''CREATE TABLE IF NOT EXISTS TEST (id INTEGER, name VARCHAR(20))''')
    return s

def add_test_data():
    cur =     cur = mysql.connection.cursor()
    s = cur.execute('''INSERT INTO TEST (id , name ) VALUES (0, "Alex")''')
    return s