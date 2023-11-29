# def abs_list(my_myst):
#     return [abs(float(x)) for x in my_myst]
#
#
# print(abs_list(input().split()))


def abs_list(my_myst):
    return [abs(x) for x in my_myst]


my_list = list(map(float, input().split()))
print(abs_list(my_list))
