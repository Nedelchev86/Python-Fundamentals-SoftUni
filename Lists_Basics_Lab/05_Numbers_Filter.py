count = int(input())
my_list = list()

for i in range(count):
    number = int(input())
    my_list.append(number)

filtred_list = list()

commands = input()

for j in my_list:
    if commands == "even" and j % 2 == 0:
        filtred_list.append(j)
    if commands == "odd" and j % 2 != 0:
        filtred_list.append(j)
    if commands == "negative" and j < 0:
        filtred_list.append(j)
    if commands == "positive" and j >= 0:
        filtred_list.append(j)

print(filtred_list)
