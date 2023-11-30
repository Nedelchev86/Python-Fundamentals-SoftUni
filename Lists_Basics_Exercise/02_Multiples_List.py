factor = int(input())
count = int(input())

new_list = []
for i in range(1, count + 1):
    new_list.append(i * factor)
print(new_list)

# factor, count,  = int(input()), int(input())
#
# print(list(map(lambda x: x * factor, range(1, count + 1))))
