my_dict = {}

while True:
    key = input()
    if key == "stop":
        break
    value = int(input())
    if key not in my_dict:
        my_dict[key] = 0
    my_dict[key] += value
for key, value in my_dict.items():
    print(F"{key} -> {value}")


# my_dict = {}
#
# while True:
#     key = input()
#     if key == "stop":
#         break
#     value = int(input())
#     if key not in my_dict:
#         my_dict[key] = 0
#     my_dict[key] += value
# for i in my_dict:
#     print(F"{i} -> {my_dict[i]}")
