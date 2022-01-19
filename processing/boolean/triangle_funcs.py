from num_funcs import is_in_range

def is_equilateral(sides):
    x = int(sides[0])
    y = int(sides[1])
    z = int(sides[2])
    if x and y and z:
        return x == y == z
def is_scalene(sides):
    x = int(sides[0])
    y = int(sides[1])
    z = int(sides[2])
    if x and y and z:
        return x != y and y != z and z != x
def is_isosceles(sides):
    x = int(sides[0])
    y = int(sides[1])
    z = int(sides[2])
    if x and y and z:
        return  x == y or y == z or z == x

def is_in_range(sides, lower_bound, upper_bound):
    x = int(sides[0])
    y = int(sides[1])
    z = int(sides[2])
    if x and y and z:
        return x and y and z in range(lower_bound, upper_bound)
    else:
        return False
def is_valid(sides):
    x = int(sides[0])
    y = int(sides[1])
    z = int(sides[2])
    if x and y and z:
        return ( x+y > z ) or ( y+z > x ) or ( z+x > y)
    else:
        return False

def classify(sides):

    if  is_equilateral(sides):
        return  "Equilateral"
    elif is_isosceles(sides):
        return "Isosceles"
    elif is_scalene(sides):
        return "Scalne"
    else:
        return None

def triangles_with_sides_in_range(lower_bound, upper_bound):
    valid_list = []
    sides = []
    if upper_bound - lower_bound >= 1:
        for x in range(lower_bound, upper_bound):
            for y in range(lower_bound, upper_bound):
                for z in range(lower_bound, upper_bound):
                    if x and y and z:
                        sides = [x, y, z]
                        if is_in_range(sides, lower_bound,upper_bound) and is_valid(sides):
                            valid_list.append(sides)

        return valid_list
    else:
        return "Invalid range values"

if __name__ == "__main__":

    print(triangles_with_sides_in_range(0,2))