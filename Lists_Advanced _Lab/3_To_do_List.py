new_list = ["" for x in range(11)]

while True:
    command = input()
    if command == "End":
        break
    commant_new = command.split("-")
    new_list[int(commant_new[0])] = commant_new[1]
print([x for x in new_list if x != ''])




#
# tasks = []
# while True:
#     command = input().split("-")
#
#     if command[0] == "End":
#         break
#
#     priority = int(command[0])
#     task = command[1]
#     tasks.append((priority, task))
#
# sorted_task =[task_data[1] for task_data in sorted(tasks)]
# print(sorted_task)

