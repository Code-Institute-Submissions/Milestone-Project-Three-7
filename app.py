import os
from flask import (
    Flask, session, render_template, redirect, url_for, request)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        #Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if existing_user:
            flash('Username alreadu exists')
            return redirect(url_for('register'))
        
        register = {
            'username': request.form.get('username').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)

        #put the new user into session cookie
        session['user'] = request.form.get('username').lower()
        flash('Registration Successful')
        return redirect(url_for('profile', username=session['user']))

    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/my_list')
def my_list():
    entry = mongo.db.entries.find()
    return render_template('my_list.html', entries=entry)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)