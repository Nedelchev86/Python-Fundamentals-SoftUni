nums = int(input())
parking = {}

for i in range(nums):
    current_data = input().split()
    command = current_data[0]
    name = current_data[1]

    if command == "register":
        plate_number = current_data[2]
        if name not in parking:
            parking[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[name]}")
    else:
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking[name]
for key, value in parking.items():
    print(f"{key} => {value}")

