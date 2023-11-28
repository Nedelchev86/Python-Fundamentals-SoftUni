import re


text = input()
pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
pattern2 = r"\d"
matches = re.findall(pattern2, text)
matches2 = re.finditer(pattern, text)
start = 1

trash = 1
for el in matches:
    trash *= int(el)

print(f"Cool threshold: {trash}")
print(f"{len(matches2)} emojis found in the text. The cool ones are:")

for x in matches2:
    sum_check = 0
    for el in x.group(2):
        sum_check += ord(el)
    if sum_check >= trash:
        print(f"{x.group(1)}{x.group(2)}{x.group(1)}")
