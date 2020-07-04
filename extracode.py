
#@app.route('/logging_in', methods=['POST'])
#def logging_in():
    #email = request.form.get('email')
    #password = request.form.get('password')
    #user_email = mongo.db.users.find_one({'email': email})
    #user_password = mongo.db.users.find_one({'password': password})
    #user = mongo.db.users.find_one({'name': request.form.get('name')})
    #query = {'$and': [{'password': request.form.get('password')}, {'email': request.form.get('email')}]}
    #result = mongo.db.users.find_one(query)
    #print(result)
    #if result == None:
    #    print("User does not exist")
    #else:
     #   print("user has been found")

    #if email and password == user_email:
    #    print("User has been found")
    #else:
    #    print("user does not exist")
    #print(user_email)
    #return redirect(url_for('index'))
#check if email is in database
#check if password is in database
#if yes, log in
#if no, user does not exist. Would you like to register?


#login line 72
    #collect_form_data = {'$and': [{'password': request.form.get('password')}, {'email': request.form.get('email')}]}


#@app.route('/searchfromhomepage', methods=['POST'])

#def searchfromhomepage():


#login_manager = LoginManager()
#login_manager.init_app(app)


#@login.user_loader
#def load_user(id):
#    return User.query.get(int(id))


#@app.route('/new_user', methods = ['POST'])
#def new_user():

    #users = mongo.db.users
   # users.insert_one(request.form.to_dict())
   # first_name = request.form.get('first_name')
   # surname = request.form.get('last_name')
   # print(first_name)
   # print(surname)
  #  return render_template('pages/newuser.html', surname=surname, first_name = first_name)



#for find

#category_to_search = request.form.get('category')
    #city_to_search = request.form.get('city')
    #name_to_search = request.form.get('name')
    #matching_activities = mongo.db.things_to_do.find({'category': category_to_search, 'name': name_to_search, 'city': city_to_search})
    #print (matching_activities)


 #search_dict = { 'city': request.form.get('city'), 'category': request.form.get('category') }

    #if request.form.get('name') != "":
    #    search_dict['name'] = request.form.get('name')

# if request.form.get('name') != "":
    #     name = {'name': request.form.get('name')}
    #     search_dict.update(name)

#edited_activities = search_dict.update(name)
    #original_activities = list(mongo.db.things_to_do.find(search_dict))

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

 #'category': request.form.get('category')

  # print result 
    #print("Is dictionary empty ? : " + str(res)) 
#print(new_dict)

#print(edited_activities)
    #print(final_activities)
