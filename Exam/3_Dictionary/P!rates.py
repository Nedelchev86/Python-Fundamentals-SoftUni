pirates = {}
while True:
    data = input()
    if data == "Sail":
        break
    data = data.split("||")
    cities = data[0]
    population = int(data[1])
    gold = int(data[2])
    if cities not in pirates:
        pirates[cities] = {}
        pirates[cities]["population"] = population
        pirates[cities]["gold"] = gold
    else:
        pirates[cities]["population"] += population
        pirates[cities]["gold"] += gold

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
        print(F"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        pirates[town]["population"] -= people
        pirates[town]["gold"] -= gold
        if pirates[town]["population"] <= 0 or pirates[town]["gold"] <= 0:
            print(F"{town} has been wiped off the map!")
            del pirates[town]
    elif command == "Prosper":
        town = data[1]
        gold = int(data[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")

        else:
            pirates[town]["gold"] += gold
            print(F"{gold} gold added to the city treasury. {town} now has {pirates[town]['gold']} gold.")

if pirates.keys():
    print(F"Ahoy, Captain! There are {len(pirates.keys())} wealthy settlements to go to:")
    for town in pirates.keys():
        print(F"{town} -> Population: {pirates[town]['population']} citizens, Gold: {pirates[town]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
