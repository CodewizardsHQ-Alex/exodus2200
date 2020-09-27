from flask import Flask, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL
from database import create_tables, add_test_data

app = Flask(__name__)
app.secret_key = 'super secret key2'

app.config['MYSQL_USER'] = 'sql7367520'
app.config['MYSQL_PASSWORD'] = 'rsLdkWPtZm'
app.config['MYSQL_HOST'] = 'sql7.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql7367520'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
    if session.get('logged_in'):
        create_tables()
        success = add_test_data()
        return render_template('index.html', success=success)
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
            return redirect(url_for('home'))
        else:
            message="username or password unknown"
    
    
    return render_template("login.html", message=message)


@app.route("/wof", methods=['GET', 'POST'])
def wof():
    name = str(request.form['name'])
    '''
    date = request.form['date']
    time = request.form['time']

    output = name + "finished the Instructorgame on" + date + "with a time of" + time
    print(output)
    return output'''
    print("route wof successfully called by", name)
    return "Hello " + name


#test
