numbers = int(input())
cars = {}

for _ in range(numbers):
    car, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split("|")]
    cars[car] = [mileage, fuel]

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break

    if command[0] == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars[car][1] >= fuel:
            cars[car][1] -= fuel
            cars[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars[car][0] >= 100_000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif command[0] == "Refuel":
        car, fuel = command[1], int(command[2])
        if cars[car][1] + fuel >= 75:
            print(f"{car} refueled with {75 - cars[car][1]} liters")
            cars[car][1] = 75
        else:
            cars[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif command[0] == "Revert":
        car, kilometers = command[1], int(command[2])
        if cars[car][0] - kilometers <= 10_000:
            cars[car][0] = 10_000
        else:
            cars[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
