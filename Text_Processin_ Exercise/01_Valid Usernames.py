def lenght(username):
    if 3 <= len(username) <= 16:
        return  True
    return False


def character(username):
    for chr in username:
        if not (chr.isalnum() or chr == "_" or chr == "-"):
            return False
    return  True


def redundant(username):
    if " " in username:
        return  False
    return True


def username_validation(username):
    if lenght(username) and character(username) and redundant(username):
        return True
    return False

usernames = input().split(", ")

for name in usernames:
    if username_validation(name):
        print(name)