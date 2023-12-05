import re

pattern = r"\d+"

while True:
    text = input()

    if not text:
        break
    output_data = re.findall(pattern, text)
    if len(output_data) > 0:
        print(" ".join(output_data), end=" ")
    