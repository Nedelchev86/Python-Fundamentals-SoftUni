import re

data = input()
pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
result = re.findall(pattern, data)

mirror_word = []

for pair in result:
    if pair[1] == pair[2][::-1]:
        mirror_word.append(F"{pair[1]} <=> {pair[2]}")
if len(result) > 0:
    print(F"{len(result)} word pairs found!")

    if not mirror_word:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(mirror_word))
else:
    print("No word pairs found!")
    print("No mirror words!")


