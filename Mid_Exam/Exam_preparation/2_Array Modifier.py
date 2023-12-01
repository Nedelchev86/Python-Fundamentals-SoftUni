array = [int(x) for x in input().split()]

data = input()

while data != "end":
    data = data.split()
    command = data[0]

    if command == "swap":
        idx1 = int(data[1])
        idx2 = int(data[2])
        array[idx1], array[idx2] = array[idx2], array[idx1]
    elif command == "multiply":
        idx1 = int(data[1])
        idx2 = int(data[2])
        array[idx1] = array[idx1] * array[idx2]
    else:
        array = [x -1 for x in array]
    data = input()
print(", ".join([str(x) for x in array]))