import re
num = int(input())

pattern = r"([^ ]+)>([0-9]{3}(\|)[a-z]{3}\3[A-Z]{3}\3[^\<\>]{3})<\1"


for _ in range(num):
    password = input()
    result = re.finditer(pattern, password)
    for match in result:
        encrypted = match.group(2)
        encrypted = encrypted.replace("|", "")
        print(f"Password: {encrypted}")
        break
    else:
        print("Try another password!")
