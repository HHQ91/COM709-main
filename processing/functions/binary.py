import os

try:
    def run():
        print("Program Started")
        number = int(input("Please enter a whole number:"))

        print(f"The binary representation of  {number} is {bin(number)}")
        print("Program Ended")

    run()
except   IOError:
    print("Invalid input")