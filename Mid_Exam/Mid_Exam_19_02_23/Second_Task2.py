vehicles = input().split(">>")
total = 0
initial_tax = 0
tax_decline = 0
tax_for_km = 0
km_traveled = 0
for cars in vehicles:
    car, year_tax, kilometers = cars.split()
    year_tax = int(year_tax)
    kilometers = int(kilometers)
    car_type = True

    if car == "family":
        initial_tax = 50
        tax_decline = 12
        tax_for_km = 5
        km_traveled = 3000
    elif car == "heavyDuty":
        initial_tax = 80
        tax_decline = 14
        tax_for_km = 8
        km_traveled = 9000
    elif car == "sports":
        initial_tax = 100
        tax_decline = 18
        tax_for_km = 9
        km_traveled = 2000
    else:
        print("Invalid car type.")
        car_type = False
    if car_type:
        taxes = (initial_tax + (tax_decline * (kilometers // km_traveled))) - (year_tax * tax_for_km)
        total += taxes
        print(F"A {car} car will pay {taxes:.2F} euros in taxes.")
print(f"The National Revenue Agency will collect {total:.2F} euros in taxes.")
