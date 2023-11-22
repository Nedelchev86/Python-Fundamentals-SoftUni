legendary_item = {"shards": 0, "fragments": 0, "motes": 0}

obtained = False

while True:
    current_items = input().lower().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index+1]
        if key not in legendary_item:
            legendary_item[key] = value
        else:
            legendary_item[key] += value

        if legendary_item["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary_item[key] -= 250
            obtained = True
        elif legendary_item["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary_item[key] -= 250
            obtained = True
        elif legendary_item["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary_item[key] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break

for key, value in legendary_item.items():
    print(F"{key}: {value}")