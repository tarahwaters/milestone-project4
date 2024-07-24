![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# 🌟 nyreewaters art 🌟
# - a full stack web e-commerce web application

------

This e-commerce website was built for professional artist and designer, Nyree Waters, as my final Milestone Project for the Code Institute Fullstack Webdevelopment diploma (2024).

My sister, Nyree, produces original and printed mix-media artworks that she often sells online, so for this project I decided to build her a new e-commerce platform for her art shop.

Through this website, Nyree hopes to share her passion for creating and design, and to offer products that have been lovingly created in her distinct abstract style.
She is also a talented musician, writer and works in art facilitation, so the website has future scope to help streamline all of her freelance services.

## Showcase

![Am I Responsive?](/documentation/readme/amiresponsive-nyreewaters-art.jpg "Am I Responsive? Website Mockup") mockup created using [Am I Responsive?](https://ui.dev/amiresponsive)

A **deployed link** to the live website can be found here - [nyreewaters art](https://nyreewaters-art-ccb67c4ebd7f.herokuapp.com/)

------

**Test card details**

Card number: 4242 4242 4242 4242

Expiry date: 04 / 24

CVC: 424

ZIP: 42424

------

## Table of Contents

1. [UX](#ux)

    - [Strategy](#strategy)
        - [Target Audience](#target-audience)
        - [User Requirements and Expectations](#user-requirements-and-expectations)
        - [User Stories](#user-stories)
            - [User](#user)
            - [Admin user or Site owner](#admin-user-or-site-owner)
    - [Scope](#scope)
        - [Trade Offs](#trade-offs)
    - [Structure](#structure)
        - [Features](#features)
            - [Existing Features](#existing-features)
            - [Future Features](#future-features)
    - [Skeleton](#skeleton)
        - [Wireframes](#wireframes)
    - [Surface](#surface)
        - [Color Scheme](#color-scheme)
        - [Typography](#typography)

2. [Information Architecture](#information-architecture)
    - [Database Structure](#database-structure)

3. [Tools and Technologies Used](#tools-and-technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries](#libraries)
    - [Platforms](#platforms)
    - [Other tools](#other-tools)

4. [Testing](#testing)
    
5. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

6. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Content](#content)
    - [Acknowledgements](#acknowledgments)

----------------------------

## UX:
## Strategy
### Target Audience

The target audience for the **nyreewaters art** shop are:

- People who are interested in buying original / printed / bespoke pieces of collaged artwork for themselves, or for others
- People who want to browse Nyree's collection of artwork
- People who want to learn more about Nyree as an artist and designer

### User Requirements and Expectations

- Simple and intuitive user interface
- Clear presentation of necessary information to invite the user to explore the page
- Features and navigation system works as expected
- Easy to navigate through products and look at reviews from other buyers before making a purchase
- Make a secure purchase
- Leave a review for a purchase
- Find out more information based on frequently asked questions (ie. for delivery costs / refunds)

**How the shop fulfils these expectations:**
- Design that is visually attractive and matches the artist's style
- Accessibility needs are met
- Standard design conventions of a shop with regard to menus, checkout, categories, etc
- Searching for products can be filtered or sorted based on what the user is looking for
- Confirmation / error messages to help guide the user through the checkout process
- User can create a secure profile to access their order details and leave a review

### Business Goals

The Business Goals of the **nyreewaters art** shop are:

- Create a page that showcases Nyree's art products and aligns with her unique style
- Encourage users to shop and learn more about Nyree as an artist, and her bespoke services
- Encourage users to contact Nyree for more details / enquiries about her work
- Showcase review highlights on the main homepage to encourage users to buy more items

### User Stories

#### User
As a user I would like:

#### Admin user or Site owner
In addition to the general user expectations, as an admin user / site owner I would like:

---

## Scope
### Trade Offs

Considering the user requirements and expectations, the table below shows the features that should be implemented to make an appealing and functional interactive game for users. Due to time constraints and my current skill level, some of these features are not implemented at this stage.

[X] indicates opportunities that were considered at the planning stage but were deemed not viable/feasible for this project sprint.
Y / N indicates a Yes / No as to whether each opportunity was acheived and implemented at this stage.

| Opportunity                                                         | Importance | Viability / Feasibility | Outcome |
| ------------------------------------------------------------------- | :--------: | :---------------------: | :------:|
| Register a secure account by creating a signin username + password  |     5      |            5            |    Y    |
| Signin page for registered users                                    |     5      |            5            |    Y    |
| Signout option with confirmation of action                          |     5      |            5            |    Y    |
| Add a cafe post by submission of a form with confirmation of action |     5      |            5            |    Y    |
| Confirmation of successful / unsuccessful actions via a flash msg   |     4      |            4            |    Y    |
| Display of all posts to main home page                              |     5      |            5            |    Y    |
| Display of all posts to admin profile (restricted access)           |     5      |            4            |    Y    |
| Display of published user posts on profile page                     |     4      |            4            |    Y    |
| Filter more relevant posts via search bar on home page              |     3      |            5            |    Y    |
| Edit / delete functionality of  published user posts (non-admin)    |     5      |            5            |    Y    |
| Edit / delete functionality of all posts (admin user only)          |     5      |            5            |    Y    |
| Confirmation of delete action via a pop up modal                    |     5      |            4            |    Y    |
| Restricted access for admin user to manage countries and images     |     5      |            5            |    Y    |
| Add / edit functionality for countries and images                   |     5      |            5            |    Y    |
| Custom Error404 page                                                |     3      |            3            |    N    |
| Option to view an individual cafe on a separate page                |     3      |            3            |    N    |
| Option to delete user account and associated posts [X]              |     4      |            3            |    X    |
| Option to upload a country image along with the country name [X]    |     2      |            2            |    X    |

---

## Structure

### Existing Features

Quick Links:

  - [Logo Link to Homepage](#logo-link-to-homepage)
  - [Desktop Navbar Dropdown](#desktop-navbar-dropdown)
  - [Mobile Navbar Menu](#mobile-navbar-menu)
  - [Signin Form with input validation](#signin-form-with-input-validation)
  - [Registration form with input validation](#registration-form-with-input-validation)
  - [Registration Success](#registration-success---welcome-message-and-redirection-to-profile-page)
  - [Signout Confirmation](#signout-confirmation)
  - [Add Cafe button](#add-cafe-button)
  - [Add Cafe form](#add-cafe-form)
  - [Add Cafe form validation](#add-cafe-form-validation)
  - [Cafe Cards](#cafe-cards-on-homepage-and-profile)
  - [Edit / Delete cafe buttons](#edit--delete-cafe-buttons)
  - [Edit Cafe (prefilled form)](#edit-cafe-prefilled-form)
  - [Delete Cafe confirmation](#delete-cafe-confirmation)
  - [Manage Locations (admin only functionality)](#manage-locations-page-admin-only-functionality)
  - [Add Country feature](#add-country-feature)
  - [Edit Country feature](#edit-country-feature)
  - [Delete Country feature](#delete-country-feature)
  - [Search Bar feature](#search-bar-feature)


### Future Features

The following features would be considered in future work to the project that would improve the useability and interest of this app:

---

## Skeleton

Wireframes for the website were created using the UI wireframe tool, [Balsamiq](https://balsamiq.com/), to plan the layout.

The layout and design were kept consistent across the pages / devices as much as possible.
The overall design evolved as the project was developed, so some of the wireframe designs were not carried out / were adapted.

The app consists of the following pages:

For Admin Users only:

### Wireframes

Below are the initial wireframes created for the project during the planning stage.

- [Homepage](/documentation/readme/wireframes-homepage.png) ✅
- [About](/documentation/readme/wireframes-about.png) ✅
- [Shop Category](/documentation/readme/wireframes-category.png) ✅
- [Shopping Bag](/documentation/readme/wireframes-shopping-bag.png) ✅
- [Checkout](/documentation/readme/wireframes-checkout.png) ✅
- [Checkout Success](/documentation/readme/wireframes-checkout-success.png) ✅
- [Individual Product](/documentation/readme/wireframes-product.png) ✅
- [My Profile](#)
- [Login](#)
- [Register](#)
- [Contact](#)
- [Leave a Review](#)
- [Search results](#)

---

## Surface

### Logo

The following logo was used from Nyree's original website:

![nyreewaters logo](/documentation/readme/nyreewaters-logo.jpg "nyreewaters name as logo")


### Color Scheme

[coolors.co](https://coolors.co/) was used to create a color palette for the design after consulting with Nyree.

![nyreewaters art colorscheme](/documentation/readme/nyreewaters-colorscheme.png "nyreewaters art colorscheme")

color contrast check - [coloors color contrast checker](https://coolors.co/contrast-checker/332e14-e5ffc8)

### Typography

With reference to Nyree's [main website](https://nyreewaters.com) and her font styling preferences, we searched for font pairings that matched.

[Typ.io](https://typ.io/s/4c28) provided us with the following font pairing inspiration which is used on [mikekus.com](https://mikekus.com):

![Typ.io font-pairing example image](/documentation/readme/font-pairing-example.jpg "font-pairing example from Typ.io")

- **Courier New** (body)
- **Helvetica** (headings)
- **Monaco**
- **Helvetica Neue**

---

## Information Architecture
## Database Structure
### Details
- I have used a **Postgres** relational database via [Supabase](https://supabase.com/) throughout the entire project development.
- The project is directly connected to the deployed database on Heroku during development  - this was necessary to work with the Code Institute Dockerfile that was used.

### Diagram
- The diagram (created on [DrawSQL](https://drawsql.app/)) shows a layout of the tables created by my models in the database.
- The diagram below omits the tables created by default, except the user table, as well as the tables created by [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html).

![Database Schema Diagram](/documentation/readme/drawSQL-schema.png "database schema diagram")


**Please Note:** 
- Default tables created by [django](https://www.djangoproject.com/) as well as [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) have been ommited from this section. Please refer to their documentation (refrenced [here](#tools-and-technologies-used)) for more information on their data models.
- The CountryField is from [django-countries](https://github.com/SmileyChris/django-countries).

---

## Tools and Technologies Used:

### Languages:
- **HTML5**
- **CSS**
- **JavaScript**
- **Python3**

### Frameworks:
- [Django v3.2](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - used for front-end components and framework design

### Libraries:
- [JQuery](https://jquery.com/) - animations and click functions
- [Google Fonts](https://fonts.google.com/) - font styles
- [FontAwesome](https://fontawesome.com/) - used for icons
- [Flaticon](https://www.flaticon.com/) - used for error / no-photo icon images

### Packages:

### Platforms:
- [GitHub and Github Pages](https://github.com/) - used to securely store the code and to host and deploy the live project
- [GitPod](https://www.gitpod.io/) - used as a cloud-based IDE for development
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - used for testing and troublshooting code, along with Lighthouse auditing

### Other tools:
- [Balsamiq](https://balsamiq.com/wireframes/) - used to create wireframes during project planning
- [redketchup.io](https://redketchup.io/) - used for resizing and converting image files to webp format
- [Coolors](https://coolors.co/) - used to generate a color palette for the website design and to check contrast of colors
- [FontJoy](https://fontjoy.com/) - used to generate visually appealing font pairings for  the website
- [JSON formatter and validator](https://jsonformatter.org/) - used for formatting and validating JSON files
- [CSV2JSON](https://csvjson.com/csv2json) - for converting CSV data from spreadsheet into JSON format
<!-- - [JSHint](https://jshint.com/) - used to validate JS code
- [Esprima](https://esprima.org/demo/validate.html) - used to validate JS syntax
- [W3 HTML validator](https://validator.w3.org/nu/) - used to validate HTML -->
- [W3 Jigsaw](https://jigsaw.w3.org/css-validator/validator) - used to validate CSS
- [Tim Nelson's Markdown Builder](https://traveltimn.github.io/markdown-builder/) to help create the structure and some of the content for the README and TESTING.md files
- [AmIResponsive?](https://ui.dev/amiresponsive) - used to create a responsive mockup of the website
- [RandomKeygen](https://randomkeygen.com/) - used to create a secure secret key
<!-- - [Code Institute Python Linter](https://pep8ci.herokuapp.com/) - used to validate Python code -->
- [DrawSQL](https://drawsql.app/) - used to create the database schema diagram

---

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

---

## Deployment
### Local Deployment
### Heroku Deployment

---

## Credits
### Code
- [Emma Walsh](https://github.com/emmawalshdev) for shop layout inspiration and adapted code on Home and About pages, also Bespoke form setup - [KayTea Art (Github repo)](https://github.com/emmawalshdev/kaytea_art/tree/main)

### Media
- [Freepik - Favicon](https://www.flaticon.com/free-animated-icons/no-camera) - No camera animated icon created by Freepik, used in cases of 'no image' rendered for images across the site
- [Freepik - Favicon](https://www.flaticon.com/free-animated-icon/warning_6569130) - Warning animated icon created by Freepik, used as an image on custom error pages
- All product images are used with the permission of the original artist, [Nyree Waters](https://www.nyreewaters.com/)
- Bio image of Nyree, also in use on her [main website](https://www.nyreewaters.com/), also used with her permission

### Content

## References
### Accessibility
In response to DevTools Lighthouse Audits, the following references were used to help improve the quality and efficiency of the site:
- [Deque University](https://dequeuniversity.com/rules/axe/4.9/link-name) - Discernible names for links (e.g. social media links / icons)

## Acknowledgements