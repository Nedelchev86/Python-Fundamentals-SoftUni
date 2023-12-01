shopping_list = input().split("!")

while True:
    data = input()
    if data == "Go Shopping!":
        break
    data = data.split()
    command = data[0]
    product = data[1]

    if command == "Urgent":
        if product not in shopping_list:
            shopping_list.insert(0, product)
    elif command == "Unnecessary":
        if product in shopping_list:
            shopping_list.remove(product)
    elif command == "Correct":
        if product in shopping_list:
            index = shopping_list.index(product)
            shopping_list[index] = data[2]
    else:
        if product in shopping_list:
            index = shopping_list.index(product)
            shopping_list.append(shopping_list.pop(index))
print(", ".join(shopping_list))
