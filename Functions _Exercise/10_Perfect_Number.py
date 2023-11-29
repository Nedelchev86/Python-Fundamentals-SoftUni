
def perfect_number(num):
    perfect_list = []
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            perfect_list.append(i)
            sum += i
            if sum == num:
                return True


result = perfect_number(int(input()))

if result:
    print("We have a perfect number!")
else:
    print(" It's not so perfect.")

#
# def perfect_number(num):
#     sum = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             sum += i
#             if sum / 2 == num:
#                 return True
#
#
# result = perfect_number(int(input()))
#
# if result:
#     print("We have a perfect number!")
# else:
#     print(" It's not so perfect.")