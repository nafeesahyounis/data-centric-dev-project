import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
  import env 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'solo_traveller_handbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def index():
    return render_template("pages/index.html", tasks=mongo.db.things_to_do.find())

@app.route('/find')

def find():
    return render_template("pages/find.html")

@app.route('/addactivity')

def add():
    return render_template("pages/addactivity.html", categories=mongo.db.things_to_do.find())

@app.route('/insert_activity', methods=['POST'])

def insert_activity():

    things_to_do = mongo.db.things_to_do
    things_to_do.insert_one(request.form.to_dict())
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)