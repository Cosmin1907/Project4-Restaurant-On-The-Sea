## Functional Testing

**Authentication**

Description:

Ensure a user can sign up to the website

Steps:

1. Navigate to [Restaurant-On-The-Sea](https://project4-restaurant-booking-cacc3b345e08.herokuapp.com/) and click Register
2. Enter username, password, and email (as an optional fiel) 
3. Click Sign up

Expected:

- A message is displayed: Successfully signed in as testuser.
- The user is redirected to the home page as a signed-in user.
- The menu options display Logout instead of Register and Login.


Actual: 

- A message is displayed: Successfully signed in as testuser.
- The user is redirected to the home page as a signed-in user.
- The menu options display Logout instead of Register and Login.

<hr>

Description:

Ensure a user can log in once signed up

Steps:
1. Navigate to [Restaurant-On-The-Sea](https://project4-restaurant-booking-cacc3b345e08.herokuapp.com/) and click Login
2. Enter login details created in previous test case
3. Click sign in

Expected:

- A message is displayed: Successfully signed in as testuser.
- The user is redirected to the home page as a signed-in user.
- The menu options display Logout instead of Register and Login.

Actual:

- A message is displayed: Successfully signed in as testuser.
- The user is redirected to the home page as a signed-in user.
- The menu options display Logout instead of Register and Login.

<hr>

Description:

Ensure a user can sign out

Steps:

1. Login to the website
2. Click the logout button
3. Click sign out on the confirm logout page

Expected:

- A message is displayed: You have signed out.
- The user is redirected to the home page.
- The menu options are updated to display Register and Login, and no longer show Logout.

Actual:

- A message is displayed: You have signed out.
- The user is redirected to the home page.
- The menu options are updated to display Register and Login, and no longer show Logout.

**Booking Forms**

Description:

Ensure a new booking can be created.

Steps:

1. Navigate to [Restaurant-On-The-Sea](https://project4-restaurant-booking-cacc3b345e08.herokuapp.com/) - and Login.
2. Click Book a Table
2. Enter the following:
    - Name: Cosmin
    - Phone No: E.164 complient format number
    - Date: Any future date
    - Time slot: Any future drop down field
    - No Of Guests: 2
    - Booking notes (as an optional field)

3. Click book

Expected:

- Form successfully submits and a message is shown to alert the user of successful booking.

Actual:

- Form successfully submits and a message is shown to alert the user of successful booking.

<hr> 

Description:

Ensure a booking can be edited.

Steps:

1. Navigate to [Restaurant-On-The-Sea](https://project4-restaurant-booking-cacc3b345e08.herokuapp.com/) - and Login.
2. Click on Bookings
3. Click on Edit
4. Enter the following:
    - Name: Cosmin
    - Phone No: E.164 complient format number.
    - Date: Any future date
    - Time slot: Any future drop down field
    - No Of Guests: 5
    - Booking notes (as an optional field)

Expected:

- Form successfully submits and a message is shown to alert the user of updated booking.

Actual:

- Form successfully submits and a message is shown to alert the user of updated booking.

<hr>

Description:

Ensure user can successfully delete a booking.

Steps:
1. Login as a user with a booking or create a new booking
2. Click on Bookings
3. Click the delete button on a booking
4. Click the confirm button on the delete page

Expected:

- Booking is successfully deleted

Actual:

- Booking is successfully deleted

<hr>

**Navigation Links**

Testing was conducted to ensure that all navigation links on the respective pages directed to the correct destinations as per the design. This was verified by clicking on the navigation links on each page.

- Home -> index.html
- Menu -> menu.html
- Bookings -> booking_list.html
- Book a Table -> booking_table.html
- Ratings -> ratings.html
- Logout -> Sign out all auth page
- Login -> Sign in all auth page
- Register -> Sign up all auth page

All navigation links directed to the corect pages as expected.

<hr>

**Footer**

Testing was conducted on the footer links by clicking all the Font Awesome social media icons. It was verified that each icon opened the respective social media site in a new tab, functioning as expected.

## Negative Testing

Tests were performed on the create booking to ensure that:

1. Booking a past date is not allowed.
2. Booking a time slot that has already passed today is not allowed.
3. Booking is prevented if there are no available tables for the guest count.
4. Editing a booking to increase the guest size is restricted if no tables have sufficient capacity.
5. Forms cannot be submitted with required fields left empty.
6. The form correctly validates the phone number format.


## Unit Testing

Unit tests were created to verify core functionality, such as template usage and redirects. These tests, covering form functionality, programming logic, and page display, are located in the test_forms.py and test_views.py files within the respective apps.`

Results:

![unit tests](docs/testing_img/tests.PNG)

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
Initially, there were errors due to trailing slashes and unclosed elements. All these issues were corrected

Due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on these files, open the page to validate, right-click and view page source. Paste the raw HTML code into the validator, as this will be only the HTML rendered code.

![HTML Validator](docs/testing_img/html_validator.PNG)

All pages were run through the CI Python Linter [Pep8](https://pep8ci.herokuapp.com/) validator to ensure all code was pep8 compliant, with the exception of the settings.py file.


![PEP8](docs/testing_img/pep8.PNG)

JavaScript code was run through [JSHINT](https://jshint.com) javascript validator. 
Warnings about ES6 features in the JavaScript file were found and addressed by adding the comment /* jshint esversion: 6 */ at the top of the file.
The only warning that remained was about an unused variable. The function was called via onclick from an HTML element, so it is in fact being used.

![JS validator](docs/testing_img/js.PNG)

## Lighthouse Report

Lighthouse report highlighted SEO and performance issues. Added meta descriptions and keywords to boost SEO to 100. Improved performance by reducing image size.

![Lighthouse v1](docs/testing_img/lighthouse.PNG)

## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open browser and navigate to [Restaurant-On-The-Sea](https://project4-restaurant-booking-cacc3b345e08.herokuapp.com/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
-  Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:

Website behaved as expected.

Website was also opened on the following devices and no responsive issues were seen:
Iphone SE
Ipad Pro

## Bugs

A bug involved creating a duplicate table instance upon update, leading to extra table instances for the booking. This was fixed by introducing code to delete the existing table instance before recreating it when the booking was updated.