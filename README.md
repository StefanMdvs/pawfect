# Pawfect!
![mockup image](static/images/mockup.png)
*Accessories for everybody's best friend*

**[Live demo](link-to-follow)**

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