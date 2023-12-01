array_values =  list(map(int, input().split()))

while True:
    command =  input().split()
    if command[0] == "end":
        break
    if command[0] == "swap":
        first = int(command[1])
        second = int(command[2])
        array_values[first], array_values[second] = array_values[second], array_values[first]
    elif command[0] == "multiply":
        first = int(command[1])
        second = int(command[2])
        array_values[first] = array_values[first] * array_values[second]
    else:
        array_values = list(map(lambda x: int(x - 1), array_values))
        # for i in range(len(array_values)):
        #     array_values[i] -= 1
print(", ".join([str(x) for x in array_values]))
