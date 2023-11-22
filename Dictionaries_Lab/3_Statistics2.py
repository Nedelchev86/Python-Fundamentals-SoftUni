text = input()
store = dict()

while text != "statistics":
    test = text.split(": ")
    product = test[0]
    quantity = int(test[1])

    if product in store.keys():
        store[product] += int(quantity)
    else:
        store[product] = int(quantity)
    text = input()
        
print("Products in stock:")
for word in store:
    print(F"- {word}: {store[word]}")
print(F"Total Products: {len(store)}")
print(F"Total Quantity: {sum(store.values())}")
