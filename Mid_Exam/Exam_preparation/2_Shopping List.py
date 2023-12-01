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
        else:
            continue
    elif command == "Unnecessary":
        if product in shopping_list:
            shopping_list.remove(product)
        else:
            continue
    elif command == "Correct":
        if product in shopping_list:
            idx = shopping_list.index(product)
            shopping_list[idx] = data[2]
        else:
            continue
    elif command == "Rearrange":
        if product in shopping_list:
            shopping_list.remove(product)
            shopping_list.append(product)
print(", ".join(shopping_list))
