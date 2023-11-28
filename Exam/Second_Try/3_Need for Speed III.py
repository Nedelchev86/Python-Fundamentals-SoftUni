num = int(input())
cars = {}

for _ in range(num):
    car, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split("|")]
    cars[car] = [mileage, fuel]

while True:
    data = input()
    if data == "Stop":
        break
    data = data.split(" : ")
    command = data[0]

    if command == "Drive":
        car, distance, fuel = [int(x) if x.isdigit() else x for x in data[1:]]
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][1] -= fuel
            cars[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif command == "Refuel":
        car, fuel = [int(x) if x.isdigit() else x for x in data[1:]]
        if cars[car][1] + fuel > 75:
            print(f"{car} refueled with {75 - cars[car][1]} liters")
            cars[car][1] = 75
        else:
            cars[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        car, mileage = [int(x) if x.isdigit() else x for x in data[1:]]
        if cars[car][0] - mileage < 10000:
            cars[car][0] = 10000
            continue
        else:
            print(f"{car} mileage decreased by {mileage} kilometers")
            cars[car][0] -= mileage

for car, info in cars.items():
    print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")