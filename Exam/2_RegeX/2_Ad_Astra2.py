import re

data = input()
pattern = r"(#|\|)([A-Za-z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
result = re.findall(pattern, data)
calories = 0
print_result = ""

for i in result:
    print_result += f"Item: {i[1]}, Best before: {i[2]}, Nutrition: {i[3]}\n"
    calories += int(i[3])

print(F"You have food to last you for: {calories // 2000} days!")
print(print_result)
