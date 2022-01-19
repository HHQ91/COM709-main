import sqlite3
db = sqlite3.connect('C:/Users/Hasan Al-Qaysi/Desktop/ass/Orinoco')
cursor = db.cursor()

import  option1


def insert(shopper_id):

    categories_query  = """SELECT category_id, category_description FROM categories"""
    cursor.execute(categories_query)
    show_categories = cursor.fetchall()
    #print(show_categories)
    cat_id= option1._display_options(show_categories, "Categories", "category")
    product_query= """ SELECT product_id, Product_description from products
                WHERE category_id = ?"""
    cursor.execute(product_query, (cat_id,))
    show_products = cursor.fetchall()
    #print(show_products)
    pro_id = option1._display_options(show_products, "Products", "product")
    #print(type(pro_id))
    seller_id_que = """ SELECT s.seller_id, seller_name, product_id, price FROM product_sellers ps
    INNER JOIN sellers s ON ps.seller_id = s.seller_id
    WHERE product_id = ?
    """
    cursor.execute(seller_id_que, (pro_id,))
    show_seller_name = cursor.fetchall()
    #print(show_seller_name)
    if show_seller_name:
        selected_seller_id = option1._display_options(show_seller_name, "Sellers who sell this product", "seller")

    #print(pro_id)
    #print(selected_seller_id)

    quantitiy = int(input("Please enter the quantity you want to buy "))
    #print(f" The total price for the selected products for this supplier is : {price} ")
    seller_price = """SELECT s.seller_id, seller_name, price

                FROM sellers s

                INNER JOIN product_sellers ps ON ps.seller_id = s.seller_id

                WHERE product_id = ?"""
    cursor.execute(seller_price, (pro_id,))
    seller_prices = cursor.fetchall()
    select_seller_price = option1._display_options(seller_prices,"Sellers", "seller", selle_prices=True)
    print(select_seller_price)
    price_query = """ SELECT price FROM product_sellers WHERE product_id = ?
                                                        AND seller_id = ?
        """
    cursor.execute(price_query, (pro_id, select_seller_price))
    price = cursor.fetchone()[0]
    print(price)


    shopper_baskets_query = """
                    SELECT * FROM shopper_baskets
                    ORDER BY basket_id DESC
                    limit 1
                    """


