import re

pattern = r"\b_([A-Za-z]+)\b"
text = input()
result = re.findall(pattern, text)

print(",".join(result))
