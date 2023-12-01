# price_rating = [int(x) for x in input().split(", ")]
#
# entry_point = int(input())
# typo_of_items = input()
#
# if typo_of_items == "cheap":
#     left = [x for x in price_rating[:entry_point] if x < price_rating[entry_point]]
#     right = [x for x in price_rating[entry_point+1:] if x < price_rating[entry_point]]
# else:
#     left = [x for x in price_rating[:entry_point] if x >= price_rating[entry_point]]
#     right = [x for x in price_rating[entry_point+1:] if x >= price_rating[entry_point]]
#
# if sum(left) >= sum(right):
#     print(f"Left - {sum(left)}")
# else:
#     print(f"Right - {sum(right)}")



# price_rating = [int(x) for x in input().split(", ")]
#
# entry_point = int(input())
# typo_of_items = input()
#
# left_side = price_rating[:entry_point]
# right_side = price_rating[entry_point + 1:]
# value = price_rating[entry_point]
#
# if typo_of_items == "cheap":
#     left = [x for x in left_side if x < value]
#     right = [x for x in right_side if x < value]
#
# else:
#     left = [x for x in left_side if x >= value]
#     right = [x for x in right_side if x >= value]
#
# if sum(left) >= sum(right):
#     print(f"Left - {sum(left)}")
# else:
#     print(f"Right - {sum(right)}")
#


price_rating = [int(x) for x in input().split(", ")]

entry_point = int(input())
typo_of_items = input()

left_side = []
right_side = []

value = price_rating[entry_point]

for i in range(entry_point):
    left_side.append(price_rating[i])

for i in range(entry_point +1, len(price_rating) ):
    right_side.append(price_rating[i])

if typo_of_items == "cheap":
    left = [x for x in left_side if x < value]
    right = [x for x in right_side if x < value]

else:
    left = [x for x in left_side if x >= value]
    right = [x for x in right_side if x >= value]

if sum(left) >= sum(right):
    print(f"Left - {sum(left)}")
else:
    print(f"Right - {sum(right)}")

