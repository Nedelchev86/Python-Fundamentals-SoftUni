destinations = input()

while True:
    command = input()
    if command == "Travel":
        break
    command, first, second = [int(x) if x.isdigit() else x for x in command.split(":")]
    if command == "Add Stop":
        if 0 <= first < len(destinations):
            destinations = destinations[:first] + second + destinations[first:]
    elif command == "Remove Stop":
        if 0 <= first < len(destinations) and 0 <= second < len(destinations):
            destinations = destinations[:first] + destinations[second+1:]
    elif command == "Switch":
        destinations = destinations.replace(first, second)
    print(destinations)
print(f"Ready for world tour! Planned stops: {destinations}")
