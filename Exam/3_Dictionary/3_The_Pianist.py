number = int(input())
pieces = dict()

for _ in range(number):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]
    pieces[piece] = [composer, key]

while True:
    text_input = input().split("|")
    command = text_input[0]
    if command == "Stop":
        break
    piece = text_input[1]

    if command == "Add":
        composer = text_input[2]
        key = text_input[3]
        if piece not in pieces.keys():
            pieces[piece] = [composer, key]
            print(F"{piece} by {composer} in {key} added to the collection!")
        else:
            print(F"{piece} is already in the collection!")
    if command == "Remove":
        if piece in pieces:
            pieces.pop(piece)
            print(F"Successfully removed {piece}!")
        else:
            print(F"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        key = text_input[2]
        if piece in pieces:
            pieces[piece][1] = key
            print(F"Changed the key of {piece} to {key}!")
        else:
            print(F"Invalid operation! {piece} does not exist in the collection.")

for piece in pieces:
    print(F"{piece} -> Composer: {pieces[piece][0]}, Key: {pieces[piece][1]}")