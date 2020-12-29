# This function will return square of sum of first n natural numbers.
def sum_of_square_of_first_n_number(n):
    value = 0
    for i in range(1, n+1):
        value = value + i*i
    return value


# The function will return square of sum of first n natural numbers
def square_of_sum_of_first_n_numbers(n):
    value = 0
    for i in range(1, n+1):
        value = value + i
    return value * value


# Difference between sqaure of sum of first 100 natural number and sum of square of first 100 numbers.
square_of_sum_of_first_n_numbers(100) - sum_of_square_of_first_n_number(100)