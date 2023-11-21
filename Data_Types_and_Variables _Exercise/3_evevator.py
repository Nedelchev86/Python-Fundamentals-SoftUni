# capacity = int(input())
# person = int(input())
#
# if capacity // person < (capacity / person):
#     print(capacity // person + 1)
# elif (capacity // person) == 0:
#     print("1")
# else:
#     print(capacity // person)


from math import  ceil

capacity = int(input())
person = int(input())

print(ceil(capacity / person))
