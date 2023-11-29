# def character(a, b):
#     news_list = []
#     for i in range(ord(a) + 1, ord(b)):
#         news_list.append(chr(i))
#     return print(*news_list)
#
#
# first = input()
# second = input()
# character(first, second)

def character(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


first = input()
second = input()
character(first, second)



