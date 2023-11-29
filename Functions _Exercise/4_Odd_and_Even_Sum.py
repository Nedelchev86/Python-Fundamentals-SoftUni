def odd_even(num):
    even_sum = 0
    odd_sum = 0
    for i in number:
        digit = int(i)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return F"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_even(number))

