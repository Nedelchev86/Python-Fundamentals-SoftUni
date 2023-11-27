import re

data = input()

pattern = r"(#|\|)([A-Za-z ]+)\1(\d+\/\d+\/\d{2})\1(\d+)\1"
output = re.findall(pattern, data)

total = 0
for i in range(len(output)):
    total += int(output[i][3])

print(F"You have food to last you for: {total // 2000} days!")
for i in range(len(output)):
    print(F"Item: {output[i][1]}, Best before: {output[i][2]}, Nutrition: {output[i][3]}")

