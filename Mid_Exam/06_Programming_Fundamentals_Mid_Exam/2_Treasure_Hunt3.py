loots = input().split("|")

while True:
    data = input()
    if data == "Yohoho!":
        break
    data = data.split()
    command = data[0]
    if command == "Loot":
        for i in range(len(data)):
            if i != 0:
                if data[i] not in loots:
                    loots.insert(0, data[i])
    elif command == "Drop":
        if int(data[1]) < len(loots) and int(data[1]) >= 0:
            loots.append(loots.pop(int(data[1])))
    elif command == "Steal":
        if int(data[1]) < len(loots):
            stealed = loots[-int(data[1]):]
            del loots[-int(data[1]):]
            print(", ".join(stealed))
        else:
            print(", ".join(loots))
            loots.clear()
            break

if loots:
    count = 0
    for words in loots:
        count += len(words)
    average_gain = count / len(loots)
    print(F"Average treasure gain: {average_gain:.2F} pirate credits.")
else:
    print("Failed treasure hunt.")