text = input()

while True:
    data = input().split(":|:")
    command = data[0]
    if command == "Reveal":
        break
    if command == "InsertSpace":
        index = int(data[1])
        text = text[:index] + " " + text[index:]
    if command == "Reverse":
        substring = data[1]
        if substring in text:
            text = text.replace(substring, "", 1)
            text = text + substring[::-1]
        else:
            print("error")
            continue
    if command == "ChangeAll":
        if data[1] in text:
            text = text.replace(data[1], data[2])
    print(text)
print(F"You have a new text message: {text}")
