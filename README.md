# Restaurant Blue Horizon
Blue Horizon Café is a fictional seaside restaurant offering a charming dining experience. This Django app provides a robust booking system for users to reserve tables and manage their bookings. Additionally, it features a review system for customers to rate and share feedback on their dining experience. The application ensures a user-friendly interface for both customers and staff to handle reservations and reviews efficiently.

The live link can be found here: [Live Site ](https://project4-restaurant-booking-cacc3b345e08.herokuapp.com/)

![Mock Up](docs/readme_img/mockup.PNG)

## Table of Contents


# User-Experience-Design

## The-Strategy-Plane

### Site-Goals


### Agile Planning


![Kanban image]()

#### Epics


## The-Scope-Plane


## The-Structure-Plane

### Features


Implementation:

**Navigation Menu**


![Navbar]()


Implementation:

**Home Page**


![Hero Image]()

![Welcome Section]()

![Find Us]()

Implementation:

**Footer**

![Footer]()


Implementation:

**Menu Page**

![Menu]()


Implementation:


**Create booking page**

![Create Booking]()


Implementation:

**Manage bookings page**

![Manage Bookings]()


Implementation:

**Edit Booking Page**

![Edit Booking]()

Implementation:

**Toasts**

Custom toasts were implemented on the successful creation and editing of bookings. This will provide feedback to the user to relay information that the booking was successfully received or updated.

![Booking Toasts]()

``text here``

Implementation:

**Delete Booking Page**

![Delete Booking]()

Favicon

![Favicon]()

**Error Pages**


Implementation:

**403 Page**

### Features Left To Implement


## The-Skeleton-Plane

### Wireframes

- Home page


![Home Page]()


- Signup page


![Sign up Page]()

- Log in

![Login Page]()

- Log Out

![Logout Page]()

- Create Booking

![Create Booking]()

- Edit Booking 

![Edit Booking]()

- Manage Bookings

![Manage Bookings]()

- Delete Booking 

![Delete Booking]()

- 403 Error 

![403 Error]()


### Database-Design

Entity relationship diagram was created using []() 

![Entity Relationship Diagram]()

### Security


## The-Surface-Plane
### Design

### Colour-Scheme


### Typography


### Imagery


## Technolgies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to make the custom slider on the menu page change and the bootstrap date picker.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for various icons throughout the site
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq 
- TinyPNG
  - This was used to compress the hero image for optimal load times

**Python Modules Used**

**External Python Modules**

* 

## Testing

Test cases and results can be found in the [TESTING.md](TESTING.md) file. 

## Deployment

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘Gars-Steakhouse’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site]()

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

## Credits 

## Sources

- [Implementing Star Rating in Django](https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c)
- [Python `datetime` Documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
- [Django Forms Validation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other)
- [Django Forms Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
- [Django ModelForm `save` Method](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method)
- [Django Messages Framework Tips](https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html)
- [Django DeleteView Documentation](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#deleteview)
- [Django Template Tags and Filters - Yesno](https://www.djangotemplatetagsandfilters.com/filters/yesno/)
- [Django UpdateView Documentation](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#updateview)
- [Django Forms Widgets Documentation](https://docs.djangoproject.com/en/4.2/ref/forms/widgets/)
- [Adding Extra Context in Django CBVs](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/#adding-extra-context)
- [Class-Based Views Overview](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
- [Django CBVs Generic Editing](https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/#using-generic-views)
- [Django RegexValidator Documentation](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.RegexValidator)
- [Django Mobile Number Regular Expression](https://stackoverflow.com/questions/47939753/django-mobile-number-regular-expression)


