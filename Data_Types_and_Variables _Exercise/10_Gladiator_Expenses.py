#
# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# helmet_broke = 0
# sword_broke = 0
# shield_Broke = 0
# armor_broke = 0
#
# for i in range(1, lost_fights + 1):
#     if i % 2 == 0:
#         helmet_broke += 1
#     if i % 3 == 0:
#         sword_broke += 1
#     if i % 2 == 0 and i % 3 == 0:
#         shield_Broke += 1
#         if shield_Broke % 2 == 0:
#             armor_broke += 1
# expenses = (helmet_price * helmet_broke) + (shield_price * shield_Broke) \
#            + (sword_price * sword_broke) + (armor_price * armor_broke)
#
# print(F"Gladiator expenses: {expenses:.2F} aureus")



lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broke = 0
sword_broke = 0
shield_Broke = 0
armor_broke = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        helmet_broke += 1
    if i % 3 == 0:
        sword_broke += 1
    if i % 6 == 0:
        shield_Broke += 1
    if i % 12 == 0:
        armor_broke += 1
expenses = (helmet_price * helmet_broke) + (shield_price * shield_Broke) \
           + (sword_price * sword_broke) + (armor_price * armor_broke)

print(F"Gladiator expenses: {expenses:.2F} aureus")
