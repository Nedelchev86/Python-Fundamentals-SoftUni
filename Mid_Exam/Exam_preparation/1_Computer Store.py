total = 0
special = False

while True:
    parts = input()
    if parts == "special":
        special = True
        break
    if parts == "regular":
        break
    parts = float(parts)
    if parts < 0:
        print("Invalid price!")
        continue

    total += parts

taxes = total * 0.20
total_with_tax = total + taxes

if special:
    total_with_tax = total_with_tax * 0.9

if total > 0:
    print("Congratulations you've just bought a new computer!")
    print(F"Price without taxes: {total:.2F}$")
    print(F"Taxes: {taxes:.2F}$")
    print("-----------")
    print(F"Total price: {total_with_tax:.2F}$")
else:
    print(F"Invalid order!")