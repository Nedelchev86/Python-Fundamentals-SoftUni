targets = [int(x) for x in input().split()]

while True:
    data = input()
    if data == "End":
        break
    data = data.split()
    command = data[0]
    idx = int(data[1])
    value = int(data[2])

    if command == "Shoot":
        if 0 <= idx < len(targets):
            targets[idx] -= value
        else:
            continue
        if targets[idx] <= 0:
            targets.pop(idx)
    elif command == "Add":
        if 0 <= idx < len(targets):
            targets.insert(idx, value)
        else:
            print("Invalid placement!")
            continue
    elif command == "Strike":
        if idx +value < len(targets) and idx - value >= 0:
            start = targets[:idx-value]
            end = targets[(idx+value+1):]
            targets = start + end
        else:
            print("Strike missed!")
            continue

print("|".join([str(x) for x in targets]))