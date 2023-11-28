some_string = input()

while True:
    command = input()
    if command == "Decode":
        break
    command = command.split("|")
    if command[0] == "Move":
        nums = int(command[1])
        some_string = some_string[nums:] + some_string[:nums]
    elif command[0] == "Insert":
        idx, value = int(command[1]), command[2]
        some_string = some_string[:idx] + value + some_string[idx:]
    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        while substring in some_string:
            some_string = some_string.replace(substring, replacement)
print(f"The decrypted message is: {some_string}")
