import re

data = input()
pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
result = re.findall(pattern, data)
threshold = 1
sum_check = 0

pattern2 = r"\d"
result2 = re.findall(pattern2, data)
for i in result2:
    threshold *= int(i)

print(F"Cool threshold: {threshold}")
print(F"{len(result)} emojis found in the text. The cool ones are:")

for i in result:
    sum_check = 0
    for j in i[1]:
        sum_check += ord(j)
    if sum_check >= threshold:
        print(i[0]+i[1]+i[0])
