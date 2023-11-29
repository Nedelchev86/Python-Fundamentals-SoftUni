# number = list(int(x) for x in input().split())
#
# print(f"The minimum number is {min(number)}")
# print(f"The maximum number is {max(number)}")
# print(f"The sum number is: {sum(number)}")



#
# def min_max_sum():
#     numbers = list(int(x) for x in input().split())
#     return f"The minimum number is {min(numbers)} \n" \
#            f"The maximum number is {max(numbers)} \n" \
#            f"The sum number is: {sum(numbers)}"
#
#
# print(min_max_sum())


number = list(map(int, input().split()))
print(f"The minimum number is {min(number)}")
print(f"The maximum number is {max(number)}")
print(f"The sum number is: {sum(number)}")
