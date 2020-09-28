from flask import Flask, render_template, redirect, request, url_for, session
import MySQLdb
from database import create_tables, add_test_data, read_user_data, read_planet_data, add_user, add_planet_data

app = Flask(__name__)
app.secret_key = 'super secret key2'

mysql = MySQLdb.connect(host="Exodus2200.mysql.pythonanywhere-services.com", user="Exodus2200", passwd="Excalibur_01", db="Exodus2200$exodus2200")


@app.route('/')
def home():
    if session.get('logged_in'):

        cur = mysql.cursor()

        #create_tables(cur)
        #add_test_data(cur)
        #add_user(cur, "Alex van Winkel", "Alexicoo", "1234", 0)
        #add_user(cur, "Peter de Wit", "pwit", "1234", 0)
        #add_planet_data(cur)
        #cur.execute('''INSERT INTO Planets (planet_id, name, x_pos, y_pos, z_pos, url, message ) VALUES ( 1, "Mygross", -234, 877, 32, "Hx18Ah1u", "We have hhacked your system")''')
        #mysql.commit()
        users = read_user_data(cur)
        planets = read_planet_data(cur)
        cur.close()
        return render_template('index.html', users=users, planets=planets)
    else:
        return redirect(url_for('login_page'))

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    message = ""
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        if username == "alex" and password == "csgo":
            session['logged_in'] = True
            session['admin'] = True
            return redirect(url_for('home'))
        else:
            message="username or password unknown"


    return render_template("login.html", message=message)


@app.route("/register", methods=['GET', 'POST'])
def register():
    cur = mysql.cursor()
    #add_user(cur, "Alex van Winkel", "Alexicoo", "1234", 0)
    #add_user(cur, "Peter de Wit", "pwit", "1234", 0)
    #add_planet_data(cur)
    #cur.execute('''INSERT INTO Planets (planet_id, name, x_pos, y_pos, z_pos, url, message ) VALUES ( 1, "Mygross", -234, 877, 32, "Hx18Ah1u", "We have hhacked your system")''')
    #mysql.commit()
    return render_template('register.html', message=message)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if session.get('admin'):
        #create_tables(cur)
        #add_test_data(cur)
        cur = mysql.cursor()
        users = read_user_data(cur)
        planets = read_planet_data(cur)
        cur.close()
        return render_template('admin.html', users=users, planets=planets)
    else:
        return redirect(url_for('login_page'))

#test
