import os

try:
    def ascii_to_number_systems(number):
        for x in range(number):
            character = input("PLease enter a character")
            character = ord(character)
            print(f"The ASCII representation of  {character} ")
            print(f"The binary representation of this is {bin(character)}")
            print(f"The octal representation of this is {oct(character)}")
            print(f"The hexadecimal representation of this is {hex(character)}")


    ascii_to_number_systems(2)

except IOError:
    print("Invalid input")