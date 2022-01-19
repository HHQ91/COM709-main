import csv
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


        selection = int(input("""
          [1] Display the names of all passengers
          [2] Display the number of passengers that survived
          [3] Display the number of passengers per gender
          [4] Display the number of passengers per age group
          [5] Display the number of survivors per age group
                         """))

        print(f"You have selected the option {selection}")


        if selection == 1:
            print("The names of the passengers are..." )
            for record in records:
                print(record[3])

        elif selection == 2:
            num_survived = 0
            for record in records:
                if record[1] == '1':
                    num_survived +=1

            print(f"{num_survived} passengers survived")


        elif selection == 3:
            females = 0
            males = 0
            for record in records:
                females += 1 if record[4] == "female" else 0
                males += 1 if record[4] == "male" else 0

            print(f"Females: {females}, males: {males}")

        elif selection == 4:
            children, adults , elderly = 0,0,0
            for record in records:
                if record[5]:
                    age = float(record[5])
                    if age < 18:
                        children +=1
                    elif age < 65:
                        adults +=1
                    else:
                        elderly +=1

            print(f"children: {children}, adults: {adults}, elderly: {elderly}")

        elif selection == 5:
            children, adults, elderly = 0, 0, 0
            children_sur, adults_sur, elderly_sur = 0, 0, 0
            #print(f"childred is {children}")
            for record in records:
                if record[5]:
                    age = float(record[5])
                    survive = int(record[1])
                    if age < 18:
                        children += 1
                        children_sur +=1 if survive else 0
                    elif age < 65:
                        adults += 1
                        adults_sur += 1 if survive else 0
                    else:
                        elderly += 1
                        elderly_sur += 1 if survive else 0

            print(f"children: {children}/{children_sur}, adults: {adults}/{adults_sur}, elderly: {elderly}/{elderly_sur}")


except IOError:
  print("Could need to read file.")
if __name__ == "__main__":
    import doctest
    doctest.testmod()