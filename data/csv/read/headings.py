import csv

file_path = '../songs.csv'


try:
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        heading = next(csv_reader)
        print(f"{heading[0]},{heading[1]},{heading[2]},{heading[3]}")

except IOError:
    print("cannot read file.")