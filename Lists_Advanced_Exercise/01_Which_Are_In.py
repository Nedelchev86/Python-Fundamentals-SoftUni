first_list = input().split(", ")
second_list = input().split(", ")
new_list = []
for i in range(len(first_list)):
    string = first_list[i]
    for j in second_list:
        if string in j and string not in new_list:
            new_list.append(string)
print(new_list)


# first = input().split(", ")
# second = input()
# filtred_list = [x for x in first if x in second]
#
# print(filtred_list)
