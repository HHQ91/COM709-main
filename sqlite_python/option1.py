import sqlite3
db = sqlite3.connect('C:/Users/Hasan Al-Qaysi/Desktop/ass/Orinoco')
cursor = db.cursor()



def _display_options(all_options,title,type,selle_prices=False):
    option_num = 1
    option_list = []
    print("\n",title,"\n")
    if selle_prices:
        for option in all_options:
            code = option[0]
            desc = option[1]
            price = option[2]
            print("{0}.\t{1}\t{2}".format(option_num, desc,price))
            option_num = option_num + 1
            option_list.append(code)
    else:

        for option in all_options:
            code = option[0]
            desc = option[1]
            print("{0}.\t{1}".format(option_num, desc))
            option_num = option_num + 1
            option_list.append(code)
    selected_option = 0
    while selected_option > len(option_list) or selected_option == 0:
        prompt = "Enter the number against the "+type+" you want to choose: "
        selected_option = int(input(prompt))
    return option_list[selected_option - 1]


def view_order(shopper_id):
    view_query = """SELECT sho.order_id AS "Order ID", sho.order_date AS "Order date", p.product_description AS "Product Description" ,
          s.seller_name AS Seller, op.price AS Price , op.quantity AS Qty, op.ordered_product_status AS Status
          FROM shopper_orders sho
          INNER JOIN ordered_products op ON sho.order_id= op.order_id
          INNER JOIN product_sellers ps ON ps.product_id= op.product_id
                                       AND ps.seller_id= op.seller_id
          INNER JOIN products p ON ps.product_id=p.product_id
          INNER JOIN sellers s ON ps.seller_id= s.seller_id
          WHERE sho.shopper_id= ?
          GROUP BY sho.order_id, op.product_id
          ORDER BY order_date DESC"""
    cursor.execute(view_query, (shopper_id,))
    shopper_orders = cursor.fetchall()
    if shopper_orders:

        print(
            "{0:4} {1:10} {2:70} {3:20}  £{4:5} {5:9} {6:15} ".format("OrderID", "Order Date", "Product Description",
                                                                        "Seller", "Price", "Qty", "Status"))

        for order in shopper_orders:
            order_id = order[0]
            order_date = order[1]
            product_description = order[2]
            seller = order[3]
            price = order[4]
            Qty = order[5]
            status = order[6]

            print("{0:4} {1:10} {2:70} {3:20}  £{4:5} {5:3}  {6:15} ".format(order_id, order_date, product_description, seller, price, Qty, status))

    else:
        print("No orders for this customer")



# view_order(10001)