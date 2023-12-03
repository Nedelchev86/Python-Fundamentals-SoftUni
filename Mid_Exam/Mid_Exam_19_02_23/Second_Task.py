vehicles = input().split(">>")
total = 0

for cars in vehicles:
    car, year_tax, kilometers = cars.split()
    year_tax = int(year_tax)
    kilometers = int(kilometers)
    car_type = True
    taxes = 0

    if car == "family":
        taxes = (50 + (12 * (kilometers // 3000))) - (year_tax * 5)
    elif car == "heavyDuty":
        taxes = (80 + (14 * (kilometers // 9000))) - (year_tax * 8)
    elif car == "sports":
        taxes = (100 + (18 * (kilometers // 2000))) - (year_tax * 9)
    else:
        print("Invalid car type.")
        car_type = False
    if car_type:
        total += taxes
        print(F"A {car} car will pay {taxes:.2F} euros in taxes.")
print(f"The National Revenue Agency will collect {total:.2F} euros in taxes.")
