import re

number = int(input())

for i in range(number):
    data = input()
    pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
    output = re.search(pattern, data)
    if output:
        code = output.group(2)
        pattern2 = r"\d+"
        barcode = re.findall(pattern2, code)
        if barcode:
            print(F"Product group: {''.join(barcode)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")