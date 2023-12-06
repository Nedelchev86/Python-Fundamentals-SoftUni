first, second = input().split()
result = 0

if len(first) > len(second):
    for i in range(len(second)):
        result += ord(first[i]) * ord(second[i])
    for i in range(len(second), len(first)):
        result += ord(first[i])


elif len(first) < len(second):
    for i in range(len(first)):
        result += ord(second[i]) * ord(first[i])
    for i in range(len(first), len(second)):
        result += ord(second[i])
else:
    for i in range(len(first)):
        result += ord(second[i]) * ord(first[i])

print(result)