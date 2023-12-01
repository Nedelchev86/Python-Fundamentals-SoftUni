# targets = list(map(int, input().split()))
#
# while True:
#     command = input().split()
#     if command[0] == "End":
#         break
#     if command[0] == "Shoot":
#         index = int(command[1])
#         power = int(command[2])
#         if index < len(targets) and index >= 0:
#             targets[index] -= power
#             if targets[index] <= 0:
#                 targets.pop(index)
#     elif command[0] == "Add":
#         index = int(command[1])
#         if index < len(targets)  and index >= 0:
#             targets.insert(index, int(command[2]))
#         else:
#             print("Invalid placement!")
#     elif command[0] == "Strike":
#         index = int(command[1])
#         radius = int(command[2])
#         if index - radius >= 0 and index + radius < len(targets):
#             targets = targets[:(index - radius)] + targets[index + radius +1:]
#         else:
#             print("Strike missed!")
# targets = [str(x) for x in targets]
# print("|".join(targets))
#

targets = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "End":
        break
    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if index < len(targets) and index >= 0:
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif command[0] == "Add":
        index = int(command[1])
        if index < len(targets) and index >= 0:
            targets.insert(index, int(command[2]))
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        if index - radius >= 0 and index + radius < len(targets):
            del targets[(index - radius):(index + radius + 1)]
        else:
            print("Strike missed!")
targets = [str(x) for x in targets]
print("|".join(targets))

