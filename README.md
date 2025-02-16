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

![Index](readme-docs/screens/index.webp)
</details>

The index or home page appears the same for all users. It features a carousel at the top of the page, visible to the user immediately upon landing on home page. The carousel currently includes three images. The first is a simple hero image with the business's name. The second is an image that advertises the hot sauce products with a link to the page. And the third is an image advertising the chilli plant seeds with a link to that page. Immediately below the carousel is the website's welcome message for the user.

The next section of the site includes text that briefly introduces the products available to the user on the website. Each short paragraph includes an inline link to the category it is referencing. 

And finally, at the bottom of the index page is a section for the "Newest Products" on the website. This section features four of the products most recently added to the website. They are displayed in "cards" with a thumbnail of the product, a short excerpt of the product's description, its stock status and the product's name as a link to its page.

Overall, the index page is intended to be engaging, informative without overwhelming the customer, and to encourage the user to explore the website further.



### Products

This section discusses the features related to the products app. 

#### Product Card
<details>
<summary>Product Card</summary>

![Product Card](readme-docs/screens/product_card.webp)
</details>

A feature used in "Newest Products", "Latest Products" and on the category pages, a product "card" has a box shadow to contain and highlight the individual product. The card features a simple summary of the products details: the name, a thumbnail image, a short excerpt of the product description, the product's stock status and a link to go to the product page. 

