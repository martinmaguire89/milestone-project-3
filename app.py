import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")

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
