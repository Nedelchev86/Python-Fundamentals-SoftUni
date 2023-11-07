# n = int(input())
# for i in range(n):
#     number = int(input())
#     if number % 2 != 0:
#         print(F"{number} is odd!")
#         exit()
# else:
#     print("All numbers are even.")


num = int(input())

for i in range(num):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")