collection_of_items =  input().split("|")
buudget = float(input())
buyed_items = []
money_spend = 0

for el in collection_of_items:
    types = el.split("->")
    kind = types[0]
    price = float(types[1])
    if (kind == "Clothes" and price > 50.00) or (kind == "Shoes" and price > 35.00) or (kind == "Accessories" and price > 20.50):
        continue
    if buudget >= price:
        print(F"{price*1.4:.2F}", end=" ")
        money_spend += price
        buudget -= price
    else:
        break

total_money  = money_spend * 1.4 + buudget
print(F"\nProfit: {money_spend*0.4:.2F}")

if total_money >= 150:
    print(F"Hello, France!")
else:
    print(F"Not enough money.")