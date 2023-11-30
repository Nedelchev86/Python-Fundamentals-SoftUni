data = input().split("#")
new_list = list()
water = int(input())
total_fire = 0
effort = 0
print("Cells:")

for i in data:
    new_list = i.split(" = ")
    type_if_fire = new_list[0]
    value_of_cell = int(new_list[1])
    if type_if_fire == "High":
        if 81 <= value_of_cell <= 125:
            total_fire += value_of_cell
            water -= value_of_cell
        else:
            continue
    if type_if_fire == "Medium":
        if 51 <= value_of_cell <= 80:
            total_fire += value_of_cell
            water -= value_of_cell
        else:
            continue
    if type_if_fire == "Low":
        if 1 <= value_of_cell <= 50:
            total_fire += value_of_cell
            water -= value_of_cell
        else:
            continue
    if water <= 0:
        total_fire -= value_of_cell
        break
    print(F" - {value_of_cell}")
print(F"Effort: {total_fire * 0.25:.2F}")
print(F"Total Fire: {total_fire}")
