# text = input()
# digits = ""
# letters = ""
# other = ""
#
# for chr in text:
#     if chr.isdigit():
#         digits += chr
#     elif chr.isalpha():
#         letters += chr
#     else:
#         other += chr
# print(digits)
# print(letters)
# print(other)

text = input()
digits = []
letters = []
other = []

for chr in text:
    if chr.isdigit():
        digits.append(chr)
    elif chr.isalpha():
        letters.append(chr)
    else:
        other.append(chr)
print("".join(digits))
print("".join(letters))
print("".join(other))