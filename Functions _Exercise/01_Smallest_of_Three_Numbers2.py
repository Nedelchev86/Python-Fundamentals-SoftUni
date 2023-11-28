def smallest_number(some_numbers):
    return min(some_numbers)


first = int(input())
second = int(input())
third = int(input())

all_numbers = [first, second, third]
min_number = smallest_number(all_numbers)
print(min_number)
