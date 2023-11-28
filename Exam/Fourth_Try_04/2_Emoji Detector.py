import re

text = input()
pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
result = re.finditer(pattern, text)

pattern2 = r"\d"


