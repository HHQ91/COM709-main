import os

try:
    def number_systems (number):
        print(f"The decimal representation of  {number} ")
        print(f"The binary representation of this is {bin(number)}")
        print(f"The octal representation of this is {oct(number)}")
        print(f"The hexadecimal representation of this is {hex(number)}")



    number_systems(33)
except IOError:
    print("Invalid input")