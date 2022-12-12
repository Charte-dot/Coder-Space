# Coder Space Testing

## Table of contents:
- ##  [Manual testing](#Manual-testing)
     - [Testing User Stories](#Testing-user-stories)


## Manual Testing
The project was thoroughly tested by the developer and multiple user from friends and family members. Thorough testing was conducted by the developer and multiple users among friends and family especially with order creation, updating totals, editing line items. Bugs were found and fixed as detailed below in [Bugs](#bugs-and-fixes) section. Testing steps and results are detailed as follows.

### Testing User Stories

For User Story testing first navigate to the [Coder Space website](https://coder-space.herokuapp.com/)


* **As a shopper I want to be able to view a list of products so that I can select some to purchase [#1](https://github.com/Charte-dot/Coder-Space/issues/1)**

**Acceptance Criteria**: User registered and unregistered can view a list of products with images and descriptions that are available to purchase.

**Testing Steps**:
1. Without logging in to the site click on the Shop now button or click all products tab on the navigation bar.
2. View list of products
3. Click on individual products to view product page.
4. Individual products page displays all information about that product.

**Expected Result**:
- Shop page opens
- Products display
- Image and summary detail are visible
- Link works as expected

**Actual Result**:
- Shop page with list of individual products is displayed
- Image and summary detail are visible
- Link works as expected

**Pass/Fail: Pass** ✅

![](documentation/screenshots/all-prods.jpg)

---

* **As a Shopper I can View individual products, So I can See the price and product description [#2](https://github.com/Charte-dot/Coder-Space/issues/2)**

**Acceptance Criteria**: User can click on individual product image and open a full detailed page about the product

**Testing Steps**:
1. Without logging in from the Shop page (see User Story test #1), click on a product image
2. Click on individual product image

**Expected Result**:
- Product detail card opens when product image is clicked
- Full product detail card is displayed
- All links in card work correctly

**Actual Result**:
- Product detail card opens when product image is clicked
- Full product detail card is displayed
- All links in card work correctly

**Pass/Fail: Pass**✅

![](documentation/screenshots/prod-detail.jpg)

---

* **As a Shopper I can easily identify each category or product available, So I can find the exact product I need [#3](https://github.com/Charte-dot/Coder-Space/issues/3)**

**Acceptance Criteria**: Well sign posted labels within the site directing users to different categories and products available.

**Testing Steps**:
1. Click on the all products link to view all products
2. Click on the labelled nav bar to narrow down the products search
3. Choose a category from each main nav tab to view certain products. ie computers nav tab - computer related products

**Expected Result**:
- Each nav tab displays sub nav category
- Each category displays a nav link to specific product category ie computer nav tab for computer related products
- All links in nav work correctly

**Actual Result**:
- Each nav tab displays sub nav category
- Each category displays a nav link to specific product category ie computer nav tab for computer related products
- All links in nav work correctly

**Pass/Fail: Pass**✅

![](documentation/screenshots/nav-bar-full.jpg)

---

* **As a Shopper I can Easily identify the total cost of my purchases at all times, So I can Keep track of total cost. [#4](https://github.com/Charte-dot/Coder-Space/issues/4)**

**Acceptance Criteria**: User's total cost displays beneath the bag icon and updates and the user places items into the bag

**Testing Steps**:
1. Without logging in check basket icon and amount are visible in navbar (0euro if basket is empty)
2. Navigate to Shop page
3. Click on product image to open product detail
4. Click on add to basket
5. Check amount beside icon in navbar
6. Click on basket icon

**Expected Result**:
- Basket icon is visible in navbar - set to 0 when basket is empty
- Total amount updates as basket changes
- When clicked basket icon opens Shopping Basket page

**Actual Result**:
- Basket icon is visible in navbar with amount corresponding to basket total visible
- When clicked basket icon opens Shopping Basket page

**Pass/Fail: Pass**✅

![](documentation/screenshots/cost-view.jpg)

![](documentation/screenshots/cost-view-2.jpg)

---

* **As a shopper I want to be able to view more information about the store so that I can increase my confidence that the store is genuine, trustworthy and reliable to purchase from [#5](https://github.com/Charte-dot/Coder-Space/issues/5)**

**Acceptance Criteria**: About page visible and linked in navigation

**Testing Steps**:
- In quick links located with in the footer click about us page.

**Expected Result**:
- About Page opens

**Actual Result**:
- About Page opens when About link is clicked

**Pass/Fail: Pass**✅

![](documentation/screenshots/about.jpg)

---


* **As a Shopper I can View a review on products, So I can decide if a product will suit my needs. [#6](https://github.com/Charte-dot/Coder-Space/issues/6)**

**Acceptance Criteria**:  A review form for registered users to leave a review on products they have bought.

**Testing Steps**:
1. Navigate to products page
2. Click on product image to open product detail
3. Previous reviews are viewable under product details

**Expected Result**:
- Reviews for each product are viewable on each product page
- If user is logged in option to leave a review if unregistered or not logged in prompt to log in to leave a review

**Actual Result**:
- Reviews for each product are viewable on each product page
- If user is logged in option to leave a review if unregistered or not logged in prompt to log in to leave a review

**Pass/Fail: Pass**✅

![](documentation/screenshots/review-view.jpg)

---

* **As a Shopper I can View a social media page for more info on products, So I can view any offers or extra content from the store [#7](https://github.com/Charte-dot/Coder-Space/issues/7)**

**Acceptance Criteria**: Add a social media page for the site

**Testing Steps**:
1. From any page navigate to the footer section
2. In turn click on Facebook, Twitter and Instagram icons

**Expected Result**:
1. When clicked Facebook icon opens Facebook in a new tab (Image is a mockup Facebook business page)
2. When clicked Twitter and Instagram main page sites open in a new tab

**Actual Result**:
- When icons are clicked Facebook, Twitter and Instagram main pages open in new tabs

**Pass/Fail: Pass**✅

![](documentation/screenshots/fb-store.png)

---

* **As a Shopper I can register for an account, So I can have a personal account to be able to save details and view previous orders [#11](https://github.com/Charte-dot/Coder-Space/issues/11)**

**Acceptance Criteria**: User can register for an account with an email and password.

**Testing Steps**:
1. Make sure to be not logged in to the website and click on my account in the navbar
2. Click on the Register link in the dropdown menu
3. In the register form click on the back to sign in link to check link
4. Repeat steps 1 and 2
5. Click on the sign up button without entering anything in the first field
6. Complete the first field and repeat step 5 for the other fields
7. With all fields complete click sign up

**Expected Result**:
**Actual Result**:
1. Back to login and sign up links link correctly to sign in page
2. Success message asking user to confirm their email address appears when user has registered
3. Email is sent to user's email address with link to confirm email address
4. Link to confirm email address functions correctly
5. Error message displays if error occurs when fillling out registration form

**Actual Result**:
1. Back to login and sign up links link correctly to sign in page
2. Success message asking user to confirm their email address appears when user has registered
3. Email is sent to user's email address with link to confirm email address
4. Link to confirm email address functions correctly
5. Error message displays if error occurs when fillling out registration form

**Pass/Fail: Pass**✅

![](documentation/screenshots/register.jpg)

![](documentation/screenshots/confirm.jpg)

![](documentation/screenshots/confirm-success.jpg)

![](documentation/screenshots/reg-error.jpg)

---

* **As a Registered shopper I can Easily login and logout of my account, So I can access my own account on the site [#12](https://github.com/Charte-dot/Coder-Space/issues/12)**

**Acceptance Criteria**: User can login to account with password and email used to set up account on registration page.

**Testing Steps**:
1. When not logged in click my account in navigation menu
2. Click on login link
3. Complete username and password boxes
4. Click sign in button

**Expected Result**:
- User is signed in when information fields are completed
- User's information is automatically completed if they have checked the remember me box

**Actual Result**:
- User is signed in
- User's information is automatically completed if they have checked the remember me box
- During testing it was apparent that it would be useful to easily see which user was logged in so the username was added to the title in the My Profile page

**Pass/Fail: Pass**✅

![](documentation/screenshots/sign-in.jpg)

![](documentation/screenshots/user-profile.jpg)

---

* **As a Registered shopper I can recover my password hassle free should I forget it, so I can gain access to my account. [#13](https://github.com/Charte-dot/Coder-Space/issues/13)**

**Acceptance Criteria**: User can recover/change password from user profile

**Testing Steps**:
1. Click on profile icon in navigation menu
2. Click on login link
3. Click on forgot password link
4. Enter email address
5. Open email and click on link to reset password

**Expected Result**:
- Password is successfully changed and success message appears
- User is able to log in with new password

**Actual Result**:
- Password is successfully changed and success message appears
- User is able to log in with new password

**Pass/Fail: Pass**✅

![](documentation/screenshots/reset.jpg)

![](documentation/screenshots/reset-email.jpg)

![](documentation/screenshots/password-change.jpg)

![](documentation/screenshots/password-success.jpg)

---

* **As a registered shopper I can Have a confirmation email to advise that registration has bee successful, So I can Have acknowledgement that my registration details were accepted and saved. [#14](https://github.com/Charte-dot/Coder-Space/issues/14)**

**Acceptance Criteria**
1: User clicks on my account nav tab in navigation to open profile
2: User can view delivery details and order history in my profile

**Testing Steps**:
1. When not logged in click on profile icon in navigation menu
2. Type https://coder-space.herokuapp.com/profile/ into the address bar
2. Log in and repeat step 1
2. Click on My Profile

**Expected Result**:
- User can view order history and delivery information for their own account when they click on My Profile
- If not logged in My Profile link is not visible
- When not logged in if user navigates to https://coder-space.herokuapp.com/profile/ they are redirected to the Sign In page

**Actual Result**:
- User can view order history and delivery information for their own account when they click on My Profile
- If not logged in My Profile link is not visible
- When not logged in if user navigates to https://cpder-space.herokuapp.com/profile/ they are redirected to the Sign In page

**Pass/Fail: Pass**✅

![](documentation/screenshots/verify.jpg)

![](documentation/screenshots/confirm.jpg)

![](documentation/screenshots/confirm-success.jpg)

![](documentation/screenshots/non-admin-sign.jpg)

---

* **As a Registered shopper I can have a personal profile, So I can View my personal details for delivery and payment and update as needed [#15](https://github.com/Charte-dot/Coder-Space/issues/15)**

**Acceptance Criteria**
- Email is sent to user account with confirmation link
- Confirmation link links to website confirmation page
- User is able to login with login credentials


**Testing Steps**:
1. Make sure to be not logged in to the website and click on the profile icon in the navbar
2. Click on the Register link in the dropdown menu
3. Complete the form fields as in User Story #9
4. Navigate to user's email account
5. Click on link in email to confirm email
6. Click on confirm button on website
7. Login with registration details

**Expected Result**:
1. Email is sent to user account with link to confirm address
2. When email link is clicked user is directed to website link to click to confirm email address.
3. Registration is confirmed with message.
4. User logs in with provided login information

**Actual Result**:
1. Email is sent to user account with link to confirm address
2. When email link is clicked user is directed to website link to click to confirm email address.
3. Registration is confirmed with message.
4. User logs in with provided login information

**Pass/Fail: Pass**✅

![](documentation/screenshots/login.jpg)

![](documentation/screenshots/non-admin-sign.jpg)

![](documentation/screenshots/user-profile.jpg)

---

* **As a shopper I want to be able to easily see what I have searched for and the number of results so that I can quickly see how many products are available[#17](https://github.com/Charte-dot/Coder-Space/issues/17)**

**Acceptance Criteria**
- Search page displays search item and number of results found above the display of search items

**Testing Steps**:
1. Type single word into search box in navbar
2. Click search icon or enter
3. Repeat and enter empty search

**Expected Result**:
1. Above products found list the search term and number of results is printed
2. If no results are found this is stated

**Actual Result**:
1. Above products found list the search term and number of results is printed
2. If no results are found this is stated

**Pass/Fail: Pass**✅

![](documentation/screenshots/product-count.jpg)

![](documentation/screenshots/product-count-2.jpg)

---

* **As a Shopper I can select the quantity of a product that I am purchasing, So I can visually see the correct quantity and modify if needed. [#18](https://github.com/Charte-dot/Coder-Space/issues/18)**

**Acceptance Criteria**
- User can select quantity of product to add to bag when looking at the product detail page

**Testing Steps**:
1. Click on products link in navbar
2. Click on item to test
3. Click on quantity selector box + and - in turn
4. Click on add to basket
5. Enter a value into the box, including decimal numbers and negative numbers
6. Click on add to basket button

**Expected Result**:
- Product quantity is updated in basket as selected
- Error message appears when decimal or negative is entered

**Actual Result**:
- Product quantity is updated as selected when integer
- Validation errors show when decimal or negative number is entered into the box

**Pass/Fail: Pass**✅

![](documentation/screenshots/amount.jpg)

![](documentation/screenshots/amount-error.jpg)

![](documentation/screenshots/bad-notif.jpg)

---

* **As a Shopper I can View items as they are placed in my basket, So I can keep account of the total cost of the purchase [#19](https://github.com/Charte-dot/Coder-Space/issues/19)**

**Acceptance Criteria**
-  User can click on basket icon in navbar from any page to see contents

**Testing Steps**
1. Follow steps in User Story #19 to add item(s) to basket
2. View basket icon in navbar
3. Click on basket icon in navbar

**Expected Result**:
1. Total cost of items in basket is viewable in navbar
2. Basket icon opens when clicked to full basket page

**Actual Result**:
1. Total cost of items in basket is viewable in navbar
2. Basket icon opens when clicked to full basket page


**Pass/Fail: Pass**✅

![](documentation/screenshots/cost-view.jpg)

![](documentation/screenshots/cost-view-2.jpg)

---

* **As a Shopper I can enter my payment details hassle free, So I can checkout my purchases quickly and easily [#21](https://github.com/Charte-dot/Coder-Space/issues/21)**

**Acceptance Criteria**

1: User clicks on checkout to complete payment form
2: Success message visible on completion of payment process

**Testing Steps**:
1. With items in basket and in basket page (follow previous steps) click Checkout button
2. Attempt to checkout without completing form fields correctly
3. Complete fields correctly
4. Complete card payment field with fake card details
5. Complete card payment with card number 4242 4242 4242 4242 

**Expected Result**:
1. Error message shows when fields are incorrectly completed
2. Error message shows when card number does not use test card number
3. Success message and order confirmation message displayed to user when order is completed
4. Payment success shown in Stripe dashboard
5. Stripe webhooks shows charge success

**Actual Result**:
1. Error message shows when fields are incorrectly completed
2. Error message shows when card number does not use test card number
3. Success message and order confirmation message displayed to user when order is completed
4. Payment success shown in Stripe dashboard
5. Stripe webhooks shows charge success

**Pass/Fail: Pass**✅

![](documentation/screenshots/check-1.jpg)

![](documentation/screenshots/check-2.jpg)

![](documentation/screenshots/card-error.jpg)

![](documentation/screenshots/stripe-3.jpg)

---

* **As a Shopper I can Give my personal payment details and information and know its secure and safe , So I can Be confident to be able to provide the necessary information to make a purchase [#22](https://github.com/Charte-dot/Coder-Space/issues/22)**

**Acceptance Criteria**
1. User receives success/error messages when completing order/payment
2. User can view order history in personalised profile when logged in
3. Padlock appears in site address bar indicating secure payment process and padlock in checkout button

**Testing Steps**:
1. Complete steps to make test purchase as outlined above
6. Click on profile icon in navbar
7. Click on My Profile link

**Expected Result**:
1. Padlock symbol appears in address bar during checkout process and padlock is on checkout button
2. Success message and order confirmation message displayed to user when order is completed
3. Order appears in user's secure profile page

**Actual Result**:
1. Padlock symbol appears in address bar during checkout process and padlock is on checkout button
2. Success message and order confirmation message displayed to user when order is completed
3. Order appears in user's secure profile page

**Pass/Fail: Pass**✅

![](documentation/screenshots/secure-checkout.jpg)

![](documentation/screenshots/profile.jpg)

---

* **As a Shopper recieve an order confirmation after order has been placed, To have an written record of my purchases [#23](https://github.com/Charte-dot/Coder-Space/issues/23)**

**Acceptance Criteria**
1. User receives order confirmation in terminal with name, order information.

**Testing Steps**:
- Complete test purchase steps as outlined above

**Expected Result**:
- Order confirmation message is visible with all order details on screen on completion of purchase

**Actual Result**:

- Order confirmation message is visible with all order details on screen on completion of purchase

![](documentation/screenshots/order-complete.png)

**Pass/Fail: Pass**✅

![](documentation/screenshots/order-confirm.jpg)

