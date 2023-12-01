targets = list(map(int, input().split()))

while True:
    data = input()
    if data == "End":
        break
    data = data.split()
    command = data[0]
    index = int(data[1])
    value = int(data[2])
    if command == "Shoot":
        if index < len(targets) and index >= 0:
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        if index < len(targets) and index >= 0:
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    else:
        if index + value < len(targets) and index - value >= 0:
            targets = targets[:(index-value)] + targets[(index+value+1):]
            #del targets[(index - radius):(index + radius + 1)]
        else:
            print("Strike missed!")
print("|".join([str(x) for x in targets]))
