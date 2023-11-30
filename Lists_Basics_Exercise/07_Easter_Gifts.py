gifts_list = input().split()

while True:
    command = input().split()
    firs_command = command[0]
    gits_command = command[1]
    if firs_command == "No" and gits_command == "Money":
        break
    if firs_command == "OutOfStock":
        count = gifts_list.count((gits_command))
        for i in range(count):
           find = int(gifts_list.index(gits_command))
           gifts_list[find] = "None"
        pass
    if firs_command == "Required":
        index = int(command[2])
        # if index < len(gifts_list) - 1:
        if len(gifts_list) > index >= 0:
            gifts_list.pop(index)
            gifts_list.insert(index, gits_command)
    if firs_command == "JustInCase":
        gifts_list[-1] = gits_command

gifts_list_new = [str(x) for x in gifts_list if x != "None"]

print(" ".join(gifts_list_new))