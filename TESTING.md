
[**Index**](#up)  
[**1. User stories**](#1-user-stories)  
[**2. Manual testing**](#2-manual-testing)   
[**3. Automated testing**](#3-automated-testing)   
[**4. Responsiveness**](#4-responsiveness) 

# 1. User stories  

As a ***Website visitor***  I want to be able to:

- **Understand what it's got to offer**: The home page displays a dog picture with the message "Quality dog accesories" and a call to action button to enter the shop.
- **Find a list of products**: upon clicking the Shop Now button the user can find all the products displayed.
- **Filter the list of products**: the products page offers several filtering options( by price, rating, name and category).
- **Search the list of products**: user can make use of the search bar displayed to look for a specific product.
- **See details about a product**: each product displays a description along other important elements (name, category, sizes, price and rating) .
- **See the total of my shopping bag**: when adding products to the shopping bag the total displays/updates accordingly.
- **Purchase products without being registered**: visitors are not required to register before making a purchase.
- **Receive email confirming my order details**: Upon successful checkout, an email is send to confirm the order.
- **Browse the blog for relevant information**: The blog contains relevant information about how to chose the right sizes for example.
- **Easily Register for an account**: the account icon is displayed on mobile and is available on all pages and the sign up process only requires an email address, a username and password.

****

As a ***registered user***  I want to be able to:  
- **Easily Log In/Out**: log in can be done with email address or username and upon clicking the log out button a confirmation message double checks the action.
- **Easily recover forgotten password**: on the Sign In page a *Forgot Password* link offers the option of recovering the password.
- **Save my default delivery details**: upon checkout, the user can tick a box to confirm they want their info to be saved. Additionally, the info can be updated on the profile page.
- **View my purchase history**: if the user is logged in they can find details about their past orders on the Profile page.
****
As a ***business owner*** I want to be able to:  
- **View, add, update and delete products**: Admin has access to all the products and can perform all CRUD operations.
- **Write blog posts about products**: Admin can write and update blog posts as well as approve/delete comments on blog posts.

# 2. Manual testing
**Navigation**
| Test                                    | Action                                        | Result                                                               | Bugs |
|-----------------------------------------|-----------------------------------------------|----------------------------------------------------------------------|------|
| Nav links change colour on hover        | Hover over elements                           | Nav links change colour to Ruby                                      |      |
| Website logo sends user to home page    | Click on logo                                 | Redirects user to home page                                          |      |
| Dropdown menu works                     | Click on dropdown and see relevant categories | User redirected to categories                                        |      |
| Click on category tag displays products | Click on tag                                  | Products from the same category are displayed                        |      |
| Search bar returns query                | Input query                                   | The query is returned with the number of products found or 0 if none |      |
| My account(logged-out)                  | Click on My Account                           | Unregistered users can only see Register and Login as options        |      |
| My account(logged-in)                   | Click on My Account                           | Logged in user can see My Profile and Logout links                   |      |
| My account(logged-in as superuser)      | Click on My Account                           | Superuser can see Product Management, My Profile and Logout links    |      |
| Bag                                     | Click on bag                                  | Sends user to Shopping bag page                                      |      |

**Footer**
| Test                       | Action                               | Result                      | Bugs |
|----------------------------|--------------------------------------|-----------------------------|------|
| Footer stays to the bottom | Check footer on each individual page | Footer sticks to the bottom |      |
| Check social links open    | Click each icon                      | Icons open in a new tab     |      |

Product cards open to show details
Cards open to show product details