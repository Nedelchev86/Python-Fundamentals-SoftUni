treasure = input().split("|")

while True:
    data = input()

    if data == "Yohoho!":
        break

    data = data.split()
    command = data[0]

    if command == "Loot":
        for i in range(len(data)):
            if i == 0:
                continue
            item = data[i]
            if item not in treasure:
                treasure.insert(0, item)

    elif command == "Drop":
        idx = int(data[1])
        if 0 <= idx < len(treasure):
            remove = treasure.pop(idx)
            treasure.append(remove)

    elif command == "Steal":
        count = int(data[1])
        if count >= len(treasure):
            print(", ".join(treasure))
            treasure.clear()
            print("Failed treasure hunt.")
            exit()
        else:
            stealed = treasure[-count:]
            del treasure[-count:]
            print(", ".join(stealed))

if treasure:
    count = 0
    for words in treasure:
        count += len(words)
    average_gain = count / len(treasure)
    print(F"Average treasure gain: {average_gain:.2F} pirate credits.")
