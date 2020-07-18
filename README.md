# Data Centric Project
## Solo-Traveller-Handbook

[Heroku App](https://solo-travel-handbook.herokuapp.com/)

<div align="center">
    <img src="/static/images/new-homepage-screenshot.png" target="_blank" rel="noopener" alt="Image of homepage looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

The Solo-Traveller Handbook was created by the developer, Nafeesah Younis, to serve the solo travelling community. I belong to many Facebook communities geared specifically towards women who like to travel solo & often when you look at sites like TripAdvisor and you search for activities geared towards people who travel solo, it takes quite a bit of filtering to find what you need.

I felt that it would be a good idea to create a database where all of the recommendations made by the solo-travelling community were in one place, hence the birth of the solo-traveller-handbook.

# UX

## Goals

### Visitor Goals

The target audience for the Solo-Traveller-Handbook is 18+, English-speaking adults with a decent grasp of technology. Primarily the site is aimed at solo-travellers, but can be used by anyone who is travelling and looking for an additional resource to help them plan their trip.

The user goals are:

- To have a database where they can quickly search for things to do in a new city.

- To be able to create a record of places they've visited and enjoyed, and share it with others.

- To contribute to a growing global solo-traveller community.

The Solo-Traveller Handbook is a great way to meet these needs because:

- Currently travel sites like TripAdvisor are catered towards all travellers, and it requires a lot of filtering to find things just for solo-travellers.

- A lot of sites have recommendations made my tourists instead of seasoned travellers and locals. The Create Activity function allows locals to also share gems from their home cities.

- The design of the site is very simple and functional.

- At the moment users can search by city, category and name. In future, I hope to expand those filters but this was not possible within the timeframe allotted for this project.

### Business Goals

The target businesses for this site are both small and big business owners. They can use the site to recommend their restaurants, experiences etc to other travellers. 

### Business User Goals

Business user goals are:

- A functional, clean and appealing-to-the eye site upon which I can advertise my business.

- The ability to easily and efficiently add data about my services.

- For the end user to easily be able to find my listings through searching via the city and/or the category.

The Solo-Traveller-Handbook currently caters towards those needs in the following ways:

- Due to its easy-to-use interface and simple form layout, businesses can easily create an account and start creating listings immediately.

- Listings created by a business are automatically and immediately added to the global database, so potential clients can see the business straight away when they search.

- The 'Manage my Listings' page allows the business to go back to any listings he or she has created and make edits at any time, or delete. 

- Navigation buttons are placed on every page, so it is easy for the business user to quickly and efficiently achieve their goals.

### Solo-Traveller-Handbook Goals

- To provide a clean, clear site where solo-travellers can access recommendations made by locals, small business owners and other solo-travellers.

- As a developer, I wanted to practice combining Front-end & Backend languages and this is my first project doing so. I wanted to experiment with HTML, CSS, Bootstrap and Javascript combined with Python, MongoDB, Flask and Jinja.

- Although this is a student project, in the future I would like to expand the filters and potentially create a space that can be used by the solo-travel Facebook communities I am a part of to consolidate all of the information that is shared.

## User Stories

### Visitor Stories

As someone who is visiting the Solo-Traveller-Handbook, I want to:

- Immediately know what the site is for and what are the different features/things I can do on the site.

- Enjoy navigating the site. Be able to navigate it with ease and not feel frustrated by inconsistencies or a lack of buttons.

- Have something beautiful yet not overwhelming to look at, in order to inspire me to travel.

- Be able to search for what I need immediately, without too much navigation and without having to read through too much information.

- As someone who is travelling and may not have a larger device, I want to be able to search for things easily on my phone or tablet.

- As a traveller with a limited budget, I want to be able to find recommendations that aren't expensive to access.

- As a user of the site, I would like to be able to contact the creator of the site easily and quickly if I encounter any issues.

### Business Stories

As a business owner:

- As a business owner, I would like to be able to create my listing quickly and easily.

- As a business owner, I would like visitors to be able to see my listing ASAP so that I can quickly generate traffic.

- As a business owner, I would like to be able to manage my listings and edit or delete them as I please.

- As a business owner, I would like to be able to contact the creator of the site easily in case I encounter any problems. 

- As a business owner, I would like my data to be safe and not accessible to anyone.

- As a business owner, I would like an easy to use interface that I can navigate within a few clicks.

- As a business owner, I would like the platform that I advertise on to be aesthetically pleasing and inspire my potential customers to travel and search.

## Design Choices

The Solo-Traveller-Handbook has an overall feeling of adventure and exploration. This is in order to inspire the users of the site to travel and contribute to the handbook.

### Fonts

- The font 'Arimo', sans-serif' was used for the main content of the site, because I felt that it was very clear and bold without detracting too much from the overall design. It is also easy to read on smaller screen sizes.

- The font 'Shadows Into Light', cursive; has been used for the headers throughout the site, as I felt that it gave a fun, adventurous feel to the titles and fit nicely with the hero images. 

### Hero images

<div align="center">
    <img src="/static/images/hero-images.jpg" target="_blank" rel="noopener" alt="Image of how home page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

The following three hero images/illustrations were chosen for the Home, Search & Add Activity Pages respectively. These three images were chosen as they immediately draw the eye of the user, and therefore enhance the user experience.

I opted for illustrations instead of photographs as I felt that they gave the site a more individual feel and a more distinctive brand.

- The Hero Image for the index page (the solo traveller looking out at a landscape) was selected because it evoked a sense of adventure and mystery. I felt that from a design perspective it captured the essence of the site.

- The Hero Image for the Search Page (the person on the motorcycle) was chosen firstly because it aligned with the colour scheme, and secondly because the illustration matched the theme of the main page image. It also aligned with the idea of an activity that you'd do while travelling, and therefore created a visual image of 'discovering things to do on holiday'.

- The Hero Image for the Create Page was selected because of its aesthetic value and how it visually fit in with the theme. I also felt that the colour scheme creates an inspiring feeling, which would make users want to create and contribute to the site.


## Wireframes

Wireframes were made with [Balsamiq](https://balsamiq.com/) during the scope part of the project.

[Home](https://ibb.co/pfKjwrJ)

[Find](https://ibb.co/zVLJhDt)

[Create Activity](https://ibb.co/HHC1yx5)

[Manage My Listings](https://ibb.co/2dBdmTh)

[Edit](https://ibb.co/w6kpMGb)

[Register/Create Account](https://ibb.co/pfKjwrJ)

[Login](https://ibb.co/pfKjwrJ)

[Permission Denied](https://ibb.co/pfKjwrJ)







## Flowchart

## Development Planes

# Features
## Existing Features

* Navbar

The navbar is on each page and on smaller screens it turns into a hamburger menu on the left hand corner of the screen.

The following items are present on the navbar when the user is not logged in:

- Home

- Search Activity 

- Login

- Register

When the user is logged in, the following items are visible:

- Home

- Search Activity

- Create Activity

- Manage my Listings

- Logout

Python code was used and the session functionality in Flask was implemented, so when the user is in session they are logged in, and the second navbar appears:

if 'email' in session:

Jinga was also used in the base template in order to hide the navbar depending on if the user is in the session.

* Footer

Due to time constraints on the project, the footer was kept very simple and displays basic contact information and the name of the developer as well as Copywright info.

I would have liked to better refine and design the footer, but the project had a very strict timeline and so priority was given to the Python backend.


### Home Page

<div align="center">
    <img src="/static/images/new-homepage-screenshot.png" target="_blank" rel="noopener" alt="Image of homepage looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

* Hero Image

- A Hero image is at the top of the Home Page. An illustration of a solo-traveller staring off into an adventure was chosen in order to evoke feelings of travel, adventure and longing.

- This picture was selected because it perfectly fit the brand of the site and the dark blue color scheme evokes the sense of mystery required to inspire a user to search for new activities and use the site.

- The picture is also very visually appealing, and design time was limited during this project due to the tight time constraints, so I chose to have powerful illustrations that would enhance the user experience and require little additional code.

- The background image is full screen on smaller screen sizes, as there is text on it and this will make the mobile experience better.

* Search bar 

- Placed on top of the Hero Image is a search bar that immediately allows the user to start searching in the site by typing in the desired city.

- This choice was made in order to supply the user with a quick and efficient User experience and to make the site relaxing to manouevre. 

* Card Panels

- There are two card panels on the homepage, both of which offer different things. 

- The first card offers the user the option to search with more fields, as the search bar only allows the user to search with a city.

- The second card changes depending on if the user is logged in. If user is not logged in, they can create an account or login. If they are logged in, they can create an activity or manage their listings.

- The purpose behind having these card panels with the buttons on them directing to these options was to enhance user experience and navigation. The user can access all the functionalities of the site both through the navbar and the homepage, so there are a minimum number of clicks and the site is very easy to navigate.



### Find Page
<div align="center">
    <img src="/static/images/searchactivity.png" target="_blank" rel="noopener" alt="Image of how find page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

* Hero Image

- The hero image, as explained above, was chosen to enhance the UX and create a beautiful, inspirational feeling for the user to search with (see image choices above).

* Search filters

- There are three search filters on the site: city, category and name.

- The search filters were modified in the python so that regardless of which case the user submits the request, it will automatically convert to lowercase and return the result capitalizing the first letter.

- The search filters do not work unless the city and category are specified. This is pointed out in the text above on the hero image. I made this choice because you can search only with the city on the index page, and so I wanted the find page filters to be more specific to distinguish from the homepage search bar.

- See features left to implement for more detail on the filters. I would have liked for this part of the site to be more complex, but had a limited timeframe.

* Results

- The results are laid out on a card on the right hand side of the page with horizontal rules in between each result.

- Jinga templating |length was used, so that when results are returned they are counted and the number of results is displayed dynamically. I chose to do this as I wanted to experiment with filters in order to enhance my own ability to use the language. I also felt that it made the page look more professional.


### Login Page
<div align="center">
    <img src="/static/images/login.png" target="_blank" rel="noopener" alt="Image of how login page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

* Important note about login and registration system: An authentication system was not required for this project. However, I chose to create it more for the purpose of experimenting with Jinga and creating a reason to use functionality such as hiding the navbar depending on whether the user is in session, and a redirect for a permission denied page. I wanted to experiment with having different things visible depending on something and having an authentication system was the best way to really experiment both in the templates and in the app.py file.

For this reason, the login system was not heavily tested and I'm sure that it could be vastly improved. As is mentioned in the features to implement section, the timeline for both the Data Centric Module and the Milestone project was one month, and so things were heavily timeboxed and the Login system was not refined or prioritised.


- The login page has a simple form which takes the user's email address and password. 

- If the password or email address are incorrectly inputted, python returns the 'doesn't exist' variable, which essentially is a string that states that the incorrect username or password have been inputted. It also prompts the user to register if there is no existing account.

- Templating was used and this message appears above the register and login buttons.

- A register button is on the page for easier navigation.

### Register Page
<div align="center">
    <img src="/static/images/create-account.png" target="_blank" rel="noopener" alt="Image of how register page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

- The register page has four simple form fields, name, last name, email address and password.

- The password is hashed in the python and securely stored in the mongodb database.

- If the user inputs something incorrectly, the username already exists or fields are left blank, then already_exists is returned which is a string that alerts the user about the error in the template.


### Create Activity Page

<div align="center">
    <img src="/static/images/create-activity.png" target="_blank" rel="noopener" alt="Image of how create page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

* The Create Activity page has a hero image that has been detailed above in Design Choices.

* There is a form with the fields: City, name, category and description. Code was added so that it is not case sensitive and it automatically convers to lowercase and returns with the correct casing.

* If the name, city and category of the listing are not inputted, then it cannot be submitted and a message is returned from the python variable not_submitted that gives the user feedback and tells them that one of the three options is missing.

### Manage Listings Page

<div align="center">
    <img src="/static/images/managelistings.png" target="_blank" rel="noopener" alt="Image of how manage listings page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

* The manage listings page has the same hero image as the Create Activity Page in order for consistency as these are the two account elements when the user logs in.

* Each listing that has been created by the user is displayed here, and next to it is an edit and delete button.

* The delete button pulls up a modal that asks the user whether or not they are sure they want to delete their listing. This was implemented in order to avoid the user accidentally deleting something and to give them a chance to turn back, so two clicks are required for something to be removed from the database rather than one.

* The Edit button takes the user to the edit activity form. 

### Edit Activity Page

<div align="center">
    <img src="/static/images/edit.png" target="_blank" rel="noopener" alt="Image of how edit page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

* The Edit Activity Page is a simple form that takes the data of the listing clicked from manage listings and populates the form accordingly.

* The user can change any of the data and resubmit and it is not case sensitive. 

## Features left to Implement

There are a lot of features I would have liked to implement in this project. However, the time was very tight and it was important to keep it minimal and purposeful.

* Filters

- Currently there are only three filters on the search page and 4 options for the Create Activity page. I would have liked to make this a lot more complex. I experimented with price, days of the week and contact information. I tried using materialize selectors and other features. However, it was important to timebox the project and it took far too long to consolidate so additional filters were removed for the time being, but will be added at a later point.

- There are also only three categories in the categories section. I plan to add more at a later point. 

* User feedback modals

- A modal already exists for when the user tries to delete. However, I would have liked to use more Javascript and create a tighter flow of user feedback with JS modals. 

- When the user adds an activity, I plan to create a modal that reconfirms what the user has added in the fields and asks if they want to submit or go back and make more changes. This way the user can check spellings, syntax etc or add anything they've forgotten.

- I would like to have an additional modal on the edit page like mentioned above for add activity.

- A modal for when the user registers or logs in welcoming them to the site instead of redirecting to the index page would have also been better in terms of user site feedback.

* Tighter authentication system

- The authentication system was created using a combination of youtube videos and github code from other sources (see credits) and it was created in order to experiment with if statements in the templating language that concealed features and elements depending on whether user is logged in.

- This provided an excellent opportunity for me to experiment with and become more confident in Flask, using the database etc, but the authentication system is not fully secure as it was not prioritised and I plan to refine it at a later stage.

* My Account Page

- It would be useful if the user could change their account details and so I plan to create a my account page which has their account settings and lets them edit details.

* Favourites

- Currently the Manage My Listings page includes only the listings that the user has created. I would like to add an option on the Search Activity Page where the user can save their favourite listings created by other users and add them to Manage My listings.

* Sort filters

- Currently the Manage My Listings page displays everything the user has created. Ideally there would be an option to filter on this page so that when the user has a lot of things in their account, they can search through their own listings instead of having to scroll.

* Search bar by key word

- Currently the search bar takes a city and searches for that. I would like to have a search bar by key word function where the user can type any word and everything with that word or phrase shows up, without need for grammatic accuracy, so for example 'london food vegan'.

* Rating system

- I would like to add a rating system from 1-5 where the user ranks the place they are creating from 1-5 so users can also know what to avoid.

- Additional users can also add ratings to this, like most conventional sites, and so you can see how many people rated it where, and this can be filtered on the search page.

* Carousel/Top places

- Building on the rating system, I would like to create a carousel that takes the top rated places and displays them on the homepage.

* More content on footer, and generally cleaner design

- A lot of the design elements, in particular the footer, could use some cleanup and refinement and I intend to do this at a later stage.

* All of these features are manageable however it was necessary to timebox the project, so basic functionality and design was prioritised. For this reason also, limited Javascript was used and the focus was on the backend.

## Information Architecture

### Database Choice

Although an SQL database would have suited this project, I chose to use Mongodb Atlas. This is because as a student this is currently my only opportunity to use Mongodb because my final project requires SQL. The database was therefore chosen not because it is the best suited for the project, but because as a learning developer I wanted to experiment.

### Data Storage Types

Data stored in Mongodb for this project takes the following forms:
- ObjectId
- String
- Binary

Due to time restrictions, I did not experiment with other data such as booleans and datetime, but in future I would like to add these to the project for further experimentation and learning.

### Collections Data Structure

There are two collections used in this project. The first is things_to_do, which is where all of the activity info is stored, and the second is users where the user info is stored.

#### Users Collection

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
first_name | first_name | text | string
last_name | last_name | text | string
Email Address | email | email | string
Password | password | text | binary 

#### Things To Do Collection

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Activity ID | _id | None | ObjectId 
email | email(*user email) |text | string
city | city |text | string
category | category |text | string
name | name |text | string
description | description |text | string

* When user is in session, their email is automatically added to any entries that they add to the database, so there is a cross-relation between the two collections.

* Given that Mongodb methods are case sensitive, all data is stored in lowercase for the things_to_do collection. Additional functionality has been added to all forms related to this database (searchbar,find, add & edit). This functionality converts all inputted form data to a lowercase string, then into a lowercase dict and then it is returned with the proper casing in the search. This is for consistency & better UX when searching and adding.



## Technologies Used

* [GitHub](https://github.com/) - Was used to remotely store the code online.
* [Picresize](https://picresize.com/) - Used to crop images.
* Images were taken from [Freepik](https://www.freepik.com/) and [Pixabay](https://pixabay.com/).
* [Am I Responsive](http://ami.responsivedesign.is/) this was used in the README file to show the responsive web pages.


### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - This was used for the main markup of the site.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - This was used was for styling.
- [jQuery 3.4.0](https://code.jquery.com/jquery/) was used for the main javascript functionality.
- [Materialize 0.100.2](https://materializecss.com/) - was the design framework chosen for this project.

### Back-End Technologies

- **Flask**
    - [Flask 1.0.2](http://flask.pocoo.org/) - This was the microframework used to build the project.
    - [Jinja 2.10](http://jinja.pocoo.org/docs/2.10/) - Templates with Flask were created using Jinja.

- **Heroku**
    - [Heroku](https://www.heroku.com) - The app has been hosted on heroku.

- - **Python**    
    - [Python 3.6.7](https://www.python.org/) - was the backend language used for this project.
    - [MongoDB Atlas](https://www.mongodb.com/) - this is where the database was stored.

## Deployment

## Running the project locally

In order for this project to be run on your own IDE, you must do the following:

Make sure you have: an IDE, such as gitpod, Webstorm or Visual Studio.

It is necessary for these things to be installed on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- Either a [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account, or MongoDB locally running on your machine. 
    - Setting up the atlas account is done like so: [here](https://docs.atlas.mongodb.com/).


## Credits
