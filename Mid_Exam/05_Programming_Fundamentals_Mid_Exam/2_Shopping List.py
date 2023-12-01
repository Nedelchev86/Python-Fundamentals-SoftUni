shopping_list = input().split("!")

while True:
    data = input().split()
    command = data[0]
    item = data[1]

    if command == "Go":
        break

    if command == "Urgent" and item not in shopping_list:
        shopping_list.insert(0, item)
    if command == "Unnecessary" and item in shopping_list:
        shopping_list.remove(item)
    if command == "Correct" and item in shopping_list:
        idx = shopping_list.index(item)
        shopping_list[idx] = data[2]
    if command == "Rearrange" and item in shopping_list:
        shopping_list.remove(item)
        shopping_list.append(item)
print(", ".join(shopping_list))
