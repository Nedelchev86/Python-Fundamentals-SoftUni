import re
import re

text = input().lower()
searched_word = input().lower()
pattern = fr"\b{searched_word}\b"

output = re.findall(pattern, text)

print(len(output))
