import re

# pattern = r"\%([A-Z][a-z]+)\%<([A-Za-z0-9]+)>\|(\d){1,}\|([0-9]+.[0-9]+)\$"
pattern = r"%([A-Z][a-z]+)%[^\|\$\%\.]*?<(\w+)>[^\|\$\%\.]*?\|[^\|\$\%\.]*?(\d+)\|[^\|\$\%\.]*?([0-9.]+[0-9]+)\$"
grand_total = 0
while True:
    data = input()
    if data == "end of shift":
        break
    result = re.findall(pattern, data)
    if result:
        total = int(result[0][2]) * float(result[0][3])
        grand_total += total
        print(f"{result[0][0]}: {result[0][1]} - {total:.2F}")
print(f"Total income: {grand_total:.2F}")