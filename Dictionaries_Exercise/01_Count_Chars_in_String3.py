data = input().replace(" ", "")
my_dict = {}

for el in data:
    my_dict[el] = my_dict.get(el, 0) + 1
for key, value in my_dict.items():
    print(f"{key} -> {value}")


