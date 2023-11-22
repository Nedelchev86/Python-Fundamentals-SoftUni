statistics = dict()

while True:
    data = input().split(":")
    if data[0] == "statistics":
        break
    product = data[0]
    quantity = int(data[1])
    if product not in statistics.keys():
        statistics[product] = quantity
    else:
        statistics[product] += int(quantity)
print("Products in stock:")
for word in statistics:
    print(F"- {word}: {statistics[word]}")
print(F"Total Products: {len(statistics)}")
print(F"Total Quantity: {sum(statistics.values())}")

