import re

data = input()

pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"

filtred_data = re.findall(pattern, data)

for i in filtred_data:
    print(F"Day: {i[0]}, Month: {i[2]}, Year: {i[3]}")