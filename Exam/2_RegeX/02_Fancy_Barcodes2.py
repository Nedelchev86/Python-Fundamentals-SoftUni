import re

number_of_barcode = int(input())

for i in range(number_of_barcode):
    barcode = input()
    pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
    result = re.match(pattern, barcode)
    if result:
        pattern2 = r"\d+"
        data = re.findall(pattern2, result.group())
        if data:
            print(F"Product group: {''.join(data)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")