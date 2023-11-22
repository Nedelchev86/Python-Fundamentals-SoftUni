bakery = input().split()
my_dict = {}

for i in range(0, len(bakery) -1, 2):
    my_dict[bakery[i]] = int(bakery[i+1])
print(my_dict)