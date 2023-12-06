# text = input().split()
# first = text[0]
# second = text[1]
# total = 0
#
# if len(first) > len(second):
#     for i in range(len(second)):
#         total += int(ord(first[i])) * int(ord(second[i]))
#     for i in range(len(second), len(first)):
#         total += int(ord(first[i]))
# elif len(first) < len(second):
#     for i in range(len(first)):
#         total += int(ord(first[i])) * int(ord(second[i]))
#     for i in range(len(first), len(second)):
#         total += int(ord(second[i]))
#
# else:
#     for i in range(len(first)):
#         total += int(ord(first[i])) * int(ord(second[i]))
#
# print(total)


text = input().split()
first = text[0]
second = text[1]
total = 0

if len(first) > len(second):
    for i in range(len(first)):
        if i < len(second):
            total += int(ord(first[i])) * int(ord(second[i]))
        else:
            total += int(ord(first[i]))
elif len(first) < len(second):
    for i in range(len(second)):
        if i < len(first):
            total += int(ord(first[i])) * int(ord(second[i]))
        else:
            total += int(ord(second[i]))

else:
    for i in range(len(first)):
        total += int(ord(first[i])) * int(ord(second[i]))

print(total)