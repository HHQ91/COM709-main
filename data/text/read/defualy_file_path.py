file_path = input('Enter file path') or 'quotes.txt'

try:

    with open(file_path) as file:
        print(file.readlines())


except IOError:
    print('Pleaseq enter an accessible file name')