my_dict = {}

while True:
    key = input()
    if key == "stop":
        break
    value = int(input())
    my_dict[key] = my_dict.get(key, 0) + value
for key, value in my_dict.items():
    print(f"{key} -> {value}")

