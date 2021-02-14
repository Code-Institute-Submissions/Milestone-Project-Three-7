# Milestone-Project-Three - Keep A Record

## Description

Keep a record is a site that allows users to sign up, log in and build a list of the programs and movies they have watched on they're favourite streaming services, rate them and write comments or a review.

## User Design/Experience

The goal of this project was to give users the ability to keep track of what they had watched on an easy to use platform. They could not only remind themselves of what they had watched and where it was available to watch, but also write a self review possibly saying what they liked and if they would watch it again. 
This goal was broken down into User Stories

### User Stories

- As a user I want to, have an easy way to keep track of things that I have watched and view them easily.
- As a user I want to, easily find my way around the site.
- As a user I want to, be able to sign up and log in to the site to save my list for future reference.
- As a user I want to, add detail to my list items such as the name, where I watched it, details/a review about it and to give it a rating.
- As a user I want to, be able to search for list items based on their name and where I watched it.
- As a user I want to, be able to edit entries to current list items if I want to change the name, streaming service, review or rating of it.
- As a user I want to, I want to be able to delete entries in the list that I no longer want in it.
- As a user I want to, use the webstie on my smartphone or tablet, not just on a desktop.

## Features

### Features currently on the site:

#### Navigation bar at the top of the page

- This contains:
  1. a logo which can route the user to the homepage,
  2. a home button which is the main navigation to the home page,
  3. a login button which directs the user to the login page to view their own content.
- Once logged in the navbar contains:
  1. a My List button which directs the user to their list of entries into the database,
  2. a logout button once they are finished using the website,
  3. a logo which will route them to the homepage
  
#### Account Creation

- Once the user navigates to the login page they will also find a link to create and account should they not already have one.
- To create and account the user has to fill in the username and password fields as follows:
  1. Their username must be between 5 and 15 characters and the field will accept all letter and number characters both lower and uppercase.
  2. Their password must also be between 5 and 15 characters and this field will also accept all letter and number characters both lower and uppercase.
  
#### Login Ability

- Once the user has a registered account they can log into the site to either start creating entries into their list or view previous entries they have made.
- The user can log out of their session at anytime with the logout button.

#### Create new entries

- Once logged in the user has the ability to create entries into their list using the Add to List button on the My List page.
- To add an entry the following fields must be filled in:
  1. Title, this field is the title of the programme/film watched and can be between 2 and 50 characters long using letters and numbers.
  2. Streaming Service, this field is the service used to view the content watched such as Netflix or nowTV etc. This field will accept between 2 and 15 characters using letters and numbers.
  3. Review/Notes, this field can take between 5 and 250 characters for the user to right a review or some notes on what they have watched using letters or numbers.
  4. Rating, this field is to rate the programme/film out of 5 and will accept entires of numbers 1,2,3,4 & 5.
- All sections are required to be filled in to put an entry into the users list.
- Once completed the entry can be added to the users list by clicking the Add to List button at the bottom of the form.

#### Viewing entries

- Once added to the list, entries will be available to view on the My List page
- Entries will the listed 3 at a time horizontally across the page before staring a new line of 3.
- Entries will be listed in the order they were put into the system, this includes after editing an entry.

#### Search for entries

- Provided above the list on the My List page is a search input field
- This field can be used by the user to find all entries that contain the search criteria
- When the search functionality is in use only the entries containing the search criteria will be shown in the list
- The search criteria can be removed by clicking the reset search button, this takes the user back to the entire list of entries.

#### Edit and Delete functionality

- The user can edit an entry of the list by clicking on the edit button of that entry.
- The user will then be taken to the edit page which will contain the 4 fields they filled in to create the entry, Title, Streaming Service, Review/Notes and Rating.
- These fields will be populated on the edit screen by the current data in that entry.
- This current data can be added to or changed
- Once edited the entry can be saved to the list by clicking the Complete Edit button at the bottom of the form.

#### Responsive Design

- The application is able to be used in a web browser on any size device ranging from smartphone to large screens such as desktops.

#### Security

- When the user creates a password it is hashed using a the systems security key, this means that the password created will never appear in the database.

### Features left to implement

- An ability for one user to share their entry with another using to suggest a programme/film.
- A page containing data about the entries such as:
  1. numbers of entries against a certain streaming service
  2. a quick view of all the ratings given, and an average rating
- Using an API it may also be possible to suggest programmes/films to the user based on their entries.

## Links

### Wireframes

The basic layout of the website was planned to be the same across all pages with a navbar and footer with content between as shown:

