# string_list = input().split()
# char = ""
# other = ""
#
# for string in string_list:
#     for i in string:
#         if i.isdigit():
#             char += str(i)
#         else:
#             other += i
#     other = other[-1] + other[1:-1]+ other[0]
#     print(chr(int(char))+other)
#     char = ""
#     other = ""


# string_list = input().split()
# char = []
# other = []
#
# for string in string_list:
#     for i in string:
#         if i.isdigit():
#             char.append(i)
#         else:
#             other.append(i)
#     other[0], other[-1] = other[-1], other[0]
#     print(f"{chr(int(''.join(char)))}{''.join(other)}", end=" ")
#     char.clear()
#     other.clear()


# message = input().split(' ')
# result = []
#
# for word in message:
#     ascii_char = [char for char in word if char.isdigit()]
#     word_list = [char for char in word if char not in ascii_char]
#
#     first_letter = chr(int(''.join(ascii_char)))
#     word_list[0], word_list[-1] = word_list[-1], word_list[0]
#     new_word = first_letter + ''.join(word_list)
#     result.append(new_word)
#
# print(' '.join(result))

# message = input().split(' ')
# result = []
#
# for word in message:
#     ascii_char = [char for char in word if char.isdigit()]
#     word_list = [char for char in word if char.isalpha()]
#
#     first_letter = chr(int(''.join(ascii_char)))
#     word_list[0], word_list[-1] = word_list[-1], word_list[0]
#     new_word = first_letter + ''.join(word_list)
#     result.append(new_word)
#
# print(' '.join(result))


# message = input().split(' ')
# result = []
#
# for word in message:
#     ascii_char = chr(int("".join([char for char in word if char.isdigit()])))
#     word_list = [char for char in word if char.isalpha()]
#
#     word_list[0], word_list[-1] = word_list[-1], word_list[0]
#     result.append(ascii_char + ''.join(word_list))
#
# print(' '.join(result))


message = input().split(' ')
result = []

for word in message:
    ascii_char = [char for char in word if char.isdigit()]
    word_str = [char for char in word if char.isalpha()]

    first_letter = chr(int(''.join(ascii_char)))
    word_str[0], word_str[-1] = word_str[-1], word_str[0]
    new_word = first_letter + ''.join(word_str)
    result.append(new_word)

print(' '.join(result))