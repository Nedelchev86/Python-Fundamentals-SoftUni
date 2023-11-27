message = input()
list_message = [letter for letter in message]

while True:
    command = input()

    if command == "Decode":
        break

    if command.split("|")[0] == "Move":
        num = int(command.split("|")[1])
        for i in range(0, num):
            list_message.append(list_message.pop(0))

    elif command.split("|")[0] == "Insert":
        idx = int(command.split("|")[1])
        value = command.split("|")[2]
        list_message.insert(idx, value)

    elif command.split("|")[0] == "ChangeAll":
        substring = command.split("|")[1]
        replacement = command.split("|")[2]

        list_message = list(map(lambda x: x.replace(substring, replacement), list_message))

message = ''.join(list_message)

print(f"The decrypted message is: {message}")