health = 100
bitcoin = 0

rooms = input().split("|")

for ind in range(len(rooms)):
    command, numbers = rooms[ind].split()
    numbers = int(numbers)
    if command == "potion":
        if health + numbers <= 100:
            health += numbers
            print(f"You healed for {numbers} hp.")
            print(F"Current health: {health} hp.")
        else:
            print(f"You healed for {numbers - ((health + numbers)- 100)} hp.")
            print(F"Current health: 100 hp.")
            health = 100
    elif command == "chest":
        bitcoin += numbers
        print(f"You found {numbers} bitcoins.")
    else:
        if health - numbers > 0:
            print(F"You slayed {command}.")
            health -= numbers
        else:
            print(F"You died! Killed by {command}.")
            print(f"Best room: {ind+1}")
            break
else:
    print(F"You've made it!")
    print(F"Bitcoins: {bitcoin}")
    print(F"Health: {health}")