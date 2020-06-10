import os
from flask import Flask, render_template
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb+srv://nafeesahyounis:milestone3@cluster0-zkr6m.mongodb.net/solo_traveller_handbook?retryWrites=true&w=majority'


@app.route('/')
def index():
    return render_template("pages/index.html")

@app.route('/find')

def find():
    return render_template("pages/find.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)