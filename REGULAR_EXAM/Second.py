import re
num = int(input())

pattern = r"(\W+|\w+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})<\1"


for _ in range(num):
    password = input()
    result = re.findall(pattern, password)
    if result:
        encrypted = result[0][1] + result[0][2] + result[0][3] + result[0][4]
        print(f"Password: {encrypted}")
    else:
        print("Try another password!")
