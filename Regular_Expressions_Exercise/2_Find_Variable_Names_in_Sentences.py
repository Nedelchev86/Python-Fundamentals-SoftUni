import re

text = input()

pattern = r"\b_([A-Za-z0-1]+)\b"
output = re.findall(pattern, text)

print(",".join(output))
