# import re
# data = input()
# total_calories = 0
#
# pattern = r"([#\|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
#
# result = re.finditer(pattern, data)
#
# for el in result:
#     nothing, product, date, calories = el.groups()
#     total_calories += int(calories)
#
# print(f"You have food to last you for: {total_calories// 2000} days!")
#
# result = re.finditer(pattern, data)
# for el in result:
#     nothing, product, date, calories = el.groups()
#     print(f"Item: {product}, Best before: {date}, Nutrition: {calories}")


import re
data = input()
total_calories = 0

pattern = r"([#\|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"

result = re.findall(pattern, data)

for el in result:
    nothing, product, date, calories = el
    total_calories += int(calories)

print(f"You have food to last you for: {total_calories// 2000} days!")

for el in result:
    nothing, product, date, calories = el
    print(f"Item: {product}, Best before: {date}, Nutrition: {calories}")
