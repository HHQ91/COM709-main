import csv
import tuii
import process
import plot
moviesdb = tuii.Netflix()
try:
    with open(moviesdb, encoding="utf-8") as file:  # read the data from the provided file
        csv_reader = csv.reader(file)
        heading = next(csv_reader)
        csv_list = list(csv_reader)
        tuii.view_summery(csv_list)
        choice = tuii.view_choises()
        # if choice == 1:
        #     #print(csv_reader)
        #     movies_details = process.specific_movie_info(csv_list)
        #     tuii.desplay_movies(movies_details, one_movie=True)
        # elif choice == 2:
        #     year_movies_list = process.movies_released_in_a_specific_year(csv_list)
        #     tuii.desplay_movies(year_movies_list)
        # elif choice == 3:
        #     process.movies_star_actor(csv_list)
        # elif choice == 4:
        #     hasan = process.top_rated_movies(csv_list)
        #     tuii.desplay_movies(hasan)
        # elif choice == 5:
        #     selected_country = tuii.country_plots()
        #     rating_movies = process.country_plots(selected_country, csv_list)
        #     plot.data_visual(selected_country, rating_movies)
except:
    print("invalid path")