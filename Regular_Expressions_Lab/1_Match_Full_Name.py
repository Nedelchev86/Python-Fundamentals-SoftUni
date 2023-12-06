# import re
#
# text = input()
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
#
# filter_names = re.findall(pattern, text)
#
# print(" ".join(filter_names))

import re

text = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

filter_names = re.findall(pattern, text)

print(" ".join(filter_names))