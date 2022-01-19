file_path = input("Ente file directory") or "output.txt"

try:
    with  open(file_path, 'w') as file: #this way do have to close the file
        file.write("data has been overwritten!")
        print("The data has been written to the file.")

except IOError:
    print("Cannot write (-_-)")