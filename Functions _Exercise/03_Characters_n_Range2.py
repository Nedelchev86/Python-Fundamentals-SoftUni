def character(a, b):
    new_list = list(map(lambda x: chr(x), range(ord(a) + 1, ord(b))))
    return new_list


first = input()
second = input()

print(*character(first, second))
