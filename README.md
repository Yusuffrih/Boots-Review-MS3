# Boots Review 

The Boots review site has the main goal of being a site where people can go to view reviews of different pairs of football boots that other people have owned. One aspect of he site is that this will be a site they can visit to assist them in making the decision of what pair of boots to purchase. 

A secondary aspect is that when these people have bought their pair of boots, they will be able to review their new pair of boots and assist others in making their decision. 

- [Boots Review](#boots-review)
  * [User Experience (UX)](#user-experience--ux-)
    + [Site Owner Goals](#site-owner-goals)
    + [User Goals](#user-goals)
    + [User Stories](#user-stories)
    + [User Requirements](#user-requirements)
    + [User Expectations](#user-expectations)
  * [Design Choices](#design-choices)
    + [Fonts](#fonts)
    + [Colours](#colours)
    + [Icons](#icons)
    + [Wireframes](#wireframes)
    + [Data Schema](#data-schema)
  * [Features](#features)
  * [Features Yet To Implement](#features-yet-to-implement)
  * [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Frameworks & Libraries](#frameworks---libraries)
    + [Tools](#tools)
  * [Testing](#testing)
    + [User Story Testing](#user-story-testing)
      - [User Registration](#user-registration)
      - [Create a secure account with a username and password](#create-a-secure-account-with-a-username-and-password)
      - [Reviews:](#reviews-)
      - [Create](#create)
      - [View](#view)
      - [Edit](#edit)
      - [Delete](#delete)
      - [Read a review that someone else wrote](#read-a-review-that-someone-else-wrote)
      - [Search the database for boot reviews based on makes, categories, reviewer, or Boots name](#search-the-database-for-boot-reviews-based-on-makes--categories--reviewer--or-boots-name)
      - [Profile:](#profile-)
      - [View](#view-1)
      - [Edit](#edit-1)
      - [Delete](#delete-1)
    + [Admin Testing](#admin-testing)
      - [Manage Categories](#manage-categories)
      - [Add Category](#add-category)
      - [Read](#read)
      - [Edit Category](#edit-category)
      - [Delete Category](#delete-category)
      - [Add Make](#add-make)
      - [Read Make](#read-make)
      - [Edit Make](#edit-make)
      - [Delete Make](#delete-make)
    + [Validator Testing](#validator-testing)
      - [HTML Validator](#html-validator)
      - [CSS Validator](#css-validator)
    + [Feature Testing](#feature-testing)
    + [Lighthouse Testing](#lighthouse-testing)
    + [Compatability Testing](#compatability-testing)
    + [CRUD Testing](#crud-testing)
    + [Bugs](#bugs)
  * [Deployment](#deployment)
    + [Github Pages](#github-pages)
    + [Run Locally](#run-locally)
    + [Deploying in Heroku](#deploying-in-heroku)
  * [Credits](#credits)
  * [Final Comments](#final-comments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## User Experience (UX)

### Site Owner Goals
* As a site owner, I want to give users no usability of the site without the requirement to register. This will ecourage registration.
* As a site owner, I would like to make it a requirement to sign up if users want to review a pair of football boots they have recently worn and then update and delete their reviews thereafter. 
* As a site owner, I would like to collect a database of reviews of football boots
* As a site owner, I would like to collect a database of star ratings of the football boots that are reviewed so that I can eventually create a ranking of the top rated boots
* As a site owner, I would like the site to be easy to use and intuitive
* As a site owner, I would like the site to have an attractive UI with an obvious color scheme
* As a site owner, I would like the user to be able to create, read, update and delete their profile
* As a site owner, I would like the user to be able to create, read, update and delete their boots reviews
* As a site owner, I would like to have access to the admin section of the site that is off limits to the normal user.
* As a site owner, I want to be able to create read and update and delete the categories and makes of the football boots


### User Goals
* I would like the site to be responsive to different screen sizes so that I can use different devices to view the site
* I would like to feel like I am part of a community of people who have the same interest in football boots
* I would like to be given feedback from the site confirming when I have completed an action such as creating or deleting a review of a pair of football boots
* I would like to be able to create, read, update and delete my profile
* I would like to be able to create, read, update and delete my reviews
* I would like to be able to contact the site owner and provide some feedback on the site
* I would like to be able to search for specific boots
* I would lile to be able to search for reviews created by specific users based on their user names
* I would like to be able to search for reviews based on specific boot makes
* I would like to be able to search for reviews based on specific boot categories
* I would like to be able to have a record of all the reviews that I have created on my profile page
* I would like to be able to securely log out and end my user session


### User Stories
* As a user of the site, I would like to be able to register my details and create a secure account with a username and password
* As a user, I would like to be able to write a review of a pair of boots I wore
* As a user, I would like to be able to update/edit a review that I wrote
* As a user, I would like to be able to read a review that someone else wrote on a pair of boots
* As a user, I would like to be able to delete a review that I wrote on a pair of boots
* As a user, I would like to be able to search the database for boot reviews based on makes, categories, reviewer, or Boots name 
* As a user, I would like to be able view, edit, and delete my profile 
* As a user, I would like to be able to view my reviews that I created in a centralised location in my profile page

### User Requirements
* The site needs to be easy to navigate between the different features via good UX and a concise navbar
* To be able easily see whether or not a CRUD action has been successful or not
* To have a landing page that tells the user what the page is at a glance
* To have a well laid out site that is easy to use and understandable
* To be able to read clearly any messaging that is displayed on screen via constrasting backgrounds
* To be given clear and easy to understand instructions via good UX
* To be able to contact the site owner to provide feedback or make a complaint if necessary
* To have my registration and personal data and password secure in the database
* All features need to be working as expected
* All features and functionality need to be well laid out and intuitive
* The site needs to be responsive across all devices and browsers

### User Expectations
* All of the content needs to be easily readable and contrasting with the background colours and imagery
* Navigation of the site needs to be really easy and intuitive
* The site owner should be easily contactable - contact page and contact info in the footer of the site
* Any forms should always provide me with instructions so that I know what input it expects

## Design Choices
Generally, football boots tend to be quite sleek and stylish so I decided to try and keep this site the same way. The overall look and feel of the site is very soft touch with nice lines and angles. The colours are quite bright and bold with lots of orange and black and blue and off white. The touch of colour, I feel gives the site an extra bit of style.

### Fonts
There is little text on the landing page. For the fonts, I used [Google Fonts](https://fonts.google.com/?standard-styles=). This is a really fantastic feature of [Google](https://google.com) which is great for getting any kind of font you want. The fonts I chose for my page are *Play* & *Roboto* with *sans-serif* as a backup font in the event that [Google Fonts](https://fonts.google.com/?standard-styles=) does not work. The reason I decided to use *Play* & *Roboto* is that I found them to be quite sleek fonts which would almost represent a pair of football boots. 

### Colours
In deciding the colour scheme for the site, I decided to go for a cool, almost retro mix between orange and blue mixed with black. There is often a lot of black with splashes of colour. The black tends to make the colour stand out and is a really good contrasting background for reading content. The same idea goes for the off white that is used throughout the site as well. 

I used the site [Coolors](https://coolors.co/) to assist in generating a colour scheme for the site. This is a great site as it gives you the codes of the colours you want in any form you want ie. Hex code. 

![Colour Pallette](static/images/color-palette.png)

The colours I have chosen are: 
* Rich Black Fogra 39 - Hex (0B0909)
* White - Hex (FFFFFF)
* Platinum - Hex (ECEAEC)
* Aero - Hex (67B7E6)
* Persian Orange - Hex (E98D50)

### Icons 
I have gone to [Font Awesome](https://fontawesome.com/) for the icons that I have used in the site. The icons, I feel just add a little bit extra to the site in terms of style and make it a bit more visually appealing which ultimately provides a better User Experience.

### Wireframes
When creating my wireframes, I first drew some rough sketches on paper but then decided that [Balsamiq](https://balsamiq.com/) would be the most suitable technology to use to assist with the design of the site.

You will see from the wireframes that a lot has changed since the planning stage of the project as I learned a lot about what direction I wanted the project to go the more I went through the development process.

I created mock ups for my page to fit into the main device types - Desktop, Tablet and Mobile. The mock-ups for the devices can be found here: 
* [Mobile](static/wireframes/mobile)
* [Tablet](static/wireframes/tablet)
* [Desktop](static/wireframes/desktop)

### Data Schema
To carry out the functionality of the site, I needed to create three different collections of data. They are: 
1. Users 
3. Categories
4. Reviews
7. Makes
8. Star Ratings

The Users collection is made up of the following fields: 
| Field       | Data Type | Default |
|-------------|-----------|---------|
| id          | ObjectId  | " "     |
| username    | string    | " "     |
| password    | string    | " "     |
| profile_pic | string    | " "     |
| bio         | string    | " "     | 

The Categories collection is made up of the following fields:
| Field          | Data Type | Default |
|----------------|-----------|---------|
| id             | ObjectId  | " "     |
| category_name  | string    | " "     |

The Reviews collection is made up of the following fields:
| Field             | Data Type | Default |
|-------------------|-----------|---------|
| id                | ObjectId  | " "     |
| user_id           | string    | " "     |
| review            | string    | " "     |
| star_rating_id    | string    | " "     |
| image_url         | string    | " "     |
| category          | string    | " "     |
| boots_name        | string    | " "     |
| make              | string    | " "     |
| review_date       | string    | " "     |

The Makes collection is made up of the following fields:
| Field | Data Type | Default |
|-------|-----------|---------|
| id    | ObjectId  | N/A     |
| name  | string    | N/A     |

The Stars collection is made up of the following fields:
| Field  | Data Type | Default |
|--------|-----------|---------|
| id     | ObjectId  | N/A     |
| rating | number    | N/A     |


## Features
The site features are as follows: 
* Navigation bar at the top of the site for easy and intuitive navigation around the different pages of the site
* Registration page where the user can input their details, username and password
* Search bar for users to be able to search through the database:
    * to find reviews of particular boots that they want to read review of
    * to find reviews of boots that are of a certain make
    * to find reviews of boots that are of a certain star rating
* User feedback whenever they carry out any of the CRUD operations
* User feedback on forms in the case that they have not filled the form in correctly
* Bootstrap css design features such as navbar, buttons cards etc.
* Bootstraps responsive web design which allows users to use the site on all device sizes
* A beautiful looking profile page displaying a photo of the user, a bio and their reviews that they have written
* A landing page that lets the user know what the site is about at a glance
* To be able to sign out whenever the user is finished
* For the admin user to be able to manage the site such as add categories and makes

## Features Yet To Implement
* I would have like to implement a feature that allows the users to attacha link to a site where you can purchase the pair of boots that they are reviewing but I did not have time to develop this feature.

## Technologies Used

### Languages
* [HTML](https://en.wikipedia.org/wiki/HTML) - HTML is a markup language I used for structuring and presenting content of my site
* [CSS](https://en.wikipedia.org/wiki/CSS) - A language used to style the presentation of the content written in HTML5
* [Javascript](https://en.wikipedia.org/wiki/JavaScript) - Javascript is the language used to provide the interactivity to the user on the site
* [Python](https://www.python.org/) - Python is a backend programming language that is highly powerful and is designed around readability. It's language constructs and object oriented approach assist programmers in writing clear and easily read code
* [BSON](https://en.wikipedia.org/wiki/BSON) - BSON is the binary encoding of JSON-like documents that MongoDB uses when storing documents in collections. It adds support for data types like Date and binary that aren't supported in JSON.

### Frameworks & Libraries
* [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - A front-end framework which assist me in creating responsive website design
* [Google Fonts](https://fonts.google.com/) - An open-source online library of thousands of fonts and icons that were free and easy to use.
* [Font Awesome](https://fontawesome.com/) - An open source online library of icons which I used for extra styling.
* [Pip3](https://pypi.org/project/pip/) - Pip3 is the package installer for Python and is used to download Python dependencies from the command line
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - used to import the following functions: flash, render_template, redirect, request, session, url_for
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - Workzeug is used in this project to for password security.

### Tools
* [Coolors](https://coolors.co/) - Used this to generate a colour scheme that matched what I wanted for the site.
* [Pexels](https://www.pexels.com/) - Online library of stock photos for use for free.
* [Balsamic](https://balsamiq.com/) - Software used to complete the wireframes. This was much easier than trying to draw.
* [CSS Formatter](https://www.cleancss.com/css-beautify/) - This is used to beautify the CSS code
* [Javascript Formatter](https://beautifier.io/) - This is used to beatify the Javascript code to ensure the correct formatting is applied
* [Git](https://en.wikipedia.org/wiki/Git) - System used version control
* [GitHub](https://github.com/) - This is where my project repository was stored.
* [GitPod](https://www.gitpod.io/) - Open source, online workspace used to work on my project
* [MongoDB](https://www.mongodb.com/1) - MongoDB is an object-oriented, simple, dynamic, and scalable NoSQL database. It where I stored the database for this project
* [Heroku](https://id.heroku.com/login) - Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps to get it to the market
* [Pep8](https://pypi.org/project/pep8/) - Used pip3 to install pep8 validator which is a tool which ensures you stick to the pep8 compliance
* [W3 HTML Validator](https://validator.w3.org/) - Used to validate my code to ensure that there were no errors.
* [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to validate my code to ensure that there were no errors.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/Chrome) - A set of development tools to assist the user create web content. They are built directly into the browser
* [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) - One of the Chrome Dev Tools which was used to assess the level of accessibility, performance and correctness that was provided by the site.
* [Youtube](https://www.youtube.com/) - Youtube videos are a great way to learn how to do different things if stuck on a particular piece of code
* [Favicon](https://favicon.io/) - An online tool that generates the icon that is found in the tab bar at the top of the page beside the title of the page.
* [RandomKeyGen](https://randomkeygen.com/) - A tool that creates a random password to be used

## Testing

### User Story Testing
1. #### User Registration
    1. #### Create a secure account with a username and password
    * #### Plan
    I planned to create the landing page with a button to for login and signup on the actual page as well as having nav items to these same pages so as to increase the likelyhood of the user seeing the link.
    The plan once the user gets to the registration page is to request that they create a username and secure password and click signup. I will discuss the form authentication for the patterns required in the username and password in the form authentication testing section.   
    * #### Implementation
    I did exactly as planned on this and created the landing page with the links found in Bootstrap buttons on the page and in the Bootstrap navbar as well so that the user would find it as easy as possible to get to these pages while also being able to see an attractive landing page.
    I created a separate page for the signup form to rest in and the set up the backend function to allow the user to add a record to the user collection in the database when they signup correctly.
    * #### Test
    To test the different scenarios of this part of the user story, I needed to test registering with a brand new username and an already existing username. I also tested the form validation to ensure the user data integrity and this is discussed in the form validation testing below.
    * #### Result
    The user registration worked exactly as expected and the user was not able to signup with an existing username and succesfully signed up with a username that didn't exist. When signup was successfull the user received a flash message to make them aware of same.
    
    This is a pass

    2. View profile (see profile testing no.8 below)
    3. Edit (see profile testing no.8 below)
    4. Delete (see profile testing no.8 below)

2. #### Reviews:
    1. #### Create
    * #### Plan
    The plan is for the user to be able to add a review is to have a button in the navbar and the profile page to allow them to essentially add a review from anyhere in the site as long as they are signed in. The user will click the button which will route them to the add review form. The form, again is valiated using the browsers in-built validation system. The user must fill in all the fields before they will be allowed to add a review so that the information is good in the database and also so that the page looks good when rendered.
    The user will be able to press the cancel button which will redirect them away from the add review form and to their profile page. Once the user clicks the submit button, this will send the record to the database and redirect the user to the profile page where they will be able to see a flash message confirming the action was successful and also see the review they just created alongside any other reviews they might have already made.

    * #### Implementation
    I created the buttons needed in the nav bar and the profile page to be able to add the reviews. I linked up the route to these buttons and created the form to add the review in html. Each of the fields is validated using the browser validation system and has a required attribute and a pattern for validation. In the form, the user can choose from a few predetermined select options for things like the boots category and make and star rating which ensures data integrity in the database. For simplification when filling out the form, I made the date of the review autofilled through the backend which always puts the date the review was actually completed. Once all the fields are filled in the user can click the submit button which sends the data to the database.

    * #### Test
    The test for this is to be signed into the site as a user to be able to access this feature and then click the button in the nav to add review which should take me to the relevant page to add a review and then add the review and ensure that the form and the submit button works as expected. Once the button is clicked the user should then be redirected to the profile page where a flash should appear confirming the action was successful and also see the review they just created alongside any other reviews they might have already made.
    The same will be done using the add review button that is in the profile page to ensure that both methods / routes are working as expected.
    * #### Result
    All of the features described above worked as expected and the testing was a success.

    1. #### View
    * #### Plan
    To view the reviews, the plan is for the user to be able to view their own reviews that they have created in their profile page. These will be visible underneath the user profile section where they will be able to see the profile pic and bio. The reviews will be listed and sorted by category alphabetically. The listed reviews, when visible in the profile page will have all the data that the user inputs in the add review form, including the review photo. The reviews will also have edit and delete buttons as well as a drop down to see the main body of the review. 
    * #### Implementation
    To implement this, I created a card for the reviews to be displayed and then looped through the reviews and created a card for each one in the database that belongs to the user in session. The cards contatain bootstrap buttons to edit and delete and also a button that targets a dropdown to display the written review. When the user is new to the site and does not have any reviews, there will be an alternative placeholder in the place of the reviews just letting the user know that they have no reviews as of yet and that they can add one by clicking the button found on the page. 
    
    * #### Test
    To test this, it would mean signing into the site with a user profile and initially not having any reviews created to see if there is some placeholder text in the space where the reviews should be. Then once this part is established, add a review and once you are directed back to the home page after completing the review, you should see the review on the profile page. 
    * #### Result
    Once the above steps are carried out and review is added, it appears on the home page as expected and displays in a grid format. The testing is a success. If more reviews are added, they all are displayed on the user's profile page.

    2. #### Edit
    * #### Plan
    The user should be able to edit the reviews that they create. The plan is to have an edit button on the review cards on the profile pages of the users so that the users can only edit their own reviews that they created. Once the button is pressed, they will be rrouted to the edit reviews page where they will see a form the same as the add review form. The only difference is that it will be pre-populated with the details of the review in question. Once the user changes any details of their boots review and submits the form, the will be redirected back to the profile page where the updates will be rendered.
    * #### Implementation
    Implementing this meant building a button and putting it in the card for the button and routing the user to the edit page via a function in the backend which passes the relevant review information to the page from the database. The user can then change the information in the html form and submit the data which is posted to the database and the user gets redirected to the homepage. 
    * #### Test
    To test this, I would have to have already have a review created and I would have to click on the edit button to ensure that the edit review page renders. Once this renders properly, I would have to ensure that all the data is being taken from the database correctly and put into the relevant fields in the form. I would then make some changes to this data and click on the submit button to post these changes back to the database. Once the profile page displays again, I would have to ensure that the edited changes have displayed correctly as this would provide confirmation of the edits being posted correctly. 
    * #### Result
    After completing the action outlined above, all of the desired results were achieved. The test is a success.

    3. #### Delete
    * #### Plan
    The user should be able to delete the reviews that they create. The plan is to have a delete button on the review cards on the profile pages of the users so that the users can only delete their own reviews that they created. Once the user clicks the delete button, it is planned that a warning modal should pop up on screen requesting them to confirm that they want to delete the review. This is good defensive programming. The user should then be able to either exit out of the modal or confirm the deletion. The modal then closes and the review deletes and dissapears from the page. A flash messsage should then display to confirm the action has been successfull. 
    * #### Implementation
    To implement this, it was important to put in place some defensive programming and making the first delete button trigger the modal to pop up rather than have the review delete immediately. So the delete function in the backend is only triggered by the modal delete button.
    * #### Test
    The user should click the delete button and see the modal appear immediately warning them that the data is irretrievable once it's been deleted and requesting them to confirm deletion. If the user clicks to close the modal, the modal should close and if they click the delete button, the review should delete from the database and disappear from the user's profile page.
    * #### Result
    The review deleted when this test was carried out. This is a successfull test.

3. #### Read a review that someone else wrote
    * #### Plan
    All users should be able to see the main database of review records in a centralised location. The reviews page should display all the reviews in the database. The user should be able to see the card of each review be able to click on the dropdown to be able to read the review part itself. The card button for the dropdown is also going to be the picture of the boots. 
    * #### Implementation
    The review are rendered to the database via the backend in a list. All the reviews are displayed in a card that has been looped through in the html document using jinja. Each review has all the information from the review displayed and contains a button/picture to display the dropdown which contains the reviewers comments on the review. The button is in the review image which is a pair of football boots.
    * #### Test
    The test for this is simply for the tester to navigate to the reviews page through the navbar and ensure that they can view the reviews
    * #### Result
    All of the results were as expected. Successfull test. 

7. #### Search the database for boot reviews based on makes, categories, reviewer, or Boots name 
    * #### Plan
    The plan is to give the user the feature that they can search the entire database of review records for certain types of boots reviews based on the above mentioned criteria. This feature is to sit on the reviews page where the reviews are to be renderred in a list anyway. The search bar will have a seach button and a reset button to reset the search the renderred data after a search has been made. If the users result is not found i.e., they are searching for something that doesn't exist, then there will be a message displayed in the place of the reviews to inform the user.

    * #### Implementation
    The search bar is a form in the html and posts a request for the database to send back the database records. This is done using the indexing which was done in the terminal and which allows the user to target the criteria as described above. 

    * #### Test
    The test is simply to input some search criteria that you know does not exist. Then to input some search criteria that does exist for each of the different criteria that is searchable under the index.

    * #### Result
    After carrying out the testing as outline above all of the search criteria displayed as expected and the correct message displayed if the search could not be found.

8. #### Profile:
    1. #### View 
    * #### Plan
    The plan is that when the user signs up, logs in or clicks on the profile tab in the navbar, that they will be able to view their profile page which should display they username, photo and bio (if added to profile) or if not already to the profile page, I plan on putting in place a default icon for the profile picture and a message in the place of the profile bio to let the user know that they can edit their profile and add the bio in it's place
    * #### Implementation
    To implement this, I created a profile page with the outlined elements above and linked the profile page where relevant. I put in place an if statement using Jinja syntax to check if the user collection has any data in the fields for the profile picture and bio and if they do, then to display the relevant data in the rendered page. If they do not have data in those fields, I put in place a default profile icon and bio message as mentioned above. Of course the functionality for the relevant features was created using the profile function in the backend. 

    * #### Test
    To test this, I logged in as a new user to first see if the expected default profile pic would be in place and also the default message in the place of the profile bio. I then logged in as an existing user who had some data in place i.e. profile pic and bio. 

    * #### Result
    I was able to see all of the features of the profile page as expected and all of the information was correct and displaying as expected.
    
    This is a pass

    2. #### Edit
    * #### Plan
    For the user to edit their profile page, I wanted to give them an edit button which sat directly underneath their profile picture and that made it really clear that they could edit their profile using good UX. As all of the other buttons in the site, this button would be made with Bootstrap and would have custom styling. The edit button would take the user to a new page where they would find the edit profile form. Once they fill in the form, they can click a submit button or they can cancel the edit profile action which would take them back to their profile page. The aim is for the user to have to input their password to be able to update their profile page. I also want to provide the user with confirmation that the profile has been successfully updated.

    * #### Implementation
    I created the button to edit the profile page with Bootstraps buttons and placed it under the profile picture. Once the user clicks this button, it redirects them to the edit profile page using Jinja and Python routing. I created the form in html and added the action and method to this so that it's a post method and made all of the input fields mandatory so that the user has to input the data which will make the site more rich and ultimately provide a better UX.

    * #### Test
    The test for this is to go into a users profile and click edit profile. It should take them to the edit profile page where they can fill in the form in it's entirity or cancel editing the profile. If they fill in a new password, this will become their new password or they can fill in their existing one to complete the form. 

    * #### Result
    I was able to carry out all of the forementioned actions without any errors. I got a flash message once I hit the submit button to say that I had successfully updated the profile page.
    This test was a success.

    3. #### Delete 
    * #### Plan
    The delete button is planned to be placed beside the edit button underneath the profile picture but I want it to be cloured in red to let the user know that it is not to be pressed without thinking first. Once the user clicks the delete button, I plan on a modal popping up for them as a form of defensive programming. The user will then warned in the modal and they would have to click another red delete button before the profile is deleted. 

    * #### Implementation
    To implement this feature and satisfy the user story, the delete button and modal was created using Bootstrap. The button targets the modal which triggers it to be brought up on screen. There is then another set of buttons in the modal and the delete button calls the delete function which is in Python to delete the user profile from the database and also delete that user's reviews. Once the deletion has occured, then the user is redirected to the homepage via the delete profile function in the backend.  

    * #### Test
    To test this, the user clicks the delete button, a modal should pop up for them as a form of defensive programming. The user will then be warned in the modal and they would have to click another red delete button before the profile is deleted. Once the claimant deletes the profile, they are redirected to the home page. Alternatively, if the user decides that they do not want to delete the page, they can click the close button to get out of the modal. 

    * #### Result
    This test was carried out on a couple of occassions and the result was as expected. The delete button was clicked, a modal popped up with a warning before deletion is completed. The close button was clicked to ensure that I could cancel the deletion of the profile page which worked as expected. The delete button was then clicked and the site was rediected to the home page and the login and signup buttons are displayed. 
    
    This test was a success.

### Admin Testing
#### Manage Categories
1. #### Add Category
    * #### Plan
    The plan is that only the 'admin' user will be able to access the manage page. This page will display the manage categories section which will have a button for adding categories. The user will have to click that button which will render the add category form which is a one field form. This form will be filled out and submitted and the manage categories page will be rendered again with the data posted to the database and the new data should be displaying in the manage categories section. 
    * #### Implement 
    To implement this, I had to create a button on bootstrap and a render the add category form on the add category page. This page takes the uses input and posts it to the database. Before this can happen though, the backend checks to see if there category name already exists. If it does, the user is given a flash message to say try again. If it doesn't exist already, the new category is added to the database and the user is redirected back to the manage page where the nw category is displayed.
    * #### Test
    To test this, the admin user must follow the steps above and try and add a category that is already there and see if the database will accept this. The admin must also try and add a category name that isn't in existence already.
    * #### Result
    The result is that the expected results are returned and the test is successfull

2. #### Read
    * #### Plan
    When the admin first goes to the manage page, they should be able to see the categories to manage. The backend should be rendering the categories in a list on the page and they should be sorted alphabetically.
    * #### Implement 
    Added a card to the html and looped over the card to add in the category name for each category on the databse. This is then passed through the manage route and displayed on the page.
    * #### Test
    Look at the database in mongo db and see what cateogories are there. Cross reference them with the ones that are on the manage page. Add a category as above and then see if that one is being rendered to the page as well. Also check to see if they are in alphabetical order.
    * #### Result
    All results are as expected.

3. #### Edit Category
    * #### Plan
    On the manage page, the admin user should be able to see an edit button on each of the cards. When this button is clicked, the user should be taken to the edit category page which will be the same as the add category page but it will be pre-populated. Once the user makes the change to the name of the category, the same check will be done to see if the new category name exists already. If not, the new name will be posted to the database and the user will be redirected to the manage page where the new name will be displayed along with the other existing categories.
    * #### Implement 
    Created a button that renders the edit category page which is auto-populated. This is done using html and jinja templates. The backend then checks the database to see if the user input exists or not. If this new category does not exist, it is added to the database, the user is redirected to the manage page and the category displays alongside the other existing categories.
    * #### Test
    Try to add a category that exists & a category that doesn't exist.
    * #### Result
    Everything worked as expected and the result is a success.

4. #### Delete Category
    * #### Plan
    The admin user will visit the homepage and want to remove a category. They will click the delete button which will be attached to each category. The button, when clicked will trigger a modal to appear on the screen warning the user that the category cannot be retrieved when it's deleted. The modal will also have a confirm deletion button and a close modal button.
    * #### Implement 
    Created a button for each category card. The button when clicked triggers the modal and each one has it's own individual id so that the backend knows what to delete from the database.
    * #### Test
    Attemp to delete something and make sure that the correct item is being deleted.
    * #### Result
    Result is as expected. Test succeeded.

1. #### Add Make
    * #### Plan
    The plan is that only the 'admin' user will be able to access the manage page. This page will display the manage makes section which will have a button for adding makes. The user will have to click that button which will render the add makes form which is a one field form. This form will be filled out and submitted and the manage makes page will be rendered again with the data posted to the database and the new data should be displaying in the manage makes section. 
    * #### Implement 
    To implement this, I had to create a button on bootstrap and a render the add makes form on the add category page. This page takes the uses input and posts it to the database. Before this can happen though, the backend checks to see if there make name already exists. If it does, the user is given a flash message to say try again. If it doesn't exist already, the new make is added to the database and the user is redirected back to the manage page where the nw make is displayed.
    * #### Test
    To test this, the admin user must follow the steps above and try and add a make that is already there and see if the database will accept this. The admin must also try and add a make name that isn't in existence already.
    * #### Result
    The result is that the expected results are returned and the test is successfull
2. #### Read Make
    * #### Plan
    When the admin first goes to the manage page, they should be able to see the make to manage. The backend should be rendering the makes in a list on the page and they should be sorted alphabetically.
    * #### Implement 
    Added a card to the html and looped over the card to add in the make name for each category on the databse. This is then passed through the manage route and displayed on the page.
    * #### Test
    Look at the database in mongo db and see what makes are there. Cross reference them with the ones that are on the manage page. Add a make as above and then see if that one is being rendered to the page as well. Also check to see if they are in alphabetical order.
    * #### Result
    All results are as expected.

3. #### Edit Make
    * #### Plan
    On the manage page, the admin user should be able to see an edit button on each of the cards. When this button is clicked, the user should be taken to the edit make page which will be the same as the add make page but it will be pre-populated. Once the user makes the change to the name of the make, the same check will be done to see if the new make name exists already. If not, the new name will be posted to the database and the user will be redirected to the manage page where the new name will be displayed along with the other existing makes.
    * #### Implement 
    Created a button that renders the edit make page which is auto-populated. This is done using html and jinja templates. The backend then checks the database to see if the user input exists or not. If this new make does not exist, it is added to the database, the user is redirected to the manage page and the make displays alongside the other existing categories.
    * #### Test
    Try to add a make that exists & a make that doesn't exist.
    * #### Result
    Everything worked as expected and the result is a success.
4. #### Delete Make
    * #### Plan
    The admin user will visit the homepage and want to remove a make. They will click the delete button which will be attached to each make. The button, when clicked will trigger a modal to appear on the screen warning the user that the make cannot be retrieved when it's deleted. The modal will also have a confirm deletion button and a close modal button.
    * #### Implement 
    Created a button for each make card. The button when clicked triggers the modal and each one has it's own individual id so that the backend knows what to delete from the database.
    * #### Test
    Attemp to delete something and make sure that the correct item is being deleted.
    * #### Result
    Result is as expected. Test succeeded.


### Validator Testing 
#### HTML Validator
As Flask is a framework, I had to validate the HTML code using the URL to avoid false error flags due to jinja2. 

* Errors:
No errors. See screenshots of passed tests [here](testing/code-validation/html)
* Fixes:
None.

#### CSS Validator
* Errors:
No errors. See screenshot of passed test [here](testing/code-validation/css)
* Fixes:
None

### Feature Testing

1. Navigation bar
#### Plan
The navbar should work as expected and bring the user to the the different links that they want and expect to be brought to. The navbar should also be responsive on different screen sizes. It should also be dynamic in that, it should display different items depending on whether the user is logged in or not or if the user is admin or not
#### Implementation
The navbar was taken from bootstraps components section and customized for my own project. It comes responsive through Bootstraps built in features and a toggler  appears at a certain small screen size. 
To make the navbar dynamic, I used jinja to create conditional checks to see the above mentioned criteria and make the navbar dynamic.
#### Test
Try and follow all of the available navbar links and ensure they work. Only the login and signup navbar items should be available to see if the user is not logged in. If the user is logged in, they should be able to see all the navbar items except for the manage navbar item which only appears for the admin user.
#### Result
This was a success.

2. Registration page - username and password (See Testing completed in user story testing section)

3. Search bar to search through the database for: (See Testing completed in user story testing section)
    1. to find reviews of particular boots
    2. to find reviews of a certain make of boots
    3. to find reviews of boots of a certain star rating

4. User feedback for CRUD operations
#### Plan
The user should be able to carry out the CRUD operations on all the collections of the databse throughout their use of the app. This excludes categories and makes as they are only for the admin user to be able to perform the crud actions on. Once they perform these actions, they should ideally recieve some feedback from the backend to let them know that they have been successful.
#### Implementation
To implement the user feedback to the crud testing, I created functions for each of the crud operations and if the crud operation was successfull or not, the user would get a flash message to say one way or the other.
#### Test
The tester should test out all of the crud operations on all aspects of the website and see if there is feedback for all the operations whether successful or not.
#### Result
The user gets a flash message upon all of the relevant crud operations. See screenshots of testing [here](testing/feature/crud-feedback) which includes all the crud operations feedback exceot for read of course as the feedback for this is simply that the user can see the data.

5. User feedback & validation on forms
#### Plan
The plan for this is that the user should not be able to fill in a form and submit it without the form matching the required pattern or without it not being filled in at all. The plan is that the browser validation system will provide the user with some feedback as to what the issue is if they have not filled in the form properly
#### Implementation
To implement this, the all of the forms have the required attributes and they also have patter attributes to ensure that the user inputs the correct data. The browser validation system should inhibit the user from submitting the form if any of the fields are not filled in correctly.
#### Test
The user must try filling in the forms that are on the site and purposely leave out some fields or put in incorrect data.
#### Result
This test is a success with all of the forms operating as expected. See the relevant screenshots [here](testing/feature/form-validation) for one example of each form validating the data.

6. Bootstrap css design features such as navbar, buttons cards etc.
#### Plan
For this feature of the site, the plan is to use the Bootstrap framework for components such as buttons, navbar cards among other components.
#### Implementation
To implement this, I linked the Bootstrap CSS to the head of the website pages and also the js links in the body. I then added the Bootstrap classes to the HTML files where needed and customised them to make them suit my project and the style that I was looking for. 
#### Test
To test these, the user must go into the site ensure that all buttons and other Bootstrap components as outlined above are functioning as expected.
#### Result
This test was a success. All of the components are operating as expected and look appealing to the user as is desired.

7. Responsive design 
#### Plan
The plan for this is to give the user a positive experience no matter what size screen they are viewing the site on. All the elements of the site need to be dynamic and change with the screen sizes as needed.
#### Implementation
Bootstrap was very helpful in creating a responsive website. The grid system was extremly useful in this. I also used some media queries to help the responsive design where some elements needed it.
#### Test
The tester needs to go into each page on the site and right click to inspect the site for responsiveness. Try out the different breakpoints to ensure that the site looks good and the different components of the site do not get distorted.
#### Result
The site is fully resopnsive and looks appealing to the user at all different screen sizes and breakpoints. 

8. profile page displaying the following: (See Testing completed in user story testing section)
    1. Profile photo
    2. Bio 
    3. Reviews
 
9. Landing page (See Testing completed in user story testing section)
    2. Sign up
    3. Log-in

10. Sign out
#### Plan
The plan for signing out is that the user will be able to click the button in the navbar at any given moment. This provides a positive UX. 
#### Implementation
To implement this, a link is was created in the navbar that called the backend to pop the session user off and redirect them to the login page. The user then gets a flash message which is also called from the backend which lets them know that they have signed out successfully. 
#### Test
The tester must sign in to their account and then click the logout button in the navbar and they should see the flash message on the page login page when they get redirected.
#### Result
This was a success and the user see's the message. No session cookie can be found on the dev tools. If the user is logged into the same account on a different device they also get logged out when they next try and action which requires them to be logged in.

11. Admin to manage categories and makes (See Testing completed in user story testing section)

### Lighthouse Testing

The Lighthouse tool, which can be found in Chrome Dev Tools is a really useful tool for testing the performance, accesibility and overall correctness of a page. All you have to do to use it is right click on a page, click inspect and click into the Lighthouse extension. Once there, all you do is generate a report for each page of the website. The report gives an overall score of how your webpage has performed in the test and it will give areas for improvement. This should be repeated for Mobile and Desktop. The reports for Boots Review can be found in the links below:

[Mobile](testing/lighthouse/mobile)

[Desktop](testing/lighthouse/desktop)

### Compatability Testing

| Browser                                          | Chrome | Firefox | Edge |
| -------------------------------------------------| ------ | ------- | ---- |
| Compatable                                       |   Yes  |    Yes  |  Yes |

### Bugs
I ran into some issues throughout the development phase of the project. Some of these are logged here:

#### Bug 1
**Bug** - Review card dropdowns would expand for each review card when the read button in the review card was pressed instead of just the relevant review expanding. 

**Fix** - I realised that I wasn’t giving them unique id and data-target values which caused them to all expand at the same time. To fix this I used 'collapse-{{loop.index}}' to target the collapse items of the review cards and then give it the index in the list of reviews to give it an indvidual id.

#### Bug 2
**Bug** - Could not access the collections in the DB that had a Dash (“-“) in the name of the collection.

**Fix** - Had to delete the collection and rename it and recreate the collection. Unfortunately, I could not simply rename the collections.

#### Bug 3
**Bug** - Could not render the edit profile function as I was not passing the correct variable into the template. I was also trying to render a template that did not exist yet.

**Fix** - I created the template needed that I was trying to render and included the correct template in the backend to render and made sure I was passing the profile object to the page to render the data from the database through jinja syntax.

#### Bug 4
**Bug** - When I put in a modal for defensive programming when trying to delete a category from the database, I did not assign the modal an unique id and so the first item on the database would delete.

Fix- To counter this, I used “modal-{{loop.index}}” to give each modal a unique id and then input that into the data-target attribute for the button to delete. This was a very similar issue to the first bug.

#### Bug 5 
**Bug** - Tried to make the date of boots review automatically become the ‘today’ date using - ‘from datetime import datetime” and use this in the backend to autofill the field in the database.

**Fix** - Had to use ‘from datetime import date’ instead as of 'from datetime import datetime' which fixed the issue. This was a learning that I got from [Odoo](https://www.odoo.com/forum/help-1/how-to-auto-fill-datefield-with-today-date-23928) 


#### Bug 6
**Bug** - Edit category and edit make functions were not operating correctly as I was not performing the correct conditional checks. I was checking if the item being edited matched an existing item in the database (which was true as it was being edited, not added). 
**Fix** - I had to change the conditional check to ensure that the new user input did not match an existing category or make in the database. 

#### Bug 7
**Bug** - The background colour of the modal which appeared during the attempt to delete a review was being inherited from the review card itself due to the way that I was targeting the element

**Fix** - I had to change the way I targeted the review card in the css sheet which then allowed the modal to have its own background colour and not inherit it.


#### Bug 7
**Bug** - Hero image on the home page had different shades of darkness in it which made the overlay text on it hard to see at times. I really wanted to use that particular image though as I liked it.

**Fix** - I had to add an extra div around the hero image section and then give it an opaque background colour that I wanted to overlay ontop of the hero image.This made the text much easier to read. 

## Deployment
All of the code was written in Gitpod, a cloud-based IDE. Github is used in conjunction with Gitpod you can deploy your project to Github Pages through the following steps: 

### Github Pages
To deplow the site, the following steps were taken: 
1. Opened Github repository
2. Opened settings 
3. Click into **Pages** section on the side menu
4. Clicked into Branches
5. Selected **Master Branch**
6. Clicked save
7. Refreshed page
8. Await confirmation of deployment to Github Pages

### Run Locally
To run the project locally, follow these simple steps:
1. Open the Repository
2. Click on the **Code** button beside the green Gitpod button
3. Click into the HTTPS tab
4. Copy the URL available
5. Open your local IDE
6. Type git clone into the terminal which should prompt you to enter your copied URL
7. Paste the URL here
8. Project should be running in local IDE now

### Deploying in Heroku
To deploy using Heroku, the following actions were carried out:
1. Created the .gitignore file and added env.py file to this as well as pycache/directory so that these files are not viewable to users


## Credits

#### Python Documentation
[Python](https://docs.python.org/3/library/index.html) - 
This was a useful reference guide to keep to hand. This was used on multiple occasions if I had any queries on how Python worked. 

#### Bootstrap
I used [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/) to assist in achieving responsive design. This is a very useful tool to use.

### W3 Schools
[W3 Schools](https://www.w3schools.com/) -
I got some good assistance throughout the development of my project from W3 Schools. This is a brilliant website for general coding tips and tricks. I used this for any kind of queries from CSS to HTML to Python and it is extremely easy to follow.

### Font Awesome 
[Font Awesome](https://fontawesome.com/v5.15/icons?d=gallery&p=2) is where I went to get the icons that I used in my project. All you have to do is copy in the CDN to the head of the HTML document and use the code that they provide.

### Odoo 
[Odoo](https://www.odoo.com/forum/help-1/how-to-auto-fill-datefield-with-today-date-23928) - I used this to help me overcome the date bug that I have outlined above in the bugs section.

### Coolors
[Coolors](https://coolors.co/) was where I went to to generate my colour scheme for the webpage. This is a brilliant and handy tool to have available as it gives the hex value of the colour that you chose to use.

### Code Institute 
[Code Institute](https://codeinstitute.net/)
Example Project - 
There was a fantastic example project run through in the Code Institute course material which really teaches you a lot about how to put together a project like this. There was a lot of time spent looking at the videos to better understand concepts and some of the code logic was taken for the some of the similar functions in my project but of course, there was a lot of customisation to make it work for how I wanted my project to function.

CI Mentor sessions - 
Code institute provide each student with an industry professional as a mentor. Simen Daehlin was my mentor on this project. This is a great resource as I get 3 sessions with them to discuss my project and get any questions answered about the planning of the project.

## Final Comments
I would like to thank the following people for all of the assistance throughout the development of this project:

* Everybody on the Slack community for always being on hand to answer any questions I had
* My family and partner for being so patient with me throughout the stressful process.
* Code Institute Tutors.
* My Mentor Simen Daehlin for all of the great advice and wisdom he passed onto me.