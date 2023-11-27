message = input()

command = input()
while command != "Decode":
    data = command.split("|")
    if data[0] == "Move":
        index = int(data[1])
        message = message[index:] + message[:index]
    elif data[0] == "Insert":
        index = int(data[1])
        message = message[:index] + data[2] + message[index:]
    elif data[0] == "ChangeAll":
        message = message.replace(data[1], data[2])
    command = input()
print(F"The decrypted message is: {message}")
