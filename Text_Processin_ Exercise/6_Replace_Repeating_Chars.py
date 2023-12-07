# text = input()
# new_text = ""
# last_chr = ""
#
# for i in range(len(text)):
#     if last_chr != text[i]:
#         new_text += text[i]
#         last_chr = text[i]
# print(new_text)


text = input()
new_text = ""
last_chr = ""

for char in text:
    if last_chr != char:
        new_text +=char
        last_chr = char
print(new_text)

