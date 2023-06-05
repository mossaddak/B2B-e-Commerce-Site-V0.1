# Marchent

    marchent:{
        name:"Marchent Name",

        shops:{

            {
                "_id":345345343,
                "title":"Shop Name",

                "category":{
                    "_id":3434343,
                    "title":"Category Name"
                },

                "connection":{
                    1,
                    2,
                    3
                },

                "cart":{
                    "products":{
                        "_id":34334534,
                        "name":"demo name",
                    }
                }
            },
            {
                "_id":345345343,
                "title":"Shop Name",

                "category":{
                    "_id":3434343,
                    "title":"Category Name"
                },

                "connection":{
                    1,
                    2,
                    3
                }
            },

        }
    }

# Category

    "category":{
        "_id":3434343,
        "title":"Category Name"
    }

# Cart

    "cart":{
        "shop":{
            "_id":3434343,
            "name":"demo name"
        },
        "products":{
            "_id":34334534,
            "name":"demo name",
        }
    }

# Shop

    {
        "_id":345345343,
        "title":"Shop Name",

        "category":{
            "_id":3434343,
            "title":"Category Name"
        },

        "request_sender" = {
            "sender1":"mossaddak",
            "sender2":"kabir"
        },

        "connection":{
            1,
            2,
            3
        },

        "cart":{
            "products":{
                "_id":34334534,
                "name":"demo name",
            }
        }
    }