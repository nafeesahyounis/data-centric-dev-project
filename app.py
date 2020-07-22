import os
from flask import Flask, render_template, redirect, session, request, \
     url_for
from flask_pymongo import PyMongo
from os import path
from bson.objectid import ObjectId
from passlib.hash import pbkdf2_sha256
import json
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'solo_traveller_handbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
# Set the secret key to some random bytes. Keep this really secret!
#app.secret_key = b'\x81\xa7\x9b\x8bq\x16x\x0b~A\x9c\xbb>\xe6\xef-'


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    User can type the city into the search bar \
    and hit submit.\
    Mongodb is case sensitive\
    so form input is first converted to a lowercase string\
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
    """
    If user tries to enter add, edit or managelistings page/
    without being logged in they will be redirected to/
    permission denied. Also if they are already logged in/
    they will be redirected here because they can't log/
    in twice.
    """
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
    convert_to_lowercase_string = json.dumps(mandatory_search_filters).lower()
    result = json.loads(convert_to_lowercase_string)
    # if user also specifies name, this will be added to the search filters
    if request.form.get('name') != "":
        name = {'name': request.form.get('name')}
        result.update(name)
    final_result = list(mongo.db.things_to_do.find(result))
    no_results = "No results found"
    return render_template("pages/find.html",
                           results=final_result,
                           no_results=no_results,
                           )


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ First checks if user is already in session and if they are/
        takes them to Permission Denied so they can't login twice./
        If user simply loads page (get request), then login form is displayed./
        If user inputs data, checks if email and password match and if they/
        don't, returns error message in template (doesn_exist). / Otherwise/
        user is successfully logged in, redirected to Index and their name/
        is stored and displayed under 'Welcome' on index page to give feedback/
        and show that they've logged in. Code was taken from PrettyPrinted and/
        modified for my use (see README for credits) """
    if 'email' in session:
        return render_template('pages/permissiondenied.html')
    else:
        doesnt_exist = "Invalid username/password \
            combination. \
            Please try again, or register to make an account"
        if request.method == "GET":
            return render_template('pages/login.html')
        elif request.method == "POST":
            email = request.form['email']
            user = mongo.db.users.find_one({'email': email})
            if user is None:
                return render_template('pages/login.html',
                                       doesnt_exist=doesnt_exist)
            user_password = user['password']
            form_password = request.form['password']
            if pbkdf2_sha256.verify(form_password, user_password):
                session['email'] = request.form['email']
                name = user.get('first_name')
                return render_template('pages/index.html',
                                       name=name)
            else:
                return render_template('pages/login.html',
                                       doesnt_exist=doesnt_exist)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """(code was taken from PrettyPrinted and modified for my use./
       see Credits in README file for full reference./
       Firstly, this checks if the method is POST. If not, it/
       just returns the form. If it is, email address entered already/
       is searched for in database and if it already exists it returns/
       the already_exists variable in the template to give user/
       feedback. If it doesn't exist, then it inserts all the info/
       into the collections 'users' and creates a new user. When new user/
       is created user is redirected to index page and their name is displayed/
       under the 'Welcome' to give feedback that the registration was successful.
    """
    if request.method == 'POST':
        users = mongo.db.users
        email = request.form.get('email')
        name = request.form.get('first_name')
        existing_user = users.find_one({'email': email})
        if existing_user is None:
            password = request.form['password']
            _hash = pbkdf2_sha256.hash(password)
            users.insert_one({
                                'first_name': name,
                                'last_name': request.form.get('last_name'),
                                'email': email,
                                'password': _hash})
            session['email'] = email
            return render_template('pages/index.html',
                                   name=name)
        return render_template("pages/register.html",
                               already_exists='That Username Already Exists!')
    else:
        return render_template("pages/register.html")


@app.route('/logout')
def logout():
    """
    Session is cleared when user logs out and redirect/
    to homepage.
    """
    session.clear()
    return redirect(url_for('index'))


@app.route('/managemylistings')
def managemylistings():
    """
    User can only access this page if he/she is logged/
    in otherwise he/she will be redirected to/
    permission denied.
    All activities created by current user in session/
    will be found by mongodb find method and displayed/
    on this page to be viewed, edited or deleted via/
    additional buttons (see update_activity and delete_activity).
    """
    if 'email' in session:
        user = session['email']
        user_activities = list(mongo.db.things_to_do.find({'user': user}))
        no_activities = "You don't have any existing activities. Would you like to create some?"
        return render_template("pages/managemylistings.html",
                               user_activities=user_activities,
                               no_activities=no_activities)
    return render_template("pages/permissiondenied.html")
    

@app.route('/edit_activity/<user_activity_id>')
def edit_activity(user_activity_id):
    """
    This is page loads upon clicking on edit button/
    on managemylistings. If user isn't logged in/
    they will be redirected to permissiondenied/
    otherwise they will be sent to a form to/
    edit listing (see update_activity).
    """
    if 'email' in session:
        the_activity = mongo.db.things_to_do.find_one(
            {"_id": ObjectId(user_activity_id)})
        return render_template("pages/editactivity.html",
                               user_activity=the_activity)
    return render_template("pages/permissiondenied.html")

 
@app.route('/update_activity/<user_activity_id>', methods=['POST'])
def update_activity(user_activity_id):
    """
    The object id from the chosen listing is taken/
    and the form is filled with the existing data./
    When form data is inputted, it is firstly converted/
    to a lowercase string and then back to a lowercase/
    dict so that the database remains in lowercase when/
    being updated./
    Once edits are done, user hits edit and is sent to/
    managemylistings where he/she can see the new edited/
    entry.
    """
    if 'email' in session:
        email = session['email']
        activities = mongo.db.things_to_do
        name = request.form.get('name')
        city = request.form.get('city')
        name_lower = json.dumps(name).lower()
        new_name = json.loads(name_lower)
        city_lower = json.dumps(city).lower()
        new_city = json.loads(city_lower)
        activities.update({'_id': ObjectId(user_activity_id)},
                          {
                            'user': email,
                            'name': new_name,
                            'category': request.form.get('category'),
                            'city': new_city,
                            'description': request.form.get('description')
                          })

    return redirect(url_for('managemylistings'))

    
@app.route('/delete_activity/<user_activity_id>')
def delete_activity(user_activity_id):
    mongo.db.things_to_do.remove({'_id': ObjectId(user_activity_id)})
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
    """First, all variables are created. Second, the code checks/
       if city is empty, if category is empty and if name is empty./
       If any of these fields are empty, form data is not submitted/
       and there is an error displayed to user asking them to enter/
       mandatory fields. If all fields have been entered, """
    email = session['email']
    things_to_do = mongo.db.things_to_do
    city = request.form.get('city')
    category = request.form.get('category')
    name = request.form.get('name')
    not_submitted = "Uh oh. Either the city, category or name were not entered, so your listing has not been submitted."
    if city == '':
        return render_template('pages/addactivity.html',
                               not_submitted=not_submitted)
    if category is None:
        return render_template('pages/addactivity.html',
                               not_submitted=not_submitted)
    if name == '':
        return render_template('pages/addactivity.html',
                               not_submitted=not_submitted)
    else:
        name_lower = json.dumps(name).lower()
        new_name = json.loads(name_lower)
        city_lower = json.dumps(city).lower()
        new_city = json.loads(city_lower)
        things_to_do.insert_one(
                            {
                             'user': email,
                             'city': new_city,
                             'category': category,
                             'name': new_name,
                             'description': request.form.get('description')

                            }
                           )
    return redirect(url_for('managemylistings'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)