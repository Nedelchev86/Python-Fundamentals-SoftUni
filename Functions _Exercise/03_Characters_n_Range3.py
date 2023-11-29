first = input()
second = input()

new_list = list(map(lambda x: chr(x), range(ord(input()) + 1, ord(input()))))


print(*new_list)
