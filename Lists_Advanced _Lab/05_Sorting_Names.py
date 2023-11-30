# name = input().split(", ")
# names = sorted(name, key=lambda x: (-len(x), x))
# print(names)


# Just test in one line
print(sorted(input().split(", "), key=lambda x: (-len(x), x)))