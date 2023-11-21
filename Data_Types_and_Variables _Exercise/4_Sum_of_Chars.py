count = int(input())
total = 0

for i in range(count):
    command = ord(input())
    total += command
print(F"The sum equals: {total}")