pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
health_capacity = int(input())
sunken = False

while not sunken:
    user_input = input()
    if user_input == "Retire":
        print(f"Pirate ship status: {(sum(pirate_ship))}")
        print(f"Warship status: {(sum(warship))}")
        break
    user_input = user_input.split()
    command = user_input[0]

    if command == "Fire":
        index = int(user_input[1])
        damage = int(user_input[2])
        if index >= len(warship) or index < 0:
            continue
        warship[index] -= damage
        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            sunken = True

    elif command == "Defend":
        start_idx = int(user_input[1])
        end_idx = int(user_input[2])
        damage = int(user_input[3])
        if start_idx < 0 or end_idx >= len(pirate_ship):
            continue
        for i in range(start_idx, end_idx + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                sunken = True
                break

    elif command == "Repair":
        idx = int(user_input[1])
        if idx < 0 or idx >= len(pirate_ship):
            continue

        pirate_ship[idx] += int(user_input[2])
        if pirate_ship[idx] > health_capacity:
            pirate_ship[idx] = health_capacity

    elif command == "Status":
        count = 0
        for i in pirate_ship:
            if i < (health_capacity * 0.2):
                count += 1
        print(f"{count} sections need repair.")
