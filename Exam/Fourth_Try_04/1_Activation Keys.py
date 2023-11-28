text = input()

while True:
    data = input()
    if data == "Generate":
        break
    command = data.split(">>>")

    if command[0] == "Contains":
        substring = command[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        case, start, end = command[1], int(command[2]), int(command[3])
        if case == "Upper":
            text = text[:start] + text[start:end].upper() + text[end:]
        elif case == "Lower":
            text = text[:start] + text[start:end].lower() + text[end:]
        print(text)
    elif command[0] == "Slice":
        start, end = int(command[1]), int(command[2])
        text = text[:start] + text[end:]
        print(text)
print(F"Your activation key is: {text}")
