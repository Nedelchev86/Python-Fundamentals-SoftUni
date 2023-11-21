num = int(input())

opening_bracket = 0
closing_bracket = 0

for i in range(1, num +1):
    command = input()
    if command == "(":
        opening_bracket += 1
    if command == ")":
        closing_bracket += 1
    if closing_bracket > opening_bracket:
        print("UNBALANCED")
        break
    if opening_bracket - closing_bracket == 2:
        print("UNBALANCED")
        break
else:
    print("BALANCED")

