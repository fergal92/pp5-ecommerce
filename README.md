# Doggo Down Under

Doggo Down under is a website selling dog products in Australia. It allwos users to purchase a wide range of dog products. Users can search for products via name, category and product description, users can filter based on price and rating. User experience and mobile development is at the heart of Doggo Down Under and users who want to purcahse dog products will have a great experience using this website.


![Doggo Down Under](static/images/readme/homepage-laptop.png)

The live site is available here: [Doggo Down Under](https://doggo-down-under-1b9b3087502e.herokuapp.com/).

## Table of Contents
- [Features](#features)
- [Agile Methodology](#agile-methodology)
- [Design](#design)
- [SEO and Marketing](#seo-and-marketing)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)


## Features
### General

This section discusses the more generic features available throughout the site for all users of the website.

#### Navigation Bar
<details>
<summary>Navigation Bar</summary>

![Navbar](static/images/readme/navbar-laptop.png)
![Navbar](static/images/readme/navbar-mobile.png)
</details>

The navigation bar is featured across all pages. The navbar is a slightly modified version of the first example from [Bootstrap's navbar documentation](https://getbootstrap.com/docs/5.2/components/navbar/). It includes drop down menus for "All Products", "Clothing" and "Accessories", a drop down menu for logging in/registering or for accessing logged in user functionality like "My Profile", "Product Management" and "My Wishlist", a link to "Home" and a cart icon. It also features the website's logo and a search bar.

The logo in the navbar is visible on all larger screens and links to the home page as user's expect so that it is quick and easy to return to the index from any page on the site.

The search bar is featured in the navbar to make it accessible from any page on the site so that a user can quickly search for a product whenever they want, however it is only immediately visible on larger screens. On smaller screens it is available in the collapsible menu through the navbar toggle to reduce clutter on the screen.

#### Footer
<details>
<summary>Footer</summary>

![Footer](static/images/readme/footer.png)
</details>

The footer is featured across all pages on the website. It includes two simple sections related to customer communication, offering ways for the customer to communicate with the business.


The first section includes the newsletter subscription form. It's a very simple form that only requests the user's email address to sign up.

The third section features social media links for the user to find the business on Facebook.

It also includes a link to a popular dog charity in AUstralia for further reading for users


#### Index Page
<details>
<summary>Index Page</summary>

![Index](static/images/readme/homepage-laptop.png)
</details>

The index or home page appears the same for all users. It features a hero image of a cute dog with a jumper on, visible to the user immediately upon landing on home page. The carousel currently includes three images. There is a call to action on the hero image to entice the user to browse the shop collection.

Overall, the index page is intended to be engaging, informative without overwhelming the customer, and to encourage the user to explore the website further.

### Products

This section discusses the features related to the products app. 

#### Search Products
<details>
<summary>Search Products</summary>

![Search Products](static/images/readme/navbar-laptop.png)
</details>

The search form in the navbar has basic search functionality. It searches for matches in the product names and description and returns the results displayed as product cards. At the top of the page it informs the user of the number of products found that match the query and includes the query in the result so the user can be sure of what they searched.


#### Categories
<details>
<summary>Categories</summary>

![Categories](static/images/readme/navbar-laptop.png)
</details>

The category pages are featured on the "Shop" drop down menu on the navbar. There is a link for each category - Sweaters, Raincoats, Bowls, Toiletries, Kits, Food, Toys. There is a link for all clothing and all accessories too

There is a single, simple category template that is used for every category page so that all of these pages have the same layout and are easy to understand for the user. The layout is very simple, the products are displayed in "Product Cards".

There is a simple filter functionality on the category pages which filters the page by subcategory. Almost all products fall within one of "Mild", "Medium", "Hot", and "Mega Hot" subcategories which the user can filter by selecting the subcategory from the drop down menu and clicking "Go".


#### Product Detail Page
<details>
<summary>Product Page</summary>

![Product Page](static/images/readme/product-detail-page.png)
</details>

The product detail page has two main sections, the second of which is the product reviews and is discussed in more detail later on in the "Reviews" features.

The first section on this page features all of the products details. The template used for this page is used for all products so that all product detail pages have a similar layout. Similarly, one product model is used for all products with the choice of fields used depending on the type of product.

A pcture of the product is displayed along with the product, name, price, category, rating, description, quantity selectyor, option to add to bag, option to keep shopping, option to add to wishlist, and a reviews section. The review form is only avalible to users who have previously purchased the product. Any reviews already written can be read at the bottom of this page.


### Shopping bag

This section discusses the features associated with the bag app and the functionality involved with managing the user's shopping bag.

<details>
<summary>Shopping bag</summary>

![Product Added](static/images/readme/shopping-bag-page.png)
</details>

The shopping bag allows the user to add products from the products pages into the shopping bag. Once in the bag the user can then proceed to checkout from there and purchase the products. The bag features a product image, name, SKU, price, quanity selector and the subtotal of all the items in the bag. The delivery cost is also displayed. There are two buttons to allow the user to continue shopping or to checkout. Products can be removed from the bag as well as increasing or decreasing the number in the bag.


### Purchasing

This section discusses the features related to the checkout app and the functionality involved with user purchases on the site.

#### Checkout
<details>
<summary>Checkout</summary>

![Checkout](static/images/readme/checkout-page.png)
</details>

To reach the checkout page, the user can click on the link in the cart offcanvas element or on the "Checkout" button below the summary table on the cart page.

The checkout page has two sections. To the right or on top, depending on the size of the user's device, is the summary of the order. Similarly to the cart page, this summary is a simple table listing the most relevant details of the items in the order. It includes small thumbnails of the items as well as the name just to be clear to the user what they are purchasing. Below this is the delivery cost and grand total.

On the left of or below the order summary, is the form for delivery details. It appears slightly differently depending on whether the user is logged in or not, and whether their details are already saved. For a guest user the form will appear blank. If the user is logged in but has not saved their details previously, the email field will be prepopulated and at the bottom of the form is an option to save their details to their profile.

Directly below the delivery details is the [Stripe](https://stripe.com) card element where the user inputs their card details to complete the order. Before the submit button, there is a warning to the user stating how much money their card is about to be charged.

For the delivery form and Stripe elements, the code is based on Code Institute's [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) project.


### User Authentication and Profiles

This section discusses features related to the user authentication, and user profiles.

#### Registration
<details>
<summary>Register</summary>

![Register](static/images/readme/profile-page.png)
</details>

[Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for user authentication for this website and so functionality for registration and authentication is handled by allauth. The templates used for registration, login/logout, and email confirmation are allauth templates which have been styled to match the rest of the website.

Registration is accessed through the "Register" link under the "Account" drop down menu and is unnecessary for most functionality on the website. A user can complete a purchase and generate a successful order without registering.

The login page is accessed through a "Login" link under the "Account" drop down menu and the template is standard from allauth and accepts either the user's username or email and their password as valid credentials to login. 

When a user is logged in, the log out page is accessed through a "Logout" link under the "Account" drop down menu. Again, this is a standard allauth template styled to match the rest of the website.


#### User Profile
<details>
<summary>User Profile</summary>

![Profile](static/images/readme/profile-page.png)
</details>

User profiles are created automatically when a user registers with the website, as based off of the code from Code Institute's [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) project. When a user logs in, they are redirected to their profile.

The main page of the user profile includes a section for the user's details and a table of their order history. Above the user's details, there are options available for the user to edit their profile details and to delete their account.

The order history table summarises their orders with their order number, the date it was placed, the total and a link to the checkout success page for that order so that they can review it in more detail there.


#### Product Reviews
<details>
<summary>Product Reviews</summary>

![No Reviews](static/images/readme/review-form.png)
</details>

Once a user has purchased a product and it is in their order history they are able to see a review form on the product detail page. They can write a text review and submit it. Once a user has left a review they cannot leave another review. All website users can read any review on the product detail page. 


### Management

Superusers can access a product management feature through the nav bar. This allows super users to add new products including images without having to use the admin panel. Super users can also edit and delete current products from the product card. 

#### Products
<details>
<summary>Management Products</summary>

![Management Products](static/images/readme/product-management-page.png)
</details>

### Admin

Most of the functionality available on the main website to staff users is also available through the admin panel. Most models are registered to allow admin users to perform CRUD functionality through the admin panel.


### Future Features

1. __Order Again__:
  - For registered users you could offer an "Order Again" button for items in their order history. This could be as simple as clicking the button and adding the item to their cart like on a product page, with the function only having to check whether it is in stock or not.
2. __Improved Category Filtering__: 
  - Expanding category filtering beyond subcategory could include filtering by average user rating or popularity, if we were to expand the product model to track the number sold.
3. __Dog Care Blog__:
  - As part of marketing and providing content to users, a dog care blog may could expand the site further beyond products, giving users another reason to return to the site between purchases.
4. __Expanded Product Range__:
  - Providing products beyond dog items. Expanding the range to include items related to other animals could draw more users, and repeat users. This may require altering the current product models. 


## Agile Methodology
### Epics, User Stories

The project board can be found [here](https://github.com/users/fergal92/projects/6).

Below are the Epics and their User Stories used to shape the creation of the project. Each are linked to their respective version on the project board, where the acceptance criteria, MoSCoW prioritisation labelling and comments can be found.

#### [Navigation](https://github.com/SJECollins/ci-pp5-the-chillibox/milestone/1):
  - Site users should be able to navigate through the site intuitively using the navigation bar and clearly marked links so that they can find the products that they are looking for.
  - User Stories:
    - 1: [View Latest Products](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/2)
      - As a site user I can navigate to latest products so that I can view the most recent products added to the site
    - 2: [Products By Category](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/3)
      - As a site user I can navigate to products by category so that I can view all products available in that category
    - 3: [Product Page](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/4)
      - As a site user I can view an individual product's page so that I can see the product's details and have the option to add to my cart
    - 4: [Search Products](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/5)
      - As a site user I can enter a search term so that I can find products that I am interested in
    - 5: [Sort Category](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/6)
      - As a site user I can sort categories so that I can view products in a category by other criteria


#### [Cart](https://github.com/SJECollins/ci-pp5-the-chillibox/milestone/2)
  - Site users should be able to add products in various quantities to their cart. They should be able to view items in the cart, adjust the quantities and remove items from the cart
  - User Stories:
    - 6: [Add To Cart](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/7)
      - As a site user I can click "add to cart" so that I can add a product to my cart
    - 7: [Adjust Quantity](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/8)
      - As a site user I can adjust quantities of products in my cart so that I can change the quantity of the product that I wish to purchase
    - 8: [Remove From Cart](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/9)
       - As a site user I can click "remove" on a product in my cart so that the product is removed from my cart
    - 9: [Product Options](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/10)
      - As a site user I can clear my cart so that all items are removed from the cart
    - 10: [Clear Cart](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/11)
      - As a site user I can choose an option/variant of a product so that option is added to my cart
    - 11: [Already In Cart](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/12)
      - As a site user I can see on a product's page if the product is already in my cart so that I know if I have already added the product to my cart without having to go through the cart itself


#### [User Registration](https://github.com/SJECollins/ci-pp5-the-chillibox/milestone/3):
  - Site users are able to register with the site and create a profile that saves their contact and delivery information. The user should be able to update the information in their profile. The user should be able to view their previous orders from their profile
  - User Stories:
    - 12: [Registration](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/13)
      - As a site user I can register with the site so that I can create a user profile with the site
    - 13: [Login](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/14)
       - As a site user I can login if I am registered so that I can use features available for registered users, e.g. view and edit profile
    - 14: [Logout](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/15)
      - As a site user I can logout so that I can logout from the site
    - 15: [Update Profile](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/16)
      - As a site user I can edit my profile so that I can update my personal details
    - 16: [Delete Profile](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/17)
      - As a site user I can delete my profile so that my personal details are removed from the site
    - 17: [Order History](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/18)
      - As a site user I can view my order history so that I can review previous purchases
    - 18: [Order Again](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/19)
      - As a site user I can click "order again" on an item from my order histroy so that I can easily order items I have ordered previously.


#### [Checkout](https://github.com/SJECollins/ci-pp5-the-chillibox/milestone/4)
  - User should be able to checkout using their card and provided delivery details. A user should receive confirmation and an order should be generated, and added to their order history if registered.
  - User Stories:
    - 19: [Checkout](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/20)
      - As a site user I can go to checkout so that I can complete my purchase
    - 20: [Review Order](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/21)
      - As a site user I can review my order prior to checkout so that I can be confident I am ordering the items I actually want
    - 21: [Delivery Details](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/22)
      - As a site user I can enter/update my delivery details prior to checkout so that I can provide the correct delivery and contact information
    - 22: [Checkout With Card](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/23)
      - As a site user I can enter my card details on the site so that I can chekcout using my card
    - 23: [Order Summary](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/24)
      - As a site user I can view an order summary so that I can review my order after it is placed


#### [Reviews](https://github.com/SJECollins/ci-pp5-the-chillibox/milestone/5)
  - Users should be able to review and rate products on the website. The reviews and ratings should be displayed on the product page. Registered users who publish reviews while logged in should be able to view, edit and delete their reviews.
  - User Stories:
    - 24: [Create Review](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/25)
      - As a site user I can create a review on a product page so that I can provide feedback on the product
    - 25: [View Reviews](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/26)
      - As a site user I can view reviews on a product so that I can see other users feedback
    - 26: [View Own Reviews](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/27)
      - As a registered site user I can view the reviews I have written in my profile so that I can easily access the reviews I've written
    - 27: [Edit Review](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/28)
      - As a registered site user I can edit a review I have written so that I can update a review
    - 28: [Delete Review](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/29)
      - As a registered site user I can delete my review so that my review is removed from the site


#### [Management Dashboard](https://github.com/SJECollins/ci-pp5-the-chillibox/milestone/6):
  - The site should contain a dashboard for staff to manage products without requiring staff to login to Django's admin dashboard. There should be limited functionality to allow staff to add, edit and delete products from this view, as well as manage stock.
  - User Stories:
    - 29: [View Management Dashboard](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/30)
      - As an admin user I can access a dashboard through the navbar so that I can access product management features without having to login in to Django's admin
    - 30: [View Products](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/31)
      - As an admin user I can view a table of the products available on the site so that I can review the available products and access management features for them
    - 31: [Add Product](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/32)
      - As an admin user I can access a form to add a new product from the management dashboard so that I can add new products to the site
    - 32: [Edit Product](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/33)
      - As an admin user I can edit existing products from the management dashboard so that I can update/change existing products
    - 33: [Delete Product](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/34)
      - As an admin user I can delete a product so that I can remove the product from the site
    - 34: [Update Stock](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/35)
      - As an admin user I can update stock from the management dashboard so that the stock of available products is changed on the site


#### [Home](https://github.com/SJECollins/ci-pp5-the-chillibox/milestone/7):
  - The home app provides users with vasic views for the site such as the index and contact pages, to introduce the user to the site and products, and provide contact information
  - User Stories:
    - 35: [View Index](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/36)
      - As a site user I can view the index page so that I can learn about and understand the site
    - 36: [View Contact Page](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/37)
      - As a site user I can navigate to the contact page so that I can access the contact details for the business
    - 37: [Location Details](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/38)
      - As a site user I can see an address and map on the contact page so that I can find the location of the business if required
    - 38: [Contact Form](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/39)
      - As a site user I can use a contact form on the contact page so that I can contact the business easily


#### [Recipes](https://github.com/SJECollins/ci-pp5-the-chillibox/milestone/8):
  - The site should contain a recipe section with recipes created by the site admin/staff for users to browse. Users should be able to comment on the recipes. Users may be able to submit recipes in some form, but not directly post recipes to the website as they should be curated by the admin.
  - User Stories:
    - 39: [Create Recipe](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/40)
      - As an admin user I can create recipes so that I can publish them on the website for users to read
    - 40: [Edit Recipe](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/41)
      - As an admin user I can edit recipes so that I can change existing recipes on the website
    - 41: [Delete Recipe](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/42)
      - As an admin user I can delete recies so that they are removed from the website
    - 42: [View Recipes](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/43)
      - As a site user I can navigate to the recipes section so that I can view the recipes available on the site
    - 43: [Add Comment](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/44)
      - As a site user I can add a comment so that I can comment on recipes on the website
    - 44: [Edit Comment](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/45)
      - As a site user I can edit comments so that I can update my comments if necessary
    - 45: [Delete Comment](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/46)
      - As a site user I can delete comments so that I can remove my comments from a recipe
    - 46: [Submit Recipe](https://github.com/SJECollins/ci-pp5-the-chillibox/issues/47)
      - As a site user I can submit recipes so that my recipes can be posted on the website


## Design

### Colour

The colour palette used for the website based on the classic look of other ecommerce stores like Amazon. Black and white are the primary colours and afford good contrast. The hero picture is a striking yellow background which provides great contrast against the rest of the site. The site is simple and elegant in colour design.

### Mockups

I had previously created a website with the idea of dropshipping dog colthes. The website was created through wordpress and some of the original feautures of that website are present in this site such as the favicons.

### Wireframes

Wireframes were created in ascii style.

<details>
<summary>Index</summary>

+-----------------------------------------------------------------------+
| 🐾 Doggo Down Under          Home | Products | Wishlist | Bag 🛒 🔍   |
+-----------------------------------------------------------------------+
|                               HERO IMAGE                              |
|                     "Premium Aussie Dog Products!"                    |
|                            [SHOP NOW BUTTON]                          |
+-----------------------------------------------------------------------+
| [Product Card 1]    [Product Card 2]    [Product Card 3]    [Product 4]  
|   Image               Image               Image               Image     
|   Name ($20)          Name ($30)          Name ($25)          Name ($40) 
+-----------------------------------------------------------------------+
| About Us | Contact | Privacy Policy | 📧 Newsletter: [Email] [Sign Up] |
| [FB] [IG] [TikTok]                                                    |
+-----------------------------------------------------------------------+

+-----------------------------+
| [☰] Doggo 🐾 [🔍]           |
+-----------------------------+
|         HERO IMAGE          |
| "Shop Aussie Dog Gear!"     |
|      [SHOP NOW BUTTON]      |
+-----------------------------+
| [Product Card 1]            |
| Image + Name + Price        |
| [Product Card 2]            |
| ... (Single Column)         |
+-----------------------------+
| About Us | Contact          |
| [FB] [IG] [TikTok]          |
| Newsletter: [Email] [Sign Up]
+-----------------------------+


</details>

<details>
<summary>Wishlist</summary>

+-----------------------------------------------------------------------+
| 🐾 Doggo Down Under          Home | Products | Wishlist ❤️ | Bag 🛒 🔍|
+-----------------------------------------------------------------------+
| WISHLIST ITEMS:                                                      |
| [Thumbnail] Chew Toy       | $15       | [Move to Bag] [🗑️ Remove]   |
| [Thumbnail] Dog Bed        | $50       | [Move to Bag] [🗑️ Remove]   |
+-----------------------------------------------------------------------+
| About Us | Contact | Privacy Policy | [Social Icons]                 |
+-----------------------------------------------------------------------+

+-----------------------------+
| [☰] Doggo 🐾 ❤️ [🔍]        |
+-----------------------------+
| Chew Toy | $15 [Move to Bag]|
| Dog Bed  | $50 [Move to Bag]|
+-----------------------------+
| About Us | Contact          |
+-----------------------------+
</details>

<details>
<summary>Products</summary>

+-----------------------------------------------------------------------+
| 🐾 Doggo Down Under          Home | Products | Wishlist | Bag 🛒 🔍   |
+-----------------------------------------------------------------------+
| Filters: Categories ▼ | Price ▼ | Sort: Relevance ▼                   |
+-----------------------------------------------------------------------+
| [Product Card] [Product Card] [Product Card] [Product Card] ...       |
| Image + Name + Price + [Add to Bag]                                   |
| ... (Repeat grid)                                                     |
+-----------------------------------------------------------------------+
| About Us | Contact | Privacy Policy | [Social Icons]                  |
+-----------------------------------------------------------------------+

+-----------------------------+
| [☰] Doggo 🐾 [🔍]           |
+-----------------------------+
| Filters: [Dropdown Menu]    |
+-----------------------------+
| [Product Card 1]            |
| Image + Name + Price        |
| [Product Card 2]            |
| ... (Single Column)         |
+-----------------------------+
| About Us | Contact          |
+-----------------------------+

</details>

<details>
<summary>Product Detail</summary>

+-----------------------------------------------------------------------+
| 🐾 Doggo Down Under          Home | Products | Wishlist | Bag 🛒 🔍   |
+-----------------------------------------------------------------------+
| [Large Product Image]          Product Name: Chew Toy                 |
|                                 Price: $15                            |
|                                 Size: [Dropdown]                      |
|                                 Color: [Dropdown]                     |
|                                 [Add to Bag] [❤️ Wishlist]            |
|                                 Description: Durable rubber...        |
+-----------------------------------------------------------------------+
| About Us | Contact | Privacy Policy | [Social Icons]                  |
+-----------------------------------------------------------------------+

+-----------------------------+
| [☰] Doggo 🐾 [🔍]           |
+-----------------------------+
| [Product Image]             |
| Name: Chew Toy ($15)        |
| Size: [Dropdown]            |
| [Add to Bag] [❤️]           |
| Description: Durable...     |
+-----------------------------+
| About Us | Contact          |
+-----------------------------+

</details>

<details>
<summary>Shopping bag</summary>

+-----------------------------------------------------------------------+
| 🐾 Doggo Down Under          Home | Products | Wishlist | Bag 🛒 🔍   |
+-----------------------------------------------------------------------+
| ITEMS IN BAG:                                                        |
| [Thumbnail] Chew Toy       | Qty: [2] | $30       | [🗑️ Remove]      |
| [Thumbnail] Dog Bed        | Qty: [1] | $50       | [🗑️ Remove]      |
+-----------------------------------------------------------------------+
| ORDER SUMMARY:                                                       |
| Subtotal: $80                                                        |
| Shipping: $10                                                        |
| Total: $90                                                           |
| [Checkout Button]                                                    |
+-----------------------------------------------------------------------+
| About Us | Contact | Privacy Policy | [Social Icons]                  |
+-----------------------------------------------------------------------+

+-----------------------------+
| [☰] Doggo 🐾 [🔍]           |
+-----------------------------+
| Chew Toy x2 | $30 [🗑️]     |
| Dog Bed x1  | $50 [🗑️]     |
+-----------------------------+
| Subtotal: $80              |
| Shipping: $10              |
| Total: $90                 |
| [Checkout Button]          |
+-----------------------------+
</details>

<details>
<summary>Checkout</summary>

+-----------------------------------------------------------------------+
| 🐾 Doggo Down Under          Home | Products | Wishlist | Bag 🛒 🔍   |
+-----------------------------------------------------------------------+
| SHIPPING ADDRESS:                                                    |
| Full Name: [__________]                                              |
| Address: [__________]                                                |
| City: [__________]                                                   |
| Payment: [Card Number] [Expiry] [CVC]                                |
+-----------------------------------------------------------------------+
| ORDER SUMMARY:                                                       |
| Chew Toy x2: $30                                                     |
| Dog Bed x1: $50                                                      |
| Subtotal: $80 | Shipping: $10 | Total: $90                           |
| [Place Order Button]                                                 |
+-----------------------------------------------------------------------+

+-----------------------------+
| [☰] Doggo 🐾 [🔍]           |
+-----------------------------+
| Full Name: [__________]     |
| Address: [__________]       |
| Card: [__________]          |
+-----------------------------+
| Items: $80 | Total: $90     |
| [Place Order]               |
+-----------------------------+
</details>

### Entity Relationship Diagrams

<details>
<summary>ERD</summary>

![ERD](static/images/readme/erd.png)
</details>


## SEO and Marketing

A link to a popular dog charity was added in the footer to increase SEO for the website. 

### SEO, Keywords

The final keywords used on the website were dog, pet, store, online, shop, toys, food, accessories.


### Marketing
Based on Code Institute's Web Marketing, questions were collected to try to decide on marketing for the website.

- What kind of business is it?
  - B2C
- Who are your customers?
  - Customers looking for quality dog products in Australia
- Which online platforms would you find lots of your users?
  - Facebook
- What do your users need? How could you deliver useful content to them?
  - Dog products. Content could be delivered in cute dog vidoes
- Would your business run sales or offer discounts? How do you think your users would most like to hear about these offers?
  - Sales and discounts could be offered. Either through posting alerts for sales on social media or sending discount codes to people on the newsletter.
- Would your business have a budget to spend on advertising? Or would it need to work with free or low cost options to market itself?
  - Possibly a small budget. Perhaps it would start with low cost options like social media and newsletters.

The e-commerce businesses that inspired aspects of this website include:
  - [Petworld](https://www.petworld.ie/)
  - [Petstop](https://www.petstop.ie/)



### Social Media
<details>
<summary>Facebook Mockup</summary>

![Facebook](static/images/readme/fb-page-doggo-down-under.png)
</details>

A Facebook business page was created for the website. Above is the screenshot of the page. This would be the primary social media site for the business to communicate with customers. Link to [Facebook page here](https://www.facebook.com/profile.php?id=61572882855702)




### Email

Through a subscription form in the footer, the website saves email addresses and allows the website owner to collect email addresses to send out a newsletter. The intention with the newsletter would be to update customers when new products are added to the site, or to send discount codes to newsletter subscribers which is a common practice.


## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5): mark-up language.
- [CSS3](https://en.wikipedia.org/wiki/CSS): styling.
- [JavaScript](https://www.javascript.com/): programming language.
- [Python 3](https://www.python.org/): programming language.
- [Django 3.2](https://www.djangoproject.com/)
  - [Django allath](https://django-allauth.readthedocs.io/en/latest/index.html): user authentication.
  - [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/): for forms.
  - [Django countries](https://pypi.org/project/django-countries/): for countries in forms.
  - [Crispy Bootstrap5](https://pypi.org/project/crispy-bootstrap5/): bootstrap5 template pack for crispy forms.
- [Stripe](https://stripe.com): payments.
- [JQuery](https://jquery.com/): UI.
- [HTMX](https://htmx.org/): UI.
- [Bootstrap](https://getbootstrap.com/): styling.
- [Cloudinary](https://cloudinary.com/): store static and media files.
- [GIT](https://git-scm.com/): for version control.
- [GitHub](https://github.com/): for host repository.
- [VSCode](https://code.visualstudio.com/): online IDE.
- [Heroku](https://)
- [Google Fonts](https://fonts.google.com/): to import fonts.
- [Font Awesome](https://fontawesome.com/): to import icons.
- [Balsamiq](https://balsamiq.com/): to create wireframes.
- [Diagrams.net](https://www.diagrams.net/): for Entity Relationship Diagram.
- [GIMP](https://www.gimp.org/): to edit images and create colour palette.


## Testing

Testing for the site can be found at the below link:
[Link to TESTING.md](TESTING.md)


## Deployment

Detailed deployment steps can be found at the below link:
[Link to DEPLOYMENT.md](DEPLOYMENT.md)

### Steps to clone site:
- In the GitHub repository, click the "Code" button.
- Select "HTTPS" and copy the URL.
- Open Git Bash and navigate to the repository where you would like to locate the cloned repository.
- Type "git clone" followed by the copied URL.
- Press enter to create the clone.
- Install required packages with the command "pip3 install -r requirements.txt"


## Credits
### Code
- The code for the website was heavily based on the code for Boutique Ado by [Code Institute](https://codeinstitute.net/ie/). All credit goes to code institute and the lecturer who gave the pp5 module for the majority of the code base has came from there.


### Media
- Favicons created with [Favicon Generator](https://favicon.io/)
- Icons are from [Font Awesome](https://fontawesome.com)
- The fonts are imported from [Google Fonts](https://fonts.google.com)
- Product images from the internet and from photos I took myslef


### Acknowledgement
- Iuliia Konovalova - My mentor Julia was very supportive during this project. She certainly pushed me to complete a high standard of project especially for the readme and testing sections. I took inspiration from her README.md and TESTING.md files for my own.
- Happiness Generator - My first hackathon project. I learned so much from participating in this project and team. We won the March hackathon for 2024 and my team members were a great source of inspiration for me.
- freeCodeCamp - I completed the freeCodeCamp responsive web design module before enrolling in code institute and I learned much from that module that I was able to utilise for this project.
- CodeInstitute - The learning material produced by code institute has been very high quality and I have learned a lot from it. 
Boutique Ado - The Boutique Ado app has heavily influnced this project. As it was only the second django project I had seen before and with the complexity of producing a django project for the second time I had to heavily lean on the existing project. A lot of the Doggo Down Under website is taken from the boutique Ado project but I have made enough changes to it to create a unique standalone project.