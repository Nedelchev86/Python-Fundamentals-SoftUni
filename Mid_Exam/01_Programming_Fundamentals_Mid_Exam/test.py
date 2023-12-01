sequence = list(map(str, input().split()))
moves = 0
while True:
    if len(sequence) == 0:
        print(f'You have won in {moves} turns!')
        break
    indexes = input()
    if indexes != 'end':
        moves += 1
        indexes = list(map(int, indexes.split()))
        if indexes[0] == indexes[1] or indexes[0] < 0 or indexes[0] >= len(sequence) or indexes[1] < 0 or indexes[
            1] >= len(sequence):
            print("Invalid input! Adding additional elements to the board")
            sequence.insert((len(sequence) // 2), F"-{moves}a")
            sequence.insert((len(sequence) // 2), F"-{moves}a")
            continue
        else:
            if sequence[indexes[0]] == sequence[indexes[1]]:
                print(f"Congrats! You have found matching elements - {sequence[indexes[0]]}!")
                removable_string = sequence[indexes[0]]
                counter = 0
                sequence.remove(removable_string)
                sequence.remove(removable_string)
            else:
                print('Try again!')
    else:
        print(f'Sorry you lose :(')
        print(*[x for x in sequence], end=' ')
        break

