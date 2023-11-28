text = input()

while True:
    command = input()
    if command == "Done":
        break
    command = command.split()
    if command[0] == "TakeOdd":
        text = "".join([text[x] for x in range(len(text)) if x % 2 != 0])

    elif command[0] == "Cut":
        idx, length = int(command[1]), int(command[2])
        substring = text[idx:idx+length]
        text = text.replace(substring, "", 1)
    elif command[0] == "Substitute":
        old, new = command[1], command[2]
        if old in text:
            text = text.replace(old, new)
        else:
            print("Nothing to replace!")
            continue
    print(text)
print(f"Your password is: {text}")
