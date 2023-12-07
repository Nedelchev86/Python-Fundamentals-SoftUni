# while True:
#     word = input()
#     if word == "end":
#         break
#     print(F"{word} = {word[::-1]}")


# while True:
#     word = input()
#     if word == "end":
#         break
#     reversed_word = word[::-1]
#     print(F"{word} = {reversed_word}")


while True:
    word = input()
    if word == "end":
        break
    reversed_word = ""
    for ch in reversed(word):
        reversed_word += ch
    print(F"{word} = {reversed_word}")
