import os

try:
    print("Program Started")
    code = abs(int(input("Please enter a ASCII code")))

    if code in range(32, 127) :
        character = chr(code)
        print(f"The character represented by ASCII code {code} is {character}")
    print("Program Ended")



except   IOError:
    print("cannot read file.")