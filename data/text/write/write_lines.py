file_path = input("Ente file directory") or "output.txt"

try:
    with  open(file_path, 'w') as file: #this way do have to close the file
        file.writelines(["This is the first line.\n", "This is the second.\n", "This is the third line.\n"]
)
        print("The data has been written to the file.")

except IOError:
    print("Cannot write (-_-)")