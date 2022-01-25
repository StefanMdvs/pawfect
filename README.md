# Pawfect!
![mockup image](media/mockup.png)
*Accessories for everybody's best friend*

**[Live demo](https://pawfect-sm.herokuapp.com/)**

---
[**Index**](#up)  
[**1. Overview**](#1-overview)  
[**2. UX**](#2-ux)  
- [2.1 User Stories](#21-user-stories)  
- [2.2 Wireframes](#22-wireframes) 
- [2.3 Database schema](#23-database-schema) 
- [2.4 Design](#24-design) 

[**3. Features**](#3-features) 
- [3.1 Existing features](#31-existing-features)  
- [3.2 Features to add](#32-features-to-add)  

[**4. Technologies used**](#4-technologies-used)  
[**5. Testing**](#5-testing)  
[**6. Deployment**](#6-deployment)  
[**7. Credits**](#7-credits)  

# 1. Overview
Pawfect, just as the name sugests, aims at providing quality affordable accesories that perfectly suits your four-legged mud-lover family members. With a range of choices from essentials to toys, you will find something that the king/queen of the house will enjoy.

## What's on offer?
Browse the *Essentials* where you can find beds, bowls and grooming kits. If your pouch needs *Toys* then you can choose from plush, throwing, chewing or squeaky! And don't forget the absolutely most important ones: *Walking* accesories, with a choice of collars, leads, harnesses and safety.
# 2. UX  
The user should find the application easy to navigate, intuitive and responsive, whilst providing consistency and security for payment details.
## 2.1 User Stories 
| User Story ID | As a...         | I want to be able to...                    | In order to...                                           |
|---------------|-----------------|--------------------------------------------|----------------------------------------------------------|
| 1             | Website visitor | Understand what it's got to offer          | Decide if it's worth browsing                            |
| 2             |                 | Find a list of products                    | Make a purchase                                          |
| 3             |                 | Filter the list of products                | Reduce the time of browsing                              |
| 4             |                 | Search the list of products                | Quickly find what I am interested in                     |
| 5             |                 | See details about a product                | Check the price, description, rating and available sizes |
| 6             |                 | See the total of my shopping bag           | Keep track of my spending                                |
| 7             |                 | Purchase products without being registered | Avoid this step at the moment                            |
| 8             |                 | Receive email confirming my order details  | Make sure the Order was placed successfully              |
| 9             |                 | Browse the blog for relevant information   | Learn about specific queries                             |
| 10            |                 | Easily Register for an account             | View my profile                                          |
| 11            | Registered user | Easily Log In/Out                          | Access my account info                                   |
| 12            |                 | Easily recover forgotten password          | Regain access to my account                              |
| 13            |                 | Save my default delivery details           | Checkout faster                                          |
| 14            |                 | View my purchase history                   | Keep track of my shopping                                |
| 15            | Business owner  | View, add, update and delete products      | Show an updated list of products to customers            |
| 16            |                 | Write blog posts about products            | Inform customers about products and dogs wellbeing       |

## 2.2 Wireframes
Full width wireframes for mobile, tablet and desktop can be accessed **[here](wireframes)**.

## 2.3 Database schema
Giving the relations between tables the project uses a relational database, with SWLite being used in development and Postgress in production. The relation between tables can be observed in the diagram below:
![DB diagram](wireframes/db-diagram.png)
The database model is focused on the following models:  
**Product**  
This model is the core model and it's main attributes are name, description, category, sizes if available and price. The model has a ForeignKey to Category in order to group products together.  
**Category**  
This model is used to group products by category and has just a name attribute.  
**Order**  
This model stores information about the order being created, such us order number for future reference and delivery details along the total cost. It will also store a user's profile.  
**OrderLineItem**  
By accessing the Product and Order models it stores info about each product line within an order.  
**UserProfile**  
The model is used to save information about users in order to speed up the checkout process. It also displays the order history.  
**Post**  
This model helps admin to create Blog posts and holds as attributes a name, a slug that helps create individual urls, the author, the body where the actual content will go and information about the date is was posted/updated.  
**Comment**  
Holds information about the user along with the text content and requires the admin to approve the comments in order to prevent spam. It also has a ForeignKey to Post so that the comment gets attached to the relevant Blog post.  
## 2.4 Design
**Color scheme**  
The project uses the following colors:
- ![#9d2646](https://via.placeholder.com/15/9d2646/000000?text=+) #9d2646 (ruby)  
and
- ![#f4fff8](https://via.placeholder.com/15/f4fff8/000000?text=+) #f4fff8 (mint green)  

The main color is ruby and can be found across the website on either the background of the elements or as a font color for header elements. 
The mint green is only used as a background color for header and footer and helps to make the transition from those elements to the page content.  
**Font**  
The project uses *Aleo* throughout the website for consistency.  
**Buttons**  
A variation between background and border has been used using the Ruby color in order to highlight various actions.  
**Icons**  
Icons used bear the colour of the elements they precede or they use the same Ruby colour.  
**Shadow**  
To highlight each individual product, the card element has a shadow effect which makes them stand out and also border the elements with a white backround.  

# 3. Features 
## 3.1 Existing features
Across the website:  
**Responsive**  
The website displays well across all devices thanks to Bootstrap's grid system.  
**Custom Navbar**  
Navbar provides user with quick access to key pages. On mobile view there's a navbar toggler along with the search and user icons and the shopping bag. On large screens the navbar menu is displayed with dropdown for various categories.  
**Search bar**  
Provides quick access to the database and makes queries to the product name and description.  
**Toasts**  
Provides feedback for user action, such as adding products to the bag or updating it.  
**Home Page**  
Home page has a call to action button and displays a hero image.  
**Products Page**  
Displays all the products and has the following features:
- **Sorting** the products based on price, rating, name and category
- **Displaying** the essential info about a product (Name, price, category and rating)
- **Edit/Delete** option for admin  

**Product Detail Page**  
- **Displays** details about a product and includes a descprition along with the details presented on Products page
- **Quantity** input form for user to select the desired quantity
- **Size** selector for products that have sizes
- **Edit/Delete** option for admin  

**Shopping bag**  
- **Displays** individual lines for each product with essential info (image, name, size if any, price and subtotal)
- **Quantity** input form for user to update product quantity
- **Delete** button if user wants to remove an item
- **Price** info displaying the total, delivery costs and Grand total  

**Checkout**  
- **Form** to fill in for delivery details
- **Displays** order summary
- **Payment** handled by Stripe
- **Form prefill** for registered users
- **Save details** option for future deliveries  

**Checkout success**  
- **Confirmation** of the order being received with Order info, Delivery and contact details being displayed along with the Total.  

**Profile**
- **Registered** users can update their delivery information and see their order history
- **Admin** can perform add/edit operations on products  

**CRUD functionality**  
- **Create**: all users can create a comment on blog posts; Admin only can create new products and Blog posts
- **Read**: all users can see details about products and read blog articles
- **Update**: reserved to registered users, they can update their profile info. On top of that, admin can update products and Blog posts
- **Delete**: Admin can delete products, Blog posts and comments.

**Access protection**  
```@login_required``` decorator was used to ensure non-super-users cannot interfere with the database.  
**Static and image file hosting**  
Project uses Amazon S3 bucket to store static files and images.  
**404 and 500 error handling** to keep user on website and minimize disruption.

## 3.2 Features to add
- Functionality to add a product to a **wish list**
- Suggestions regarding **related products**

# 4. Technologies used
**Languages**
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

**Frameworks**
- [Bootstrap](https://getbootstrap.com/)
- [Django](https://www.djangoproject.com/)
- [jQuery](https://jquery.com/)

**Database**
- [Heroku Postgres](https://www.heroku.com/postgres)

**Extensions**
- [Stripe](https://stripe.com/docs)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

**Project Management**
- [Balsamiq](https://balsamiq.com/wireframes/)
- [GitPod](https://gitpod.io/workspaces)
- [GitHub](https://github.com/)
- [Amazon AWS](https://aws.amazon.com/) (S3)

**Tools**
- [DB Diagram](https://dbdiagram.io/home)
- [Favicon.io](https://favicon.io//)  
- [Panda image compression](https://tinypng.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [Mockup generator](http://techsini.com/multi-mockup/index.php)

# 5. Testing 
Details about this section can be found [here](TESTING.md).




