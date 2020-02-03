import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Hello():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
