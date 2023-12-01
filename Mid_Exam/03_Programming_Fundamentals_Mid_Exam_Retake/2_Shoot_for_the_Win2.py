targets = [int(x) for x in input().split()]
count = 0
while True:
    command = input()
    if command == "End":
        break
    command = int(command)
    if command >= len(targets):
        continue
    count += 1
    value = targets[command]
    for i in range(len(targets)):
        if targets[i] > value:
            targets[i] -= value
        else:
            if targets[i] >= 0:
                targets[i] += value
    targets[command] = -1
print(F"Shot targets: {count} -> {' '.join([str(x) for x in targets])}")