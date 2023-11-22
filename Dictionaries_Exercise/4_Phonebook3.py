data = input()
phonebook = {}

while "-" in data:
    name, phone = data.split("-")
    phonebook[name] = phone
    data = input()

for i in range(int(data)):
    name = input()
    if name in phonebook:
        print(F"{name} -> {phonebook[name]}")
    else:
        print(F"Contact {name} does not exist.")
