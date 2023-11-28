import re
from functools import reduce

data = input()
pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
result = re.finditer(pattern, data)
final_list = []
counter = 0
coolest = 0

pattern2 = r"\d"
result2 = re.findall(pattern2, data)
if len(result2) > 1:
    coolest = reduce((lambda x, y: int(x) * int(y)), result2)
else:
    coolest = int(result2[0])

for match in result:
    counter += 1
    total = sum(ord(x) for x in match.group(2))
    if total >= coolest:
        final_list.append(match.group(1) + match.group(2) + match.group(1))
print(f"Cool threshold: {coolest}")
print(f"{counter} emojis found in the text. The cool ones are:")
print("\n".join(final_list))
