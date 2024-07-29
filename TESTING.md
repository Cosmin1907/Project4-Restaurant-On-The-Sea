## Functional Testing

**Authentication**

Description:

Ensure a user can sign up to the website

Steps:

1. Navigate to [Restaurant-On-The-Sea]() and click Register
2. Enter email, username and password 
3. Click Sign up

Expected:



Actual: 



<hr>

Description:

Ensure a user can log in once signed up

Steps:
1. Navigate to [Restaurant-On-The-Sea]()
2. Enter login details created in previous test case
3. Click SIGN IN

Expected:



Actual:



<hr>

Description:

Ensure a user can sign out

Steps:

1. Login to the website
2. Click the logout button
3. Click SIGN OUT on the confirm logout page

Expected:



Actual:



**Booking Forms**

Description:

Ensure a new booking can be created.

Steps:

1. Navigate to [page]() - Login if prompted.
2. Enter the following:
    - Name: 
    
    - Date: Any future date
    - No Of Guests: 

3. Click book

Expected:



Actual:



<hr> 

Description:

Ensure a booking can be edited.

Steps:

1. Navigate to [page]() - Login if prompted.
2. Enter the following:
   

Expected:


Actual:


<hr>

Description:

Ensure user can successfully delete a booking.

Steps:
1. Login as a user with a booking or create a new booking

Expected:



Actual:



<hr>

**Menu Page**



**Navigation Links**

Testing was conducted to ensure that all navigation links on the respective pages directed to the correct destinations as per the design. This was verified by clicking on the navigation links on each page.

- Home -> index.html


- Logout -> Sign out all auth page
- Login -> Sign in all auth page
- Register -> Sign up all auth page

All navigation links directed to the corect pages as expected.

<hr>

**Footer**

Testing was conducted on the footer links by clicking all the Font Awesome social media icons. It was verified that each icon opened the respective social media site in a new tab, functioning as expected.

## Negative Testing

Tests were performed on the create booking to ensure that:

1. A customer cannot book a date in the past


## Unit Testing

Unit tests were created to verify basic functionality, including template usage and redirects. These tests, which evaluate the form functionality, programming logic, and page display according to the logic, can be found in the test_forms.py and test_views.py files within the respective apps.

Results:

![unit tests]()

## Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs
- Color contrasts meet a minimum ratio as specified in [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
- All content is contained within landmarks to ensure ease of use for assistive technology, allowing the user to navigate by page regions
- All not textual content had alternative text or titles so descriptions are read out to screen readers
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- WCAG 2.1 Coding best practices being followed

## Validator Testing

All pages were run through the [w3 HTML Validator](https://validator.w3.org/). 

Due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.

![HTML Validator]()

All pages were run through the official [Pep8](http://pep8online.com/) validator to ensure all code was pep8 compliant, with the exception of the settings.py file.


![PEP8]()

JavaScript code was run through [JSHINT](https://jshint.com) javascript validator. 

![JS validator]()

## Lighthouse Report



![Lighthouse v1]()

## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open browser and navigate to [Restaurant-On-The-Sea]()
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
-  Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:

Website behaved as expected.

Website was also opened on the following devices and no responsive issues were seen:



## Bugs

