def family_car(year, km):
    initial_tax = 50
    tax_decline = 12
    tax_for_km = 5
    km_traveled = 3000
    return (initial_tax + (tax_decline * (km // km_traveled))) - (year * tax_for_km)


def heavy(year, km):
    initial_tax = 80
    tax_decline = 14
    tax_for_km = 8
    km_traveled = 9000
    return (initial_tax + (tax_decline * (km // km_traveled))) - (year * tax_for_km)


def sports(year, km):
    initial_tax = 100
    tax_decline = 18
    tax_for_km = 9
    km_traveled = 2000
    return (initial_tax + (tax_decline * (km // km_traveled))) - (year * tax_for_km)


vehicles = input().split(">>")
total = 0

for cars in vehicles:
    car, year_tax, kilometers = cars.split()
    year_tax = int(year_tax)
    kilometers = int(kilometers)
    car_type = True

    if car == "family":
        taxes = family_car(year_tax, kilometers)

    elif car == "heavyDuty":
        taxes = heavy(year_tax, kilometers)

    elif car == "sports":
        taxes = sports(year_tax, kilometers)
    else:
        print("Invalid car type.")
        car_type = False
    if car_type:
        total += taxes
        print(F"A {car} car will pay {taxes:.2F} euros in taxes.")
print(f"The National Revenue Agency will collect {total:.2F} euros in taxes.")
