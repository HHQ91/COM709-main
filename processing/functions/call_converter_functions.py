import number_system_converter as nsc

if __name__ == "__main__":

    try:
        number = int(input("Enter a number"))

        nsc.to_binary(number)
        nsc.to_octal(number)
        nsc.to_hex(number)

    except IOError:
        print("Input Invalid")