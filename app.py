import os
from flask import Flask, render_template, redirect, request, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'greatest_fighters'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/fighters')
def fighters():
    return render_template("fighters.html",
     categories=mongo.db.categories.find())
    if 'username' in session:
        return 'You are logged in as' + session ['username']

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():

    return render_template('login.html')

    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('addfighter.html'))

            return 'invalid username/password combination'

    

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users

        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf - 8'),
                                    bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return render_template('login.html')

        return 'That username already exists'

    return render_template('signup.html')


@app.route('/addfighter')
def addfighter():
    return render_template('addfighter.html',
       categories=mongo.db.categories.find())

@app.route('/insert_fighter', methods=['post'])
def insert_fighter():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('fighters'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
