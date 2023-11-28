import re
nums = int(input())

pattern = r"@#{1,}([A-Z][A-Za-z0-9]{4,}[A-Z])@#{1,}"
pattern2 = r"\d"

for _ in range(nums):
    data = input()
    barcode = re.findall(pattern, data)
    if barcode:
        product_code = re.findall(pattern2, barcode[0])
        if product_code:
            print(f"Product group: {''.join(product_code)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
