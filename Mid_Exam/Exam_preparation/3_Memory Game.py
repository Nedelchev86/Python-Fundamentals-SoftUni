memory = input().split()
count = 0

while True:
    count +=1
    data = input()
    if data == "end":
        break
    first, second = [int(x) for x in data.split()]

    if first == second or first < 0 or first >= len(memory) or second >= len(memory) or second < 0:
        # idx = int(len(memory) / 2)
        idx = len(memory) // 2
        memory.insert(idx, str(-count)+"a")
        memory.insert(idx, str(-count)+"a")
        print("Invalid input! Adding additional elements to the board")
        continue

    if memory[first] == memory[second]:
        print(F"Congrats! You have found matching elements - {memory[first]}!")
        current = memory[first]
        memory.remove(current)
        memory.remove(current)
    else:
        print("Try again!")

    if not memory:
        print(F"You have won in {count} turns!")
        break
if memory:
    print("Sorry you lose :(")
    print(" ".join(memory))
