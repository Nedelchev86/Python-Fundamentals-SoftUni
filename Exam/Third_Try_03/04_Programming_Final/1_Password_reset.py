text = input()

while True:
    command = input()
    command = command.split()
    if command[0] == "Done":
        break
    if command[0] == "TakeOdd":
        text = text[1::2]
    elif command[0] == "Cut":
        command, idx, length = command
        idx = int(idx)
        length = int(length)
        text = text[:idx] + text[idx+length:]
    elif command[0] == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in text:
            text = text.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            continue
    print(text)
print(f"Your password is: {text}")
