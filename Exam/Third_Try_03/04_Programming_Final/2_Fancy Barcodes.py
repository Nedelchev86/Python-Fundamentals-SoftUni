import re

nums = int(input())
pattern = r"(@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,})"
pattern2 = r"\d"

for _ in range(nums):
    text = input()
    result = re.findall(pattern, text)
    result2 = re.findall(pattern2, text)
    if result:
        if result2:
            print(f'Product group: {"".join([str(x) for x in result2])}')
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
