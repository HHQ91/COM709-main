

def is_equal(number1, number2):
    return (number1 == number2)

def is_lower(number1, number2):
    return (number1 < number2)

def is_greater(number1, number2):
    return (number1 > number2)

def is_in_range(number, lower_bound, upper_bound):
    return number in range(lower_bound, upper_bound)

def is_even(number):
    return not number%2

def is_odd(number):
    return number%2

def is_in_list(number, numbers):
    return bool([number for num in numbers if number == num])


