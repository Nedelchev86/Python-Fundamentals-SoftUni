nums = int(input())

my_list = []

for _ in range(nums):
    my_list.append(int(input()))

command = input()

if command == "even":
    print([x for x in my_list if x % 2 == 0])
elif command == "odd":
    print([x for x in my_list if x % 2 != 0])
elif command == "negative":
    print([x for x in my_list if x < 0])
else:
    print([x for x in my_list if x >= 0])
