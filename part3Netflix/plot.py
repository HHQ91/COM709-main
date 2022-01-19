

from matplotlib import pyplot as plt
def data_visual(country, rating):
    x = [rating["Low_rated"], rating["Avg_rated"], rating["High_rated"]]
    y = ['Low rating movies ', 'Avg rating movies', 'High rating movies']
    plt.pie(x, labels = y)
    plt.title(f"The Total Movie Ratings in {country}")
    plt.show()