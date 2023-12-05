notebook = {}

some_input = input().split(" | ")

for el in some_input:
    el = el.split(": ")
    word, definition = el

    if word not in notebook:
        notebook[word] = []
    notebook[word].append(definition)

word_for_test = input().split(" | ")

command = input()

if command == "Test":
    for el in word_for_test:
        if el in notebook:
            print(f"{el}:")
            for things in notebook[el]:
                print(f" -{things}")

if command == "Hand Over":
    result = []
    for key,value in notebook.items():
        result.append(key)
    print(" ".join(result))

