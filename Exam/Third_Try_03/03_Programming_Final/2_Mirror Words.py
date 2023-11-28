import re

message = input()
pattern = r"(@|#){,2}([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
result = re.findall(pattern, message)
mirror = []

if not result:
    print("No word pairs found!")
    print("No mirror words!")
else:
    for match in result:
        reversed_word = match[1][::-1]
        if match[2] == reversed_word:
            mirror.append(f"{match[1]} <=> {match[2]}")
    print(f"{len(result)} word pairs found!")
    if mirror:
        print("The mirror words are:")
        print(", ".join(mirror))
    else:
        print("No mirror words!")
