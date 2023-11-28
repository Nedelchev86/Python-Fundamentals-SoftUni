nums = int(input())
heroes = {}

for i in range(nums):
    name, hp, mp = input().split()
    heroes[name] = {}
    heroes[name]["HP"] = int(hp)
    heroes[name]["MP"] = int(mp)
while True:
    command = input()
    if command == "End":
        break
    command, name, *other = command.split(" - ")
    if command == "CastSpell":
        mp_needed, spell_name = other
        if heroes[name]["MP"] >= int(mp_needed):
            heroes[name]["MP"] -= int(mp_needed)
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['MP']} MP!")
        else:
            print(F"{name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        damage, attacker = other
        if heroes[name]["HP"] > int(damage):
            heroes[name]["HP"] -= int(damage)
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
        else:
            print(F"{name} has been killed by {attacker}!")
            del heroes[name]
    elif command == "Recharge":
        other = other[0]
        if int(other) + heroes[name]["MP"] >= 200:
            print(f"{name} recharged for {200 - heroes[name]['MP']} MP!")
            heroes[name]["MP"] = 200
        else:
            heroes[name]["MP"] += int(other)
            print(f"{name} recharged for {int(other)} MP!")
    elif command == "Heal":
        other = other[0]
        if int(other) + heroes[name]["HP"] >= 100:
            print(f"{name} healed for {100 - heroes[name]['HP']} HP!")
            heroes[name]["HP"] = 100
        else:
            heroes[name]["HP"] += int(other)
            print(f"{name} healed for {other} HP!")
for key, value in heroes.items():
    print(key)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")