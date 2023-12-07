# text = input().split()
#
# for word in text:
#     print(word * len(word), end="")

print("".join([x * len(x) for x in input().split()]))

