message = input()

while True:
    command = input()
    if command == "Reveal":
        break
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        idx = int(command[1])
        message = message[:idx] + " " + message[idx:]
    if command[0] == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message = message + substring[::-1]
        else:
            print("error")
            continue
    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        if substring in message:
            while substring in message:
                message = message.replace(substring, replacement)
        else:
            continue
    print(message)

print(f"You have a new text message: {message}")