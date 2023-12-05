some_string = input()

while True:
    command = input().split()

    if command[0] == "Abracadabra":
        break

    if command[0] == "Abjuration":
        some_string = some_string.upper()
        print(some_string)

    elif command[0] == "Necromancy":
        some_string = some_string.lower()
        print(some_string)

    elif command[0] == "Illusion":
        idx, letter = int(command[1]), command[2]
        if idx >= 0 and idx < len(some_string):
            some_string = some_string[:idx] + letter + some_string[idx+1:]
            print("Done!")
        else:
            print("The spell was too weak.")

    elif command[0] == "Divination":
        first, second = command[1], command[2]
        if first in some_string:
            some_string = some_string.replace(first, second)
            print(some_string)
        else:
            continue

    elif command[0] == "Alteration":
        substring = command[1]
        if substring in some_string:
            some_string = some_string.replace(substring, "")
            print(some_string)
        else:
            continue
    else:
        print("The spell did not work!")

