
neighborhood = list(map(int, input().split("@")))
current_index = 0
count = 0

while True:
    data = input().split()
    if data[0] == "Love!":
        print(F"Cupid's last position was {current_index}.")
        for nums in neighborhood:
            if nums == 0:
                count += 1
        if count == len(neighborhood):
            print("Mission was successful.")

        else:
            print(F"Cupid has failed {len(neighborhood) - neighborhood.count(0)} places.")
        break
    jump = int(data[1])
    current_index += jump
    if current_index >= len(neighborhood):
        current_index = 0
    if neighborhood[current_index] == 0:
        print(F"Place {current_index} already had Valentine's day.")
    else:
        neighborhood[current_index] -= 2
        if neighborhood[current_index] == 0:
            print(F"Place {current_index} has Valentine's day.")

