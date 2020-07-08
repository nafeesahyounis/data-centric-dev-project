import os
from flask import Flask, flash, render_template, redirect, session, request, \
     url_for
from flask_pymongo import PyMongo
from os import path
from bson.objectid import ObjectId
from bson.json_util import dumps
from passlib.hash import pbkdf2_sha256
import json 
import bcrypt
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'solo_traveller_handbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'\x81\xa7\x9b\x8bq\x16x\x0b~A\x9c\xbb>\xe6\xef-'


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    User can type the city into the search bar \
    and hit submit. \ Mongodb is case sensitive\
    so for input is first converted to a lowercase string\
    and then returned as lowercase as the database is entirely\
    in lowercase.\
    If database entry matches city name, 
    the user will be redirected to the search activity page \
    and results will be displayed. 
    """
    search_bar_original = request.form.get('city')
    convert_to_lowercase_string = json.dumps(search_bar_original).lower()
    result = json.loads(convert_to_lowercase_string)
    if (request.method == 'POST'):
        search_database = list(
            mongo.db.things_to_do.find({'city': result}))
        return render_template('pages/find.html',
                               results=search_database)
    else:
        return render_template('pages/index.html')    


@app.route('/permissiondenied')
def permissiondenied():
    return render_template('pages/permissiondenied.html')

@app.route('/find')
def find():
    return render_template('pages/find.html')


@app.route('/find_activity', methods=['GET', 'POST'])
def find_activity(): 
    """
    User must type the name of a city and choose a category\
    Mongodb will be searched and all entries matching both the \
    city and category will be returned and displayed on \
    the find.html page. If user wants to also search for \
    additional filters like 'name', an if statement is used \
    and if the name field isn't empty, it's value will be \
    added to the search.
    """
    # form filters will not work if city and category are not specified.
    mandatory_search_filters = {'city': request.form.get('city'), 
                                'category': request.form.get('category')}
    # if user also specifies name, this will be added to the search filters
    if request.form.get('name') != "":
        name = {'name': request.form.get('name')}
        mandatory_search_filters.update(name)
    final_result = list(mongo.db.things_to_do.find(mandatory_search_filters))
    
   # if mandatory_search_filters == [] and request.form.get('name') != "":
   #     name = {'name': request.form.get('name')}
   # only_name_result = list(mongo.db.things_to_do.find(mandatory_search_filters))

    #print(only_name_result)
    print(final_result)
    no_results="No results found"
    return render_template("pages/find.html", 
                           results=final_result,
                           no_results=no_results,
                           )
                           

@app.route('/login', methods=['GET', 'POST'])
def login():
    users = mongo.db.users
    email = request.form.get('email')
    email_exists = users.find_one({'email' : email})
    user_password = users['password']
    form_password = request.form.get('password')

    if email_exists:
        if pbkdf2_sha256.verify(form_password, user_password):
            session['email'] = request.form['email']
            return redirect(url_for('index'))
            doesnt_exist = "Invalid username/password \
            combination. \
            Please try again, or register to make an account"
    print(doesnt_exist)
    return render_template("pages/login.html",
                            doesnt_exist=doesnt_exist)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email': request.form.get('email')})

        if existing_user is None:
            password = request.form['password']
            _hash = pbkdf2_sha256.hash(password)
            new_user = users.insert_one({
                                         'first_name': request.form.get('first_name'),
                                         'last_name': request.form.get('last_name'),
                                         'email': request.form.get('email'),
                                         'password': _hash})
            session['email'] = request.form.get('email')
            session['user'] = request.form.get('first_name', 'last_name')
            print(session['user'])
            print(new_user)
            return redirect(url_for('index'))
        return 'That Username Already Exists!'
    else:
        return render_template("pages/register.html")


@app.route('/logout')
def logout():
    session.clear()
    flash(f'Thank you for using Oly-Track. See you soon.', 'primary')
    return redirect(url_for('index'))


@app.route('/managemylistings')
def managemylistings():
    if 'email' in session:
        user = session['email']
        user_activities = list(mongo.db.things_to_do.find({'user': user}))
        no_activities = "You don't have any existing activities. Would you like to create some?"
        print(no_activities)
        print(user_activities)
        return render_template("pages/managemylistings.html", 
                               user_activities=user_activities, 
                               no_activities=no_activities)
    return render_template("pages/permissiondenied.html")
    

@app.route('/edit_activity/<user_activity_id>')
def edit_activity(user_activity_id):

    if 'email' in session:
        the_activity = mongo.db.things_to_do.find_one(
            {"_id": ObjectId(user_activity_id)})
        categories = mongo.db.things_to_do.find()
        return render_template("pages/editactivity.html", 
                               user_activity=the_activity, 
                               categories=categories)
    return render_template("pages/permissiondenied.html")

 
@app.route('/update_activity/<user_activity_id>', methods=['POST'])
def update_activity(user_activity_id):
    if 'email' in session:
        email = session['email']
        activities = mongo.db.things_to_do
        activities.update({'_id': ObjectId(user_activity_id)},
                          {
                            'user': email,
                            'name': request.form.get('name'),
                            'category': request.form.get('category'),
                            'city': request.form.get('city'),
                            'description': request.form.get('description')   
                          })

    return redirect(url_for('managemylistings'))

    
@app.route('/addactivity')
def addactivity():

    if 'email' in session:
        return render_template("pages/addactivity.html", 
                               categories=mongo.db.things_to_do.find())
    else:
        return render_template("pages/permissiondenied.html")


@app.route('/insert_activity', methods=['POST'])
def insert_activity():

    email = session['email']
    print(email)
    things_to_do = mongo.db.things_to_do
    things_to_do.insert_one(
                            {
                             'user': email,
                             'city': request.form.get('city'),
                             'category': request.form.get('category'),
                             'name': request.form.get('name'),
                             'description': request.form.get('description')

                            }
                           )
    return redirect(url_for('managemylistings'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)