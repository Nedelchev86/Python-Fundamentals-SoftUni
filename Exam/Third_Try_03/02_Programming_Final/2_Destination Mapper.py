import re

destination = input()
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
result = re.finditer(pattern, destination)
points = 0
matches = []

for match in result:
    points += len(match.group(2))
    matches.append(match.group(2))
print(f"Destinations: {', '.join(matches)}")
print(f"Travel Points: {points}")
