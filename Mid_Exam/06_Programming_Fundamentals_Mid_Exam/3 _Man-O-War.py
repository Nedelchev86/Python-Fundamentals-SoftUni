pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
health = int(input())

while True:
    data = input()
    if data == "Retire":
        print(F"Pirate ship status: {sum(pirate_ship)}")
        print(F"Warship status: {sum(warship)}")
        break
    data = data.split()
    command = data[0]
    if command == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if index < len(warship) and index >= 0:
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif command == "Defend":
        damage = int(data[3])
        start = int(data[1])
        end = int(data[2])
        if start >= 0 and end < len(pirate_ship) and end > start:
            for i in range(start, end +1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif command == "Repair":
        index = int(data[1])
        add_health = int(data[2])
        if index >= 0 and index < len(pirate_ship):
            pirate_ship[index] += add_health
            if pirate_ship[index] > health:
                pirate_ship[index] = health
    elif command == "Status":
        lower_than = 0.2 * health
        count = 0
        for i in range(len(pirate_ship)):
            if pirate_ship[i] < lower_than:
                count +=1
        print(F"{count} sections need repair.")