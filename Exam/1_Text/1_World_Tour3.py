text = input()

while True:
    data = input().split(":")
    command = data[0]
    if command == "Travel":
        print(F"Ready for world tour! Planned stops: {text}")
        break
    if command == "Add Stop":
        index = int(data[1])
        if 0 <= index <= (len(text) - 1):
            text = text[:index] + data[2] + text[index:]
    elif command == "Remove Stop":
        start = int(data[1])
        end = int(data[2])
        if 0 <= start <= (len(text) - 1) and end <= (len(text) - 1):
            text = text[:start] + text[end+1:]
    elif command == "Switch":
        text = text.replace(data[1], data[2])
    print(text)

