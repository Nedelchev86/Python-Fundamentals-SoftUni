import re

pattern = r"\d+"

while True:
    data = input()

    if not data:
        break

    result = re.findall(pattern, data)
    if len(result) > 0:
        print(" ".join(result), end=" ")