# Coder Space

![Mock up](documentation/screenshots/mockup.jpg)

## View the live site [here](https://coder-space.herokuapp.com)

## Table of contents:
- ##  [UX Design](#Manual-testing)
    - [Agile Planning](#Agile-Planning)
    - [Project Goal](#Project-goal)
    - [Target Audience](#Target-audience)
    - [Business Goals](#Business-goals)
    - [Customer Goals](#customer-goals)
    - [User Stories](#User-stories)
    - [Seo and web marketing](#Seo-and-web-marketing)
    - [Scope](#Scope)
    - [Structure](#Structure)
    - [Database](#Database)
    - [Models](#Models)
    - [Skeleton](#Skeleton)



# UX Design
---
## Agile Planning

User stories (Issues) with acceptance criteria and tasks are each linked to an Epic (Milestone) and placed in an Iteration kanban board (Projects 1, 2 and 3). Each user story in the kanban board is labelled with a "must-have", "should-have", or "could-have" label of different colours to show their prioritisation for the project. See the table of User Stories [here](#user-stories).

## Project Goal

The goal of the project is to create an online store that sells a custom office/gaming/office space products all in one place. As the work place has changed since Covid and hybrid working is now a reality, more and more people are working at a desk space at home. The main goal was to showcase a range of products to help make a more productive work environment. A creative space that the customer can truly enjoy whilst working or creating and developing. Coder space was created for coders, software developers and software engineers at the forefront of the initial design phase. During development it became apparent that the store is for anyone looking to customize or upgrade their work space at home.

## Target audience

- People who work from home 
- People who like to play console and or online games
- People who want a stylish functional creative space to work, game or develope software
- People looking for unique office style products but with a custom feel.

## Business Goals

- To create a professional online store
- To provide an easy and secure means to purchase items.
- To increase an one stop shop for creating your personal work space
- To create a brand for the store and increase brand awareness

## Customer Goals

- To view the products available
- To buy functional office like products but with a customized feel.
- To navigate easily through the website
- To be able to pay securely for items
- To be confident that the site is genuine and trustworthy

---
# User Stories

Using the Agile approach Epics (Github Milestones) were created and broken down into User Stories (Github Issues). User Stories were planned out with Acceptance Criteria and Tasks assigned to each. Acceptance criteria was used in measuring testing outcomes (see [TESTING.md](https://github.com/Charte-dot/Coder-Space/blob/main/TESTING.md) ).

User Stories were sorted into Three priority levels with 1 as top priority and 3 as least prioritised. User Stories with Priority 1 were allocated a label of 1 as 'must-have', 2 as 'should-have', 3 as 'could-have'. These User Stories were divided into three Iterations (Github Projects). Some user stories have been allocated a label of 'could-have' and feature on the kanban board in iteration 3. These user stories are in the to-do column and can be previewed in the [Future Features](#future-features) section of the READ.me. User stories in the kanban board which were not implemented are marked "F" for Future Feature in the table below. One of the issues has a 'B' in the priority column this is due to on going bug. More information regarding this in [TESTING.md](https://github.com/Charte-dot/Coder-Space/blob/main/TESTING.md).

| User Story ID | As A/An | I want to be able to | So that I can | | # | Priority | Iteration |
|---------------|--------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---|-----|----------|----------:|
| EPIC | Enable users to view and navigate the site | | | | | |
| 1 | | | | | | | |
| 1.1 | Shopper | View a list of products | Select some to purchase | |[#1](https://github.com/Charte-dot/Coder-Space/issues/1)| 1 | 1 |
| 1.2 | Shopper | View Individual Products  | See the price and product description | |[#2](https://github.com/Charte-dot/Coder-Space/issues/2)| 1 | 1 |
| 1.3 | Shopper |identify each category or product available  | find the exact product I need | |[#3](https://github.com/Charte-dot/Coder-Space/issues/3)| 1 | 1 |
| 1.4 | Shopper |Easily identify the total cost of my purchases at all times | Keep track of total cost. | |[#4](https://github.com/Charte-dot/Coder-Space/issues/4)| 1 | 2 |
| 1.5 | Shopper | I want to be able to view more information about the store  | increase my confidence that the store is genuine, trustworthy and reliable to purchase from | |[#5](https://github.com/Charte-dot/Coder-Space/issues/5)| 1 | 3 |
| 1.6 | Shopper | View a review on products |  decide if a product will suit my needs | |[#6](https://github.com/Charte-dot/Coder-Space/issues/6)| 1 | 2 |
| 1.7 | Shopper | I can View a social media page for more info on products | any offers or extra content from the store | |[#7](https://github.com/Charte-dot/Coder-Space/issues/7)| 1 | 1 |
| 1.8 | Shopper |I can View the average ratings on a product | get an idea of the quality of a product at a glance| |[#8](https://github.com/Charte-dot/Coder-Space/issues/8)| F | 2 |
| 1.9 | Shopper |I can View a list of FAQ's,  | easily find answers about the site | |[#9](https://github.com/Charte-dot/Coder-Space/issues/9)| F | 3 |
| 1.10 | Shopper |I can create a wish list, | come back at a late date to purchase | |[#10](https://github.com/Charte-dot/Coder-Space/issues/10)| F | 3 |
| EPIC | | Enable user Sorting and searching functionality | | | | | |
| 2 | | Sorting and searching | | | | | |
| 2.1 | Shopper |Sort the list of available products available, | easily find the product I am looking for.| |[#16](https://github.com/Charte-dot/Coder-Space/issues/16)| F | 3 |
| 2.2 | Shopper |I want to be able to easily see what I have searched for and the number of results| quickly see how many products are available.| |[#17](https://github.com/Charte-dot/Coder-Space/issues/17)| 1 | 2 |
| EPIC | Enable users to Register and manage own account | | | | | |
| 3 | |  | | | | | |
| 3.1 | Shopper |I can register for an account |  have a personal account to be able to save details and view previous orders| |[#11](https://github.com/Charte-dot/Coder-Space/issues/11)| 1 | 1 |
| 3.2 | Shopper |I can Easily login and logout of my account| access my own account on the site| |[#12](https://github.com/Charte-dot/Coder-Space/issues/12)| 1 | 1 |
| 3.3 | Shopper | I can recover my password hassle free should I forget it | gain access to my account.| |[#13](https://github.com/Charte-dot/Coder-Space/issues/13)| 1 | 1 |
| 3.4 | Shopper |Have a confirmation email to advise that registration has been successful | Have acknowledgement that my registration details were accepted and saved.| |[#14](https://github.com/Charte-dot/Coder-Space/issues/14)| 1 | 1 |
| 3.5 | Shopper |I can have a personal profile, | View my personal details for delivery and payment and update as needed | |[#15](https://github.com/Charte-dot/Coder-Space/issues/15)| 1 | 1 |
| EPIC | Enable users a safe and secure checkout | | | | | |
| 4 | | | | | | | |
| 4.1 | Shopper | select the quantity of a product that I am purchasing | visually see the correct quantity and modify if needed.| |[#18](https://github.com/Charte-dot/Coder-Space/issues/18)| 1 | 2 |
| 4.2 | Shopper |View items as they are placed in my basket | keep account of the total cost of the purchase| |[#19](https://github.com/Charte-dot/Coder-Space/issues/19)| 1 | 2 |
| 4.3 | Shopper | modify the quantity of each item in my basket | make changes to my purchase before I checkout| |[#20](https://github.com/Charte-dot/Coder-Space/issues/20)| 1 | 2 |
| 4.4 | Shopper | enter my payment details hassle free | checkout my purchases quickly and easily.| |[#21](https://github.com/Charte-dot/Coder-Space/issues/21)| 1 | 2 |
| 4.5 | Shopper |  Give my personal payment details and information and know its secure and safe | Be confident to be able to provide the necessary information to make a purchase.| |[#22](https://github.com/Charte-dot/Coder-Space/issues/22)| 1 | 3 |
| 4.6 | Shopper |  receive an order confirmation after order has been placed |  have an written record of my purchases| |[#23](https://github.com/Charte-dot/Coder-Space/issues/23)| 1 | 2 |
| 4.7 | Shopper | receive an confirmation email after order has been placed | have an written record of my purchases.| |[#31](https://github.com/Charte-dot/Coder-Space/issues/31)| B | 3 |
| EPIC | Set up admin to manage site | | | | | |
| 5 | | | | | | | |
| 5.1 | Site Owner | a product that I am purchasing | add new items to the site when needed.| |[#24](https://github.com/Charte-dot/Coder-Space/issues/24)| 1 | 2 |
| 5.2 | Site Owner | can select the quantity of a product that I am purchasing | change information on a product as needed.| |[#25](https://github.com/Charte-dot/Coder-Space/issues/25)| 1 | 3 |
| 5.3 | Site Owner | delete products |  remove Items no longer for sale.| |[#26](https://github.com/Charte-dot/Coder-Space/issues/26)| 1 | 3 |
| EPIC | Enable Users to interact with the site  | | | | | | |
| 6 | |  | | | | | |
| 6.1 | Shopper | rate a Product | give feedback to other shoppers.| |[#27](https://github.com/Charte-dot/Coder-Space/issues/27)| 3 | 3 |
| 6.2 | Shopper | review Products | give a good view to other shoppers of the product.| |[#28](https://github.com/Charte-dot/Coder-Space/issues/28)| 1 | 3 |
| 6.3 | Shopper | contact the store with any product or purchase queries | resolve any product or purchase issues I may have.| |[#29](https://github.com/Charte-dot/Coder-Space/issues/29)| 1 | 3 |
| 6.4 | Shopper | sign up to a newsletter | keep up to date with new products that become available.| |[#30](https://github.com/Charte-dot/Coder-Space/issues/30)| 1 | 3 |
---

# SEO and Web Marketing

- SEO 

Research on short and long-tail keywords was conducted via google searches to find the search words and phrases that most related to a site like Coder Space. "Personalized" was found to be particularly useful to a good search result when incorporated with the product categories ("Chairs", "Desks", "lights"). Keywords were incorporated into the meta tags and headings where appropriate while not overloading the site content and maintaining the usefulness of the site.

- Web Marketing

Paid web advertising is not currently within the scope of this project. However a newsletter link has been added to the website as an easy way for a small business such as Coder Space to reach customers and keep them up to date with new products, special offers and to keep the ecommerce store fresh.

- Facebook Business Page

As part of the scope of this project, social media marketing was a key element. Due to a change in Facebook's policy, creating a fake business page is against community standards. In place of a live facebook business page, a mock up of what the Facebook business page would have appeared to customers. 

![Coder Space Facebook Business Page](documentation/screenshots/fb-store.png)

- Privacy Policy

A privacy policy is a legal requirement because of GDPR legislation. This also benefits the website as it looks professional and more importantly inspires trust in the website user. A link to the privacy policy page is included in the footer.

![Privacy](documentation/screenshots/privacy.jpg)

---
# Scope

- Requirements

The approach taken was to create a minimum viable product to create a functioning ecommerce store with the ability to view and purchase a product via a seamless payment facility (in this case Stripe).

The User Stories were prioritised as described [above](#user-stories) and shown in the table with functional requirements prioritised as 1

## Structure

The website consists of thirteen pages:
- Home page with shop now button.
- Products page were the user can view all products available.
- Product details page where the user can view individual products in greater detail.
- A profile page that registered users can view their previous orders.
- An accounts page for registering, loging in and loging out.
- Products management page for admin to create, update, edit and delete products.
- A contact page for users to contact store owners.
- An about page to give more information about the store.
- A newletter subscription and unsubscription page.
- A review page for users to leave reviews on products.
- A shopping bag page that users can view products they placed in their bag.
- A checkout page with functional payment section.
- Confirmation of order page which saves in users profile if logged in.

## Database

For this project the PostgreSql database ElephantSQL was used from mid-point in the project due to changes with Heroku. A fixtures file was used for this project due to the amount of products within the project. I used the fixtures file provide the Boutique Ado walkthrough as a template and modified the files with [json file editor](https://jsonformatter.org/json-editor) to add and create my own fixtures file for categories and products.

## Models

As required by the project brief, three custom models were to be created and include within the project along side the other models that create the site.
The three custom models created and implemented for the purpose of this ecommerce store: Reviews, Newsletter subscription and a Contact form.

- Reviews Model:
A simple review model that allows uses to leave a review on products through the products details page.
Admin can delete the reviews from the admin panel. A possible future feature of reviews appearing with in admin profile on the site for easy monitoring. 

![Reviews](documentation/screenshots/cust-mod-review.jpg)


- Contact Model:
A contact model that complements the implementation of a contact form for Users to contact the ecommerce with any queries or complaints. Admin can view any messages from the contact form with in the admin panel.

![Contact](documentation/screenshots/cust-mod-contact.jpg)


- Newsletter subscription model:
A simple newsletter subscription model that allows the user to subscribe to an online newsletter from Coder Space. A link within the the subscription page also allows the user to unsubscribe. Admin can view subcribers to the newsletter form the admin panel and an email is auto sent to the subcriber advising of the newsletter subscription.

![Newsletter](documentation/screenshots/cust-mod-sub.jpg)

---

## Skeleton

### Wireframes
Wireframe created to help assist the design element and keep the project within the original design idea.
Some elements have been changed for a more appealing design on the final project.

- Home Page

![Home](documentation/wireframes/1-main-page-wireframe.jpg)


- Products Page

![Products](documentation/wireframes/2-products-wireframe.jpg)


- Product Details Page

![Product details](documentation/wireframes/3-product-details-wireframe.jpg)


- Add to bag Page

![Add to bag](documentation/wireframes/4-add-to-bag-wireframe.jpg)


- Bag Page

![Bag](documentation/wireframes/5-bag-wireframe.jpg)


- Checkout Page

![Checkout](documentation/wireframes/6-checkout-page.jpg)


- Sign-in Page

![Sign in](documentation/wireframes/7-sign-in-wireframe.jpg)


- Register Page

![Register](documentation/wireframes/8-register-wireframe.jpg)


- Profile Page

![Profile](documentation/wireframes/9-profile-wireframe.jpg)


- Contact Page

![Home](documentation/wireframes/10-contact-wireframe.jpg)