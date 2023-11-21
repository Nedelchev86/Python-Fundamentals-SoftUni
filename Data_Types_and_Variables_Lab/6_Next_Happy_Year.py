# number = int(input())
#
# while True:
#     year = str(number)
#     if len(set(year)) == len(year):
#         print(year)
#         break
#     number += 1



year = int(input())

while True:
    year += 1
    set_year = str(year)
    if len(set(set_year)) == len(set_year):
        print(set_year)
        break
