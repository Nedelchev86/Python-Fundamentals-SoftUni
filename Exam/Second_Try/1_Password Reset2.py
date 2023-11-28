text = input()

while True:
    data = input().split()
    if data[0] == "Done":
        break
    command = data[0]

    if command == "TakeOdd":
        text = "".join([text[i] for i in range(len(text)) if i % 2 != 0])
    elif command == "Cut":
        index, length = [int(x) for x in data[1:]]
        remove = text[index:index+length]
        text = text.replace(remove, "", 1)
    elif command == "Substitute":
        substring, substitute = data[1:]
        if substring in text:
            text = text.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            continue
    print(text)
print(f"Your password is: {text}")


