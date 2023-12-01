data = [int(x) for x in input().split()]
count = 0

while True:
    current_data = input()
    if current_data == "end":
        break
    current_data = current_data.split()
    command = current_data[0]
    if command == "swap":
        count += 1
        index1 = int(current_data[1])
        index2 = int(current_data[2])
        if index1 >=0 and index1 < len(data) and index2 >=0 and index2 < len(data):

            data[index1], data[index2] = data[index2], data[index1]
            print(data)
        else:
            print(data)

    elif command == "enumerate_list":
        enumerate_list = list(enumerate(data))
        print(enumerate_list)
        count += 1

    elif command == "max":
        max_num = max(data)
        print(max_num)
        count += 1

    elif command == "min":
        min_num = min(data)
        print(min_num)
        count += 1
    elif command == "get_divisible":
        print([x for x in data if x % int(current_data[2]) == 0])
        count += 1
print(count)
