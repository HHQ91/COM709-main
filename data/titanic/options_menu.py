import  csv

file_path = "titanic.csv"
records = []
try:
    print("Loading data....", end="")
    with open(file_path) as file:
        csv_reading = csv.reader(file)
        heading = next(csv_reading)
        count = 0
        for line in csv_reading:
            records.append(line)
        print("Done!")
        print(f"Successfully loaded {len(records)} records.")


except IOError:
  print("Could need to read file.")