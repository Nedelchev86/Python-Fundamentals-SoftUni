# number = int(input())
#
# for i in range(97, 97 + number):
#     for j in range(97, 97 + number):
#         for k in range(97, 97 + number):
#             print(F"{chr(i)}{chr(j)}{chr(k)}")


number = int(input())
start = ord("a")
end = 97 + number

for first in range(start, end):
    for second in range(start, end):
        for third in range(start, end):
            print(F"{chr(first)}{chr(second)}{chr(third)}")
