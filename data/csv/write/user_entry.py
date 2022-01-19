import csv

file_path = 'user_entries.csv'

with open(file_path, 'a') as file:
    file.write('Year, Artist Song, Song Title\n')

    for count in range(3):
        year = int(input("Enter the Year"))
        Artist_Song = input("Enter Artist Song")
        Song_Title = input("Enter Song Title")

        file.write(f"{year}, {Artist_Song}, {Song_Title}\n")