The intention behind displaying products like this in the sections mentioned above was partly inspired by the [Bootstrap Card](https://getbootstrap.com/docs/5.0/components/card/) element and to limit the information provided for products outside of the product detail page. Only the most essential information needs to be available. The name is obviously important, especialy if it is what the user is searching for. The image is present to draw the user in visually and the excerpt to try to catch the user's attention. The stock information is obviously important as you don't want the user to go to the product page only to find it out of stock, which would be frustrating. And then, of course, the link so the user can access the product page.

Some consideration was put into a "Quick Add" feature for users on the card, but as most products have different variants it was decided to forgo that feature currently.


#### Newest Products
<details>
<summary>Newest Products</summary>

![Newest Products](readme-docs/screens/newest_products.webp)
</details>

The most immediate area of the website related to products is the "Newest Products" section on the index page. As described in the "Index Page" feature description above, it displays four of the products most recently added to the website. Its intention is to highlight recently added products, to push them to the front of customers' minds. Users may come to the site with a particular products in mind, but hopefully by advertising newer products on the home page it will encourage users to look at these products as well. For regular users who may be visiting the site for reasons other than an immediate purchase (e.g. browsing, reading recipes) the hope is that they would take a quick look at the "Newest Products" when they visit and find something new they are interested in.

The products are displayed in "Product Cards" which are discussed in the section of the same name above.

#### Search Products
<details>
<summary>Search Products</summary>

![Search Products](readme-docs/screens/search.webp)
</details>

The search form in the navbar has basic search functionality. It searches for matches in the product names and description and returns the results displayed as product cards. At the top of the page it informs the user of the number of products found that match the query and includes the query in the result so the user can be sure of what they searched.


#### Latest Products
<details>
<summary>Latest Products</summary>

![Latest Products](readme-docs/screens/latest_products.webp)
</details>

Similar to the "Newest Products" section of the index page, the first link under "Shop" is "Latest Products". And like the "Newest Products", this page displays four of the most recently added products, but in each category so a broader range of products may be featured. Again, the intention is to highlight recently added products to give them a boost. While it would be possible to filter individual category pages to display by recently added, and may be necessary in the future if the number of categories were to grow, the latest product page allows the user to simply click a link and view recently added products in all categories on one page. 

The products are displayed in "Product Cards" which are discussed in the section of the same name above.


#### Categories
<details>
<summary>Categories</summary>

![Categories](readme-docs/screens/category.webp)
</details>

The category pages are featured on the "Shop" drop down menu on the navbar. There is a link for each category - "Seeds", "Sauces", "Seedboxes" and "Sauceboxes". 

There is a single, simple category template that is used for every category page so that all of these pages have the same layout and are easy to understand for the user. The layout is very simple, the products are displayed in "Product Cards" as described in the section of the same name above, in rows of up to four on larger screens.

There is a simple filter functionality on the category pages which filters the page by subcategory. Almost all products fall within one of "Mild", "Medium", "Hot", and "Mega Hot" subcategories which the user can filter by selecting the subcategory from the drop down menu and clicking "Go".


#### Product Detail Page
<details>
<summary>Product Page</summary>

![Product Page](readme-docs/screens/product_page.webp)
</details>

The product detail page has two main sections, the second of which is the product reviews and is discussed in more detail later on in the "Reviews" features.

The first section on this page features all of the products details. The template used for this page is used for all products so that all product detail pages have a similar layout. Similarly, one product model is used for all products with the choice of fields used depending on the type of product. For example, a basic seed product does not require the "ingredients" field to be filled out and, likewise, a hot sauce does not need "growth time". So, the template uses multiple if statements within tables to display a very similar layout for all products to keep a uniform look to the website.

The first part of the product detail page is the section including the product name, the product image and the product description. Then we have the product's details in a table, which includes different information depending on which type of product the user is viewing. This table may include: the product category, heat level, growth time, ingredients, box contents, box in which the product appears, and rating. These details are dependent on factors such as the type of product, whether it has been reviewed, and whether the staff member who entered the product remembered to fill in the field.

The final part of this section of the product detail page is the "Add To Cart" form, which will be discussed in more detail in "Product Variants" and "Cart" features below. Briefly, it allows the user to select which variant of the product they wish to purchase, the quantity, and to add it to their card.


#### Product Variants
<details>
<summary>Variants</summary>

![Variants](readme-docs/screens/variants.webp)
</details>

The product's variants are displayed twice on the product detail page. First in the product details table with the heading "Options" and then in the "Select Option" drop down menu in the "Add To Cart" form element. 

The variant model is related to the product model in a one-to-many relationship where each product can have multiple variants for the user to choose from. Where the product model holds the basic information for each product on the site, the related variant model allows for management of options, prices and stock for products. 

When a user selects a variant in the "Add To Cart" form element, the current stock of that variant of the product is then displayed for the user.


#### Box Contents
<details>
<summary>Box Contents</summary>

![Box Contents](readme-docs/screens/box_contents.webp)
</details>

"Box contents" is a field in the product model which is used for seedboxes and sauceboxes. It is a many-to-many field related to "self", meaning the product model itself, so that a seedbox contains many seed products, for exmaple.

On a box product page, the products included are shown in the product detail table with the heading "Contents". These are the products the user will receive if they order the box. And then the variants of this box products manages the sizes of the included products and the price of the box, like other products.

If a product is included in a box, when you visit that product's page you will see a line in the table called "Find in" which indicates which box that product is included in. An example of this can be seen in the image above in "Product Variants".


### Cart

This section discusses the features associated with the cart app and the functionality involved with managing the user's cart.

#### Add To Cart
<details>
<summary>Product Added</summary>

![Product Added](readme-docs/screens/product_added.webp)
</details>

The "Add To Cart" functionality of the product detail page is one of the most important features of the website, as expected of an e-commerce site. As previously mentioned in the section about "Product Variants", the form element for adding a product to the cart is dependent on the user selecting a variant of the product.

Prior to selecting an option, the "Add To Cart" button is disabled to prevent the user from submitting the form erroneously. This is controlled through a simple event listener in the javascript calling a function that enables/disables the button depending on whether the user has selected the "Select an option" option in the drop down menu. When the user selects a product variant to add to the cart, the button is then activated and the user is able to add the variant they selected to their cart, depending on availability.
```
    const addBtn = document.getElementById("add")  # Where "add" is the button id
    function updateStock() {
        currentStock = stock.textContent
        if (currentStock == "") {
            addBtn.disabled = true
            warning.style.display = "none"
        } else if (currentStock <= 0) {
            quantity.textContent = 0
            warning.style.display = "block"
            addBtn.disabled = true
        } else {
            quantity.textContent = 1
            warning.style.display = "none"
            addBtn.disabled = false
        }        
    }
```
Also, when the user selects a variant in that drop down menu, the "Stock" field in the form element is then filled with the current stock of that variant of the product. The quantity of that variant that the user is able to add to their cart is dependent on the stock available, which is plainly visible to the user. 
<details>
<summary>Add Max To cart</summary>

![Add Max](readme-docs/screens/not_available.webp)
</details>

When a variant is initially in stock and the user then goes to add the maximum available to their cart, the quantity buttons disable when they reach the limit (there is also functionality in place to prevent the user selecting a quantity below 0). At the same time, a message is displayed below the quantity field to alert the user in case they do not realise they have reached the limit and that there are no more available.

<details>
<summary>Not Available</summary>

![Not Available](readme-docs/screens/unavailable.webp)
</details>

If a user selects away from this option after adding to cart and then selects it again or comes across a variant on another product that is not in stock, when they select that variant the stock field displays "0", the select quantity field displays "0", they are unable to change the quantity, the "No more available" message is displayed and the "Add To Cart" functionality is disabled.

The ability to alter functionality of the "Add To Cart" form element based on user selections in vanilla JavaScript is achieved through the use of a MutationObserver as based on code from [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver)
```
    const config = { childList: true }
    const callback = (mutationList, observer) => {
        for (const mutation of mutationList) {
            if (mutation.type === 'childList') {
                updateStock()
                } else {
                console.log(mutation.type)
            }
        }
    }
    const observer = new MutationObserver(callback)
    observer.observe(stock, config)
```
Stock has been mentioned quite a bit in this section, but for brevity will be discussed later in the "Stock" section of the "Management" features.


### Purchasing

This section discusses the features related to the checkout app and the functionality involved with user purchases on the site.

#### Checkout
<details>
<summary>Checkout Empty Form</summary>

![Checkout](readme-docs/screens/checkout_empty.webp)
</details>

To reach the checkout page, the user can click on the link in the cart offcanvas element or on the "Checkout" button below the summary table on the cart page.

The checkout page has two sections. To the left or on top, depending on the size of the user's device, is the summary of the order. Similarly to the cart page, this summary is a simple table listing the most relevant details of the items in the order. It includes small thumbnails of the items as well as the name just to be clear to the user what they are purchasing. Below this is the delivery cost and grand total.

On the right of or below the order summary, is the form for delivery details. It appears slightly differently depending on whether the user is logged in or not, and whether their details are already saved. For a guest user the form will appear blank. If the user is logged in but has not saved their details previously, the email field will be prepopulated and at the bottom of the form is an option to save their details to their profile.

<details>
<summary>Checkout Filled Form</summary>

![Checkout Filled](readme-docs/screens/checkout_filled.webp)
</details>

If the user has previously had their details saved to their profile, these details will be prepopulated in the form fields when the user loads the checkout page. Any changes the user makes to their details in the form can be saved by selecting the save option when they submit the form

Directly below the delivery details is the [Stripe](https://stripe.com) card element where the user inputs their card details to complete the order.

Before the submit button, there is a warning to the user stating how much money their card is about to be charged.

For the delivery form and Stripe elements, the code is based on Code Institute's [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) project.


#### Complete Order
<details>
<summary>Checkout Success</summary>

![Checkout Success](readme-docs/screens/checkout_success.webp)
</details>

When the user completes their order successfully, they are brought to the checkout success page which summarises the details of their order and their delivery details.
A success message is displayed on the top of the page which notifies the user of their order number and that a confirmation email will be sent to the email they provided on the delivery form.

Just below the "We have your order" message at the top of the page, there is a link for the user to download a PDF copy of their order so that they can print a simple hardcopy.


#### Order Confirmation
![Order Confirmation Subject](readme-docs/screens/order_confirm_email_line.webp)
<details>
<summary>Order Confirmation Email</summary>

![Order Email](readme-docs/screens/order_confirm_email_body.webp)
</details>

Using Stripe webhooks based on the Code Institute [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) project, when a user submits their order a confirmation email is then sent to the user with their payment and delivery details.


#### Order PDF

The PDF of the user's order is created using [Reportlab](https://docs.djangoproject.com/en/4.1/howto/outputting-pdf/). It generates a very simple summary of the user's order, not unlike the confirmation email, except that the items the user ordered are also listed in the summary. The intention is to provide a convenient method for the user to download or print a copy of all the relevant details of their order.


### User Authentication and Profiles

This section discusses features related to the user authentication, and user profiles and reviews in the profiles app.

#### Registration
<details>
<summary>Register</summary>

![Register](readme-docs/screens/register.webp)
</details>

[Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for user authentication for this website and so functionality for registration and authentication is handled by allauth. The templates used for registration, login/logout, and email confirmation are allauth templates which have been styled to match the rest of the website.

Registration is accessed through the "Register" link under the "Account" drop down menu and is unnecessary for most functionality on the website. A user can complete a purchase and generate a successful order without registering. Most functionality that requires registration is secondary to the purpose of the site and related to customer engagement and retention.

Above is the registration form. Once successfully completed, the user is redirected to the page in the image below where they are informed that a verification has been sent to their email address.

<details>
<summary>Verification Sent</summary>

![Verification Sent](readme-docs/screens/verify_sent.webp)
</details>

![Verification Inbox](readme-docs/screens/verify_email_inbox.webp)
<details>
<summary>Verification Email</summary>

![Verification Email](readme-docs/screens/verify_email.webp)
</details>

Following the link in the email above, the user is brought to the confirmation page where they can confirm their email address and then are able to login to their profile. When a user successful registers with the site and logs in for the first time, a user profile is created for them in a one-to-one relationship.

<details>
<summary>Confirm Email</summary>

![Confirm Email](readme-docs/screens/confirm_email.webp)
</details>
<details>
<summary>Email Confirmed</summary>

![Login Confirmed](readme-docs/screens/login_confirmed.webp)
</details>


#### Login
<details>
<summary>Login</summary>

![Login](readme-docs/screens/login.webp)
</details>

The login page is accessed through a "Login" link under the "Account" drop down menu and the template is standard from allauth and accepts either the user's username or email and their password as valid credentials to login. 

Upon logging in, the user is redirected to their user profile.


#### Logout
<details>
<summary>Logout</summary>

![Logout](readme-docs/screens/logout.webp)
</details>

When a user is logged in, the log out page is accessed through a "Logout" link under the "Account" drop down menu. Again, this is a standard allauth template styled to match the rest of the website.


#### User Profile
<details>
<summary>User Profile</summary>

![Profile](readme-docs/screens/user_profile.webp)
</details>

User profiles are created automatically when a user registers with the website, as based off of the code from Code Institute's [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) project. When a user logs in, they are redirected to their profile.

The main page of the user profile includes a section for the user's details and a table of their order history. Above the user's details, there are options available for the user to edit their profile details and to delete their account.

The order history table summarises their orders with their order number, the date it was placed, the total and a link to the checkout success page for that order so that they can review it in more detail there.

There are two links below the "Your Profile" heading at the top of the page. One link brings the user to the page containing their reviews and the other links to the page where they can manage their submitted recipes.


#### Your Reviews
<details>
<summary>User Reviews</summary>

![User Reviews](readme-docs/screens/user_reviews.webp)
</details>

"Your Reviews" on a user's profile is a page which contains a list of the reviews that the user has left on products. A user can leave a review anonymously, but there are certain features related to reviews which require a user to be logged in. One of these is the ability to access this history of their reviews.

This page displays each review with all relevant details. It states which product the review is for and links to that product page. It states the date of the review, the body of the review and the rating which the user left. There are also options to edit or delete the review. The user can also edit or delete their reviews directly in the review section of the product's detail page. This functionality is only available to registered users.


#### Your Recipes
<details>
<summary>User Recipes</summary>

![User Recipes](readme-docs/screens/user_recipes.webp)
</details>

On the "Your Recipes" page the user is able to submit a recipe for the website to consider for publication and view a list of the recipes that they have submitted already.

User submitted recipes are not published directly by the website. User's are given a simple form with which to submit the recipe, but if the website chooses to publish the submitted recipe they will do so through their own recipe page in the "Management" section. This area in the user profile provides a way for user's to suggest recipes to the site to encourage engagement.

If the website chooses to use a submitted recipe, they will mark it as published and a message will appear on this page next to the recipe. 

In future this area of the user profile could be expanded to include a section where the user can save their favourite recipes from the website.


#### Product Reviews
<details>
<summary>No Product Reviews</summary>

![No Reviews](readme-docs/screens/review_none.webp)
</details>

<details>
<summary>Product Review</summary>

![Review](readme-docs/screens/approved_review.webp)
</details>

The product detail page features a review form which user's can complete to submit a review and rating for a product. The user does not need to be registered to do so, but if they are not they cannot edit or delete their reviews after they have been published.

When a user submits a review, a message is displayed thanking the user for submitting the review but it is not displayed immediately. Reviews require moderation and have to be approved from the "Management" section of the website. Once approved, the review will be displayed on the product page.

If a user is logged in when looking at their own review on the product page, the options for edit and delete are present on the review they submitted. For an admin user, the option to delete a review is always present on all reviews.


#### Product Ratings
![Rating](readme-docs/screens/rating.webp)

On each review that is submitted for a product, the individual rating that a user submitted is displayed. The average for all of these submitted ratings is then taken and displayed on the product's detail table.


### Management

This section discusses features related to the management app. A lot of the features discussed here relate to other apps in the project where their functionality is accessed through the management app by staff.

The management section or dashboard of the website is only accessible to site user who are staff. This section of the website contains functionality related to product and recipe management and user moderation. Similar functionality is available to admin users through the admin panel, however this management dashboard allows staff to perform basic management tasks without having to leave the main website.

To prevent non-staff users from accessing the management dashboard the link only appears in the "Account" drop down menu for user's who are staff, and there is a simple mixin - the StaffRequiredMixin - that leverages Django's LoginRequiredMixin and UserPassesTestMixin for the management views in case users try to manually enter the url.
```
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
```

#### Products
<details>
<summary>Management Products</summary>

![Management Products](readme-docs/screens/management_products.webp)
</details>

The product dashboard is the first page that the staff user will arrive on when they access the management. Immediately at the top of the page, below the "Products" heading is a button to "Add New Product" which allows the user to add new products to the website.

The bulk of this dashboard are tables of the products on the website. These tables are best displayed on large screens, but do function on small devices. However there is a disclaimer on smaller screens that warns that the page is better suited to large screens.

These product tables are grouped by category and then subcategory. For example, within the Seeds category, you will find a table for Mild Seeds which will include all the seeds whose subcategory is mild. The number of products within each category and subcategory is visible for the user.

Within each table, there is minimal information for the product as the focus is on functionality. A typical product entry will include a name which links to the product's page, whether the thumbnail is present or not (as this also tells us if the product has an image unless something has gone wrong), then options to "Edit" the product, "Delete" the product, "Add" a variant, and view the variants.

If no variants are present, this is indicated on the table when the product's variants are toggled to visible. Variants can be added by clicking "Add" under the variant heading for a product. When variants are present their details include the "Size", "Price", and "Stock", and options to "Update Stock", "Edit" and "Delete" the variant.

From this table, the user is able to perform basic CRUD functions for the products and variants on the website, which is the aim of this section of the website. However, for each product on the website the options to "Edit" and "Delete" are also available on other pages for staff members. For example, if a user is a logged in as staff when they view the product detail page, below the description there are options to "Edit" and "Delete" the product. These options, particularly to edit, are available here in case the staff member is viewing the product page and notices a simple error like a typo and so does not need to return to the management dashboard to correct this.


#### Stock
<details>
<summary>Management Stock</summary>

![Management Stock](readme-docs/screens/management_stock.webp)
</details>

On the products page of the management dashboard, staff users can adjust the stock for variants by clicking "Update Stock" in the table. This opens a modal with a single field for the user to enter the stock. They can then see the new stock under the "Stock" heading in the table.

This variant stock can be managed here in the management dashboard by manually altering the stock field, but throughout the rest of the website stock is mainly managed by models and functions in the cart app. When a user adds a product to their cart, the item is also added to the HeldCart and HeldItems model in a similar way to the cart in their session. The quantity of the item is also added and the quantity of stock available for purchase is then reduced by this amount.

There is a time limit for how long users can hold items in their cart. This is to prevent stock from being added to a cart, reducing the amount of available stock for other users, then abandoning their cart and having the stock disappear from the database. How this is prevented is that user's have a two hour window to checkout from the time they last added an item to their cart. When the user reaches the end of this two hour window without checking out, the items are removed from their cart and restocked.

The held cart objects are tied to the user's session cart via the session key. This tethers the held cart object to the session cart without having the user needing to have an account and prevents duplicate carts. If a user is to log in or out, the session key is changed and the held cart is then left to count down to restock the items. A warning is displayed on product pages by the "Add To Cart" button advising users to login before they start shopping.

Restocking abandoned carts is handled by functionality implemented through [APScheduler](https://apscheduler.readthedocs.io/en/3.x/). Within the cart app, there is a simple restock job that checks the cart's time and if it has reached the limit will restock items and delete the held cart.
```
def restock():
    carts = HeldCart.objects.all()

    if carts is not None:
        for cart in carts:
            if cart.check_time():
                for held_item in cart.held_items.all():
                    variant = Variant.objects.get(id=held_item.variant.id)
                    variant.current_stock += held_item.qty
                    held_item.delete()
                if not cart.held_items.exists():
                    cart.delete()
```
Scheduling of this task is handled within updater.py and runs this function every 15 minutes when the app is running.
```
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .job import restock


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(restock, 'interval', minutes=15)
    scheduler.start()
```
The implementation of APScheduler for handling this job is based on a tutorial from [Did Coding](https://www.youtube.com/watch?v=Lzy4G1wZ7NQ&ab_channel=DidCoding).


#### Reviews
<details>
<summary>Management Reviews</summary>

![Management Reviews](readme-docs/screens/management_reviews.webp)
</details>

In the management dashboard, there are links available at the top of the page to navigate to different pages within the dashboard. One of these navigates to "Reviews" which lists the user reviews.

User reviews are displayed as a list. Each review displays the name of the reviewer (or anonymous), the date of the submitted review, the products reviewed, the rating and the content. Options are available for each review to "Delete" the review or approve it. Once a review has been approved, this status is then displayed.

In the future, it may be beneficial to introduce further classifications for user reviews beyond a boolean of approved or not. Possibly classifications could include "Pending Approval", "Not Approved", and "Approve". However, currently with the option to delete reviews, reviews that are not acceptable can be removed in that way.


#### Recipes
<details>
<summary>Management Recipes</summary>

![Management Recipes](readme-docs/screens/management_recipe.webp)
</details>

The recipes section of the management dashboard also includes the submitted recipes and the recipe comments. At the top of the page, beneath the links, is the button to "Add Recipe" which brings the user to the recipe form for submitting recipes to the site. 

The recipes page itself is a list of recipes displayed as a summary. It displays the title linking to the recipe page, the date created, the excerpt from the recipe, and options to "Publish", "Edit" and "Delete" the recipes. When the recipe is published on the website, this option to publish is replaced with a message stating that it has been publish and displays the link to the recipe page.

Staff users can also edit and delete recipes directly from the recipe pages. These options are displayed for users who are logged in and who are staff.


#### Submitted Recipes
<details>
<summary>Submitted Recipe</summary>

![Submitted Recipes](readme-docs/screens/user_recipe_approve.webp)
</details>

Within the recipes section of the management dashboard, there is a link to the "Submitted Recipes" page which displays the recipes submitted by users. From this page, the staff users are able to review the submitted recipes and if they are chosen to publish on the website, they can mark them as "Published" to provide feedback to the owner.

The intention is not to directly publish the recipe. From this point, the staff user is expected to add the recipe to the site via the normal route while crediting the original user.


#### Comments
<details>
<summary>Management Comment</summary>

![Management Comment](readme-docs/screens/management_comments.webp)
</details>

Also within the recipes section of the management dashboard, is a link to the "Recipe Comments" to allow staff users to manage comments on recipe pages.

In the same way that user reviews are displayed, the user comments display the user who commented, the date it was added, the comment body and options to "Delete" or "Approve" the comment. This section allows for moderation of comments on the recipes as comments are not displayed until approved by a staff member.


### Admin

Most of the functionality available on the main website to staff users is also available through the admin panel. Most models are registered to allow admin users to perform CRUD functionality through the admin panel.

In some cases CRUD functionality is only available through the admin panel. For example, categories are registered with admin but there's no functionality available through the management dashboard on the main site. It was decided that because any addition to categories also may require changes to templates (e.g. navigation links, the latest products template), that it would beyond the scope of an average staff member to make any additions to categories and so this functionality should remain within admin where it can be accessed by an IT person.

Similarly, users and user profiles can be managed through the admin panel, including changing passwords and deleting users, but this functionality is not present on the management dashboard to discourage staff from attempting to manipulate the user database. Users are able to edit their own profile details or delete their account themselves, but these options are available to them through their profile as they have the right to manage their own personal information.


### Future Features

1. __Improved Stock Management__:
  - Stock management can be improved to allow users more control over their cart. Users could be allowed to keep their carts when logging, or, when logged in, be allowed to save their cart for a period of time.
2. __Order Again__:
  - For registered users you could offer an "Order Again" button for items in their order history. This could be as simple as clicking the button and adding the item to their cart like on a product page, with the function only having to check whether it is in stock or not.
3. __Improved Category Filtering__: 
  - Expanding category filtering beyond subcategory could include filtering by average user rating or popularity, if we were to expand the product model to track the number sold.
4. __Plant Care Blog__:
  - As part of marketing and providing content to users, a plant care blog may could expand the site further beyond products, giving users another reason to return to the site between purchases.
5. __Expanded Product Range__:
  - Providing products beyond seeds and sauces. Expanding the range to include items related to plant care or cooking could draw more users, and repeat users. This may require altering the current product models. 


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

The colour palette used for the website based on the central red which was colour picked from the main image used on the carousel on the index page. From there, colours were chosen to compliment or contrast, selecting for legibility, simplicity and to stay with the chilli pepper theme. 

<details>
<summary>Colour Palette</summary>

![Colour Palette](readme-docs/mockups/palette.webp)
</details>

### Mockups

Initially, the project idea came about during planning for a previous project and mockups were created then. At that stage the project was put aside in favour of another idea that better fit the requirements. At the time, the project was proposed as a subscription box service. It has since changed but the design of the website still shares some similarities visually with the intial mockups.

<details>
<summary>Mock Up One</summary>

![Mock Up One](readme-docs/mockups/mockup_one.webp)
</details>

<details>
<summary>Mock Up Two</summary>

![Mock Up Two](readme-docs/mockups/mockup_two.webp)
</details>

### Wireframes

Wireframes were created in Balsamiq. They were used for initial planning for the layout of the website.

<details>
<summary>Index</summary>

![Index](readme-docs/mockups/index.png)
</details>

<details>
<summary>Contact</summary>

![Contact](readme-docs/mockups/contact.png)
</details>

<details>
<summary>Products</summary>

![Products](readme-docs/mockups/products.png)
</details>

<details>
<summary>Product Detail</summary>

![Product Detail](readme-docs/mockups/product_detail.png)
</details>

<details>
<summary>Cart</summary>

![Cart](readme-docs/mockups/cart.png)
</details>

<details>
<summary>Checkout</summary>

![Checkout](readme-docs/mockups/checkout.png)
</details>

<details>
<summary>Checkout Success</summary>

![Checkout Success](readme-docs/mockups/checkout_success.png)
</details>

### Entity Relationship Diagrams

<details>
<summary>ERD</summary>

![ERD](readme-docs/mockups/ERD.WEBP)
</details>


## SEO and Marketing

A link to a popular dog charity was added in the footer to increase SEO for the website. 

### SEO, Keywords

Keyword research was performed using [Wordtracker](https://www.wordtracker.com/search), 

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