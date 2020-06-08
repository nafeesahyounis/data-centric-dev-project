import os
from flask import Flask, render_template

app = Flask(__name__)


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