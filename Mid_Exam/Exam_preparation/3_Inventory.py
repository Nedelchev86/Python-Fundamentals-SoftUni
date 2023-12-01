collection = input().split(", ")

while True:
    data = input()
    if data == "Craft!":
        break
    data = data.split(" - ")
    command = data[0]
    item = data[1]

    if command == "Collect":
        if item not in collection:
            collection.append(item)
        else:
            continue
    elif command == "Drop":
        if item in collection:
            collection.remove(item)
        else:
            continue
    elif command == "Combine Items":
        old_item, new_intem = item.split(":")
        if old_item in collection:
            idx = collection.index(old_item)
            collection.insert(idx+1, new_intem)
        else:
            continue
    else:
        if item in collection:
            collection.remove(item)
            collection.append(item)
print(", ".join(collection))
