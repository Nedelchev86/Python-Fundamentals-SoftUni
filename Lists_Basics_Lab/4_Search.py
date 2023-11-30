# number = int(input())
# keyword = input()
# list_one = []
#
# for i in range(number):
#     list_one.append(input())
# print(list_one)
#
# filtred_list = list()
# for i in list_one:
#     if keyword in i:
#         filtred_list.append(i)
# print(filtred_list)



number = int(input())
keyword = input()
list_one = []
filtred_list = []

for i in range(number):
    current_string = input()
    list_one.append(current_string)
    if keyword in current_string:
        filtred_list.append(current_string)

print(list_one)
print(filtred_list)

