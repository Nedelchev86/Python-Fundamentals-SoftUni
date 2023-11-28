import re

text = input()
mirror = []

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})"
result = re.finditer(pattern, text)
result_count = 0

for i in result:
    result_count += 1
    if i.group(2) == i.group(3)[::-1]:
        mirror.append(f"{i.group(2)} <=> {i.group(3)}")
if result:
    print(f"{result_count if result_count != 0 else 'No'} word pairs found!")
    if mirror:
        print("The mirror words are:")
        print(", ".join(mirror))
    else:
        print("No mirror words!")

else:
    print("No word pairs found!")

