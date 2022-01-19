import csv

file_path = "numbers.csv"

def to_binary(number):

    print(f"{number} as binary: {bin(number)}")


def to_octal(number):
    print(f"{number} as octal: {oct(number)}")


def to_hex(number):
    print(f"{number} as hexadecimal: {hex(number)}")


if __name__ == "__main__":

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for value, base in csv_reader:
                if base == "2":
                    to_binary(int(value))
                elif base == "8":
                    to_octal(int(value))
                elif base == "16":
                    to_hex(int(value))
                else:
                    print("Unknown base format")


    except IOError:
        print("Error 404")




