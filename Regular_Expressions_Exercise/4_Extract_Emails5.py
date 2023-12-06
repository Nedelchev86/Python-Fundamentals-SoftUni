# import re
# text = input()
#
# pattern = r"\s(([a-z0-9]+[a-z0-9\-\_\.]*)@[\w-]+(\.\w+)+)\b"
# result = re.findall(pattern, text)
#
# for el in result:
#     print(el[0])

import re
text = input()

pattern = r"\s(([a-z0-9]+[a-z0-9\-\_\.]*)@[\w-]+(\.\w+)+)\b"
result = re.finditer(pattern, text)

for el in result:
    print(el.group())