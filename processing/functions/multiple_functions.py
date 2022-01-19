

def to_binary(number):

    print(f"{number} as binary: {bin(number)}")


def to_octal(number):
    print(f"{number} as octal: {oct(number)}")


def to_hex(number):
    print(f"{number} as hexadecimal: {hex(number)}")

def run():
    char_input = input("Enter a Character")
    ascii = ord(char_input)
    print(f"The ASCII value of {char_input} is: {ascii}")
    to_binary(ascii)
    to_octal(ascii)
    to_hex(ascii)



if __name__ == "__main__":
  run()