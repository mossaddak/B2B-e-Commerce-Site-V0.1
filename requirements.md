B2B Ecommerce Website Model design 

 
# User : 

    Username 

    Email 

    Password 

    Type : default=merchant 

    Tc 

# Category: 

    Category_name 

    Description 

# Shop : 

    Merchant = Foreignkey(User) 

    Name 

    Category =Foreignkey(category) 

    Activate_code  

    Is_Active  

# Product : 

    Shop = foreignkey 

    Product name  

    Description 

    price 

# Cart: 

    Shop = onetoone field(shop) 

    Cartitem: 

    Cart = foreignkey(cart) 

    Product =foreignkey(product) 

    Quantity 

# Connection: 

    Source_shop = foreignkey(shop) 

    Target_shop = foreignkey(shop) 

    Status = dropdown 