def sum_numbers(a, b):
    return a + b


def subtract(sums, c):
    return sums - c


def add_and_subtract(a, b, c):
    sum_of_first_and_second = sum_numbers(a, b)
    result = subtract(sum_of_first_and_second, c)
    return result


first, second,third = int(input()), int(input()), int(input())


print(add_and_subtract(first, second, third))
