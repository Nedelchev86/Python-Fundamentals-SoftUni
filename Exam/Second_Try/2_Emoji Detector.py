import re

data = input()
pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
patern2 = r"\d"
result = re.findall(pattern, data)

cool_threshold = 1
cool = re.findall(patern2, data)

for i in cool:
    cool_threshold *= int(i)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(result)} emojis found in the text. The cool ones are:")

for el in result:
    curent_total = 0
    for x in el[1]:
        curent_total += ord(x)
    if curent_total >= cool_threshold:
        print(f"{el[0]}{el[1]}{el[0]}")

