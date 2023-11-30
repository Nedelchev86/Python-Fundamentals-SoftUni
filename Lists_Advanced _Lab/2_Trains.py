wagons = int(input())

train = [0 for x in range(wagons)]

while True:
    command = input().split()
    if command[0] == "End":
        break
    index = int(command[1])
    if command[0] == "add":
        train[-1] += index
    if command[0] == "insert":
        train[index] += int(command[2])
    if command[0] == "leave":
        train[index] -= int(command[2])
print(train)

