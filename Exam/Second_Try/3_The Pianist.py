nums = int(input())
pianist = {}

for _ in range(nums):
    piece, composer, key = input().split("|")
    pianist[piece] = [composer, key]

while True:
    data = input()
    if data == "Stop":
        break
    data = data.split("|")
    command = data[0]

    if command == "Add":
        piece, composer, key = data[1:]
        if piece not in pianist:
            pianist[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command == "Remove":
        piece = data[1]
        if piece in pianist:
            del pianist[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        piece, new_key = data[1:]
        if piece in pianist:
            pianist[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in pianist.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
    