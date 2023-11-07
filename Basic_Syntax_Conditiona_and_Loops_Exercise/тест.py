while True:
    words = str(input())

    if words == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif words == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(words) < 5:
        print(f"{words} goes to Gryffindor.")
    elif len(words) == 5:
        print(f"{words} goes to Slytherin.")
    elif len(words) == 6:
        print(f"{words} goes to Ravenclaw.")
    elif len(words) > 6:
        print(f"{words} goes to Hufflepuff.")