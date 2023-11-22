products_dict = {}
products = input()

while products != "buy":
    products = products.split()
    product = products[0]
    price = float(products[1])
    quantity = int(products[2])

    if product not in products_dict:
        products_dict[product] = [0, 0]
    products_dict[product][0] = price
    products_dict[product][1] += quantity

    products = input()

for key, value in products_dict.items():
    print(f"{key} -> {value[0] * value[1]:.2F}")
