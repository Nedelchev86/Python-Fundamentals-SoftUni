pirates = {}

while True:
    data = input()
    if data == "Sail":
        break
    town, people, gold = [int(x) if x.isdigit() else x for x in data.split("||")]
    pirates[town] = pirates.get(town, {"gold": 0, "people": 0})
    pirates[town]["people"] += people
    pirates[town]["gold"] += gold


while True:
    command = input()
    if command == "End":
        break
    command, city, *other = command.split("=>")
    if command == "Plunder":
        people, gold = other
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        pirates[city]["gold"] -= int(gold)
        pirates[city]["people"] -= int(people)
        if pirates[city]["gold"] <= 0 or pirates[city]["people"] <= 0:
            print(f"{city} has been wiped off the map!")
            del pirates[city]
    elif command == "Prosper":
        gold = int(other[0])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        pirates[city]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {pirates[city]['gold']} gold.")
if pirates:
    print(f"Ahoy, Captain! There are {len(pirates)} wealthy settlements to go to:")
    for key, value in pirates.items():
        print(f"{key} -> Population: {value['people']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
