text = input()
upper = ""
while True:
    data= input().split(">>>")
    command = data[0]
    if command == "Generate":
        break
    if command == "Contains":
        if data[1] in text:
            print(F"{text} contains {data[1]}")
        else:
            print(F"Substring not found!")
    elif command == "Flip":
        if data[1] == "Upper":
            big = text[int(data[2]):int(data[3])]
            text = text[:int(data[2])] + big.upper() + text[int(data[3]):]
            print(text)
        else:
            small = text[int(data[2]):int(data[3])]
            text = text[:int(data[2])] + small.lower() + text[int(data[3]):]
            print(text)
    elif command == "Slice":
        text = text[:int(data[1])] + text[int(data[2]):]
        print(text)
print(f"Your activation key is: {text}")

