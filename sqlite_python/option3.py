import sqlite3
db = sqlite3.connect('C:/Users/Hasan Al-Qaysi/Desktop/ass/Orinoco')
cursor = db.cursor()


def show_basket(shopper_id):
    view_basket = """SELECT p.product_description, s.seller_name, bc.quantity,bc.price AS Price,
            bc.quantity*bc.price AS Total
            FROM sellers s
            INNER JOIN product_sellers ps ON s.seller_id = ps.seller_id
            INNER JOIN products p ON ps.product_id = p.product_id
            INNER JOIN basket_contents bc ON ps.seller_id = bc.seller_id
            INNER JOIN shopper_baskets sb ON bc.basket_id = sb.basket_id
            WHERE shopper_id = ?"""
    cursor.execute(view_basket, (shopper_id,))
    shopper_basket = cursor.fetchall()
    sum = 0
    if shopper_basket:
        print("Basket contents:\n---------------------------")

        print(
            "{0:25} {1:20} {2:10} {3:15}  £{4:15} ".format("Product Description","Seller name", "Qty", "Price","Total"))

        for order in shopper_basket:
            product_description = order[0]
            seller_name = order[1]
            qty = order[2]
            price = order[3]
            total = order[4]

            print("{0:25} {1:20} {2:10} {3:15}  £{4:15} ".format(product_description,seller_name, qty,price , total))
            sum += order[4]
            print("\n\t\t\t\t\t{0:30}Basket Total:  £{1:7.2f}".format(" ", sum))

    else:
        print("No orders for this customer")

#show_basket(10000)