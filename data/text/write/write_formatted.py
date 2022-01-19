file_path = input("Ente file directory") or "output.txt"
lines = ["This is the first line.", "This is the second.", "This is the third line."]

try:

    with  open(file_path, 'w') as file: #this way do have to close the file
        for line in lines:
            file.write(f'{line}\n')
            print("The data has been written to the file.")
except IOError:
    print("Cannot write (-_-)")