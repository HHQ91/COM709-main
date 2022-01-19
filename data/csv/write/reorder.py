import csv

file_path = '../songs.csv'
dest_file_path = 'output.csv'

with open(file_path, 'r') as file:

    csv_reading = csv.reader(file)
    header = next(csv_reading)
    print(header)
    with open(dest_file_path, 'w') as output:
        output.write(f'{header[3]},{header[2]},{header[1]},{header[0]}')
        for values in csv_reading:
            output.write(f'\n{values[3]},{values[2]},{values[1]},{values[0]}')
