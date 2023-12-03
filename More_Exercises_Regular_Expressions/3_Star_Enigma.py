import re

number_of_messages = int(input())

attacked = list()
destroyed = list()


for message in range(number_of_messages):
    encrypted_message = input()
    decrypted_message = ''

    pattern = r'[starSTAR]'
    matches = len(re.findall(pattern, encrypted_message))

    for character in encrypted_message:
        decrypted_character = chr((ord(character)) - matches)
        decrypted_message += decrypted_character
    pattern2 = r"@([A-Za-z]+)\d*:[\d]+\!([A|D])\!->\d+"
    result = re.findall(pattern2, decrypted_message)
    if result:
        if result[0][1] == "A":
            attacked.append(result[0])
        elif result[0][1] == "D":
            destroyed.append(result[0])

print(F"Attacked planets: {len(attacked)}")
if attacked:
    for i in sorted(attacked):
        print(F"-> {i[0]}")
print(F"Destroyed planets: {len(destroyed)}")
if destroyed:
    for i in sorted(destroyed):
        print(F"-> {i[0]}")
