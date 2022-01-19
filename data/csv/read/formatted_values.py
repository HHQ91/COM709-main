import csv

file_path = '../songs.csv'

try:
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        heading = next(csv_reader)

        for line in csv_reader:
            print(f"[{line[3]}] {line[0]} (by {line[2]})")


except IOError:
    print("cannot read file.")