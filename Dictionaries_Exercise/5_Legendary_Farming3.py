my_dict = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}

obtained = False
while True:
    data = input().lower().split()
    for i in range(0, len(data), 2):
        value = data[i]
        key = data[i+1]
        if key not in my_dict:
            my_dict[key] = 0
        my_dict[key] += int(value)

        if my_dict["shards"] >= 250:
            print("Shadowmourne obtained!")
            my_dict["shards"] -= 250
            obtained = True
        elif my_dict["fragments"] >= 250:
            print("Valanyr obtained!")
            my_dict["fragments"] -= 250
            obtained = True
        elif my_dict["motes"] >= 250:
            my_dict["motes"] -= 250
            print("Dragonwrath obtained!")
            obtained = True
        if obtained:
            break
    if obtained:
        break

for key, value in my_dict.items():
    print(f"{key}: {value}")

