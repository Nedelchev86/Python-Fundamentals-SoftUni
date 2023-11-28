import re
text = input()
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
result = re.finditer(pattern, text)
points = 0
destinations = []

for match in result:
    points += len(match.group(2))
    destinations.append(match.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
