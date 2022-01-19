import csv
#import matplotlib.pyplotp as plt

def specific_movie_info(movie_data):
    print ("Please enter the movie name you want details for")
    movie_name = input()
    #print(movie_data)
    for movie in movie_data:
        if movie_name == movie[1]:
            return (movie)

# with open("movies.csv", encoding="utf8") as file:
#         csv_reader = csv.reader(file)
#         heading = next(csv_reader)
#         specific_movie_info(csv_reader)


def movies_released_in_a_specific_year(movie_year):
    print("please enter the movie year")
    movie_year_search = input()
    list_year = []
    for movie in movie_year:
        if movie_year_search == movie[3]:

            list_year.append(movie)
    return(list_year)

def movies_star_actor (movies_actor):
    print (" Which star actor you want to retrieve his\her movies")
    movies_star = input()
    list_actor_movies = []
    for movie in movies_actor:
        #print(movies_star)
        #print(movie[6])
        if movies_star in movie[6]: #and rating (movie[8]) >=7 and input = country
           list_actor_movies.append(movie)


    #print(list_actor_movies)
    print(f"Number of movies star by {movies_star} is: ", len(list_actor_movies))
    print("Below are some details about each movie\n %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    for x in list_actor_movies:
        moviename = x[1]
        duration = x[2]
        year = x [3]
        print(f"movie name:{moviename}\nduration:{duration}\nyear:{year}")


def top_rated_movies(movie_rate):
    country = input("Please enter which country: ")
    top_rated = 0
    list_top = []
    for movie in movie_rate:
        if country == movie[7]:
            x = float(movie[8])  # rating column
            if x > top_rated:
                top_rated = x
                if top_rated not in list_top:
                    if x >= 7:  # ratings more than 7
                        list_top.append(movie)  # to add high rate movies to the list (list_top)

                        top_rated = 0
    print(f'There are {len(list_top)} number of the top rated movies in {country}')
    # if list_top[0] >= 7.0:
    #     print(list_top[7])

    return (list_top)

def country_plots(user_country, csv_list):
    low_rating = 0
    average_rating = 0
    high_rating = 0
    for movie in csv_list:
        if movie[7] == user_country:
            rating = float(movie[8])
            if rating <= 3:
                low_rating += 1
            elif rating >= 7:
                high_rating += 1
            else:
                average_rating += 1
    rated_movies = {"Low_rated": low_rating, "Avg_rated": average_rating, "High_rated": high_rating}
    # print(rated_movies["Low_rated"])
    # print(rated_movies["Avg_rated"])
    # print(rated_movies["High_rated"])
    return rated_movies





