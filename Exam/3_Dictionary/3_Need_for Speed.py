number = int(input())

cars = dict()
for _ in range(number):
    data = input().split("|")
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    current_dict = dict()
    current_dict["mileage"] = mileage
    current_dict["fuel"] = fuel
    cars[car] = current_dict

while True:
    current_command = input().split(" : ")
    command = current_command[0]
    if command == "Stop":
        break
    car = current_command[1]
    if command == "Drive":
        distance = int(current_command[2])
        fuel = int(current_command[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(F"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] > 100000:
            print(F"Time to sell the {car}!")
            del cars[car]
    if command == "Refuel":
        fuel = int(current_command[2])
        if cars[car]["fuel"] + fuel > 75:
            print(F"{car} refueled with {75 - cars[car]['fuel']} liters")
            cars[car]["fuel"] = 75
        else:
            cars[car]["fuel"] += fuel
            print(F"{car} refueled with {fuel} liters")
    if command == "Revert":
        kilometers = int(current_command[2])
        if cars[car]["mileage"] - kilometers > 10000:
            cars[car]["mileage"] -= kilometers
            print(F"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car]["mileage"] = 10000
for car in cars:
    print(F"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")