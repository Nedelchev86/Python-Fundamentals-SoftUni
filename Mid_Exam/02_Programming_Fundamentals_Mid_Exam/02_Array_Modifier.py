array_with_integers = list(map(int, input().split()))
if len(array_with_integers) < 2 or len(array_with_integers) > 100:
    exit()
while True:
    command = input().split()
    if command[0] == "end":
        break
    if command[0] == "swap":
        index1, index2 = int(command[1]), int(command[2])
        array_with_integers[index1], array_with_integers[index2] = array_with_integers[index2], array_with_integers[index1]
    if command[0] == "multiply":
        array_with_integers[int(command[1])] = array_with_integers[int(command[1])] * array_with_integers[int(command[2])]
    if command[0] == "decrease":
        array_with_integers = list(map(lambda x: int(x - 1), array_with_integers))

array_with_integers = [str(x) for x in array_with_integers]
print(", ".join(array_with_integers))


# array_with_integers = list(map(int, input().split()))
# if len(array_with_integers) < 2 or len(array_with_integers) > 100:
#     exit()
# while True:
#     command = input().split()
#     if command[0] == "end":
#         break
#     if command[0] == "swap":
#         index1, index2 = int(command[1]), int(command[2])
#         array_with_integers[index1], array_with_integers[index2] = array_with_integers[index2], array_with_integers[index1]
#     if command[0] == "multiply":
#         array_with_integers[int(command[1])] = array_with_integers[int(command[1])] * array_with_integers[int(command[2])]
#     if command[0] == "decrease":
#         array_with_integers = [x - 1 for x in array_with_integers]
#
# array_with_integers = [str(x) for x in array_with_integers]
# print(", ".join(array_with_integers))
