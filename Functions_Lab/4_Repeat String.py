#
# def repeat_string(word, num):
#     result = word * num
#     return result
#
#
# string = input()
# count = int(input())
# print(repeat_string(string, count))


# def x(a, b):
#     return a * b
#
# string = input()
# quantity = int(input())
# print(x(string, quantity))


x = lambda a, b: a * b
print(x(input(), int(input())))
