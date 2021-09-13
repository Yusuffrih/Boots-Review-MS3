# Boots Review 

The Boots review site has the main goal of being a site where people can go to view reviews of different pairs of football boots that other people have owned. The aim is that this will be a site they can visit to assist them in making the decision of what pair of boots to purchase. 

A secondary aim of the site is that when these people have bought their pair of boots, they will be able to review their new pair of boots and assist others in making their decision. 

## Table of Contents
* User Experience (UX)
    * Site Owner Goals
    * User Goals
    * User Stories
        * First Time User
        * Registered User
    * User Requirements
    * User Expectations
    * Design Choices
        * Fonts
        * Colours
        * Icons
        * Wireframes
        * Data Schema 
* Features
    * Implemented Features
    * Features Yet To Implemented
* Technologies Used
    * Languages
    * Frameworks & Libraries
    * Tools
* Testing
    * User Story Testing
    * Validator Testing 
    * Feature Testing 
    * Lighthouse Testing
    * Compatability Testing
    * CRUD Testing
    * Bugs
* Deployment
* Credits
* Final Comments

## User Experience (UX)

### Site Owner Goals
* As a site owner, I want to give users no usability of the site without the requirement to register. This will ecourage registration.
* As a site owner, I would like to make it a requirement to sign up if users want to review a pair of football boots they have recently worn and then update and delete their reviews thereafter. 
* As a site owner, I would like to collect a database of reviews of football boots
* As a site owner, I would like to collect a database of star ratings of the football boots that are reviewed so that I can eventually create a ranking of the top rated boots
* As a site owner, I would like the site to be easy to use and intuitive
* As a site owner, I would like the site to have an attractive UI with an obvious color scheme
* As a site owner, I would like the user to be able to create, read, update and delete their profile
* As a site owner, I would like the user to be able to creat, read, update and delete their boots reviews
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
* As a user, I would like to be able to read a review that someone else wrote on a pair of boots
* As a user, I would like to be able to update/edit a review that I wrote
* As a user, I would like to be able to delete a review that I wrote on a pair of boots
* As a user, I would like to be able to see pictures of boots that have been reviewed
* As a user, I would like to be able to follow a link to a purchase boots that have been reviewed
* As a user, I would like to be able to search the database for boot reviews based on certain criteria
* As a user, I would like to be able to save boots that have been reviewed so that I may see them at a later stage

### User Requirements
* The site needs to be easy to navigate between the different features via good UX and a concise navbar
* To be able easily see whether or not an CRUD action has been successful or not
* To have a landing page that tells the user what the page is at a glance
* To have a well laid out site that is easy to use and understandable
* To be able to read clearly any messaging that is displayed on screen via constrasting backgrounds
* To be given clear and easy to understand instructions via really good UX
* To be able to contact the site owner to provide feedback or make a complaint if necessary
* To have my registration and personal data secure in the database
* All features need to be operating efficiently
* All features and functionality need to be well laid out and very intuitive
* The site needs to be responsive across all devices and browsers

### User Expectations
* Any external links need to open in a separate tab so that I don't lose where I am on the site and have to navigate there again
* All of the content needs to be easily readable and contrasting with the background colours and imagery
* Navigation of the site needs to be really easy and intuitive
* The site owner should be easily contactable - contact page and contact info in the footer of the site
* Any forms should always provide me with feedback so that I know what input it expects

## Design Choices
Generally, football boots tend to be quite sleek and stylish so I decided to try and keep this site the same way. The overall look and feel of the site is very soft touch with nice lines and angles. The colours are quite simple with lots of black and white but with a bit of colour to give it that little bit of extra style.

### Fonts
There is very little text on the landing page so as not to distract the user and not to take the user's attention away from understanding what the overall aim of the site actually is. For the fonts, I used [Google Fonts](https://fonts.google.com/?standard-styles=). This is a really fantastic feature of [Google](https://google.com) which is great for getting any kind of font you want. The fonts I chose for my page are *Play* & *Roboto* with *sans-serif* as a backup font in the event that [Google Fonts](https://fonts.google.com/?standard-styles=) does not work. The reason I decided to use *Play* & *Roboto* is that I found them to be quite sleek fonts which would almost represent a pair of football boots. 

### Colours
In deciding the colour scheme for the site, I decided to keep it nice and simple while at the same time trying to make it sleek and almost stealthy as this is the feel that is often hinted upon in tv ads for football boots. There is often a lot of black with splashes of colour. The black tends to make the colour stand out and is a really good contrasting background for reading content. The same idea goes for white. 

