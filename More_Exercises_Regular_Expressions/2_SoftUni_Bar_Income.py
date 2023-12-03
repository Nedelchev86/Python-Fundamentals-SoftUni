# import re
# total = 0
# while True:
#
#     data = input()
#     if data == "end of shift":
#         break
#     pattern = r"%([A-Z][a-z]+)%([^\|\$\%\.]*?)<(\w+)>([^\|\$\%\.]*?)\|([^\|\$\%\.]*?)(\d+)\|([^\|\$\%\.]*?)([0-9.]+[0-9]+)\$"
#
#
#     output = re.search(pattern, data)
#     if output:
#         name = output.group(1)
#         product = output.group(3)
#         quantity = output.group(6)
#         price = output.group(8)
#         print(F"{name}: {product} - {int(quantity) * float(price):.2F}")
#         total += int(quantity) * float(price)
# if total != 0:
#     print(F"Total income: {total:.2F}")


import re
total = 0
while True:

    data = input()
    if data == "end of shift":
        break
    pattern = r"%([A-Z][a-z]+)%[^\|\$\%\.]*?<(\w+)>[^\|\$\%\.]*?\|[^\|\$\%\.]*?(\d+)\|[^\|\$\%\.]*?([0-9.]+[0-9]+)\$"

    output = re.search(pattern, data)
    if output:
        name, product, quantity, price = output.groups()
        print(F"{name}: {product} - {int(quantity) * float(price):.2F}")
        total += int(quantity) * float(price)
if total != 0:
    print(F"Total income: {total:.2F}")
