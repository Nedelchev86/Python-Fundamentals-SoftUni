import re

text = input()
searched_word = input()
pattern = fr"(?i)\b{searched_word}\b"

output = re.findall(pattern, text)

print(len(output))