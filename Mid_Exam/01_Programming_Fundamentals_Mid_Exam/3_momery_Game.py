memory = input().split()
count = 0
while True:
    command = input()
    if command == "end":
        if len(memory) > 0:
            print("Sorry you lose :(")
            print(" ".join(list(map(str, memory))))
            break
    command = [int(x) for x in command.split()]
    first = command[0]
    second = command[1]
    count += 1
    if first < 0 or second < 0 or first == second or first >= len(memory) or second >= len(memory):
        print("Invalid input! Adding additional elements to the board")
        memory.insert((len(memory) // 2), str(-count) + "a")
        memory.insert((len(memory) // 2), str(-count) + "a")
        continue
    if memory[first] == memory[second]:
        print(F"Congrats! You have found matching elements - {memory[first]}!")
        if first > second:
            del memory[first]
            del memory[second]
        else:
            del memory[second]
            del memory[first]
    else:
        print("Try again!")
    if len(memory) == 0:
        print(F"You have won in {count} turns!")
        break
