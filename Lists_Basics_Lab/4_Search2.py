num = int(input())
word = input()
my_lsit = []

for i in range(num):
    strings = input()
    my_lsit.append(strings)
print(my_lsit)

for el in range(len(my_lsit) -1, -1, -1):
    if word not in my_lsit[el]:
        my_lsit.remove(my_lsit[el])
print(my_lsit)