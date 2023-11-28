import re
text = input()

pattern = r"(#|\|)([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]+)\1"
result = re.finditer(pattern, text)
total_calories = 0
final_list = []

for i in result:
    total_calories += int(i.group(4))
    final_list.append(f"Item: {i.group(2)}, Best before: {i.group(3)}, Nutrition: {i.group(4)}")

print(f"You have food to last you for: {total_calories//2000} days!")
print("\n".join(final_list))
