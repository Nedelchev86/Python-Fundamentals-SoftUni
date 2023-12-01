loots = input().split("|")

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
            if item not in loots:
                loots.insert(0, item)
    elif command == "Drop":
        index = int(data[1])
        if 0 <= index < len(loots):
            x = loots.pop(index)
            loots.append(x)
    elif command == "Steal":
        ind = int(data[1])
        if ind >= len(loots):
            removed = loots
            print(', '.join(removed))
            print('Failed treasure hunt.')
            exit()
        else:
            removed = loots[-ind:]
            del loots[-ind:]
            print(', '.join(removed))


if len(loots) > 0:
    sum_items = sum(map(len, loots))

    avg = f'{sum_items / len(loots):.2f}'
    print(f'Average treasure gain: {avg} pirate credits.')