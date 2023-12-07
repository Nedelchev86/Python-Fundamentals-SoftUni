data = input()
digits = []
letter = []
symbol = []

for char in data:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letter.append(char)
    else:
        symbol.append(char)
print("".join(digits))
print("".join(letter))
print("".join(symbol))
