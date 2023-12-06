# import re
# while True:
#     data = input()
#     if not data:
#         break
#     pattern = r"(\bwww\.[A-Za-z-0-9\-]+(\.[A-Za-z0-9]+){1,}[\w+]\b)"
#     result = re.findall(pattern, data)
#     if result:
#         print(result[0][0])
#

import re
while True:
    data = input()
    if not data:
        break
    pattern = r"(www\.[A-Za-z-0-9]+\.[A-Za-z]+(\.\w+)*)"
    result = re.findall(pattern, data)
    if result:
        print(result[0][0])