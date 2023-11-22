count = 0
my_dict = {}

while True:
    current_data = input()
    if current_data == "stop":
        break
    count += 1
    if count % 2 != 0:
        key = current_data
        if key not in my_dict:
            my_dict[key] = 0

    else:
        my_dict[key] += int(current_data)
for key, value in my_dict.items():
    print(F"{key} -> {value}")
