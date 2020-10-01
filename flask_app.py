from flask import Flask, render_template, redirect, request, url_for, session
import MySQLdb
from database import create_tables, add_test_data, read_user_data, read_planet_data, add_user, add_planet_data
from database import read_invitation_codes
app = Flask(__name__)
app.secret_key = 'super secret key2'

mysql = MySQLdb.connect(host="Exodus2200.mysql.pythonanywhere-services.com", user="Exodus2200", passwd="Excalibur_01", db="Exodus2200$exodus2200")


@app.route('/', methods=['GET', 'POST'])
def home():
    if session.get('logged_in'):
        message = ""
        if request.method == "POST":

            if request.form.get("L") == "logout":
                session.clear()
                return redirect(url_for('login_page'))
            else:
                message = "L = " + str(request.form.get("L"))
            return render_template('index.html',  message=message)
        else:
            message = "All systems operational"
            return render_template('index.html',  message=message)
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
    print(0)
    message = ""
    if request.method == 'POST':
        
        cur = mysql.cursor()
        valid_inv_codes = []
        data = read_invitation_codes(cur)
        cur.close()
        
        for d in data:
            valid_inv_codes.append(d[1])
        print("Invitation codes :", valid_inv_codes)
        print("Data :", data)
        print(3)
        inv_code = request.form['invitation_code']
        print(4)
        username = request.form['username']
        print(5)
        pssw1 = request.form['password1']
        print(6)
        pssw2 = request.form['password2']
        
        if pssw1 != pssw2:
            
            message = "passwords don't match"
        else:
            
            message = "All good : " + str(inv_code) + " ; " + str(username)
            
        return render_template('register.html', message=message)
    print(7)
    return render_template('register.html', message=message)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if session.get('admin'):
        cur = mysql.cursor()
        #create_tables(cur)
        add_test_data(cur)
        users = read_user_data(cur)
        planets = read_planet_data(cur)
        invitation_codes = read_invitation_codes(cur)
        mysql.commit()
        cur.close()
        return render_template('admin.html', 
                                users=users, 
                                planets=planets,
                                invitation_codes=invitation_codes)
    else:
        return redirect(url_for('login_page'))

