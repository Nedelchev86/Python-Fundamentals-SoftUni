import re

pattern = r"\d+"
text = input()

while text:
    output_data = re.findall(pattern, text)
    if output_data:
        print(" ".join(output_data), end=" ")
    text = input()