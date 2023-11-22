data = input()
phonebook = dict()

while "-" in data:
    data = data.split("-")
    name = data[0]
    phone = data[1]
    if name not in phonebook:
        phonebook[name] = phone
    data = input()
for i in range(int(data)):
    name = input()
    if name in phonebook:
        print(F"{name} -> {phonebook[name]}")
    else:
        print(F"Contact {name} does not exist.")