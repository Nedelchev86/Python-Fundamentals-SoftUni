text = input()
while True:
    data = input().split("|")
    command = data[0]
    if command == "Decode":
        break
    if command == "Move":
        index = int(data[1])
        text = text[index:] + text[:index]
    elif command == "Insert":
        index = int(data[1])
        text = text[:index] + data[2] + text[index:]
    elif command == "ChangeAll":
        text = text.replace(data[1], data[2])
print(F"The decrypted message is: {text}")
