text = input()
data = input()

while data != "Travel":
    command, start, end = [int(x) if x.isdigit() else x for x in data.split(":")]

    if command == "Add Stop" and 0 <= start < len(text):
        text = text[:start] + end + text[start:]
    elif command == "Remove Stop" and start >=0 and end < len(text):
        text = text[:start] + text[end+1:]
    elif command == "Switch" and start in text:
        text = text.replace(start, end)
    data = input()
    print(text)
print(f"Ready for world tour! Planned stops: {text}")
