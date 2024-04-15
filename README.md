![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# 🌟 nyreewaters art 🌟
# - a full stack web e-commerce web application

------

This e-commerce website was built for professional artist and designer, Nyree Waters, as my final Milestone Project for the Code Institute Fullstack Webdevelopment diploma (2024).

My sister, Nyree, produces original and printed mix-media artworks that she often sells online, so for this project I decided to build her a new e-commerce platform for her art shop.

Through this website, Nyree hopes to share her passion for creating and design, and to offer products that have been lovingly created in her distinct abstract style.
She is also a talented musician, writer and works in art facilitation, so the website has future scope to help streamline all of her freelance services.

## Showcase

![Am I Responsive?](/documentation/readme/# "Am I Responsive? Website Mockup")

The **Am I Responsive?** link can be found here - [Am I Responsive?](#)

A **deployed link** to the live website can be found here - [nyreewaters art](#)

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
    - [Data Models](#data-models)

3. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)
    - [Dependencies](#dependencies)

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

### User Requirements and Expectations

- Simple and intuitive user interface
- Clear presentation of necessary information to invite the user to join
- Secure platform that uses a login system with username and password to access and manage personal posts
- Quick and easy to search through existing posts
- Quick and easy to create an account and start sharing posts with others
- Quick and easy to add, edit or delete posts from the an account
- Design that is visually attractive
- Accessibility
- Features and navigation system works as expected


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


### Color Scheme

[coolors.co](https://coolors.co/) was used to create a color palette for the design after consulting with Nyree.

![nyreewaters art colorscheme](/documentation/readme/nyreewaters-colorscheme.png "nyreewaters art colorscheme")

### Typography

With reference to Nyree's [main website](https://nyreewaters.com) and her font styling preferences, we searched for font pairings that matched.

[Typ.io](https://typ.io/s/4c28) provided us with the following font pairing inspiration which is used on [mikekus.com](https://mikekus.com):

![Typ.io font-pairing example image](/documentation/readme/font-pairing-example.jpg)

- **Courier New** (body)
- **Helvetica** (headings)
- **Monaco**
- **Helvetica Neue**

---

## Information Architecture
### Data Models

---

## Technologies Used
### Languages
### Frameworks, Libraries and Programs
### Dependencies

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
### Media
### Content
### Acknowledgements