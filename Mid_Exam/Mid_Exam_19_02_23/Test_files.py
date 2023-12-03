route_to_titan = input().split("||")
fuel = int(input())
ammunition = int(input())

for elements in route_to_titan:
    element = elements.split(" ")
    command = element[0]
    if command == "Titan":
        print(f"You have reached Titan, all passengers are safe.")
        break
    amount = element[1]

    if command == "Travel":
        needed_fuel = amount
        fuel = fuel - int(needed_fuel)
        if fuel >= 0:
            print(f"The spaceship travelled {needed_fuel} light-years.")
        else:
            print("Mission failed.")
            break
    if command == "Enemy":
        ammunition = ammunition - int(amount)
        if ammunition >= 0:
            print(f"An enemy with {amount} armour is defeated.")
        else:
            if fuel / 2 >= abs(ammunition):
                print(f"An enemy with {amount} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    if command == "Repair":
        fuel += int(amount)
        new_ammunition = 2 * int(amount)
        ammunition += int(new_ammunition)
        print(f"Ammunitions added: {new_ammunition}.")
        print(f"Fuel added: {amount}.")