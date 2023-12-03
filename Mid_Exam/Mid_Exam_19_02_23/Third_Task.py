shelf_with_books = input().split("&")

while True:
    current_input = input()

    if current_input == "Done":
        break

    current_data = current_input.split(" | ")
    command = current_data[0]

    if command == "Add Book":
        book = current_data[1]
        if book not in shelf_with_books:
            shelf_with_books.insert(0, book)
        else:
            continue
    elif command == "Take Book":
        book = current_data[1]
        if book in shelf_with_books:
            shelf_with_books.remove(book)
        else:
            continue
    elif command == "Swap Books":
        book1 = current_data[1]
        book2 = current_data[2]
        if book1 in shelf_with_books and book2 in shelf_with_books:
            idx1 = int(shelf_with_books.index(book1))
            idx2 = int(shelf_with_books.index(book2))
            shelf_with_books[idx1], shelf_with_books[idx2] = shelf_with_books[idx2], shelf_with_books[idx1]
        else:
            continue
    elif command == "Insert Book":
        book = current_data[1]
        if book not in shelf_with_books:
            shelf_with_books.append(book)
        else:
            continue
    elif command == "Check Book":
        idx = int(current_data[1])
        if idx >= 0 and idx < len(shelf_with_books):
            print(shelf_with_books[idx])
        else:
            continue
print(", ".join(shelf_with_books))



