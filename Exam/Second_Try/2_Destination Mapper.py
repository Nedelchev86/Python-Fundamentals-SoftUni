import re

data = input()
pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"
result = re.findall(pattern, data)
destination = []
total = 0

for el in result:
    destination.append(el[1])
    total += len(el[1])

print(f"Destinations: {', '.join(destination)}")
print(f"Travel Points: {total}")