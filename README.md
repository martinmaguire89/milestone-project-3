# Milestone-project-3
# Pound For Pound

My 3rd milestone project is a full-stack site website that allows users to manage a common dataset about a particular domain. My project is a page for all fight fans and enthusiasts around the world to come together and put there favourite fighter in the website to be classed as one of the greatest ever. I wanted to use mma fighters for this project as I feel a lot of current fighter stat pages look quite outdated and do very little to look appealing. I wanted to provide a website to show stats of fighters, but also look good so a fan will return.  For purpsoes of this site you can use Username martinmaguire89 and password - password to log in to show the page for adding your own figther. 

It can be viewed on heroku [Pound for Pound](https://pound-for-pound.herokuapp.com/)

## UX
### Who is the target audience?
*	This website is for people who are big fight fans from around the world of all different organisation of MMA. It also appeals to fans of boxing, wrestling, judo, or even taekwondo. It It’s designed for people who want to express an opinion about which fighters the feel have ruled over there sports for decades. 


### How does this attract our target audience?
* The name of the site is pound for pound. Pound for pound is a ranking used in combat sports. As these fighters do not compete directly, judging the best fighter pound for pound is subjective, and ratings vary. They may be based on a range of criteria including to determine who would win if all those ranked were the same size. This site would bring all these fighters together for fans to look at there stats and bio to put there case for there favourite fighter being the best ever. 
Using the large picture attract the fan straight away with 5 of the most recognisable fighters in MMA. The colours used in the website are similar to the colour of the octagon used in MMA which will stir up notions of the fighters n the octagon. 


## User Stories
*	As a user, I want the initial page to be eye catching
*	As a user, I want it to be easy to navigate.
*	As a user, I want to have an easy way to get further information on fighters and what makes them so special.
* As a User, I want to be met with a visually appealing and easy to read layout of cards sections for each fighter.
*	As a User, I want to be able to register/sign-up to add my own fighter to the website for other people to see and read about. 
* As a User, I want to be able to edit my own fighter and delete if I no longer wish to shcase my desired fighter. 


## Wireframe
* Link to my [balsamiq wireframe](https://github.com/martinmaguire89/milestone-project-3/blob/master/milestone%20project-3.pdf)
*	I decided to use Balsamiq to create my wireframe because it was recommended in the milestone project and by code institute mentors on slack.

## Technologies used
* Html
*	CSS
*	[Google Fonts](https://fonts.google.com/) - Used to style the fonts of the website.
*	[jQuery](https://jquery.com/) - To make certain features function on the page.
*	[git](https://github.com/) - Used as a repository
*	[Gitpod](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki) - Used for a development and testing area.
*	[Bootstrap](https://www.bootstrapcdn.com/) - Bootstrap framework to create responsive design.
*	[fontawesome](https://fontawesome.com/) - for social media icons.
* Flask
* [MongoDB](https://www.mongodb.com/) backend database used to store the information on the fighters
* [Python](https://www.python.org/)- 
* [Heroku](https://dashboard.heroku.com/auth/heroku/callback?code=61fc81a2-ba86-42ec-ac96-a904a0153b77)- A cloud platform as a service enabling deployment for this CRUD application.


## Features
### Feature 1 – Large picture.
The large picture is designed to look pleasing on the eye the minute you log on the webpage.  Using the large picture attract the fan straight away with some of the most recognisable fighters in MMA.It’s used to try and encourage the user to update his own fighter who he may one day see on the cover of this site.

### Feature 2 –  card grid.
A card is a flexible and extensible content container. It includes options for headers and footers, a wide variety of content, contextual background colours, and powerful display options. The card grid is laid out in a simple but effective way of displaying all fighters’ cards that has been added. It allows users to see a striking photo of each fighter and a small bit of information before clicking through the more info page.

### Feature 3 –  login/signup.
A page that inherits the navbar and footer from the base.html file, containing a small form group to capture and validate the user's username and password. This page will also feature a small hyperlink so the user can register their details to login to the page. As with the Login page, this page is very similar with the only slight changes to the language used. 

### Feature 4 – add fighter.
The add fighter page takes in the Create part of the CRUD application. This is revealed after the user signs in and can add their own fighter to the website along with a photo of them. 

### Feature 5 – More Info.
The more info page provides the user with a small biography that another user has uploaded to show tell other users abit more about there fighter. 


## Features Left to Implement
* I would like to add a comment/forum page for all users to leave a comment about who and why they think certain fighters are the greatest. This would strike up a lively debate between all users on the website.
* A upvote button on each card so each user can cvote for there faviourite fighter, this will also show off the more poplur ones.
*  would like to upgrade my log in/sign up system. Currently you need to log in to show the add fighter page however entering the in page in the URL will take you to this page without any security. Also i would like to make it that your cannot update or delete unless your are logged in. My tutor Rahul has provides me with he solution for this [digitaloccean]( https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login). However due to time constraints I was not able to update this before course submission date but will make a priority after submission. 

## Testing
* Used Google Chrome developer tools to test website responsiveness across multiple devices such as Tablets, Mobiles and laptop. This allowed me to see any issue's with sizing in different version control.
*  I used different web browsers such as Microsoft edge and Firefox to test how my page would run on different web browsers. I then used each responsive tool in each browser to again test my version control to see if it would still work effectively or if I would encounter any problems. 
* Used [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.
* I used [cssautoprefixer](https://autoprefixer.github.io/) to help get the appropriate vendor prefixes needed for my code to work in all browsers.
* Used [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.
*  I used [codebeautify](https://codebeautify.org/python-formatter-beautifier) to help with the correct Indentation of my python code

## Issues when Testing
* when I clicked on more info it showed every fighter available biography and not the one, I selected. Thankfully to the tutor support they were able to show me that I had placed the more info into a for loop using the categories and the  end for. This resulted in all fighters being called and not the specific one. Once removed this sorted the issue.
* There where a number of issues with the logging and signing in portions of the page. unfortunately thanks to the help of the tutors you can now log in and sign up for the website. 
* When a new fighter was uploaded due to different sizes of photos used on small screens it sometimes pushed the fighter image outside of the card section. To rectify this I set the height at 100% and the width to 360px so that they stayed within the card on all screen sizes. 

## Deployment
Heroku
* This site is deployed on Heroku
My project has also been deployed via the master branch and hosted on Heroku. Heroku is a cloud platform that allows for building, developing and operating applications on the cloud Heroku in a range of programming languages. Python was the mainly used for this project.

The following process was undertaken to succesfully deploy the project on the Heroku:

New app creted on Heroku
* After creating my env.py file (along with the .gitignore file), I added the MONGO URI..
* I installed Heroku via my command line interface, using install npm install heroku on my git hub terminal.
Afterwards type heroku login, which would redirect me to another tab where I would sign in to heroku as proceed once more in the terminal.
The next step was to initialise a git repo and add my Heroku remote repo command.
However, as per the requirements, before I can push my code to the Heroku app, I installed:
* A requirements.txt file is needed to run the installed dependencies, so to create and commit this file, the following command was used: $ sudo pip3 freeze --local > requirements.txt (and also used to update the file if any libraries were added).
* A Procfile is needed to direct the Heroku app to the file that it needs to run. So I used the command $ echo web: python > Procfile in the terminal to install the file. 
* This was followed by a simple command in the terminal to run the web process: $ heroku ps:scale web=1.
* Finally, to deploy I would use the $ git push heroku master to deploy my code on the Heroku app.
After any change on my code, I would push my code to the Heroku app to check if it was functioning. There were some slight issues with the MONGO URI and SECRET KEY but it was resolved quickly.


## Credits
* Credit goes to the tutos for there hlep wiht my log in problems and my mentor rahul for everything.
### Content
* The log in paage html was taken form a login.signup page from [colorlib](https://colorlib.com/).
* the login/sign up usinf flask + python was found on [prettyprinted](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) Youtube page.

### Media

