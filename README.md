# Milestone-project-3
# Pound For Pound

My 3rd milestone project is a full-stack site website that allows users to manage a common dataset about a particular domain. My project is basically a page for all fight fans and enthusiasts around the world to come together and put there favourite fighter in the website to be classed as one of the greatest ever. I went for a easy layout for all people using the site. For purpsoes of this site you can use Username martinmaguire89 and password - password to log in to show the page for adding your own figther. 

it can be viewed on heroku 

## UX
### Who is the target audience?
*	This website is for people who are big fight fans from around the world and all different organisation of MMA.


### How does this attract our target audience?
The Websit
## User Stories
*	As a user, I want the initial page to be eye catching.
*	As a user, I want it to be easy to navigate.
*	As a user, I want to have an easy way to get further information on fighters and what makes them so special.

## Wireframe
* Link to my [balsamiq wireframe](https://github.com/martinmaguire89/milestone-project-3/blob/master/milestone%20project-3.pdf)
*	I decided to use Balsamiq to create my wireframe because it was recommended in the milestone project and by code institute mentors on slack.

## Technologies used
* Html
*	CSS
*	[Google Fonts](https://fonts.google.com/) - Used to style the fonts of the website.
*	[jQuery](https://jquery.com/) - To make certain features function on the page.
*	[git](https://github.com/)- Used as a repository
*	[Gitpod](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki)- Used for a development and testing area.
*	[Bootstrap](https://www.bootstrapcdn.com/) - Bootstrap framework to create responsive design.
*	[fontawesome](https://fontawesome.com/) for social media icons.
* Flask
* [MongoDB](https://www.mongodb.com/) backend database used to store the information on the fighters
* [Python](https://www.python.org/)


## Features
### Feature 1 – Large picture.
The large picture is designed to look pleasing on the eye the minute you log on the webpage. It’s used to try and encourage the user to update his own fighter who he may one day see on the cover of this site.
### Feature 2 –  card grid.
The card grid is laid out in a simple but effective way of displaying all fighters’ cards that has been added. It allows users to see a striking photo of each fighter and a small bit of information before clicking through the more info page.
### Feature 2 –  login/signup.
The log in/sign up page is where the user will go if they want to upload who they believe to be the greatest pound for pound fighter ever.
### Feature 4 – More Info.
The more info page does what it says, provides the user with a small biography that another user has uploaded to show tell other users abit more about there fighter. 


## Features Left to Implement
* I would like to add a comment/forum page for all users to leave a comment about who and why they think certain fighters are the greatest. This would strike up a lively debate between all users on the website.
* A upvote button on each card so each user can cvote for there faviourite fighter, this will also show off the more poplur ones.
* Currently you have to log in to add a fighter but you can edit and delete without doing this. i would like to update this so you cannot do any of this until you have logged in
## Testing
* Used Google Chrome developer tools to test website responsiveness across multiple devices such as Tablets, Mobiles and laptop. This allowed me to see any issue's with sizing in different version control.
*  I used different web browsers such as Microsoft edge and Firefox to test how my page would run on different web browsers. I then used each responsive tool in each browser to again test my version control to see if it would still work effectively or if I would encounter any problems. 
* Used [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.
* I tested each button when adding the JavaScript for each of them. Once one worked, I tested if it was still working on smaller screens and if there were any delay when clicked. Once I sorted this, I used the same JavaScript for each button to change the centre of the map to a specific location when clicked.
* I used [cssautoprefixer](https://autoprefixer.github.io/) to help get the appropriate vendor prefixes needed for my code to work in all browsers.
* Used [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.
*  I used [codebeautify](https://codebeautify.org/python-formatter-beautifier) to help with the correct Indentation of my python code

## Issues when Testing
* The biggest issue I faced and still not found a solution for is when you select a fighter to find out more info on or update it will give you every fighter on the database not just the one you need. I was offered a tutor one to one but unfortunately not before my completion date.
* There where a number of issues with the logging and signing in portions of the page. unfortunately thanks to the help of the tutors you can now log in and sign up for the website. 

## Deployment
Heroku
* This site is deployed on Heroku
My project has also been deployed via the master branch and hosted on Heroku. Heroku is a cloud platform that allows for building, developing and operating applications on the cloud Heroku in a range of programming languages. Python was the mainly used for this project.

The following process was undertaken to succesfully deploy the project on the Heroku:

New app creted on Heroku
After creating my env.py file (along with the .gitignore file), I added the MONGO URI..
I installed Heroku via my command line interface, using install npm install heroku on my git hub terminal.
Afterwards type heroku login, which would redirect me to another tab where I would sign in to heroku as proceed once more in the terminal.
The next step was to initialise a git repo and add my Heroku remote repo command.
However, as per the requirements, before I can push my code to the Heroku app, I installed:
A requirements.txt file is needed to run the installed dependencies, so to create and commit this file, the following command was used: $ sudo pip3 freeze --local > requirements.txt (and also used to update the file if any libraries were added).
A Procfile is needed to direct the Heroku app to the file that it needs to run. So I used the command $ echo web: python > Procfile in the terminal to install the file. This was followed by a simple command in the terminal to run the web process: $ heroku ps:scale web=1.
Finally, to deploy I would use the $ git push heroku master to deploy my code on the Heroku app.
After any big changes, advancements on my code, I would push my code to the Heroku app to check if it was functioning. There were some slight issues with the MONGO URI and SECRET KEY but it was resolved quickly.


## Credits
* Thank you to the mentors who helped me with everything. 
### Content

### Media

