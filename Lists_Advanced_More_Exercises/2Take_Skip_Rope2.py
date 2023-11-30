data = input()
digit = [int(x) for x in data if x.isdigit()]
letter = "".join([x for x in data if not x.isdigit()])
new_string = ""


take_list = [digit[num] for num in range(len(digit)) if num % 2 == 0]
skip_list = [digit[num] for num in range(len(digit)) if num % 2 != 0]


for i in range(len(take_list)):
    new_string += letter[:(take_list[i])]
    letter = letter[(skip_list[i] + take_list[i]):]
print(new_string)
