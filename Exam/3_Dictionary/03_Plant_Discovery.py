number = int(input())
plants = dict()

for _ in range(number):
    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])

    current_hero_dict = dict()
    current_hero_dict["Rarity"] = rarity
    current_hero_dict["Rating"] = list()

    plants[plant] = current_hero_dict

while True:
    current_input = input()
    if current_input == "Exhibition":
        break
    current_input = current_input.split(": ")
    command = current_input[0]
    data = current_input[1].split(" - ")
    plant = data[0]

    if command == "Rate":
        if plant in plants.keys():
            plants[plant]["Rating"].append(int(data[1]))
        else:
            print("error")
    if command == "Update":
        if plant in plants.keys():
            plants[plant]["Rarity"] = int(data[1])
        else:
            print("error")
    if command == "Reset":
        if plant in plants.keys():
            plants[plant]["Rating"].clear()
        else:
            print("error")
print("Plants for the exhibition:")
for plant in plants.keys():
    if len(plants[plant]["Rating"]) > 0:
        average_rating = sum(plants[plant]["Rating"]) / len(plants[plant]["Rating"])
    else:
        average_rating = 0
    print(F"- {plant}; Rarity: {plants[plant]['Rarity']}; Rating: {average_rating:.2F}")

