first, second, data = ord(input()),ord(input()), input()


result = sum([ord(x) for x in data if first < ord(x) < second])
print(result)
