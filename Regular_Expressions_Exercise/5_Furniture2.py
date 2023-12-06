# import re
# pattern = r">>(\w+)<<(\d+\.?\d*)!(\d+)"
# total = 0
# bought = []
# while True:
#     data = input()
#     if data == "Purchase":
#         break
#     result = re.search(pattern, data)
#     if result:
#         furniture, price, quantity = result.groups()
#         bought.append(furniture)
#         total += float(price) * int(quantity)
# print("Bought furniture:")
# if bought:
#     print("\n".join(bought))
# print(F"Total money spend: {total:.2F}")


import re

pattern = r">>(\w+)<<(\d+\.?\d*)!(\d+)"
total = 0
bought = []

while True:
    data = input()
    if data == "Purchase":
        break
    result = re.findall(pattern, data)
    if result:
        furniture, price, quantity = result[0]
        bought.append(furniture)
        current_sum = float(price) * int(quantity)
        total += current_sum
print("Bought furniture:")
if bought:
    print("\n".join(bought))
print(F"Total money spend: {total:.2F}")