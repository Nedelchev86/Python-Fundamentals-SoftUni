shopping_list = input().split("!")

while True:
    user_input = input().split(" ")
    command = user_input[0]
    item = user_input[1]
    if user_input[1] == "Shopping!":
        break
    if command == "Urgent" and item not in shopping_list:
        shopping_list.insert(0, item)
    if command == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
    if command == "Correct":
        for j in range(len(shopping_list)):
            if shopping_list[j] == item:
                shopping_list[j] = user_input[2]
    if command == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
print(", ".join(shopping_list))
