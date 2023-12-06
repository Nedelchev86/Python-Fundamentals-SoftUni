import re
while True:
    data = input()
    if not data:
        break
    pattern = r"(\bwww\.[A-Za-z0-9\-]+(\.[A-Za-z0-9]+){1,}[a-z]\b)"
    result = re.findall(pattern, data)
    if result:
        print("".join(result[0][0]))