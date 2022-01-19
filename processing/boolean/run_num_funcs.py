import num_funcs as nf

if __name__ == "__main__":

    try:
        selection = int(input("""
Please select an option:
        [1] Equal
        [2] Lower
        [3] Greater
        [4] In Range
        [5] Even
        [6] Odd
        [7] In List
        """))
        print(f"Selected option {selection}")

        if selection == 1:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            print("The numbers are equal.") if nf.is_equal(num1, num2) else print("The numbers are not equal.")
        elif selection == 2:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            print("Number 1 is lower than number 2") if nf.is_lower(num1, num2) else print("Number 1 is not lowe than number 2")
        elif selection == 3:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            print("Number 1 is greater than number 2") if nf.is_greater(num1, num2) else print("Number 1 is not greater than number 2")

        elif selection == 4:
            num = int(input("Please enter the number: "))
            lower_bound = int(input("Please enter the lower bound: "))
            upper_bound = int(input("Please enter the upper bound: "))
            print("Number is in the range") if nf.is_in_range(num, lower_bound, upper_bound) else print("Number is not in the range")
        elif selection == 5:
            num = int(input("Please enter the number: "))
            print("Number is even") if nf.is_even(num) else print("Number is not even")
        elif selection == 6:
            num = int(input("Please enter the number: "))
            print("Number is odd") if nf.is_odd(num) else print("Number is not odd")
        elif selection == 7:
            list = []
            num = int(input("Please enter a number "))
            list_number = int(input("Please enter number of elements in the list "))
            for n in range(0, list_number):
                element = int(input(f"Enter no.{n+1}"))
                list.append(element)
            print("Number is in the list") if nf.is_in_list(num, list) else print("Number is not in the list")

        else:
            print("Not valid input")

    except IOError:
        print("Invalid Input")