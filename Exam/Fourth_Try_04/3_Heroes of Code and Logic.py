numbers = int(input())
heroes = {}

for _ in range(numbers):
    name, HP, MP = [int(x) if x.isdigit() else x for x in input().split()]
    heroes[name] = {"HP": HP, "MP": MP}


while True:
    command = input().split(" - ")
    if command[0] == "End":
        break
    if command[0] == "CastSpell":
        hero_name, MP_needed, spell_name = command[1], int(command[2]), command[3]
        if heroes[hero_name]["MP"] >= MP_needed:
            heroes[hero_name]["MP"] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        if heroes[hero_name]["HP"] - damage > 0:
            heroes[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif command[0] == "Recharge":
        hero_name, amount = command[1], int(command[2])
        if heroes[hero_name]["MP"] + amount >= 200:
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['MP']} MP!")
            heroes[hero_name]["MP"] = 200
        else:
            heroes[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif command[0] == "Heal":
        hero_name, amount = command[1], int(command[2])
        if heroes[hero_name]["HP"] + amount >= 100:
            print(f"{hero_name} healed for {100 - heroes[hero_name]['HP']} HP!")
            heroes[hero_name]["HP"] = 100
        else:
            heroes[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")

for key, value in heroes.items():
    print(key)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")

