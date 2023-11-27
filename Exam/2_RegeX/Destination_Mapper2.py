import re

data = input()
pattern = r"(=|\/)[A-Z][A-Za-z]{2,}\1"
result = re.finditer(pattern, data)

points = 0
all_destnations = []

for destination in result:
    current_destination = re.split('\/|=', destination.group())[1]
    points += len(current_destination)
    all_destnations.append(current_destination)

print(F"Destinations: {', '.join(all_destnations)}")
print(F"Travel Points: {points}")
