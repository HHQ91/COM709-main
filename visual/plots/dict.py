import matplotlib.pylab as plt
import  random as rnd

def data():
    baths = {}
    line_type = input("Enter the line type  (:, -- or -)")
    line_color = input("Enter the line colour  (r, g or b)")
    line_marker = input("Enter the line colour  (o, s or ^)")
    baths.update({"line_type": line_type, "line_color": line_color, "line_marker": line_marker} )
    return baths

def generate():
    print("How many lines would you like to display?")
    lines = int(input())
    for num in range(lines):
        values = data()
        x_values = rnd.sample(range(1, 20), 6)
        y_values = rnd.sample(range(1,30), 6)
        style = f"{values['line_color']}{values['line_type']}{values['line_marker']}"
        plt.plot(x_values, y_values, style)

    plt.show()
generate()

