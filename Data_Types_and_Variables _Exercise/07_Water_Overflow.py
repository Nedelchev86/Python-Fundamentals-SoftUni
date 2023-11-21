# tank_capacity = 255
# current_water = 0
# number = int(input())
#
# for i in range(number):
#     liters_of_water = int(input())
#     current_water += liters_of_water
#     if tank_capacity < current_water:
#         print("Insufficient capacity!")
#         current_water -= liters_of_water
# print(current_water)


capacity = 255
n = int(input())
tank = 0

for _ in range(n):
    water_liters = int(input())
    if tank + water_liters > capacity:
         print("Insufficient capacity!")
    else:
        tank += water_liters
print(tank)
