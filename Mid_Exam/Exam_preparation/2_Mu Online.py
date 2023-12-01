health = 100
bitcoin = 0

rooms = input().split("|")
room = 0

for i in rooms:
    room +=1
    command, number = i.split()
    number = int(number)

    if command == "potion":
        if health + number > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
        else:
            print(f"You healed for {number} hp.")
            health += number
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoin += number
        print(F"You found {number} bitcoins.")
    else:
        if health - number > 0:
            print(f"You slayed {command}.")
            health -= number
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")
