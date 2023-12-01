journal = input().split(", ")

while True:
    data = input()
    if data == "Craft!":
        break
    command, item = data.split(" - ")
    if command == "Collect":
        if item not in journal:
            journal.append(item)
    elif command == "Drop":
        if item in journal:
            journal.remove(item)
    elif command == "Combine Items":
        olditem, newitem  = item.split(":")
        if olditem in journal:
            journal.insert(journal.index(olditem) +1, newitem)
    elif command == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)
print(", ".join(journal))