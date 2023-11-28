cities = {}

while True:
    data = input()
    if data == "Sail":
        break
    city, population, gold = [int(x) if x.isdigit() else x for x in data.split("||")]

    if city not in cities:
        cities[city] = [0, 0]
    cities[city][0] += population
    cities[city][1] += gold

while True:
    data = input()
    if data == "End":
        break
    data = data.split("=>")
    command = data[0]

    if command == "Plunder":
        town = data[1]
        people = int(data[2])
        gold = int(data[3])

        cities[town][0] -= people
        cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[town][0] <= 0 or cities[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]
    elif command == "Prosper":
        town = data [1]
        gold = int(data[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, other in cities.items():
        print(f"{town} -> Population: {other[0]} citizens, Gold: {other[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")