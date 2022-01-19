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