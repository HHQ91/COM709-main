import csv

import triangle_funcs as tf

file_path = "triangle.csv"


def run():
    try:

        print(tf.triangles_with_sides_in_range(1, 11))

        with open(file_path) as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)

            with open("triangles_processed.csv", "w") as output:
                output.write(f"side_a,side_b, side_c, is_in_range, is_valid, classification\n")
                for record in csv_reader:
                    output.write(f"{record[0]}, {record[1]}, {record[2]},{tf.is_in_range(record,1,10)}, \
{tf.is_valid(record)}, {tf.classify(record)}\n")

    except IOError:
        print("Error 404")

if __name__ == "__main__":
    run()