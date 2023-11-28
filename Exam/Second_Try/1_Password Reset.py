text = input()

data = input()

while data != "Done":
    data = data.split()
    command = data[0]

    if command == "TakeOdd":
        text = "".join([text[i] for i in range(len(text)) if i % 2 != 0])
    elif command == "Cut":
        index = int(data[1])
        length = int(data[2])
        remove = text[index:index+length]
        text = text.replace(remove, "", 1)
    elif command == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in text:
            while substring in text:
                text = text.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            data = input()
            continue
    print(text)
    data = input()
print(f"Your password is: {text}")


