# first = int(input())
# second = int(input())
#
# for i in range (first, second +1):
#     print(chr(i), end=" ")

first = int(input())
second = int(input())
result = ""
delimiter = " "

for i in range (first, second +1):
    result += chr(i) + delimiter
print(result)
