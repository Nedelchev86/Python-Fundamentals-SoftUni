events_lsit = input().split("|")
energy, coints = 100, 100

for el in events_lsit:
    data = el.split("-")
    event = data[0]
    number = int(data[1])
    if event == "rest":
        if energy + number > 100:
            print(F"You gained {100 - energy} energy.")
            energy = 100
        else:
            print(F"You gained {number} energy.")
            energy += number
        print(F"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            print(F"You earned {number} coins.")
            energy -= 30
            coints += number
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coints >= number:
            print(F"You bought {event}.")
            coints -= number
        else:
            print(F"Closed! Cannot afford {event}.")
            exit()
print("Day completed!")
print(F"Coins: {coints}")
print(F"Energy: {energy}")