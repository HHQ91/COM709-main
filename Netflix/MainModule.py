

import TuiModule
import csv
moviesdb = TuiModule.Netflix()
with open(moviesdb, encoding="utf-8") as file:  # read the data from the provided file
    csv_reader = csv.reader(file)
    heading = next(csv_reader)
    csv_list = list(csv_reader)
    TuiModule.view_summery(csv_list)
    choice = TuiModule.view_choises()