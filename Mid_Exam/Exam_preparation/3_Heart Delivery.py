houses = [int(x) for x in input().split("@")]
current_idx = 0

while True:
    data = input()
    if data == "Love!":
        break
    data = data.split()
    command = data[0]
    idx = int(data[1])

    if current_idx + idx >= 0 and current_idx + idx < len(houses):
        current_idx += idx
    else:
        current_idx = 0
    if houses[current_idx] == 0:
        print(F"Place {current_idx} already had Valentine's day.")
        continue
    houses[current_idx] -= 2
    if houses[current_idx] <=0:
        print(f"Place {current_idx} has Valentine's day." )
        houses[current_idx] = 0


print(f"Cupid's last position was {current_idx}.")
if houses.count(0) == len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - houses.count(0)} places.")



