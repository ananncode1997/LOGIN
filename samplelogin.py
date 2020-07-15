from flask import Flask,render_template,redirect,url_for,request,session,flash, g
from functools import wraps
import sqlite3
app = Flask(__name__)


app.secret_key = 'my session'
app.database = 'sample.db'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('log'))
    return wrap

@app.route('/')
@login_required
def hello():
    g.db = connect_db()
    cur = g.db.execute('Select * from posts')
    posts = [dict(title = row[0], description = row[1]) for row in cur.fetchall()]
    g.db.close()
    # return "hello world"
    #return 'welcome ' + session['user']
    return render_template("index.html",posts = posts)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/log',methods=['GET','POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please Try Again'
        else:
            session['logged_in'] = True
            flash("YOu are logged in")
            return redirect(url_for('hello'))
    return render_template("log.html",error = error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("YOu are logged out")
    return redirect(url_for('welcome'))

def connect_db():
    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run(debug=True)
