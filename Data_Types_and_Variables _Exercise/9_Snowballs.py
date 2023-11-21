# snowballs = int(input())
# value = 0
# weight = 0
# time = 0
# quality = 0
#
# for i in range(1, snowballs +1):
#     current_weight = int(input())
#     current_time = int(input())
#     current_quality = int(input())
#     current_value = int((current_weight / current_time) ** current_quality)
#     if current_value > value:
#         value = current_value
#         weight = current_weight
#         time = current_time
#         quality = current_quality
#
# print(F"{weight} : {time} = {value} ({quality})")



n = int(input())
best_snowball = 0
output = ""

for idx in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight // time) ** quality

    if result > best_snowball:
        best_snowball = result
        output = F"{weight} : {time} = {result} ({quality})"


print(output)