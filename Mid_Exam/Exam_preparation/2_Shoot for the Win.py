targets = [int(x) for x in input().split()]
shoot = 0

while True:
    idx = input()
    if idx == "End":
        break
    idx = int(idx)
    if idx >= 0 and idx < len(targets):
        value = targets[idx]
        for i in range(len(targets)):
            if targets[i] > value:
               targets[i] -= value
            else:
                if targets[i] > 0:
                    targets[i] += value
        targets[idx] = -1
        shoot += 1

print(f"Shot targets: {shoot} -> {' '.join([str(x) for x in targets])}")
