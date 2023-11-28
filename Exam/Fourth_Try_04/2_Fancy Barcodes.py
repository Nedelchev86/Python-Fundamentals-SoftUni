import re

number = int(input())


pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
pattern2 = r"\d"

for _ in range(number):
    text = input()
    result = re.findall(pattern, text)
    if not result:
        print("Invalid barcode")
        continue
    result2 = re.findall(pattern2, result[0])
    if result2:
        print(f"Product group: {''.join(str(x) for x in result2)}")
    else:
        print(f"Product group: 00")
