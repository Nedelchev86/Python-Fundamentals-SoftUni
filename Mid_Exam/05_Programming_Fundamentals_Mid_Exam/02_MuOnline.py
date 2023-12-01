command = input()
health = 100
bitcoins = 0

first_list = command.split("|")
new_list = [i.split() for i in first_list]
room_count = 0

for i in range(len(new_list)):
    room_count += 1
    if new_list[i][0] == "potion":
        health += int(new_list[i][1])
        current_health = int(new_list[i][1])
        if health >= 100:
            current_health = int(new_list[i][1]) - (health - 100)
            health = 100
        print(F"You healed for {current_health} hp.")
        print(F"Current health: {health} hp.")
    elif new_list[i][0] == "chest":
        print(F"You found {new_list[i][1]} bitcoins.")
        bitcoins += int(new_list[i][1])
    else:
        health -= int(new_list[i][1])
        if health <= 0:
            print(F"You died! Killed by {new_list[i][0]}.")
            print(F"Best room: {room_count}")
            exit()
        else:
            print(F"You slayed {new_list[i][0]}.")
print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")
