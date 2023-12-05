notebook = {}

some_input = input().split(" | ")

for el in some_input:
    el = el.split(": ")
    word, definition = el

    notebook[word] = notebook.get(word, [])
    notebook[word].append(definition)

word_for_test = input().split(" | ")

command = input()

if command == "Test":
    for el in word_for_test:
        if el in notebook:
            print(f"{el}:")
            result = [f" -{x}" for x in notebook[el]]
            print("\n".join(result))

elif command == "Hand Over":
    for key, value in notebook.items():
        print(key, end=" ")

