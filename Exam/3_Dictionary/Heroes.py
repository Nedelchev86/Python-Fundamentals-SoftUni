number = int(input())
heroes = {}

for _ in range(number):
    data = input().split()
    name = data[0]
    heroes[name] = {}
    heroes[name]["HP"] = int(data[1])
    heroes[name]["MP"] = int(data[2])

while True:
    current_data = input().split(" - ")
    command = current_data[0]
    if command == "End":
        break
    hero = current_data[1]
    if command == "CastSpell":
        MP = int(current_data[2])
        if heroes[hero]["MP"] >= MP:
            heroes[hero]["MP"] -= MP
            print(F"{hero} has successfully cast {current_data[3]} and now has {heroes[hero]['MP']} MP!")
        else:
            print(F"{hero} does not have enough MP to cast {current_data[3]}!")
    elif command == "TakeDamage":
        damage = int(current_data[2])
        if heroes[hero]["HP"] - damage > 0:
            heroes[hero]["HP"] -= damage
            print(F"{hero} was hit for {damage} HP by {current_data[3]} and now has {heroes[hero]['HP']} HP left!")
        else:
            print(F"{hero} has been killed by {current_data[3]}!")
            del heroes[hero]
    elif command == "Recharge":
        amount = int(current_data[2])
        if heroes[hero]["MP"] + amount > 200:
            print(F"{hero} recharged for {200 - heroes[hero]['MP'] } MP!")
            heroes[hero]["MP"] = 200
        else:
            print(F"{hero} recharged for {amount} MP!")
            heroes[hero]["MP"] += amount

    elif command == "Heal":
        amount = int(current_data[2])
        if heroes[hero]["HP"] + amount > 100:
            print(F"{hero} healed for {100 - heroes[hero]['HP'] } HP!")
            heroes[hero]["HP"] = 100
        else:
            print(F"{hero} healed for {amount} HP!")
            heroes[hero]["HP"] += amount
for hero in heroes:
    print(hero)
    print(F"  HP: {heroes[hero]['HP']}")
    print(F"  MP: {heroes[hero]['MP']}")
