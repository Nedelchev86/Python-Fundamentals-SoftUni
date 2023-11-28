text = input()

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break
    if command[0] == "Move":
        index = int(command[1])
        text = text[index:] + text[:index]
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        text = text[:index] + value + text[index:]
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        text = text.replace(substring, replacement)

print(f"The decrypted message is: {text}")


