import os
from flask import (
    Flask, session, render_template, redirect, url_for, request, flash)
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
@app.route('/home')
def home():
    return render_template('home.html')


# Error handling code for most common errors 404, 500
# Discussion had with Mentor about how to include error handling
# Code adapted from https://www.askpython.com/python-modules/flask/flask-error-handling
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))

        register = {
            'username': request.form.get('username').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)

        # putting the new user into session cookie
        session['user'] = request.form.get('username').lower()
        flash('Registration Successful')
        return redirect(url_for('my_list', username=session['user']))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user['password'], request.form.get('password')):
                    session['user'] = request.form.get('username').lower()
                    flash('Welcome, {}'.format(
                        request.form.get('username')))
                    return redirect(url_for(
                        'my_list', username=session['user']))
            else:
                # invalid password match
                flash('Incorrect Username and/or Password')
                return redirect(url_for('login'))
        else:
            # username doesn't exist
            flash('Incorrect Username and/or Password')
            return redirect(url_for('login'))
            
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove user session from cookies
    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('login'))


@app.route('/my_list')
def my_list():
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    entry = mongo.db.entries.find()

    if session['user']:
        return render_template('my_list.html', username=username, entries=entry)

    return redirect(url_for('login'))


@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        entry = {
            'programme_name': request.form.get('programme_name'),
            'streaming_service': request.form.get('streaming_service'),
            'comment': request.form.get('comment'),
            'rating': request.form.get('rating'),
            'created_by': session['user']
        }
        mongo.db.entries.insert_one(entry)
        flash('Entry Successfully Added')
        return redirect(url_for('my_list'))
    
    return render_template('add_entry.html')


@app.route('/edit_entry/<entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    if request.method == 'POST':
        submit = {
            'programme_name': request.form.get('programme_name'),
            'streaming_service': request.form.get('streaming_service'),
            'comment': request.form.get('comment'),
            'rating': request.form.get('rating'),
            'created_by': session['user']
        }
        mongo.db.entries.update({'_id': ObjectId(entry_id)}, submit)
        flash('Entry Successfully Updated')
        return redirect(url_for('my_list'))

    entry = mongo.db.entries.find_one({'_id': ObjectId(entry_id)})
    return render_template('edit_entry.html', entry=entry)


@app.route('/delete_entry/<entry_id>')
def delete_entry(entry_id):
    mongo.db.entries.remove({'_id': ObjectId(entry_id)})
    flash('Entry Successfully Deleted')
    return redirect(url_for('my_list'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
