# data = input().lower().split()
# my_dict = {}
#
# for key in data:
#     if key not in my_dict:
#         my_dict[key] = 0
#     my_dict[key] += 1
# for key, value in my_dict.items():
#     if value % 2 != 0:
#         print(key, end=" ")


data = [x.lower() for x in input().lower().split()]
my_dict = {}

for key in data:
    if key not in my_dict:
        my_dict[key] = 0
    my_dict[key] += 1
for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")