def Netflix():       #function to start the connection with database
    print('Enter the path file name')
    csv_name = input()
    return(csv_name)
def view_summery(info): # funtion to display the total number of movies in the database
    records = len(list(info))
    print(f'NUMBER OF MOVIES={records}')
def view_choises():
    print("please select one of the choises below")
    #retrieve the choices
    choice = int(input(""" 1.Retrieve the details for a specific movie
 2.	Retrieve the details for movies released in a specific year
 3.	Retrieve the details for movies that star a particular actor
 4.	Retrieve the top movies by rating for a specific country
 5.	Produce suitable and interesting visualisations (plots or graphs) for the
 data.
 6. Exit
 """))
    return(choice)
#Netflix()

def desplay_movies(list_movies,one_movie = False):
    if one_movie:
        name = list_movies[1]
        Duration = list_movies[2]
        year_of_production = list_movies[3]
        genre = list_movies[4]
        Director = list_movies[5]
        actors = list_movies[6]

        print(f"Details for:{name} movie")
        print(f"Movie Duration:{Duration} Min")
        print(f"Year of prodution:{year_of_production}")
        print(f"Genre:{genre}")
        print(f"Director:{Director}")
        print(f"actors: {actors}")

    else:
        for movie in list_movies:
            name = movie[1]
            Duration = movie[2]
            year_of_production = movie[3]
            genre = movie[4]
            Director = movie[5]
            actors = movie[6]
            country = movie[7]
            rating = movie[8]
            print(f"Details for:{name} movie")
            print(f"Movie Duration:{Duration} Min")
            print(f"Year of prodution:{year_of_production}")
            print(f"Genre:{genre}")
            print(f"Director:{Director}")
            print(f"actors: {actors}")
            print(f"country: {country}")
            print(f"rating: {rating}")
            print("##############")

def country_plots():
    country = input("Please enter the country name you want : ")
    return (country)