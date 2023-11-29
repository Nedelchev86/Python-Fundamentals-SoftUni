# list_x = input().split(", ")
#
# for x in list_x:
#     w = ""
#     for i in x:
#         w = i + w
#     if (x == w):
#          print("True")
#     else:
#         print("False")


# def is_palindrome(s):
#     rev = ''.join(reversed(s))
#     if (s == rev):
#         return True
#     return False
#
# list_of_numbers = input().split(", ")
# for i in list_of_numbers:
#     ans = is_palindrome(i)
#     if (ans):
#         print("True")
#     else:
#         print("False")



my_list = input().split(", ")

for i in my_list:
    reverse = "".join(reversed(i))
    if reverse == i:
        print("True")
    else:
        print("False")


# my_list = input().split(", ")
#
# for word in my_list:
#     reverse = word[::-1]
#     if reverse == word:
#         print("True")
#     else:
#         print("False")


# def is_palindrome(s):
#     rev = s[::-1]
#     if s == rev:
#         return "True"
#     else:
#         return "False"
#
# list_of_numbers = input().split(", ")
# for i in list_of_numbers:
#     print(is_palindrome(i))


# def is_palindrome(s):
#
#     for i in s:
#         rev = i[::-1]
#         if i == rev:
#             print("True")
#         else:
#             print("False")
#
#
# list_of_numbers = input().split(", ")
# is_palindrome(list_of_numbers)
