numbers = int(input())
plants = {}

for _ in range(numbers):
    plant, rarity = input().split("<->")
    plants[plant] = [rarity, []]

while True:
    data = input()
    if data == "Exhibition":
        break
    data = data.split(": ")
    command = data[0]

    if command == "Rate":
        plant, rating = data[1].split(" - ")
        if plant in plants:
            plants[plant][1].append(int(rating))
        else:
            print("error")
    elif command == "Update":
        plant, rarity = data[1].split(" - ")
        if plant in plants:
            plants[plant][0] = rarity
        else:
            print("error")
    elif command == "Reset":
        if data[1] in plants:
            plants[data[1]][1].clear()
        else:
            print("error")
print("Plants for the exhibition:")
for key, value in plants.items():
    if value[1]:
        print(f"- {key}; Rarity: {value[0]}; Rating: {sum(value[1])/len(value[1]):.2F}")
    else:
        print(f"- {key}; Rarity: {value[0]}; Rating: 0.00")
