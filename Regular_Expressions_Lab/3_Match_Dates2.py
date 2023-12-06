# import re
#
# data = input()
#
# pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"
# result = re.findall(pattern, data)
#
# for el in result:
#     print(f"Day: {el[0]}, Month: {el[2]}, Year: {el[3]}")


import re

data = input()

pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"
result = re.finditer(pattern, data)

for el in result:
    print(f"Day: {el.group(1)}, Month: {el.group(3)}, Year: {el.group(4)}")
