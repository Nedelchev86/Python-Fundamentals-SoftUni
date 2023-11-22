product_list = input().split()
searched_products = input().split()

products = {}

for i in range(0, len(product_list), 2):
    key = product_list[i]
    value = int(product_list[i+1])
    products[key] = value

for product in searched_products:
    if product in products.keys():
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
