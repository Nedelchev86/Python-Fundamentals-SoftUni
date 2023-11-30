numbers_list = input().split(", ")
list_of_integer = list(map(int, numbers_list))
for i in range(list_of_integer.count(0)):
    list_of_integer.remove(0)
    list_of_integer.append(0)
print(list_of_integer)
