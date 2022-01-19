import matplotlib.pylab as plt

def coordinate():
    x = int(input("Enter x value"))
    y = int(input("Enter y value"))
    return (x, y)

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]

def run():
    values = path()
    print(values)
    plt.plot(values[0], values[1])
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.show()

run()