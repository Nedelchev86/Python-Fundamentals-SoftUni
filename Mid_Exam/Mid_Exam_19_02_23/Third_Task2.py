shelf_with_books = input().split("&")
current_input = input()

while current_input != "Done":

    current_data = current_input.split(" | ")
    command = current_data[0]
    book = current_data[1]

    if command == "Add Book":
        if book not in shelf_with_books:
            shelf_with_books.insert(0, book)

    elif command == "Take Book":
        if book in shelf_with_books:
            shelf_with_books.remove(book)

    elif command == "Swap Books":
        book2 = current_data[2]
        if book in shelf_with_books and book2 in shelf_with_books:
            idx1 = int(shelf_with_books.index(book))
            idx2 = int(shelf_with_books.index(book2))
            shelf_with_books[idx1] = book2
            shelf_with_books[idx2] = book

    elif command == "Insert Book":
        if book not in shelf_with_books:
            shelf_with_books.append(book)

    elif command == "Check Book":
        idx = int(book)
        if 0 <= idx < len(shelf_with_books):
            print(shelf_with_books[idx])
    current_input = input()

print(", ".join(shelf_with_books))
