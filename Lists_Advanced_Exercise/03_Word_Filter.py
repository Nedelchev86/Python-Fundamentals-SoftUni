#
# my_list = [x for x in input().split(" ") if len(x) % 2 == 0]
# print("\n".join(my_list))


print("\n".join([word for word in input().split(" ") if len(word) % 2 == 0]))


[print(word) for word in input().split(" ") if len(word) % 2 == 0]


