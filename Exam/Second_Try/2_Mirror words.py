import re

data = input()
pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
mirror = []
result = re.findall(pattern, data)

if result:
    print(f"{len(result)} word pairs found!")
    for el in result:
        first = el[1]
        second = el[2]
        if first == second[::-1]:
            mirror.append(f"{first} <=> {second}")
    if mirror:
        print("The mirror words are:")
        print(", ".join(mirror))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")


