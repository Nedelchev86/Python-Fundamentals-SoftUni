total = 0
special = False
while True:
    price = input()
    if price == "special":
        special = True
        break
    if price == "regular":
        break
    price = float(price)
    if price < 0:
        print("Invalid price!")
        continue
    total += price

if total == 0:
    print("Invalid order!")
else:
        print("Congratulations you've just bought a new computer!")
        print(F"Price without taxes: {total:.2f}$")
        print(F"Taxes: {total * 0.2:.2f}$")
        print(F"-----------")
        if special:
            print(F"Total price: {(total + (total * 0.2)) * 0.90:.2f}$")
        else:
            print(F"Total price: {total + (total * 0.2):.2f}$")