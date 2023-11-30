# vowles = ['a', 'o', 'u', 'e', 'i']
# no_vowels = []
# string = input()
#
# for i in string:
#     if i not in vowles:
#         no_vowels.append(i)
# print("".join(no_vowels))


# vowles = ['a', 'o', 'u', 'e', 'i']
#
# no_vowels = [x for x in input() if x not in vowles]
# print("".join(no_vowels))



print("".join([x for x in input() if x not in ['a', 'o', 'u', 'e', 'i']]))
