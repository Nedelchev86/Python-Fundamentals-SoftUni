from math import ceil
number_students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
best_students = 0

for i in range(number_students):
    attendance_of_each_student = int(input())
    total_bonus = attendance_of_each_student / lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        best_students = attendance_of_each_student

print(f"Max Bonus: {ceil(max_bonus)}.")
print(F"The student has attended {best_students} lectures.")

# import math
#
# students = int(input())
# lectures = int(input())
# initial_bonus = int(input())
# attendance_list = []
#
# if lectures == 0:
#     print(f'Max Bonus: 0.')
#     print(f'The student has attended 0 lectures.')
# else:
#     for i in range(1, students + 1):
#         attendances = int(input())
#         attendance_list.append(attendances)
#
#     print(f'Max Bonus: {math.ceil((max(attendance_list) / lectures) * (5 + initial_bonus))}.')
#     print(f'The student has attended {max(attendance_list)} lectures.')