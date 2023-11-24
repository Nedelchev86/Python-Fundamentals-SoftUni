# data = input().split()
# data_lower = list(map(lambda x: x.lower(), data))
# my_dict = {}
#
# for word in data_lower:
#     if word not in my_dict:
#         my_dict[word] = 0
#     my_dict[word] += 1
# for key, value in my_dict.items():
#     if value % 2 != 0:
#         print(key, end=" ")

data = input().lower().split()
my_dict = {}

for word in data:
    if word not in my_dict:
        my_dict[word] = 0
    my_dict[word] += 1
for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
