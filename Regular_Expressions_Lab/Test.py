initial_energy = int(input())
count = 0

while True:
    distance = input()
    if distance == "End of battle":
        break
    distance = int(distance)
    if initial_energy - distance >= 0:
        count += 1
        initial_energy -= distance
        if count % 3 == 0:
            initial_energy += count
    else:
        print(F"Not enough energy! Game ends with {count} won battles and {initial_energy} energy")
        exit()
print(F"Won battles: {count}. Energy left: {initial_energy}")

