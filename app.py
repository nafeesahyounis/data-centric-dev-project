import os
from flask import Flask, render_template, redirect, session, flash, request, url_for
from flask_login import LoginManager
from flask_pymongo import PyMongo
from os import path
from bson.objectid import ObjectId
from bson.json_util import dumps
import bcrypt
#from app import login

if path.exists("env.py"):
  import env 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'solo_traveller_handbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'\x81\xa7\x9b\x8bq\x16x\x0b~A\x9c\xbb>\xe6\xef-'
#login_manager = LoginManager()
#login_manager.init_app(app)


#@login.user_loader
#def load_user(id):
#    return User.query.get(int(id))

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():

    if 'email' in session:
        return 'You are logged in as' + session['email']
    else:
        return render_template("pages/index.html")

    
    
    city_to_search = {'city': request.form.get('city')}
    if (request.method == "POST"):
      
        search_database = list(mongo.db.things_to_do.find(city_to_search))
        print(search_database)
        print(city_to_search)
        return redirect(url_for('findactivity'))
    else:
        return render_template("pages/index.html", activities=mongo.db.things_to_do.find())


#@app.route('/searchfromhomepage', methods=['POST'])

#def searchfromhomepage():

    result = request.form.get('city')
    final_result = mongo.db.things_to_do.find_one({result})
    print(result)
    print(final_result)
    return redirect(url_for('pages/findactivity.html'))


@app.route('/find')
def find():
    return render_template("pages/find.html", categories=mongo.db.things_to_do.find())


@app.route('/login')
def login():
    return render_template("pages/login.html")


@app.route('/logging_in', methods=['POST'])
def logging_in():
    #email = request.form.get('email')
    #password = request.form.get('password')
    #user_email = mongo.db.users.find_one({'email': email})
    #user_password = mongo.db.users.find_one({'password': password})
    user = mongo.db.users.find_one({'name': request.form.get('name')})
    query = {'$and': [{'password': request.form.get('password')}, {'email': request.form.get('email')}]}
    result = mongo.db.users.find_one(query)
    print(result)
    if result == None:
        print("User does not exist")
    else:
        print("user has been found")

    #if email and password == user_email:
    #    print("User has been found")
    #else:
    #    print("user does not exist")
    #print(user_email)
    return redirect(url_for('index'))
#check if email is in database
#check if password is in database
#if yes, log in
#if no, user does not exist. Would you like to register?


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method =='POST':
        users = mongo.db.users
        existing_user = users.find_one({'email': request.form.get('email')})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            new_user = users.insert_one(request.form.to_dict())
            session['email'] = request.form.get('email')
            print(new_user)
            return redirect(url_for('index'))
        return 'That Username Already Exists!'
    else:
        return render_template("pages/register.html")

@app.route('/logout')
def logout():
   session.clear()
   return redirect(url_for('index'))
#@app.route('/new_user', methods = ['POST'])
#def new_user():

    #users = mongo.db.users
   # users.insert_one(request.form.to_dict())
   # first_name = request.form.get('first_name')
   # surname = request.form.get('last_name')
   # print(first_name)
   # print(surname)
  #  return render_template('pages/newuser.html', surname=surname, first_name = first_name)


@app.route('/find_activity', methods=['GET', 'POST'])
def find_activity():

    #category_to_search = request.form.get('category')
    #city_to_search = request.form.get('city')
    #name_to_search = request.form.get('name')
    #matching_activities = mongo.db.things_to_do.find({'category': category_to_search, 'name': name_to_search, 'city': city_to_search})
    #print (matching_activities)
    my_name= "Nafeesah2"

    #search_dict = { 'city': request.form.get('city'), 'category': request.form.get('category') }

    #if request.form.get('name') != "":
    #    search_dict['name'] = request.form.get('name')
    search_dict = {'city': request.form.get('city')}  #'category': request.form.get('category')
    # if request.form.get('name') != "":
    #     name = {'name': request.form.get('name')}
    #     search_dict.update(name)

    #edited_activities = search_dict.update(name)
    #original_activities = list(mongo.db.things_to_do.find(search_dict))
    final_activities = list(mongo.db.things_to_do.find(search_dict))


    #if name !="":
    #    one_activity = list(mongo.db.things_to_do.find(search_dict.update(name))
    #return(one_activity)

    # create an instance of the dictionary for category & city
    # create an instance of the name attribute
    # when form data includes name, modify search_dict and add a name filter 
    # need to test and see if dictionary value for name is empty
    
    #if name is !="":
    #    new_dict = search_dict.update(name)
     #   final_activities = list(mongo.db.things_to_do.find(new_dict))
    #return (final_activities)

    # using bool() 
    # Check if dictionary is empty 
    #res = not bool(name) 
    #if res:
    #    final_activities= list(mongo.db.things_to_do.find(search_dict))
    #else:
    #    final_activities= list(mongo.db.things_to_do.find(new_dict))
    #    print("Is dictionary empty ? : " + str(res)) 


    #    print(new_dict)

    #    print(my_name)
    #    print(final_activities)
    #    return render_template('pages/findactivity.html', result=search_dict)


    # print result 
    #print("Is dictionary empty ? : " + str(res)) 


    print(search_dict)
    #print(new_dict)

    print(my_name)
    print(final_activities)
    #print(edited_activities)
    #print(final_activities)
    
    return render_template("pages/findactivity.html", result=final_activities)


@app.route('/edit_activity/<activity_id>')
def edit_activity(activity_id):

        the_activity = mongo.db.things_to_do.find_one({"_id": ObjectId(activity_id)})
        categories = mongo.db.things_to_do.find()
        return render_template("pages/editactivity.html", activity=the_activity, categories=categories)

 
@app.route('/update_activity/<activity_id>', methods=['POST'])
def update_activity(activity_id):

    activities=mongo.db.things_to_do
    activities.update({'_id': ObjectId(activity_id)},
    {
     'name': request.form.get('name'),
     'category': request.form.get('category'),
     'city': request.form.get('city'),
        
    })

    return redirect(url_for('index'))

    
@app.route('/addactivity')
def add():

    if 'email' in session:
        return render_template("pages/addactivity.html", categories=mongo.db.things_to_do.find())
    else:
        return "Permission Denied"


@app.route('/insert_activity', methods=['POST'])
def insert_activity():

    things_to_do = mongo.db.things_to_do
    things_to_do.insert_one(request.form.to_dict())
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)