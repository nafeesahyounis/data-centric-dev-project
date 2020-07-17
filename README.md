# Data Centric Project
## Solo-Traveller-Handbook

[Heroku App](https://solo-travel-handbook.herokuapp.com/)

<div align="center">
    <img src="/static/images/homepageimage.png" target="_blank" rel="noopener" alt="Image of how home page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
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


### Create Activity Page

<div align="center">
    <img src="/static/images/create-activity.png" target="_blank" rel="noopener" alt="Image of how create page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

### Manage Listings Page

<div align="center">
    <img src="/static/images/managelistings.png" target="_blank" rel="noopener" alt="Image of how manage listings page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>




