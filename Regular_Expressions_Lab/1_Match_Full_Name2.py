import re
pattern = r"[A-Z][a-z]+ [A-Z][a-z]+"
data = input()
names = re.findall(pattern, data)

print(" ".join(names))
