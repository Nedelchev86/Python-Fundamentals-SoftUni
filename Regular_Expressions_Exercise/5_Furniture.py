import re
bought_furniture = []
total_money = 0
while True:
    command = input()
    if command == "Purchase":
        break
    pattern = r">>(\w+)<<(\d+\.?\d*)!(\d+)"
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)
print("Bought furniture:")
if bought_furniture:
    print("\n".join(bought_furniture))
print(F"Total money spend: {total_money:.2F}")