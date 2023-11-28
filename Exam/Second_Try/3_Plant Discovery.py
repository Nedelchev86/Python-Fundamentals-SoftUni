number = int(input())
plants = {}

for i in range(number):
    plant, rarity = [int(x) if x.isdigit() else x for x in input().split("<->")]
    if plant not in plants:
        plants[plant] = [[], []]
    plants[plant][0] = rarity

while True:
    data = input()
    if data == "Exhibition":
        break
    command = data.split(": ")
    current_command = command[0]

    if current_command == "Rate":
        other = command[1].split(" - ")
        plant = other[0]
        rating = int(other[1])
        if plant in plants:
            plants[plant][1].append(rating)
        else:
            print("error")
            continue
    elif current_command == "Update":
        other = command[1].split(" - ")
        plant = other[0]
        rating = int(other[1])
        if plant in plants:
            plants[plant][0] = rating
        else:
            print("error")
            continue
    elif current_command == "Reset":
        plant = command[1]
        if plant in plants:
            plants[plant][1].clear()
        else:
            print("error")
            continue
print(f"Plants for the exhibition:")
for key, value in plants.items():
    if value[1]:
        print(f"- {key}; Rarity: {value[0]}; Rating: {(sum(value[1])/ len(value[1])):.2F}")
    else:
        print(f"- {key}; Rarity: {value[0]}; Rating: 0.00")
