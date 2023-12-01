initial_energy = int(input())
battles = 0
while True:
    distance = input()
    if distance == "End of battle":
        print(F"Won battles: {battles}. Energy left: {initial_energy}")
        break
    distance = int(distance)
    if initial_energy >= distance:
        initial_energy -= distance
        battles += 1
        if battles % 3 == 0:
            initial_energy += battles

    else:
        print(F"Not enough energy! Game ends with {battles} won battles and {initial_energy} energy")
        exit()

# print(F"Won battles: {battles}. Energy left: {initial_energy}")
