message = input()
while True:
    command = input()
    if command == "Decode":
        break
    command = command.split("|")

    if command[0] == "Move":
        numbers = int(command[1])
        if numbers >= 0 and numbers < len(message):
            message = message[numbers:] + message[:numbers]
    elif command[0] == "Insert":
        index = int(command[1])
        message = message[:index] + command[2] + message[index:]
    elif command[0] == "ChangeAll":
        message = message.replace(command[1], command[2])
print(f"The decrypted message is: {message}")
