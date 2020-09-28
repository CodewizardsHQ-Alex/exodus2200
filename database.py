from flask import Flask, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

def create_tables():
    cur = mysql.connection.cursor()
    #s = cur.execute('''CREATE TABLE IF NOT EXISTS TEST (id INT, name VARCHAR(20))''')
    #s = cur.execute('''DROP TABLE Users''')
    s = cur.execute('''CREATE TABLE IF NOT EXISTS Users (   user_id INT NOT NULL AUTO_INCREMENT, 
                                                            name VARCHAR(255),
                                                            username VARCHAR(32),
                                                            password VARCHAR(32),
                                                            date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                            level INT NOT NULL DEFAULT 0,
                                                            state VARCHAR(32) DEFAULT 'clear',
                                                            last_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                                                            PRIMARY KEY (user_id) 
                                                            )''')
    s = cur.execute('''CREATE TABLE IF NOT EXISTS Planets ( planet_id INT NOT NULL, 
                                                            name VARCHAR(50),
                                                            x_pos INT,
                                                            y_pos INT,
                                                            z_pos INT,
                                                            url VARCHAR(255),
                                                            message VARCHAR(255),
                                                            PRIMARY KEY (planet_id) 
                                                            )''')
    
    #s = cur.execute('''CREATE TABLE IF NOT EXISTS Planets (id INT, name VARCHAR(20))''')
    #s = cur.execute('''CREATE TABLE IF NOT EXISTS State (id INT, name VARCHAR(20))''')
    cur.close()
    return

def add_test_data():
    cur = mysql.connection.cursor()
    #s = cur.execute('''INSERT INTO Users (name, username, password, level ) VALUES ("Alex van Winkel", "alexicoo", "1234", 0)''')
    s = cur.execute('''INSERT INTO Users (name, username, password, level ) VALUES ("Peter de Wit", "peter", "1234", 0)''')
    s = cur.execute('''INSERT INTO Users (name, username, password, level ) VALUES ("Frank de Wit", "frank", "1234", 0)''')
    cur.close()
    return

def add_planet_data():
    cur = mysql.connection.cursor()
    s = cur.execute('''INSERT INTO Planets (planet_id, name, x_pos, y_pos, z_pos, url, message ) VALUES ( 0, "Tygross", -234, 877, 32, "Hx78Ah1u", "We have hacked your system")''')
    cur.close()
    return

def add_user(name, username, password, level):
    cur = mysql.connection.cursor()
    s = cur.execute('''INSERT INTO Users (name, username, password, level ) VALUES (%s, %s, %s, %s)''', (name, username, password, level ))
    cur.close()

def read_all_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM Planets''')
    records = cur.fetchall()
    cur.close()
    return records

