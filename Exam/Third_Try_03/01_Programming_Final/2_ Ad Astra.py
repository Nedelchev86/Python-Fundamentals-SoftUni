import re

some_text = input()

pattern = r"([#|])([A-Za-z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
result = re.finditer(pattern, some_text)

calories = 0
for match in result:
    calories += int(match.group(4))

print(f"You have food to last you for: {calories//2000} days!")
result = re.finditer(pattern, some_text)
for match in result:
    print(f"Item: {match.group(2)}, Best before: {match.group(3)}, Nutrition: {match.group(4)}")
