import re
num = int(input())

pattern = r"(\W+|\w+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})<\1"


for _ in range(num):
    password = input()
    result = re.finditer(pattern, password)
    for match in result:
        encrypted = match.group(2) +match.group(3) + match.group(4)+ match.group(5)
        print(f"Password: {encrypted}")
        break
    else:
        print("Try another password!")
