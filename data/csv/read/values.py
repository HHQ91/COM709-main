import csv

file_path = '../songs.csv'


try:
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        heading = next(csv_reader)
        print(heading, '\n')

        for line in csv_reader:
            print(f"{line[0]},{line[1]},{line[2]},{line[3]}")


except IOError:
    print("cannot read file.")