number = int(input())
parking = {}

for _ in range(number):
    data = input().split()
    command = data[0]
    username = data[1]

    if command == "register":
        license_plate_number = data[2]
        if username not in parking:
            parking[username] = license_plate_number
            print(F"{username} registered {license_plate_number} successfully")
        else:
            print(F"ERROR: already registered with plate number {license_plate_number}")
    if command == "unregister":
        if username not in parking:
            print(F"ERROR: user {username} not found")
        else:
            print(F"{username} unregistered successfully")
            del parking[username]
for key, value in parking.items():
    print(F"{key} => {value}")
