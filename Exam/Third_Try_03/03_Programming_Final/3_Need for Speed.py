nums = int(input())
cars = {}

for _ in range(nums):
    car, mileage, fuel = input().split("|")
    cars[car] = [int(mileage), int(fuel)]

while True:
    command = input()
    if command == "Stop":
        break
    command, *other = command.split(" : ")
    if command == "Drive":
        car, distance, fuel = other
        if cars[car][1] >= int(fuel):
            cars[car][1] -= int(fuel)
            cars[car][0] += int(distance)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif command == "Refuel":
        car, fuel = other
        if cars[car][1] + int(fuel) >= 75:
            print(f"{car} refueled with {75 - cars[car][1]} liters")
            cars[car][1] = 75
        else:
            print(f"{car} refueled with {fuel} liters")
            cars[car][1] += int(fuel)
    elif command == "Revert":
        car, kilometers = other
        if cars[car][0] - int(kilometers) >= 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
            cars[car][0] -= int(kilometers)
        else:
            cars[car][0] = 10000
for key, value in cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")