data = input().split()
palindrome = []
searched_palindrome = input()
count = 0

for word in data:
    # if word == word[::-1]:
    if word == "".join(reversed(word)):
        palindrome.append(word)
print(palindrome)
print(F"Found palindrome {palindrome.count(searched_palindrome)} times")

# for data in palindrome:
#     if data == searched_palindrome:
#         count +=1
# print(F"Found palindrome {count} times")
