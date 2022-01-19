import os

try:
    def run():
        print("Program Started")
        number = int(input("Please enter a whole number:"))
        oct_hex = input("octal or hex..?")
        if oct_hex == "octal":
            print(f"The octal representation of  {number} is {oct(number)}")
        elif oct_hex == "hex":
            print(f"The octal representation of  {number} is {hex(number)}")
        else:
            yn = input("invalid input try again? y/n")
            if yn == 'y':
                run()

        print("Program Ended")

    run()
except   IOError:
    print("Invalid input")