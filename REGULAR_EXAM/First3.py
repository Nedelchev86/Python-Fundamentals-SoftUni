spell = input()
allowed_command = ["Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]

while True:
    command = input().split()

    if command[0] == "Abracadabra":
        break
    if command[0] not in allowed_command:
        print("The spell did not work!")
        continue

    if command[0] == "Abjuration":
        spell = spell.upper()

    elif command[0] == "Necromancy":
        spell = spell.lower()

    elif command[0] == "Illusion":
        idx, letter = int(command[1]), command[2]
        if 0 <= idx < len(spell):
            spell = spell[:idx] + letter + spell[idx+1:]
            print("Done!")
            continue
        else:
            print("The spell was too weak.")
            continue

    elif command[0] == "Divination":
        first, second = command[1], command[2]
        if first in spell:
            spell = spell.replace(first, second)
        else:
            continue

    elif command[0] == "Alteration":
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring, "")
        else:
            continue
    print(spell)