![Welcome Page](https://github.com/ShaunWard/Milestone-Project-Three/blob/master/static/img/Welcome%20Page.png?raw=true)

The other pages of the website followed the same theme and structure and can be found here:
- [Login/Sign up Page](https://github.com/ShaunWard/Milestone-Project-Three/blob/master/static/img/Login%20Page.png?raw=true)
- [My list page](https://github.com/ShaunWard/Milestone-Project-Three/blob/master/static/img/My%20List%20Page.png?raw=true)

## Testing

### Manual Testing

Google Developer tools in the chrome broswer was used extensively throughout the project as an efficient error checking method.

Further manual testing was done to ensure each aspect of the application worked as expected.

#### Front/Home Page

- Loaded from the heroku link https://milestone-project-three-shaun.herokuapp.com/
- Home page appears as expected, the user is presented with:
  - A Navbar with home button, KaR logo and Log in button
- Logo when clikced sends the user back to the home page as required.
- Home when clicked sends the user back to the home page as required.
- Login send the user to the login page

#### Login Page

- User is presented with input fields for username and password.
- If user is not registered and enters a username and password and clicks log in the page reloads and 'Incorrect Username and/or Password' flashes to the screen.
- If the user enters a username or password into the form and leaves a field blank and clicks log in they are prompted to fill in the empty field.
- Username field prompts the user if username is under 5 characters.
- Username field does not allow input of over 15 characters.
- Password field prompts the user if password is under 5 characters.
- Password field does not allow input of over 15 characters.
- Both Username and password fields prompt the user to only use letters or numbers if any other characters are entered.

#### Register Page

- If the user cannot log in becuase they are not registered they can access the register page from the bottom of the login page by clikcing on get account.
- If the user enters a username or password into the form and leaves a field blank and clicks log in they are prompted to fill in the empty field.
- Username field prompts the user if username is under 5 characters.
- Username field does not allow input of over 15 characters.
- Password field prompts the user if password is under 5 characters.
- Password field does not allow input of over 15 characters.
- Both Username and password fields prompt the user to only use letters or numbers if any other characters are entered.
- When both fields are inputed correctly and the register button is clicked the user is taken to the My List page.

#### My List Page

- If the user has just registered a flash message appears at the top of this page to say registration was successful.
- Users username is displayed correctly
- No entries are shown on the page unless they belong to the user
- If the search button is clicked with an empty field the user is prompted to fill in the field
- If the user has no entries nothing is returned if the search bar is used
- Reset search reloads the page if there are no entries available
- Add to list button take the user to the add to list page
- If there are entries on the page, the edit button when clicked takes the user to the edit page.
- If there are entries on the page, the delete button when clicked deleted the entry from the page.
- If there are entries on the page and the search box is used, the entries relating to the search are displayed only.
- If there are entires and the reset search button is pressed, all entries are now shown.

#### Add to list Page

- Text at the top of the page asks the user to add what they have watched and a form is displayed.
- The title field accepts 1-50 letters or numbers and spaces as expected.
- If any other character is entered in the title field the user is prompted to use only letters and numbers.
- The Streaming service field accepts 1-15 letters or numbers and spaces as expected.
- If any other character is entered in the streaming service field the user is prompted to use only letters and numbers.
- The Review/notes field accepts 1-250 characters as expected.
- The rating field only accepts numbers 1-5 as expected.
- If anything other than the numbers 1-5 is entered into rating the user is prompted.
- If any field is left blank the user is prompted to fill in the field
- The add to list button takes the user back to the my list page and presents them with their inputted entry.

#### Edit page

- When accessing the edit page the user is asked to edit what they have watched.
- The form on the page is complete with the information from the entry the edit button was clicked on as expected.
- The title field accepts 1-50 letters or numbers and spaces as expected.
- If any other character is entered in the title field the user is prompted to use only letters and numbers.
- The Streaming service field accepts 1-15 letters or numbers and spaces as expected.
- If any other character is entered in the streaming service field the user is prompted to use only letters and numbers.
- The Review/notes field accepts 1-250 characters as expected.
- The rating field only accepts numbers 1-5 as expected.
- If anything other than the numbers 1-5 is entered into rating the user is prompted.
- If any field is left blank the user is prompted to fill in the field
- The complete edit button takes the user back to the my list page and displays the edited entry.

#### Testing user stories

- As a user I want to, have an easy way to keep track of things that I have watched and view them easily.
  - The user is displayed with a list of their entries into the application when they are logged in as tested above.
  
- As a user I want to, easily find my way around the site.
  - All buttons and froms were tested as above which should easily guide the user around the site
  
- As a user I want to, be able to sign up and log in to the site to save my list for future reference.
  - Covered by the register and login functionality tested on the register and login pages.
  
- As a user I want to, add detail to my list items such as the name, where I watched it, details/a review about it and to give it a rating.
  - This ability is given to the user and has been tested on the add item page.
  
- As a user I want to, be able to search for list items based on their name and where I watched it.
  - This functionality is given to the user through the search function on the my list page and has been tested above.
  
- As a user I want to, be able to edit entries to current list items if I want to change the name, streaming service, review or rating of it.
  - The user is able to do this with the edit function on every entry which was tested above.

- As a user I want to, I want to be able to delete entries in the list that I no longer want in it.
  - The user is able to delete entries with the delete button as tested above.

- As a user I want to, use the webstie on my smartphone or tablet, not just on a desktop.
  - The site has been tested on various screen sizes from smartphones to desktop screens to ensure maximum responsiveness.


## Technologies

### Languages/Technologies/Tools Used

#### Languages

- HTML
- CSS
- Python

#### Frameworks

- [Materialize](https://materializecss.com) - for the layout and components
- Flask
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) Templating Language

#### Technologies/Tools

- [MongoDB](https://www.mongodb.com/) as a database for the inputted data
- [Heroku](https://www.heroku.com) to deploy the application
- [Gitpod IDE](https://www.gitpod.io)
- Git & [Github](https://github.com/) for version control
- [Balsamiq](https://balsamiq.com/) to create wireframes
- [Am I Responsive](http://ami.responsivedesign.is/#)

## Deployment

The project has been deployed using Heroku, and is available to view [here](https://milestone-project-three-shaun.herokuapp.com/)

### Local Deployment

To deploy locally:

1. Go to the applications [repository](https://github.com/ShaunWard/Milestone-Project-Three) on github.
2. Click on the 'code' button to access the dropdown and click 'download zip'.
3. Unzip the downloaded file and open into your development environment.
4. Start by installing the required systems listed in the requirements.txt file using
  ```
  pip3 install -r requirements.txt
  ```
5. Next create a Cluster on MongoDB, in this cluster create a database.
6. Within this database create two collections called 'entries' and 'users'.
7. Back in your IDE create an env.py file at the same level as the app.py file, this should contain the following information:
  ```
  import os
  os.environ.setdefault('IP', '0.0.0.0')
  os.environ.setdefault('PORT', '5000')
  os.environ.setdefault('SECRET_KEY', 'YOUR_KEY')
  os.environ.setdefault('MONGO_URI', 'YOUR_MONGO_URI')
  os.environ.setdefault('MONGO_DBNAME', 'YOUR_DATABASE')
  ```
8. You will be required to fill in the SECRET_KEY with a key of your choice, MONGO_URI (which can be found under your cluster with the 'connect' button) and MONGO_DBNAME with your own information from MongoDB.
9. Run the app.py file in your terminal by using the command:
  ```
  python3 app.py
  ```
Please note that if you wish to then push this project to a public repository such as your github then you must create a .gitignore file and make sure you add the env.py file into this to stop your valuable inforamtion being pushed.

### Heroku via Github Deployment

To Deploy to [Heroku](https://www.heroku.com) via Github

1. Sign Up/Login into Heroku.
2. Create a new app using a relevant region and app title.
3. In your IDEs terminal create a new requirements.txt file using:
  ```
  pip3 freeze --local > requirements.txt
  ```
  This will be used by Heroku to install all dependancies for the application.
4. Create a Procfile at root level, ensuring it contains the following:
  ```
  web: python app.py
  ```
5. Now these files have been created, add them to the staging area, give them a commit message and push them to github.
6. In your Heroku app click on the 'deploy' tab and under deployment method select Github.
7. Make sure your github name, repository and correct branch are selected and click connect.
8. Next go back to the tabs near the top and click on the settings button.
9. Under Config Vars click the Reveal Config Vars button.
10. Add the following information into the revealed config vars:
  ```
  'IP'|'0.0.0.0'
  'PORT'|'5000'
  'SECRET_KEY'|'YOUR_KEY'
  'MONGO_URI'|'YOUR_MONGO_URI'
  'MONGO_DBNAME'|'YOUR_DATABASE'
  ```
You will be required to fill in the SECRET_KEY with a key of your choice, MONGO_URI (which can be found under your cluster with the 'connect' button) and MONGO_DBNAME with your own information from MongoDB.

11. Once this information is filled in, go back to the Deploy tab and at the bottom of the page under Maunal Deploy click Deploy Branch.
12. Once your have a message to say the app was deployed you can click the open app button.
13. (Optional) You can also enable automatic deploys from the data you push to the chosen Github repo under Automatic deploys.

## Acknowledgements

I'd like to acknowledge my mentor, Felipe Souza Alarcon, for his support throughout this project.
