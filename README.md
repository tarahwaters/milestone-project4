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

**Note** * Bespoke and Contact page forms were created and have some POST functionality but data is not currently saved to the database (more details in [existing features](#existing-features)).


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

  Admin:
  - [Product Management](#product-management)
  - [Django Admin](#django-admin)

  #### Logo Link to Homepage

  Clicking the Nyree Waters logo anywhere on the site takes the user back to the homepage.
  
  ![nyreewaters logo](/documentation/features/feature-logo-home.png "nyreewaters name as logo")

  #### Desktop Navbar Dropdown

  Viewing the website on a desktop displays the navbar menu in a central position that is easy to access. The 'shop' link contains a dropdown to search for all shop items, or by category:

  ![desktop nav dropdown menu](/documentation/features/feature-dropdown-menu-shop.png "desktop nav dropdown menu for shop contents")

  #### Mobile Navbar Dropdown
  
  Viewing the website from a mobile device allows the user easy access to the navbar via a dropdown menu:

  ![mobile nav dropdown menu](/documentation/features/features-mob-nav-menu.png "image of mobile nav dropdown menu")

  #### Search Bar Feature

  A search bar is located at the top of each page and allows the user to search the shop items using keywords.

  ![search bar feature](/documentation/features/feature-search-shop.png "image of search bar feature")
  
  Results will show if the keyword is present in either the product title / description.

  ![search bar feature - results](/documentation/features/feature-search-results.png "example of search bar feature results")

  If there are no results, then feedback of 'no results' is displayed to the user.
  
  ![search bar feature - no results](/documentation/features/feature-search-no-results.png "example of search bar feature when no results are found")

  #### Footer Links

  A footer containing Nyree's social links, as well as links to my github / linkedin pages (as the webdeveloper), is consistent and accessible at the bottom of each page. It contains the logo and similar font styling to the rest of the site. There are also quick nav links for the user to access other pages if/when convenient.

   ![footer links](/documentation/features/feature-footer-links.png "image of footer and links to socials or other site pages")

  #### Toast Messages

  Toast Messages were utilised using Bootstrap and provide the user with regular feedback in the top right corner of the page (for visual users - via a box that pops up by the shopping bag). These messages can show a successful process has been completed, an error message explaining the issue, alert or general update:

  ![toast success for confirming an email](/documentation/features/feature-signup-success.png "a toast success messsage for confirming an email address")

  #### Login

  Users with an account already can 'login' via the link found in the 'my account' dropdown or the 'signin' link on the 'register' page. This is what all users see before they sign in:

  ![login link](/documentation/features/feature-account-dropdown-no-signin.png "login link")

  On the signin page, users need to fill in the form with their email address and password - this is validated and any errors will result in an message being displayed. 
  
  A successful signin results in a toast message in the right corner, and the following account options will now be available for non-admin users:

  ![account dropdown for signed in non-admin](/documentation/features/feature-account-dropdown-user.png "account dropdown for signed in non-admin")

  And for admin users, a secure product management link will be available as well as access to the profile / logout:

  ![account dropdown for signed in admin](/documentation/features/feature-account-dropdown-admin.png "account dropdown for signed in admin")

  #### Register Account

  For new users, they can register an account via the validated registration form:

  ![new account registration form](/documentation/features/feature-register-form.png "new account registration form")

  Emails that have already been registered / invalid inputs will result in an error message which tells the user what to do.

  #### Registration Verification

  A new registration using a valid email address will receive an update explaining that an email verification link has been sent:

  ![email verification page](/documentation/features/feature-verify-email-registration.png "email verification page")

  An example of the sent verification email is below:

  ![registration email example](/documentation/features/feature-register-email.png "registration email example")

  #### Registration Success

  Clicking the verification link, the user is sent to a confirmation page and upon clicking 'confirm', they will receive a signup success message:

  ![signup success message](/documentation/features/feature-signup-success.png "signup success message")

  #### Signout Confirmation

  Clicking the 'logout' link from the account dropdown opens the 'signout confirmation' page:

  ![signout confirmation page](/documentation/features/feature-sign-out-confirm.png "signout confirmation page")

  A successful signout will result in a toast message in the corner. And the user can no longer access their Profile until they log back in.

  #### Profile Page

  A signed in user can access a Profile page which has a dynamic form (on the left side for larger screens) to store delivery address details (which can be added / edited and saved) for easy access at the checkout page. A successful order will automatically populate the details for returning users if they clicked the option to save their details.

  ![profile page](/documentation/features/feature-profile-page.png "profile page")

  On the right side (or below, for mobile users), the user's Order History is listed. This contains the general order details such as: order number, date, items and total.
  The order number is linked to a more detailed view of the original 'order confirmation' received when a purchase was made. This can be useful for users who want to check this information at a later date. Any future orders will be saved here if the user was logged into their account when they made a purchase.

  ![profile order confirmation](/documentation/features/feature-profile-order-confirmation.png "profile order confirmation")

  From the profile order confirmation page, the user can return to their profile by clicking the button 'back to profile'.

  As you can see in the example, reference to the order email address in the top description, order summary and Alert message, are all linked to the same address associated with the order ID.

  #### All Products

  Accessing the shop to view 'all items' can be done via the navbar dropdown menu for 'shop'. Or if the user has selected either the 'prints' or 'originals' links on the main page, there is a link to 'All items' from the top left either product category page.

  ![desktop nav dropdown menu](/documentation/features/feature-dropdown-menu-shop.png "desktop nav dropdown menu for shop contents")

  The main products page lists all items available for purchase of both major categories: Originals and Prints.

  This view is for non-admin users / non-signed in users:

  ![all products page](/documentation/responsive-xl-products.png "all products page")

  Admin users are able to see the edit / delete icons next to each product (see below for more details in [product management](#product-management))

  #### Shop Category Buttons

  The shop category buttons are arranged centrally on each product page for easy access and the hover styling highlights when they are selected.

  ![product category buttons](/documentation/features/feature-product-sorting.png "product category buttons")

  On the home page there are also buttons that link to the product categories, that showcase an example piece or Original or Printed artwork for sale to entice customers:

  ![home page shop buttons](/documentation/features/feature-shop-online-links.png "home page shop buttons")

  Clicking either 'products' or 'originals' will take the user to a page listing only the products listed under that category.

  Clicking 'bespoke' will take the user to the [bespoke](#bespoke-details-and-form) collage page, where they can submit an enquriry.

  #### Shop Prints

  Shopping on the Prints category page looks like this:

  ![prints product page](/documentation/responsive-desktop-products.png "prints product page")

  #### Shop Originals

  Shopping on the Originals category page looks like this:

  ![originals product page](/documentation/features/feature-products-non-admin.png "originals product page")

  On this main product view, each item contains basic info such as the product image, name, rating, category tag, price. Users can click the item to open up further details about the product, where it can also be added to the shopping bag ready for purchasing.

  #### Product Sort Selector

  On each product page, users have the option of sorting items by name / price - either ascending or descending in order. There is also potential to include the product rating as a sorting option (to be expanded on in future with a customer 'review' feature).

  As previously mentioned, there is a link to return to 'All items' from the catergory views, and the number of products per page is also listed here (updates accordingly).

  ![product sorting buttons](/documentation/features/feature-product-sorting.png "product sorting buttons")

  #### Scroll to Top Button

  With an increasing number of items added to the shop, the page is likely to become quite long when scrolling through products. There is a handy button included (arrow up button, bottom right of larger pages) that allows the user to scroll back to the top of the page. Once clicked the button turns an orange colour.

  #### Product Detail

  The product detail view shows an individual product with more details, and the option to choose the number of items required, add those items to the shopping bag, or return to the 'all items' page via the 'keep shopping' button.

  The following image contains the edit / delete buttons that are only visible for admin users, otherwise the page looks exactly the same for non-admin users.

  ![product detail view](/documentation/features/feature-edit-delete-product-detail.png "product detail view")

  #### Product Quantity Tool

  The product quantity tool allows the user to increase / decrease the number of items they wish to add to the shopping bag. The '-' button does not function below 1, and equally, the '+' button can only goes up to 99. The user can also enter the numerical value by keyboard.

  #### Add to Shopping Bag

  Once the 'add to bag' button has been clicked, the user is updated by a message up by the shopping bag icon. This message summarises the item/s added, updates the bag total and will flash a message about the free delivery threshold (currently set at orders over £40). Here, the user is told how much more they need to spend before qualifying for free delivery.

  ![add to bag update message](/documentation/features/feature-free-delivery-notification.png "add to bag update message")

  From then on, with items now in the shopping bag, the icon will turn blue and it will show the updated cost of the items.

  ![bag icon updated with price](/documentation/features/feature-bag-icon-updates.png "bag icon updated with price")

  #### View/Edit Shopping Bag

  To view or edit the shopping bag, users need to click the bag icon.
  This will open the shopping bag view. If no items are in the bag, a message confirming this will be displayed on the page, and the user is encouraged to click a button to 'continue shopping'.

  If there are items in the bag, users will see a summary of their bag items as well as an option to increase / decrease the quantity, and update / remove the items via the links.

  ![shopping bag page](/documentation/features/feature-shopping-bag.png "shopping bag page with items with items")

  If an item quantity is changed and 'updated', the total costs listed will also be updated to reflect the new cost. 

  There are also two main buttons to either 'keep shopping' (which returns to all items page) or proceed to the 'secure checkout'.

  #### Secure Checkout

  The secure checkout page allows users to review their bag items once more before paying. There is the option to 'adjust bag' which returns to the bag page if the user is not ready to pay. Or if the user wants to commit to a purchase, they can enter their personal details, delivery details and payment info into the validated form.

  ![secure checkout page](/documentation/features/feature-secure-checkout.png "secure checkout page")

  There is an option for a signed in user to save their personal details to their Profle (for a quicker checkout next time), or if they are not signed in / have not registered, links will be offered for them to complete these actions first.

  #### Stripe Payment

  The payment form is securely linked to the Stripe platform. For this project, as it is a test project for educational purposes only, only the Stripe [test card details](#test-card-details-from-stripe) will return a successful order.

  Using other card details will return different validation error messages through the Stripe API.

  ![Stripe payment validation declined card error example](/documentation/features/feature-payment-validation.png "Stripe payment validation declined card error example")

  A payment submission triggers an orange loading overlay animation to display while the process is updated (this allows time for the backend checks to be run and the Stripe webhook to be updated) - either returning the user back to the form, in cases or validation error, or redirecting to a checkout success page with their new order details.

  #### Order Confirmation

  A successful order triggers that order to be saved into the database and a record is accessible for the Stripe account owner. The checkout success page then gives the user a confirmation of their order, with a success toast message confirming the order details have also been sent to the registered email address from the submitted form.

  ![checkout success page with order confirmation updates](/documentation/features/feature-checkout-success.png "checkout success page with order confirmation updates")

  #### Email Order Confirmation

  A confirmation email containing the order details seen on the checkout success page will be sent to the email address submitted in the form. An example of what this email looks like is below (generated by a temporary email, verified for an account):

  ![order email confirmation example](/documentation/features/feature-order-confirmation-email.png "order email confirmation example containing order details")

  #### Bespoke Details and Form

  Since Nyree often makes bespoke art for friends and family, we wanted to design a page that offers a particular bespoke product: "hopes / dreams / wishes".

  These consist of beautiful bespoke made mini collages that can be framed. Each collage contains words of affirmation or wishes for the recipient.

  ![bespoke collage page details](/documentation/features/feature-bespoke-collage-page.png "bespoke collage page details")

  The bespoke feature of the website gives details of this product and there is a form that can be filled in to send a bespoke enquiry to Nyree. The form is tailored with questions that help Nyree to know the style of collages to make, the size, and bearing in mind if it's for a particular occasion. Or if certain words or wishes resonant with the customer, there is an option to specify this in the custom message.

  ![bespoke enquiry form](/documentation/features/feature-bespoke-collage-form.png "bespoke enquiry form")

  This feature is still in development so there is much to be improved in future (functionality as well as styling / information included).
  Currently, the form is validated before submission so that important information is included in the enquiry:

  ![validation example on bespoke enquiry form](/documentation/features/feature-bespoke-form-validation.png "validation example on bespoke enquiry form")

  And if the form is successfully submitted, the user will be redirected to a confirmation page thanking them for their enquiry:

  ![bespoke form submission success page](/documentation/features/feature-bespoke-form-success.png "bespoke form submission success page")

  The enquiry is not currently saved into the database and therefore cannot be accessed or managed by an admin. This funtionality would be worked on further as part of [future features](#future-features).

  #### Contact Form

  The contact form works in a similar way as the bespoke form, in the way users can input details to make an enquiry or get in touch with Nyree.

  ![contact form page](/documentation/features/feature-contact-form.png "contact form page")

  Current functionality does not redirect the user to a confirmation page, but a success message will show in the top corner if a message has been successfully 'sent'. Again, in future the plan is to have the information properly submitted and saved into the database so that Nyree can access and manage these enquiries.

  ![contact form submission success message](/documentation/features/feature-contact-submit-success.png "contact form submission success message")

  #### FAQs

  The frequently asked questions page offers answers to common questions about products, delivery, returns policy etc. This gives users more support and confidence during their shopping experience. The question tabs on the accordion (from Bootstrap) are interactive and when clicked will reveal the answer below.

  ![FAQ page screenshot](/documentation/features/feature-faqs-accordion.png "FAQ page screenshot")

  This particular question is highlighted because currently there is no 'notes' section at the checkout, but this would be a useful feature for [future](#future-features).

  Since the FAQs structure has been added to [django admin](#django-admin), Nyree can update and edit the FAQ information via the admin interface.

  #### Product Management

  Admin users can also access product information via the django admin interface, but a frontend feature has been designed for improved flow and easier access.

  By signing in as a 'super-user' (admin), Nyree can edit / add / delete products via the Product Management tools.

  By clicking 'product management' in the account dropdown, this takes the admin user to the 'add product' page:

  ![add product page screenshot](/documentation/features/feature-product-management-add.png "add product page screenshot")

  The form is empty when adding a completely new product, but all field inputs match the current structure of product details on the site (e.g product category, SKU, product name, description etc).

  There is also the option to upload a product image to be displayed on the site. Since the site is linked up with image hosting via AWS, this process is dynamic and simple to use. Currently, there is no preview of the selected image which would be useful to see in the form before adding (like the view when editing a product), but functionality works well.

  Upon a successful product 'add' the admin is then taken to the product detail page of the newly uploaded product:

  ![newly added product detail](/documentation/features/feature-add-product-test.png "newly added product detail")

  If the admin is happy with the new product it is displayed in the same way as all other products, but if they wish to edit / delete, this is an option via the blue pencil (edit) and red trash can (delete) buttons next to the product rating.

  Clicking the edit button takes the admin to the 'edit product' page - a form prefilled with the product information fields which can all be adjusted and updated if necessary.

  Here is an example a print product's edit form:

  ![edit product form for a print product](/documentation/features/feature-edit-product-form.png "edit product for a print product")

  Clicking 'update product' will save the new data and the product can be viewed in the main product listings.

  This is the general view of the products seen by the admin where all products have the edit / delete buttons accessible:

  ![admin user view of all products](/documentation/features/feature-edit-delete-product-list.png "admin user view of all products")

  If the admin wishes to delete a product, this can be done via the 'delete' product button (a red trash can). Currently, there is no confirmation before delete functionality implemented so the user must be careful not to delete products by mistake! 
  
  This is definitely a priority for future work, and can be fixed by implementing a pop up modal to confirm / cancel the delete action.

  Once the admin has deleted a product, a success message will confirm this action, and the product will disappear from the site:

  ![deleted product success message](/documentation/features/feature-delete-product-test.png "deleted product success message")

  #### Django Admin

  As mentioned, the admin user has the option of managing products,orders and many other aspects to the site via django's own admin interface. The plan would be to customise all aspects of admin via a frontend interface but this is still a very useful feature with smooth operations.

  Django admin is secured by a super-user login:

  ![django login](/documentation/features/feature-django-admin-login.png "django login")

  From the django admin dashboard, the site owner / admin user can manage products, users, orders and FAQs.

  ![django dashboard - orders view](/documentation/features/feature-django-admin-orders.png "django dashboard - orders view")

  There is CRUD functionality included for the FAQs feature as seen here:

  ![django dashboard - FAQs view](/documentation/features/feature-django-admin-faqs.png "django dashboard - FAQs view")

  ![adding an FAQ via django admin](/documentation/features/feature-django-admin-faq-add.png "adding an FAQ via django admin")


### Future Features

The following features would be considered in future work to the project that would improve the useability and interest of this app:

- Add a review / product rating:
    - There are already placeholder producting ratings added to the product details, but in future this could be a full feature that allows users with an account to add their own rating for a purchased product and / leave a review.
    - Positive reviews can then be posted to the homepage to encourage more custom.

- Complete Bespoke / Contact functionality:
    - As previously mentioned, the bespoke and contact forms were built but the data is not yet stored and cannot be managed by the admin user. This would be completed in future works, so that Nyree can easily access enquiries from customers.

- Note section added to the checkout form:
    - Discussing with Nyree, she finds it useful to have a 'notes' section when a customer is completing an order in case they have any extra requirements that can be accommodated for. This would improve the shopper's experience.

- Add more customisation to the bespoke or product options:
    - Particularly with Prints, they can be available in different sizes which would allow customers to customise the artwork to their needs. This was considered at the beginning of the project, but since we would need to implement a stock management system to accommodating for sizing options, this was not included at this stage.

- Stock management system:
    - This would be very useful for the site owner to be able to adjust product options based on the amount of stock left. Products that are out of stock could still be listed to show they are popular, but cannot be purchased.

- New Collections and Limited Editions
    - Showcasing new products or limited editions would add interest for both new and returning customers, especially if they can get customised updates of what Nyree is currently working on or future products.

- General improvements to site layout and accessbility

---

## Skeleton

Wireframes for the website were created using the UI wireframe tool, [Balsamiq](https://balsamiq.com/), to plan the layout.

The layout and design were kept consistent across the pages / devices as much as possible.
The overall design evolved as the project was developed, so some of the wireframe designs were not carried out / were adapted.

The app consists of the following main pages:

- Home
- About
- FAQs
- Shop
    - All Items
    - Originals
    - Prints
    - Bespoke (enquiry page / success page)
- Contact
- Shopping Bag
- Checkout / Checkout Success
- My Account
    - Signin / Register / Logout
    - Profile
    - Order confirmation page (via Profile)

For Admin Users only:
- Product Management (via my account)
    - Add a product
    - Edit a product

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

- #E5543C
- #35CCCF
- #000000
- #343A40
- #EADECE
- #F8F9FA

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
- The project is directly connected to the deployed database on Heroku during development.

### Diagram
- The diagram (created on [DrawSQL](https://drawsql.app/)) shows a layout of the tables created by my models in the database.
- The diagram below omits the tables created by default, except the user table, as well as the tables created by [django-allauth](https://docs.allauth.org/en/latest/).

![Database Schema Diagram](/documentation/drawSQL-schema.png "database schema diagram")

## Database Models

**Please Note:** 
- Default tables created by [django](https://www.djangoproject.com/) as well as [django-allauth](hhttps://docs.allauth.org/en/latest/) have been ommited from this section. Please refer to their documentation (refrenced [here](#tools-and-technologies-used)) for more information on their data models.
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