I used the site [Coolors](https://coolors.co/) to assist in generating a colour scheme for the site. This is a great site as it gives you the codes of the colours you want in any form you want ie. Hex code. 

![Colour Pallette]()

The colours I have chosen are: 
* Rich Black Fogra 39 - Hex (0B0909)
* White - Hex (FFFFFF)
* Platinum - Hex (ECEAEC)
* Capri - Hex (21C2FD)
* Red RYB - Hex (FF1F0A)

### Icons 
I have gone to [Font Awesome](https://fontawesome.com/) for the icons that I have used in the site. The icons, I feel just add a little bit extra to the site in terms of style and make it a bit more visually appealing which ultimately provides a better User Experience.

### Wireframes
When creating my wireframes, I first drew some rough sketches on paper but then decided that [Balsamiq](https://balsamiq.com/) would be the most suitable technology to use to assist with the design of the site. 

I created mock ups for my page to fit into the main device types - Desktop, Tablet and Mobile. The mock-ups for the devices can be found here: 
* [Mobile]()
* [Tablet] ()
* [Desktop] ()

### Data Schema
To carry out the functionality of the site, I needed to create three different collections of data. They are: 
1. Users 
2. Boots
3. Categories
4. Reviews
5. Colours
6. Price Ranges
7. Makes
8. Star Ratings

The Users collection is made up of the following fields: 
| Field    | Data Type | Default |
|----------|-----------|---------|
| id       | ObjectId  | N/A     |
| is_admin | boolean   | True    |
| username | string    | N/A     |
| password | string    | N/A     |
| bio      | string    | N/A     | 

The Boots collection is made up of the following fields:
| Field         | Data Type | Default |
|---------------|-----------|---------|
| id            | ObjectId  | N/A     |
| name          | string    | N/A     |
| make_id       | string    | N/A     |
| color_id  | string    | N/A     |
| price-range_id| string    | N/A     |
| purchase_url  | string    | N/A     |
| image_url     | string    | N/A     |
| star_rating_id| number    | N/A     |
| review_id     | array     | N/A     |
| category_id     | string     | N/A  |

The Categories collection is made up of the following fields:
| Field | Data Type | Default |
|-------|-----------|---------|
| id    | ObjectId  | N/A     |
| name  | string    | N/A     |

The Reviews collection is made up of the following fields:
| Field       | Data Type | Default |
|-------------|-----------|---------|
| id          | ObjectId  | N/A     |
| boot_id     | string    | N/A     |
| user_id     | string    | N/A     |
| review_date | string    | N/A     |

The Colours collections is made up of the following fields:
| Field         | Data Type | Default |
|---------------|-----------|---------|
| id            | ObjectId  | N/A     |
| color | string    | N/A     |

The Price Ranges collection is made up of the following fields:
| Field       | Data Type | Default |
|-------------|-----------|---------|
| id          | ObjectId  | N/A     |
| price_range | string    | N/A     |

The Makes collection is made up of the following fields:
| Field | Data Type | Default |
|-------|-----------|---------|
| id    | ObjectId  | N/A     |
| name  | string    | N/A     |

The Star Ratings collection is made up of the following fields:
| Field | Data Type | Default |
|-------|-----------|---------|
| id    | ObjectId  | N/A     |
| stars | number    | N/A     |


## Features
The site features are as follows: 
* Navigation bar at the top of the site for easy and intuitive navigation around the different pages of the site
* Registration page where the user can input their details, username and password
* Search bar for users to be able to search through the database:
    * to find reviews of particular boots that they want to read review of
    * to find reviews of boots that are in a particular price range
    * to find reviews of boots that are made with specific materials
    * to find reviews of boots that are of a certain make
    * to find reviews of boots that are of a certain star rating
* To be able to follow the link attached to the boots review which will take the user to an external site where they can purchase the boots
* User feedback whenever they carry out any of the CRUD operations
* User feedback on forms
* Bootstrap css design features such as navabr, buttons cards etc.
* Bootstraps responsive web design which allows users to use the site on all device sizes

## Features Yet To Implement
None

## Technologies Used

### Languages
* [HTML](https://en.wikipedia.org/wiki/HTML) - HTML is a markup language I used for structuring and presenting content of my site
* [CSS](https://en.wikipedia.org/wiki/CSS) - A language used to style the presentation of the content written in HTML5
* [Javascript](https://en.wikipedia.org/wiki/JavaScript) - Javascript is the language used to provide the interactivity to the user on the site
* [Python](https://www.python.org/) - Python is a backend programming language that is highly powerful and is designed around readability. It's language constructs and object oriented approach assist programmers in writing clear and easily read code

### Frameworks & Libraries
* [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - A front-end framework which assist me in creating responsive website design
* [Google Fonts](https://fonts.google.com/) - An open-source online library of thousands of fonts and icons that were free and easy to use.
* [Font Awesome](https://fontawesome.com/) - An open source online library of icons which I used for extra styling.
* [Pip3](https://pypi.org/project/pip/) - Pip3 is the package installer for Python and is used to download Python dependencies from the command line
* [BSON](https://en.wikipedia.org/wiki/BSON) - BSON is the binary encoding of JSON-like documents that MongoDB uses when storing documents in collections. It adds support for data types like Date and binary that aren't supported in JSON.
* [Pep8](https://pypi.org/project/pep8/) - Used pip3 to install pep8 validator which is a tool which ensures you stick to the pep8 compliance
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - used to import the following functions: flash, render_template, redirect, request, session, url_for
* [MongoDB](https://www.mongodb.com/1) - MongoDB is an object-oriented, simple, dynamic, and scalable NoSQL database. It where I stored the database for this project
* [Heroku](https://id.heroku.com/login) - Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps to get it to the market
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
* [W3 HTML Validator](https://validator.w3.org/) - Used to validate my code to ensure that there were no errors.
* [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to validate my code to ensure that there were no errors.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/Chrome) - A set of development tools to assist the user create web content. They are built directly into the browser
* [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) - One of the Chrome Dev Tools which was used to assess the level of accessibility, performance and correctness that was provided by the site.
* [JS Fiddle](https://jsfiddle.net/) - An online playground IDE used to test and trial Javascript code with HTML and CSS
* [Youtube](https://www.youtube.com/) - Youtube videos are a great way to learn how to do different things if stuck on a particular piece of code
* [Favicon](https://favicon.io/) - An online tool that generates the icon that is found in the tab bar at the top of the page beside the title of the page.
* [RandomKeyGen](https://randomkeygen.com/) - A tool that creates a random password to be used

## Testing

### User Story Testing
### Validator Testing 
### Feature Testing 
### Lighthouse Testing
### Compatability Testing
### CRUD Testing
### Bugs

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

## Credits

## Final Comments