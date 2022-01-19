import csv

file_path = '../songs.csv'

try:
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        heading = next(csv_reader)

        for line in csv_reader:
            print(line[0])


except IOError:
    print("cannot read file.")