import csv

with open('movies.csv', encoding="utf8") as file:
    csv_reader = csv.reader(file)
    heading = next(csv_reader) # pass the heading row
    # print(heading)
    # print('Space')

    for values in csv_reader:
        print(values)
