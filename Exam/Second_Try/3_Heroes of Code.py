nums = int(input())
heroes = {}

for _ in range(nums):
    name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
    heroes[name] = [hp, mp]

while True:
    data = input().split(" - ")
    if data[0] == "End":
        break
    command = data[0]

    if command == "CastSpell":
        name, mp, spell = [int(x) if x.isdigit() else x for x in data[1:]]
        if heroes[name][1] >= mp:
            heroes[name][1] -= mp
            print(f"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")
    elif command == "TakeDamage":
        name, damage, attacker = [int(x) if x.isdigit() else x for x in data[1:]]
        if heroes[name][0] > damage:
            heroes[name][0] -= damage
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]
    elif command == "Recharge":
        name, amount = [int(x) if x.isdigit() else x for x in data[1:]]
        if heroes[name][1] + amount <= 200:
            heroes[name][1] += amount
            print(f"{name} recharged for {amount} MP!")
        else:
            print(f"{name} recharged for {200 - heroes[name][1]} MP!")
            heroes[name][1] = 200
    elif command == "Heal":
        name, amount = [int(x) if x.isdigit() else x for x in data[1:]]
        if heroes[name][0] + amount <= 100:
            heroes[name][0] += amount
            print(f"{name} healed for {amount} HP!")
        else:
            print(f"{name} healed for {100 - heroes[name][0]} HP!")
            heroes[name][0] = 100
if heroes:
    for name, value in heroes.items():
        print(f"{name}")
        hp, mp = value
        print(f"  HP: {hp}")
        print(f"  MP: {mp}")
