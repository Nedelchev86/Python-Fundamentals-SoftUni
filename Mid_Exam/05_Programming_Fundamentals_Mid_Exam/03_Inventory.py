# journal = input().split(", ")
#
#
# while True:
#     command = input().split(" - ")
#     if command[0] == "Craft!":
#         break
#     if command[0] == "Collect":
#         if command[1] not in journal:
#             journal.append(command[1])
#     elif command[0] == "Drop":
#         if command[1] in journal:
#             journal.remove(command[1])
#     elif command[0] == "Combine Items":
#         combine_list = command[1].split(":")
#         if combine_list[0] in journal:
#             find = journal.index(combine_list[0])
#             journal.insert(journal.index(combine_list[0]) + 1, combine_list[1])
#     else:
#         if command[1] in journal:
#             find = journal.index(command[1])
#             journal.append(command[1])
#             journal.pop(find)
# print(", ".join(journal))

journal = input().split(", ")


while True:
    command = input().split(" - ")
    if command[0] == "Craft!":
        break
    action = command[0]
    item = command[1]
    if action == "Collect":
        if item not in journal:
            journal.append(item)
    elif action == "Drop":
        if item in journal:
            journal.remove(item)
    elif action == "Combine Items":
        combine_list = item.split(":")
        if combine_list[0] in journal:
            find = journal.index(combine_list[0])
            journal.insert(journal.index(combine_list[0]) + 1, combine_list[1])
    else:
        if command[1] in journal:
            find = journal.index(item)
            journal.append(item)
            journal.pop(find)
print(", ".join(journal))
