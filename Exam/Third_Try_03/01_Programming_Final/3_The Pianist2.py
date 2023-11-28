nums = int(input())

pianist = {}

for _ in range(nums):
    piece, composer, key = input().split("|")
    pianist[piece] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split("|")

    if command[0] == "Add":
        piece, composer, key = command[1],command[2], command[3]
        if piece not in pianist:
            print(F"{piece} by {composer} in {key} added to the collection!")
            pianist[piece] = [composer, key]
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in pianist:
            del pianist[piece]
            print(F"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece, new_key = command[1], command[2]
        if piece in pianist:
            print(f"Changed the key of {piece} to {new_key}!")
            pianist[piece][1] = new_key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, (composer, key) in pianist.items():
    print(f"{piece} -> Composer: {composer}, Key: {key}")
