some_list = input().split()

print(F"{[x for x in some_list if len(x) % 2 == 0]}")