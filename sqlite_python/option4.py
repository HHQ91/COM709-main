import sqlite3
db = sqlite3.connect('C:/Users/Hasan Al-Qaysi/Desktop/ass/Orinoco')
cursor = db.cursor()
import option1

def checkout_basket (cursor,shopper_id):
       checkout =  """ SELECT p.product_description, s.seller_name, bc.quantity,bc.price AS Price,
                bc.quantity*bc.price AS Total
                FROM sellers s
                INNER JOIN product_sellers ps ON s.seller_id = ps.seller_id
                INNER JOIN products p ON ps.product_id = p.product_id
                INNER JOIN basket_contents bc ON ps.seller_id = bc.seller_id
                INNER JOIN shopper_baskets sb ON bc.basket_id = sb.basket_id
                WHERE shopper_id = ?"""
       cursor.execute(checkout,(shopper_id,))
       shopper_checkout = cursor.fetchall()
       if shopper_checkout:
           print("Basket contents:\n---------------------------")

           print(
               "{0:25} {1:20} {2:10} {3:15}  £{4:15}".format("Product Description", "Seller name", "Qty", "Price",
                                                                    "Total"))

           for order in shopper_checkout:
               product_description = order[0]
               seller_name = order[1]
               qty = order[2]
               price = order[3]
               total = order[4]

               print("{0:25} {1:20} {2:10} {3:15}  £{4:15}".format(product_description, seller_name, qty, price, total))

       else:
           print("No orders for this customer")

       checks = """ SELECT sda.delivery_address_line_1, sda.delivery_address_line_2, sda.delivery_address_line_3
                FROM shopper_orders sho
                INNER JOIN shopper_delivery_addresses sda ON sho.delivery_address_id = sda.delivery_address_id
                WHERE sho.shopper_id = ?
                ORDER BY order_date DESC"""
       cursor.execute(cursor,checks, shopper_id)
       show_address = cursor.fetchall()
       if show_address :
           add = option1._display_options(show_address,"Address","address")
       else:
           address_line_1 = input("Enter the delivery address line 1: ")
           address_line_2 = input("Enter the delivery address line 2: ")
           address_line_3 = input("Enter the delivery address line 3: ")
           country = input("Enter the delivery country: ")
           post_code = input("Enter the delivery post code: ")
           address_insert = """INSERT INTO shopper_delivery_addresses (delivery_address_line_1, delivery_address_line_2, delivery_address_line_3,
                                            delivery_county, delivery_post_code)
                                            VALUES(?, ?, ?, ?, ?)
                                        """

           cursor.execute(address_insert, (address_line_1,address_line_2, address_line_3, country, post_code))
           cursor.fetchall()
           db.commit()

       card_query = """        
               SELECT spc.payment_card_id, card_type, card_number
               FROM shopper_payment_cards spc
               INNER JOIN shopper_orders so ON so.payment_card_id = spc.payment_card_id
               WHERE so.shopper_id = ?
               GROUP BY spc.payment_card_id"""

       cards = cursor.execute(cursor, card_query, shopper_id)

       if cards:
            selected_card_id = option1._display_options(
                cards, "Checkout cards", "card")


       else:
            print("please inter your card details")
            type = ["Visa", "Mastercard"]
            display_cards = option1._display_options(type, "Cards type", "card")




