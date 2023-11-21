data = input()
data = data.replace(" ", "")
my_dict = {}

for letter in data:
    if letter not in my_dict:
        my_dict[letter] = 0
    my_dict[letter] += 1

for i in my_dict:
    print(F"{i} -> {my_dict[i]}")


# data = input().split()
# data = "".join(data)
# my_dict = {}
#
# for letter in data:
#     if letter not in my_dict:
#         my_dict[letter] = 0
#     my_dict[letter] += 1
#
# for i in my_dict:
#     print(F"{i} -> {my_dict[i]}")
