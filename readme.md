# Sing Up
post => http://127.0.0.1:8000/api/user-account/sing-up/

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

    post => http://127.0.0.1:8000/api/user-account/account-verify-code/

-)Second:

    then you have to hit the below link with the otp you got through the email 

    post => http://127.0.0.1:8000/api/user-account/verify/

    required field:

        {
            "otp":"12279"
        }

# Login
post => http://127.0.0.1:8000/api/user-account/login/

required fields:

    {
        "email":"10000mossaddak1@gmail.com",
        "password":"1234"
    }

# Profile Picture

post, get, delete, patch => http://127.0.0.1:8000/api/user-account/profile-picture/

required field: img

Note: Authentication Mandetory

# Profile 
post, patch => http://127.0.0.1:8000/api/user-account/profile/

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

post => http://127.0.0.1:8000/api/recovery-account/reset-password/

required fields:

    {
        "email":"demo@gmail.com"
    }

<b>Set New Password:</b>

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

<b>Category:</b>

    post, get => http://127.0.0.1:8000/api/shop/shop-category/

    details, put => http://127.0.0.1:8000/api/shop/shop-category/<slug>/

reqyured field:

    {
        "title":"Electronics"
    }


