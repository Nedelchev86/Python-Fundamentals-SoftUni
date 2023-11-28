def sum_numbers(a, b):
    return a + b


def subtract(sums, c):
    return sums - c


first, second, third = int(input()), int(input()), int(input())

result = subtract((sum_numbers(first, second)), third)
print(result)
