import re

prone_numbers = input()
pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"

filtered_phones = re.findall(pattern, prone_numbers)

print(", ".join(filtered_phones))
