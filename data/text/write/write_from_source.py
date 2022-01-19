file_path = input("Ente read file directory") or "../read/quotes.txt"
out_path = input("Enter write file directory") or "output.txt"
list = []
try:
    with open(file_path) as read_file:
        for line in read_file.readlines():

            list.append(line.strip())

    with open(out_path, 'w') as out_file: #this way do have to close the file
        for item in list:

            out_file.write(f'{item}\n')

except IOError:
    print("Cannot access the file (-_-)")

