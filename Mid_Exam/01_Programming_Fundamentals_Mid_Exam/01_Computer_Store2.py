total = 0
while True:
    data = input()
    if data == "special":
        total_with_taxes = (total + (total * 0.2)) * 0.9
        break
    elif data == "regular":
        total_with_taxes = total + (total * 0.2)
        break
    data = float(data)
    if data < 0:
        print("Invalid price!")
        continue
    total += data

if total == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(F"Price without taxes: {total:.2F}$")
    print(F"Taxes: {total * 0.2:.2F}$")
    print("-----------")
    print(F"Total price: {total_with_taxes:.2F}$")