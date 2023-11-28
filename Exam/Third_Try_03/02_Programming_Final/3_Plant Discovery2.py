nums = int(input())
plants = {}


def check_name(name, plants_dict):
    if name not in plants_dict:
        print("error")
        return
    return True


for _ in range(nums):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": rarity, "rating": []}


while True:
    command = input()
    if command == "Exhibition":
        break
    command, other = command.split(": ")

    if command == "Rate":
        plant, rating = other.split(" - ")
        if check_name(plant, plants):
            plants[plant]["rating"].append(int(rating))
    elif command == "Update":
        plant, rating = other.split(" - ")
        if check_name(plant, plants):
            plants[plant]["rarity"] = rating
    else:
        if check_name(other, plants):
            plants[other]["rating"].clear()
print("Plants for the exhibition:")
for key, value in plants.items():
    if value["rating"]:
        average = sum(value['rating']) / len(value['rating'])
    else:
        average = 0.00

    print(f"- {key}; Rarity: {value['rarity']}; Rating: {average:.2F}")
