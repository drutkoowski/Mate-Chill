# Mate&Chill
<p align="center">
  <img src="/readme/main_image.png?raw=true" alt="Mate-Chill"/>
</p>

> Mate&Chill is an ecommerce web application with products mainly related to Yerba Mate.<br>

Live demo <br>
• [Polish](http://18.192.210.224) <br>

**Dummy user credentials** <br>
<b> Username</b>: testing@o2.pl <br>
<b> Password</b>: testing123


**Doomie card data to test payments** <br>
Number: 4242 4242 4242 4242 <br>
Exp date: 12/34 <br>
CVV: 123 <br>

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
Mate&Chill is an e-commerce (online store) web application. <br>
Thanks to this application users can order products, which can be easily entered by the site administrator (the seller) using the admin panel, which has been specially adapted for this purpose. <br>
The project was made mainly using Django REST Framework and Vue.js, payments functionality is handled by Stripe API which is connected to backend API using webhook.


## Technologies Used
- <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20" align='center'/> Python 3.11.1 &nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="Django" alt="Django" width="20" height="20" align='center'/> Django 4.1.6 &nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="Django" alt="Django" width="20" height="20" align='center'/> DRF 3.14.0 (http-only cookie auth) &nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original-wordmark.svg" title="HTML5" alt="HTML5" width="20" height="20" align='center'/> HTML5&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/sass/sass-original.svg" title="SASS" alt="SASS" width="20" height="20" align='center'/> SASS&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/tailwindcss/tailwindcss-original-wordmark.svg" title="Tailwind" alt="Tailwind" width="20" height="20" align='center'/> Tailwind&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" title="JavaScript" alt="JavaScript" width="20" height="20" align='center'/> JavaScript ES6+&nbsp;
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Vitejs-logo.svg/1039px-Vitejs-logo.svg.png" title="Vite" alt="Vite" width="20" height="20" align='center'/> Vite&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/vuejs/vuejs-original.svg" title="Vue" alt="Vue" width="20" height="20" align='center'/> Vue&nbsp;
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Axios_logo_%282020%29.svg/1200px-Axios_logo_%282020%29.svg.png" title="Axios" alt="Axios" width="20" height="20" align='center'/> Axios&nbsp;
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Stripe_Logo%2C_revised_2016.svg/512px-Stripe_Logo%2C_revised_2016.svg.png?20210114172858" title="Stripe" alt="Stripe" width="20" height="20" align='center'/> Stripe&nbsp;


### :hammer_and_wrench: Tools & Deployment:
- <img src="https://github.com/devicons/devicon/blob/master/icons/pycharm/pycharm-original.svg" title="PyCharm" alt="Pycharm" width="20" height="20" align='center'/> PyCharm&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-plain-wordmark.svg" title="MySql" alt="MySql" width="20" height="20" align='center'/> MySQL (development)&nbsp;
- <img src="https://symbols.getvecta.com/stencil_9/32_aws-elastic-beanstalk.3cbb564d52.svg" title="AWS" alt="AWS" width="20" height="20" align='center'/> AWS EC2&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/nginx/nginx-original.svg" title="Nginx" alt="Nginx" width="20" height="20" align='center'/> Nginx&nbsp;
- <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="20" height="20" align='center'/> Docker&nbsp;

## Features
List the ready features here:
- Creating an account
- Searching for product by name
- Searching for products by categories
- Searching for products by subcategories
- Searching for products by price
- Ordering products
- Displaying single product
- Adding review to product (for users who bought it) or viewing it
- Adding product to cart
- Product variations
- Customized Admin Panel
- Paying for the product

## Screenshots
![name](/readme/main_image.png)


![name](/readme/photo_1.png)


![name](/readme/photo_2.png)


![name](/readme/photo_3.png)


![name](/readme/photo_4.png)


![name](/readme/photo_5.png)


![name](/readme/photo_6.png)


![name](/readme/photo_7.png)


![name](/readme/photo_8.png)


![name](/readme/photo_9.png)


![name](/readme/photo_10.png)


![name](/readme/photo_11.png)


![name](/readme/photo_12.png)


![name](/readme/photo_13.png)


![name](/readme/photo_14.png)


![name](/readme/photo_15.png)


![name](/readme/photo_16.png)
... and many more!

## Setup
1. Create New Folder <br>

2. Type <br>
> 'git clone https://github.com/drutkoowski/Mate-Chill.git' into the console/git cli <br>
Then <br>
> 'cd Mate-Chill' <br>

3. Create '.env' file in frontend and backend root directory<br>

4. Build Docker images <br>
>'docker-compose build'<br>

5. Aggregate the output of each container <br>
> 'django-compose up' <br>

**Backend will run at port 8000** <br>
**Frontend will run at port 5372** <br>

## Project Status
Project is: :fire: COMPLETED :fire:

## Improvements to be done
- Adding on sale functionality or discount codes
- Improving responsive layout
- Fixing some bugs

## Contact
Created by Damian Rutkowski - feel free to contact me!
<div id="badges">
  <a href="https://www.facebook.com/drutkoowski/">
    <img src="https://img.shields.io/badge/Facebook-blue?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook Badge"/>
  </a>
  
   <a href="mailto:d.rutkowski2000@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail Badge"/>
  </a>
  
  <a href="https://www.linkedin.com/in/damian-rutkowski-810428237/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  
</div>
