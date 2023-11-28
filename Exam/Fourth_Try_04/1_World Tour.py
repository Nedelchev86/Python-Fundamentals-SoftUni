text = input()

while True:
    data = input().split(":")
    if data[0] == "Travel":
        break
    command = data[0]

    if command == "Add Stop":
        index = int(data[1])
        if index >= 0 and index < len(text):
            text = text[:index] + data[2] + text[index:]
    elif command == "Remove Stop":
        start, end = int(data[1]), int(data[2])
        if start >= 0 and start < len(text) and end >= 0 and end < len(text):
            text = text[:start] + text[end+1:]
    elif command == "Switch":
        old, new = data[1], data[2]
        text = text.replace(old, new)
    print(text)

print(f"Ready for world tour! Planned stops: {text}")

