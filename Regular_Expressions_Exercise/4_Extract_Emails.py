# import re
#
# text = input()
# pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b"
#
# output = re.findall(pattern, text)
#
# for i in output:
#     print(i[0])

import re

text = input()
pattern = r"\s(([a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b"

output = re.findall(pattern, text)

for i in output:
    print(i[0])