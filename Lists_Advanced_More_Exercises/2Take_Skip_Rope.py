data = input()
digit = []
letter = []
new_string = ""
for i in data:
    if i.isdigit():
        digit.append(int(i))
    else:
        letter.append(i)

take_list = [digit[num] for num in range(len(digit)) if num % 2 == 0]
skip_list = [digit[num] for num in range(len(digit)) if num % 2 != 0]

letter = "".join(letter)

for i in range(len(take_list)):
    new_string += letter[:(take_list[i])]
    letter = letter[(skip_list[i] + take_list[i]):]
print(new_string)
