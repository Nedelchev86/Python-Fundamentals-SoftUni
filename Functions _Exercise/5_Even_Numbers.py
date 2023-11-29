# numbers = list(int(x) for x in input().split())
# print(list(filter(lambda x: x % 2 == 0, numbers)))





# print(list(filter(lambda x: x % 2 == 0, list(int(x) for x in input().split()))))


print(list(filter(lambda x: x % 2 == 0, list(map(int, input().split(" "))))))


# lis1 = list(int(x) for x in input().split())
#
#
# def is_even(x):
#     return x % 2 == 0
#
#
# lis2 = list(filter(is_even, lis1))
#
# print(lis2)