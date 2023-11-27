import re
total = 0
data = input()
destnation = list()
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
result = re.findall(pattern, data)

for i in range(len(result)):
    destnation.append(result[i][1])
    total += int(len(result[i][1]))

print(F"Destinations: {', '.join(destnation)}")
print(F"Travel Points: {total}")