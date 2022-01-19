import os

try:
    print("Program Started")

    letter = input("Please enter a standard character")

    if len(letter) == 1:

        value = ord(letter)

        print(f"The ASCII code for {letter} is {value}")

    print("Program Ended")

except IOError:
    print("cannot read file.")