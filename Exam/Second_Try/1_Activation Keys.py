text = input()

while True:
    data = input()
    if data == "Generate":
        break
    data = data.split(">>>")
    command = data[0]

    if command == "Contains":
        substring = data[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        start = int(data[2])
        end = int(data[3])
        if data[1] == "Upper":
            text = text[:start] + text[start:end].upper() + text[end:]
        else:
            text = text[:start] + text[start:end].lower() + text[end:]
        print(text)
    elif command == "Slice":
        start = int(data[1])
        end = int(data[2])
        text = text[:start]+text[end:]
        print(text)
print(f"Your activation key is: {text}")
