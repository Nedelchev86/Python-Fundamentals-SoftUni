products = dict()

while True:
    data = input()
    if data == "buy":
        break
    data = data.split()
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])
    if product not in products:
        products[product] = [0, 0]
    products[product] = [price, (quantity + products[product][1])]


for key, value in products.items():
    print(F"{key} -> {value[0] * value[1]:.2F}")
