energy  = int(input())
count = 0

while True:
    distance = input()
    if distance == "End of battle":
        print(F"Won battles: {count}. Energy left: {energy}")
        exit()
    distance = int(distance)
    if energy >= distance:
        energy -= distance
        count += 1
        if count % 3 == 0:
            energy += count
    else:
        print(F"Not enough energy! Game ends with {count} won battles and {energy} energy")
        exit()
print(F"Won battles: {count}. Energy left: {energy}")