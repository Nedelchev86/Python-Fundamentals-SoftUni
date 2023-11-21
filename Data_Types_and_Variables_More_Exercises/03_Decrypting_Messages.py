# key = int(input())
# num = int(input())
#
# for i in range(1, num + 1):
#     command = input()
#     print(chr(ord(command)+key), end='')



# key, n  = int(input()) , int(input())
# new_symbol = ""
#
# for i in range(n):
#     new_symbol += chr(ord(input()) + key)
#
# print(new_symbol)

key, n  = int(input()) , int(input())

for i in range(n):
    print((chr(ord(input()) + key)), end="")
