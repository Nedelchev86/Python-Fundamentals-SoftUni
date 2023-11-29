# def factoriel(num):
#     result = 1
#     for i in range(num, 0, -1):
#         result *= i
#     return result
#
#
# first = factoriel(int(input()))
# second = factoriel(int(input()))
# print(F"{first / second:.2F}")


def factoriel(num):
    return 1 if num == 0 or num == 1 else num * factoriel(num -1)


number1 = int(input())
number2 = int(input())
result = factoriel(number1) / factoriel(number2)
print(f"{result:.2F}")