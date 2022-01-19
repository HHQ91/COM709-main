import sqlite3
import option1
import option2
import option3
import option4

db = sqlite3.connect('C:/Users/Hasan Al-Qaysi/Desktop/ass/Orinoco')
cursor = db.cursor()
shopper_id = int(input("Please enter the shopper ID"))
cursor.execute("""SELECT shopper_id FROM shoppers WHERE shopper_id = ? """, (shopper_id,))
shopper = cursor.fetchone()
#shopper_id = shopper[0]
if shopper :
   choice= int(input("""1.	Display your order history
2.	Add an item to your basket
3.	View your basket
4.	Checkout
5.	Exit
"""))
   if choice == 1:
      option1.view_order(shopper_id)
   elif choice == 2:
      option2.insert(shopper_id)
   elif choice == 3:
      option3.show_basket(shopper_id)
   elif choice == 4:
      option4.checkout_basket(cursor,shopper_id)
   elif choice == 5:
      print("Thank you... see you later")
      exit()
   else:
      print("You did not make a valid selection.")
else:
   print("your shopper ID is not in our Database")



