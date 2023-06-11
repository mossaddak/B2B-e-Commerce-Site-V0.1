# Sing Up
post => http://127.0.0.1:8000/user-account/sing-up

required field: 

    {
        "email":"demomail@gmail.com",
        "password":"1234",
        "first_name":"Mossaddak",
        "last_name":"Hossain"
    }

# Account Verification
-)First:

    need to hit this url, user must need loged in. there is no need any field. after hit this user will get an otp through the email:

    post => http://127.0.0.1:8000/account/send-code

-)Second:

    then you have to hit the below link with the otp you got through the email 

    post => http://127.0.0.1:8000/account/verification

    required field:

        {
            "otp":"12279"
        }

# Login
post => http://127.0.0.1:8000/user-account/login

required fields:

    {
        "email":"10000mossaddak1@gmail.com",
        "password":"1234"
    }

# Profile Picture

post, get, delete, patch => http://127.0.0.1:8000/account/profile-picture/

required field: img

Note: Authentication Mandetory

# Profile 
post, patch => http://127.0.0.1:8000/account/profile

required fields:

    {
        "id": 16,
        "username": "mossaddak1",
        "first_name": "Mossaddak",
        "last_name": "",
        "email": "demomail1@gmail.com"
    }

Note: Here have to pass "username" field for patching


# Account Recovery

<b>Send OTP to the mail:

post => http://127.0.0.1:8000/recovery/account/otp-sent

required fields:

    {
        "email":"demo@gmail.com"
    }

<b>Set New Password:</b>

post => http://127.0.0.1:8000/recovery/account/set-new-password

required fields:

    {
        "password_reset_token":"56411416043889561",
        "new_password":1234
    }


# How to create app password?
=)
    go to this link: https://myaccount.google.com/?hl=en_GB&utm_source=OGB&utm_medium=act

    then,

        security > 2 step verification > sing into your account > App passwords(it will get in bottom) > select app(other) > give a name > click generate


# Shop

<h2>Category Create, Update, Delete, Details:</h2>

    post, get => http://127.0.0.1:8000/categories

    details, put => http://127.0.0.1:8000/categories/{slug}

reqyured field:

    {
        "title":"Electronics"
    }


<h2>Shop Create, Update, Delete, Details:</h2>

    post, get => http://127.0.0.1:8000/me/shops

    details, put => http://127.0.0.1:8000/me/shops/<slug>

required field:

    {
        "title": "shop1",
        "category_title": "Electronics"
    }

<h2>Shop activation</h2>

<p>Just hit this below URL:</p>

    post => http://127.0.0.1:8000/me/shops/activate/

requirde fields:

    {
        "_id":"0aa0aaa3-3d58-4d07-ba50-071601c698c5"
    }
    
<b>Note: _id = Shop Id</b>


<h2>Get all shop</h2>

    get => http://127.0.0.1:8000/shop/all/



<h2>Shop to shop connection</h2>

post, get => http://127.0.0.1:8000/shop/connection/

required fields:

    {
        "_id":"6b76a493-ed10-40a6-9eaf-aa8ad25b2bf3"
    }

<b>Note: _id = Shop Id you want to sent connection</b>

<h2>Accept shop connection</h2>

required fields:

    {
        "_id":"6b76a493-ed10-40a6-9eaf-aa8ad25b2bf3"
    }

<b>Note: _id = Shop Id you want to sent connection</b>


# Product 

<h2>Product add</h2>

post => http://127.0.0.1:8000/products

required fields:

    title, desc, price, img

Note: These are form data

<h2>My Product list</h2>

post => http://127.0.0.1:8000/product/my-products

<h2>All Product list</h2>

get => http://127.0.0.1:8000/product/products


<h2>Product Details</h2>

get, put, delete => http://127.0.0.1:8000/product/products/<slug>

# Shopping Cart

add cart => http://127.0.0.1:8000/cart/add

get cart => http://127.0.0.1:8000/cart/my-carts

required fields:

    {
        "product_id":"2e059b50-9d9d-4ee9-9677-533f5360f772"
    }


# Order Product

order product:

post => http://127.0.0.1:8000/orders/order-products

<p>Just hit the URL</p>






