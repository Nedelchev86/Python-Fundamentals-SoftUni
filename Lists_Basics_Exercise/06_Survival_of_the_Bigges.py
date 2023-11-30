list_of_integer = [int(x) for x in input().split(" ")]

count = int(input())

for i in range(count):
    list_of_integer.remove(min(list_of_integer))

print(*list_of_integer, sep=", ")

#
# list_of_integer = [int(x) for x in input().split(" ")]
#
# count = int(input())
#
# for i in range(count):
#     list_of_integer.remove(min(list_of_integer))
# list_as_string = [str(x) for x in list_of_integer]
# print(", ".join(list_as_string))
