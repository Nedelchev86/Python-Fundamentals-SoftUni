nums = int(input())
plants = {}

for _ in range(nums):
    plant, rarity = input().split("<->")
    plants[plant] = [int(rarity), []]

while True:
    command = input()
    if command == "Exhibition":
        break
    command, other = command.split(": ")

    if command == "Rate":
        plant, rating = other.split(" - ")
        if plant not in plants:
            print("error")
            continue
        plants[plant][1].append(int(rating))
    elif command == "Update":
        plant, rating = other.split(" - ")
        if plant not in plants:
            print("error")
            continue
        plants[plant][0] = int(rating)
    else:
        if other not in plants:
            print("error")
            continue
        plants[other][1].clear()
print("Plants for the exhibition:")
for key, value in plants.items():
    if value[1]:
        print(f"- {key}; Rarity: {value[0]}; Rating: {(sum(value[1]) / len(value[1])):.2F}")
    else:
        print(f"- {key}; Rarity: {value[0]}; Rating: 0.00")
