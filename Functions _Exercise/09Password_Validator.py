
def password_count(a):
    if len(a) > 5 and len(a) < 11:
        return True
    else:
        return False


def digit_count(a):
    digit_counter = 0
    for i in a:
        ord_sym = ord(i)
        if ord_sym > 47 and ord_sym < 58:
            digit_counter += 1
    if digit_counter >= 2:
        return True
    else:
        return False


def password_symbol(a):
    valid = True
    for i in a:
        ord_sym = ord(i)
        if ord_sym > 96 and ord_sym < 123 or ord_sym > 47 and ord_sym < 58 or ord_sym > 64 and ord_sym < 107:
            valid = True
        else:
            valid = False
            break
    if valid:
        return True
    else:
        return False


def password_validator(text):
    check_count = password_count(text)
    check_symbol = password_symbol(text)
    check_digit = digit_count(text)
    if check_count and check_symbol and check_digit:
        print("Password is valid")
    if not check_count:
        print("Password must be between 6 and 10 characters")
    if not check_symbol:
        print("Password must consist only of letters and digits")
    if not check_digit:
        print("Password must have at least 2 digits")


password_validator(input())
