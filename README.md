![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# 🌟 nyreewaters art 🌟
# - a full stack e-commerce web application

------

This e-commerce website was built for professional artist and designer, Nyree Waters, as my final Milestone Project for the Code Institute Fullstack Webdevelopment diploma (2024).

My sister, Nyree, produces original and printed mix-media artworks that she often sells online, so for this project I decided to build her a new e-commerce platform for her art shop.

Through this website, Nyree hopes to share her passion for creating and design, and to offer products that have been lovingly created in her distinct abstract style.
She is also a talented musician, writer and works in art facilitation, so the website has future scope to help streamline all of her freelance services.

## Showcase

![Am I Responsive?](/documentation/amiresponsive-nyreewaters-art.jpg "Am I Responsive? Website Mockup") mockup created using [Am I Responsive?](https://ui.dev/amiresponsive)

A **deployed link** to the live website can be found here - [nyreewaters art](https://nyreewaters-art-ccb67c4ebd7f.herokuapp.com/)

If you'd like to test the checkout and payment functionality of the website, please use the [test card details](#test-card-details-from-stripe) below.

------

### Test card details (from Stripe):

- Card number: 4242 4242 4242 4242

- Expiry date: 04 / 245 (or any future date)

- CVC: 424 (example)

- ZIP: 42424

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
        - [Details](#details)
        - [Diagram](#diagram)
    - [Database Models](#database-models)
        - [Product App](#product-app)
        - [Checkout App](#checkout-app)
        - [Profiles Apps](#profiles-app)
        - [FAQs App](#faqs-app)
        - [Contact App](#contact-app)
        - [Bespoke App](#bespoke-app)

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
- Contact the site owner with questions / a bespoke enquiry

**How the shop fulfils these expectations:**
- Design that is visually attractive and matches the artist's style
- Accessibility needs are met
- Standard design conventions of a shop with regard to menus, checkout, categories, etc
- Searching for products can be filtered or sorted based on what the user is looking for
- Confirmation / error messages to help guide the user through the checkout process
- User can create a secure profile to access their order details
- Users can get in touch with Nyree via the contact page / by email directly / by submitting a bespoke enquiry form (these forms do not have POST functionality yet)

### Business Goals

The Business Goals of the **nyreewaters art** shop are:

- Create a page that showcases Nyree's art products and aligns with her unique style
- Encourage users to shop and learn more about Nyree as an artist, and her bespoke services
- Encourage users to contact Nyree for more details / enquiries about her work
- Showcase review highlights on the main homepage to encourage users to buy more items

### User Stories

#### User
As a new user:

1. I would like to explore some details about the artist, Nyree Waters, to see if her style and products may interest me.
2. I would like to browse interesting, unique art products available to buy online.
3. I would like to create an account with a profile, so that I can save my order details and have a more personalised experience whilst shopping.

As a returning user:

1. I would like to log into my account and view my profile, so I can access my saved personal details and previous orders.
2. I would like to browse products easily based on the type of artwork I am looking for, and have the ability to search for specific products.
3. I would like to sort products by various criteria to make the (e.g. price, type, name) so that I can find what I'm looking for more easily.
4. I would like to add items to a shopping bag to keep track of the products I wish to purchase, with the ability to add / remove items where necessary.
5. I would like to follow a familiar process for making a secure purchase via a checkout page, and have regular feedback that my information has been submitted and processed successfully.
6. I would like to receive an email confirmation of my order once I have purchased something, and have access to these details via my account for future reference.
7. I would like my order details to be saved to my profile, and have the option of add or updating my address for quick access in future.
8. I would like to view some details about payment /shipping / delivery before making a purchase.


#### Admin user or Site owner
In addition to the general user expectations, as an admin user / site owner:

1. I would like to manage the product listings that are displayed on the site
2. I would like secure access to editing or adding new products - and to add appropriate details such as SKU, 
product name and description, price and an image.
3. I would like the option to remove products that are no longer in stock / I no longer wish to sell.
4. I would like to manage the FAQ section so that I can easily update and add answers to common questions as required.
5. I would like to manage user permissions and roles, and control the access to the admin panel, ensuring the site data remains secure.
---

## Scope
### Trade Offs

Considering the user requirements and expectations, the table below shows the features that should be implemented to make an appealing and functional interactive game for users. Due to time constraints and my current skill level, some of these features are not implemented at this stage.

[X] indicates opportunities that were considered at the planning stage but were deemed not viable/feasible for this project sprint.
Y / N indicates a Yes / No as to whether each opportunity was acheived and implemented at this stage.

| Opportunity                                                         | Importance | Viability / Feasibility | Outcome |
| ------------------------------------------------------------------- | :--------: | :---------------------: | :------:|
| Register a secure account by creating a signin username + password  |     5      |            5            |    Y    |
| Email verification to register an account                           |     5      |            5            |    Y    |
| Signin page for registered users                                    |     5      |            5            |    Y    |
| Signout option with confirmation of action                          |     5      |            5            |    Y    |
| Confirmation of successful / unsuccessful actions via a toast msg   |     4      |            4            |    Y    |
| Home page with shop and artist details and links                    |     5      |            5            |    Y    |
| Shop page listing products, and options to view by category / sort  |     5      |            5            |    Y    |
| Access to Profile page for signed in users                          |     5      |            4            |    Y    |
| Save / update personal details in user profile                      |     4      |            4            |    Y    |
| Search bar (for products)                                           |     4      |            4            |    Y    |
| Edit / delete functionality of products (admin user only)           |     4      |            5            |    Y    |
| Confirmation of delete action via a pop up modal                    |     4      |            2            |    N    |
| Restricted access for admin user to manage products                 |     5      |            5            |    Y    |
| Shopping bag functionality (add / edit bag before purchase)         |     5      |            5            |    Y    |
| Secure checkout functionality                                       |     5      |            5            |    Y    |
| Order confirmation page (with email)                                |     5      |            5            |    Y    |
| About page (with details and links about artist)                    |     4      |            5            |    Y    |
| Frequently asked questions page                                     |     3      |            5            |    Y    |
| Bespoke Enquiry page*                                               |     3      |            3            |    Y    |
| Contact page*                                                       |     4      |            4            |    Y    |
| Add a product review (functionality and page)                       |     3      |            2            |    X    |

* Bespoke and Contact page forms were created but without POST functionality due to time restraints


---

## Structure

### Existing Features

General:
  - [Logo Link to Homepage](#logo-link-to-homepage)
  - [Desktop Navbar Dropdown](#desktop-navbar-dropdown)
  - [Mobile Navbar Menu](#mobile-navbar-menu)
  - [Search Bar feature](#search-bar-feature)
  - [Footer Links](#footer-links)
  - [Toast Messages](#toast-messages)
  - [Custom Error Pages](#custom-error-pages)

  My Account:
  - [Login](#login)
  - [Register Account](#register-account)
  - [Registration verification](#registration-verification)
  - [Registration Success](#registration-success)
  - [Signout Confirmation](#signout-confirmation)
  - [Profile page](#profile-page)

  Shop:
  - [All Products](#all-products)
  - [Shop Category Buttons](#shop-category-buttons)
  - [Shop Prints](#shop-prints)
  - [Shop Originals](#shop-originals)
  - [Product Sort Selector](#product-sort-selector)
  - [Scroll To Top Button](#scroll-to-top-button)
  - [Product Detail](#product-detail)
  - [Product Quantity Tool](#product-quantity-tool)
  - [Add To Shopping Bag](#add-to-shopping-bag)
  - [View/Edit Shopping Bag](#adjust/edit-shopping-bag)
  - [Secure Checkout](#secure-checkout)
  - [Stripe Payment](#stripe-payment)
  - [Order Confirmation](#order-confirmation)
  - [Email Order Confirmation](#email-order-confirmation)

  Other pages:
  - [Bespoke Details and Form](#bespoke-details-and-form)
  - [Contact Form](#contact-form)
  - [FAQs](#faqs)



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

Below are the initial wireframes created for the project during the planning stage. As the project developed, the layouts were adapted to accomodate for the content included / limitations in design scope.

- [Homepage](/documentation/wireframes-homepage.png) ✅
- [About](/documentation/wireframes-about.png) ✅
- [Shop Category](/documentation/wireframes-category.png) ✅
- [Shopping Bag](/documentation/wireframes-shopping-bag.png) ✅
- [Checkout](/documentation/wireframes-checkout.png) ✅
- [Checkout Success](/documentation/wireframes-checkout-success.png) ✅
- [Individual Product](/documentation/wireframes-product.png) ✅

The following pages were not designed using wireframes due to time restraints, and instead followed a similar layout structure to the main pages (above) that were created first:
- My Profile
- Login
- Register
- Contact
- Leave a Review **
- Search results
- Bespoke
- FAQs

****Note** - Review feature was not included at this stage of production (see [Scope](#scope) for more details)

---

## Surface

### Logo

The following logo was used from Nyree's original website:

![nyreewaters logo](/documentation/nyreewaters-logo.jpg "nyreewaters name as logo")


### Color Scheme

[coolors.co](https://coolors.co/) was used to create a color palette for the design after consulting with Nyree.

![nyreewaters art colorscheme](/documentation/nyreewaters-final-colorscheme.png "nyreewaters art colorscheme")

[Coloors color contrast checker](https://coolors.co/contrast-checker/332e14-e5ffc8) was also used to check font colors contrasted well against coloured backgrounds for improved accessibility.

#E5543C
#35CCCF
#000000
#343A40
#EADECE
#F8F9FA

### Typography

With reference to Nyree's [main website](https://nyreewaters.com) and her font styling preferences, we searched for font pairings that matched.

[Typ.io](https://typ.io/s/4c28) provided us with the following font pairing inspiration which is used on [mikekus.com](https://mikekus.com):

![Typ.io font-pairing example image](/documentation/font-pairing-example.jpg "font-pairing example from Typ.io")

Font Pairing Inspiration:
- **Courier New** (body)
- **Helvetica** (headings)
- **Monaco**
- **Helvetica Neue**

Since not all these fonts were available for free or were not accessible using [Google Fonts](https://fonts.google.com/), the following font styles were used as close alternatives:

Font Styles used in project:

- **Courier New** (body)
- **Courier Prime** (backup body)
- **Inter** (headings, nav links, or for style emphasis)
- **San-serif** (backup font)

---

## Information Architecture
## Database Structure
### Details
- I have used a **Postgres** relational database via [Supabase](https://supabase.com/) throughout the entire project development.
- The project is directly connected to the deployed database on Heroku during development  - this was necessary to work with the Code Institute Dockerfile that was used.

### Diagram
- The diagram (created on [DrawSQL](https://drawsql.app/)) shows a layout of the tables created by my models in the database.
- The diagram below omits the tables created by default, except the user table, as well as the tables created by [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html).

![Database Schema Diagram](/documentation/drawSQL-schema.png "database schema diagram")

## Database Models

**Please Note:** 
- Default tables created by [django](https://www.djangoproject.com/) as well as [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) have been ommited from this section. Please refer to their documentation (refrenced [here](#tools-and-technologies-used)) for more information on their data models.
- The CountryField is from [django-countries](https://github.com/SmileyChris/django-countries).

### Product App
### Checkout App
### Profiles App
### FAQs App
### Contact App
### Bespoke App

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
- **asgiref** - ASGI is the standard interface for asynchronous Python web servers, frameworks and applications to communicate with eachother
- **boto3** - used to configure and manage AWS S3
- **botocore** - session, credential and configuration data
- **dj-database-url** - from django, used to parse a DATABASE_URL to configure a django app
- **django** - Python-based free opensource web framework (follows a model-template-view structure)
- **django-allauth** - integrated set of django applications for authentication, registering an account, managing accounts etc.
- **django-countries** - from django, provides country choices for use in forms and model fields
- **django-crispy-forms** - using the crispy filter and tag, this helps with consistency of form styling
- **django-storages** - custom storage backends from a single library, for use with AWS
- **gunicorn** - helps to deploy the server on Heroku
- **jmespath** - specifies how to extract data from a JSON file
- **oauthlib** - framework that uses OAuth1 or OAuth2 logic without assuming a specific HTTP request object / web framework.
- **pillow** - Python imaging library that provides tools to manipulate images
- **psycopg2** - popular PostgreSQL database adaptor for Python
- **python-dotenv** - reads key-value pairs from an environment file and sets them as env variables
- **python3-openid** - python packages to support use of OpenID decentralised identity system in the application
- **pytz** - library that brings the Olson tz database into Python to support cross platform timezone calculations
- **requests-oauthlib** - provides a easy Python interface for building OAuth1 and OAuth2 clients
- **s3transfer** - Python library that manages Amazon S3 transfers
- **sqlparse** - provides support for parsing, splitting and formatting SQL statements
- **stripe** - Python library for the Stripe API

### Platforms:
- [GitHub and Github Pages](https://github.com/) - used to securely store the code and to host and deploy the live project
- [GitPod](https://www.gitpod.io/) - used as a cloud-based IDE for development
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - used for testing and troublshooting code, along with Lighthouse auditing
- [Heroku](https://www.heroku.com/) -used for production deployment
- [Amazon Web Services](https://aws.amazon.com/) - S3 Bucket used for static file hosting
- [Supabase](https://supabase.com/) - PostgreSQL database for deployment with Heroku

### Other tools:
- [Balsamiq](https://balsamiq.com/wireframes/) - used to create wireframes during project planning
- [redketchup.io](https://redketchup.io/) - used for resizing and converting image files to webp format
- [Coolors](https://coolors.co/) - used to generate a color palette for the website design and to check contrast of colors
- [FontJoy](https://fontjoy.com/) - used to generate visually appealing font pairings for  the website
- [JSON formatter and validator](https://jsonformatter.org/) - used for formatting and validating JSON files
- [CSV2JSON](https://csvjson.com/csv2json) - for converting CSV data from spreadsheet into JSON format
- [JSHint](https://jshint.com/) - used to validate JS code
- [W3 HTML validator](https://validator.w3.org/nu/) - used to validate HTML
- [W3 Jigsaw](https://jigsaw.w3.org/css-validator/validator) - used to validate CSS
- [Tim Nelson's Markdown Builder](https://traveltimn.github.io/markdown-builder/) to help create the structure and some of the content for the README and TESTING.md files
- [AmIResponsive?](https://ui.dev/amiresponsive) - used to create a responsive mockup of the website
- [RandomKeygen](https://randomkeygen.com/) - used to create a secure secret key
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/) - used to validate Python code
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
- [Code Institute's Boutique Ado Walkthrough](https://github.com/Code-Institute-Solutions/boutique_ado_v1) - base code used follows the structure of the Boutique Ado project and was adapated for use
- [CSS tricks](https://css-tricks.com/snippets/css/css-triangle/) - also referenced by Code Institute in the Boutique Ado project, the 'arrow-up' styling was used for the 'scroll to top' button
- [Emma Walsh](https://github.com/emmawalshdev) for shop layout inspiration and adapted code on Home and About pages, also Bespoke form setup - [KayTea Art (Github repo)](https://github.com/emmawalshdev/kaytea_art/tree/main)
- [Rory Sheridan](https://github.com/Ri-Dearg/neverlost-thrift/tree/master) - general project inspiration and reference, but also README documentation help (e.g. Database Structure)
- [Delyth Jennings](https://github.com/D3lyth/lunar_glow/) - for TESTING section boilerplate

### Media
- [Freepik - Favicon](https://www.flaticon.com/free-animated-icons/no-camera) - No camera animated icon created by Freepik, used in cases of 'no image' rendered for images across the site
- [Freepik - Favicon](https://www.flaticon.com/free-animated-icon/warning_6569130) - Warning animated icon created by Freepik, used as an image on custom error pages
- All product images are used with the permission of the original artist, [Nyree Waters](https://www.nyreewaters.com/)
- Bio image of Nyree, also in use on her [main website](https://www.nyreewaters.com/), also used with her permission

### Content

Some of the written content e.g. artist bio, was taken from [Nyree Waters' website](https://www.nyreewaters.com/) with her permission.

## References

### Project Inspiration (Github Repos)

- [Emma Walsh](https://github.com/emmawalshdev) - KayTea Artwork
- [Delyth Jennings](https://github.com/D3lyth/lunar_glow/tree/main) - Lunar Glow
- [Rory Sheridan](https://github.com/Ri-Dearg/neverlost-thrift/) - NeverLost Thrift
- [Erikas Ramanauskas](https://github.com/Erikas-Ramanauskas/Milestone-Project-4) - G-mark
- [Anthony Griffiths](https://github.com/Ant2210/keto-kreations/) - KetoKreations

### Accessibility
In response to DevTools Lighthouse Audits, the following references were used to help improve the quality and efficiency of the site:
- [Deque University](https://dequeuniversity.com/rules/axe/4.9/link-name) - Discernible names for links (e.g. social media links / icons)

## Acknowledgements
- [Rory Sheridan](https://github.com/Ri-Dearg) - for his great mentorship and support throughout the project