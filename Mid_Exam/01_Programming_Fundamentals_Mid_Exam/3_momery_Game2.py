memory = input().split()
count = 0

while True:
    data = input().split()
    if data[0] == "end":
        break
    fist = int(data[0])
    second = int(data[1])
    count += 1
    if fist == second or fist < 0 or fist >= len(memory) or second < 0 or second >= len(memory):
        print("Invalid input! Adding additional elements to the board")
        memory.insert((len(memory)//2), F"-{count}a")
        memory.insert((len(memory)//2), F"-{count}a")
        continue
    if memory[fist] == memory[second]:
        print(F"Congrats! You have found matching elements - {memory[fist]}!")
        if fist > second:
            memory.pop(fist)
            memory.pop(second)
        else:
            memory.pop(second)
            memory.pop(fist)
    else:
        print("Try again!")
    if len(memory) == 0:
        print(F"You have won in {count} turns!")
        exit()
print("Sorry you lose :(")
print(" ".join(memory))