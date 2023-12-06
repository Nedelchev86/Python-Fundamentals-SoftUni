import re
pattern = r"(\+359)([ -])(2\1\d{3}\1\d{4}\b)"
prone_numbers = input()
result = re.findall(pattern, prone_numbers)

print(result)
