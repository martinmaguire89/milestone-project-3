# Milestone-project-3
# Pound For Pound

My 3rd milestone project is a full-stack site website that allows users to manage a common dataset about a particular domain. My project is basically a page for all fight fans and enthusiasts around the world to come together and put there favourite fighter in the website to be classed as one of the greatest ever. I went for a easy layout for all people using the site. For purpsoes of this site you can use Username martinmaguire89 and password - password to log in to show the page for adding your own figther. 

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
* Link to my [balsamiq wireframe](https://github.com/martinmaguire89/milestone-project-2/blob/master/milestone%20project-2.pdf)
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
*	[google.maps javascript api](https://developers.google.com/maps/documentation/javascript/tutorial) used to get my api key and render my map onto the webpage. Also used for adding markers and info windows.
*	[email.js](https://www.emailjs.com/) used to connect my contact form with my gmail to be notified when someone sends a request. 

## Features
### Feature 1 – Large dog picture.
The large dog picture is designed to show a fun and welcoming side of the web page. It’s used to provoke the image of their own dog enjoying themselves on holiday with the owner. It shows them that this is a fun and easy to use website that will serve their needs.
### Feature 2 –  Paragraph section.
The small paragraph is just a few lines to let the customer know what this page is about and how the needs of them and their dogs will be catered for. 
### Feature 4 – Search by counties.
The search by counties allows the user to narrow down the search field on the map. If they are looking to search for dog friendly hotels in a specific county, they can simply do that at the click of the button.  
### Feature 5 – The map section.
The maps section allows for a complete look of all potential place to stay with a dog in Northern Ireland.   The markers section allows for them to see where the hotels are and the info window provides them with a link to the hotel for making a booking. 
### Feature 6 – Contact Form.
Allows potential owners of hotel or restaurants to contact me to advise of what they offer for dogs and to have them establishment added to the map.  
### Feature 7 – Social media icons in footer.
Allows the customer to connect and follow me through my social media accounts.

## Features Left to Implement
* I would like to add a page for previous user to leave a review of their recent stay at dog friendly hotels to allow other users to know how they got on staying with there dog. This will improve their decision making when trying to decide where to stay.
* Personalised markers to differentiate between what markers are for places to stay, places to eat where dogs are allowed and both. 
* A further API added to the page to hotel booking site such as Booking.com to allow the user to see the prices of a night’s stay and potentially book rather than having to leave the webpage.  

## Testing
* Used Google Chrome developer tools to test website responsiveness across multiple devices such as Tablets, Mobiles and laptop. This allowed me to see any issue's with sizing in different version control.
*  I used different web browsers such as Microsoft edge and Firefox to test how my page would run on different web browsers. I then used each responsive tool in each browser to again test my version control to see if it would still work effectively or if I would encounter any problems. 
* Used [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.
* I tested each button when adding the JavaScript for each of them. Once one worked, I tested if it was still working on smaller screens and if there were any delay when clicked. Once I sorted this, I used the same JavaScript for each button to change the centre of the map to a specific location when clicked.
* I used [cssautoprefixer](https://autoprefixer.github.io/) to help get the appropriate vendor prefixes needed for my code to work in all browsers.
* Used [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.

## Issues when Testing
* On certain screen sizes smaller than a large view all the heading where being pushed to the left along with the submit button. I corrected this by text centring all heading and the submit so that if flowed nicely when going to smaller screens and remained in the middle.
* The Pawcation header was slightly to the left of the screen on all screen sizes. When testing this I found the navbar- heading was set with 15px padding right and 0 padding left. I fixed this by changing the padding to 15 px on the left too. This ensure it remained centred on all screen sizes.
* When I reduced the screen to anything smaller than large screen size, I noticed that all my button where being stacked on top of each other in a column. Also, the last two buttons where overlapping each other. This did not look pleasing on the eye. Speaking with my mentor he suggested I use a flexbox for my buttons. I used a flex-container to wrap my buttons which allowed for appropriate spacing between them stopping the overlapping. It also meant when I went to a smaller screen size the buttons where responsive and fitted appropriately onto two line.
* When moving to smaller screens I noticed the large picture at the top of the page caused everything to move down and leave a big gap between the picture and paragraph. I noticed that I had the min height of the picture set to 360px in my css. I removed this and this allowed the rest of the page ot move up and leave no unnecessary gaps.
* One issue I had with the JavaScript was adding info windows. As the code I found from Traversy media you tube video was different I had to change my code from the previous code institute video for rendering the map on the page to allow me to insert the info window.  Once I done this however it allowed me to insert info windows with no issues. 
* When testing on different browser I found the code had not been optimised and used [Autoprefixer](https://autoprefixer.github.io/) to optimize it. I copied and pasted the code and it added the necessary code to fix this.

## Deployment
The website was developed using Gitpod, it was then committed to git and pushed to GitHub using the terminal in Gitpod.
To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:
* Log into GitHub.
* Select the repository martinmaguire89/milestone_project_2.
* At the top of the page, select Settings.
* Scroll down to the GitHub Pages section.
*Under Source, select Master Branch
* The live link for the website will now appear beneath the GitHub Pages header.
* Click the link and a live website will open in a new tab.

### How to run this project locally
If you wish to clone this project from GitHub:
* Click on this [link](https://github.com/martinmaguire89/milestone-project-2) to the GitHub repository.
* There is a green button saying "Clone or download" on the right-hand side, click on this.
* Next copy the clone URL for the repository that is provided.
* Open Git Bash in your local IDE.
* Change the current working directory to the location where you want the cloned directory to be created.
* Type git clone, and then paste the URL copied in Step 3.
git clone https://github.com/USERNAME/REPOSITORY
* Press Enter to create your local clone.

## Credits
* Credit goes to Rahul Lakhanpal my mentor for all his help on this course.
### Content
* Adding markers with info windows was used from travery media from his youtube channel.
* Buttons added to change the center of the map to specific county. code solution found on stack overflow.
### Media
* Footer social icons were taken from the "rosie cv" module.
* The large logo picture at the top was a stock photo taken from [https://www.shutterstock.com](https://www.shutterstock.com/home).
* This is for educational use.
