# my_list = [int(x) for x in input().split()]
#
# average = sum(my_list) / len(my_list)
# top5 = [x for x in my_list if x > average]
# sorted_list = list(sorted(top5, reverse=True))
#
# if sorted_list:
#     if len(sorted_list) > 5:
#         result = sorted_list[:5]
#         print(" ".join([str(x) for x in result]))
#     else:
#         print(" ".join([str(x) for x in sorted_list]))
# else:
#     print("No")
#


my_list = [int(x) for x in input().split()]

average = sum(my_list) / len(my_list)
top5 = [x for x in my_list if x > average]
sorted_list = list(sorted(top5, reverse=True))

if len(sorted_list) == 0:
    print("No")
else:
    print(" ".join([str(x) for x in sorted_list[:5]]))
