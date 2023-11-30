def multiplication_sign(first, second, third):
    if first == 0 or second == 0 or third == 0:
        return "zero"
    if first < 0 and second < 0 and third > 0:
        return "positive"
    if first > 0 and second < 0 and third < 0:
        return "positive"
    if first < 0 and second > 0 and third < 0:
        return "positive"
    if first < 0 or second < 0 or third < 0:
        return "negative"
    else:
        return "positive"


print(multiplication_sign(int(input()), int(input()), int(input())))
