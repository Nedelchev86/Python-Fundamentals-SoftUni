text = input()
command = input()

while command != "Reveal":
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        text = text[:index] + " " + text[index:]
    elif command[0] == "Reverse":
        if command[1] in text:
            string = command[1]
            text = text.replace(string, "", 1) + string[::-1]
        else:
            print("error")
            command = input()
            continue
    elif command[0] == "ChangeAll":
        text = text.replace(command[1], command[2])
    print(text)
    command = input()

print(f"You have a new text message: {text}")
