import re

prone_numbers = input()
pattern = r"\+359([ -])2\1\d{3}\1\d{4}\b"

filtered_phones = re.finditer(pattern, prone_numbers)
phone_list = list()
for match in filtered_phones:
    phone_list.append(match.group())

print(", ".join(phone_list))