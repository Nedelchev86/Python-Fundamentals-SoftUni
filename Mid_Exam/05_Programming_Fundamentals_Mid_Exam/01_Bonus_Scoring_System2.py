from math import ceil
number_students = int(input())
lectures = int(input())
additional_bonus = int(input())
list_ot_score = []


def best_of_the_best(a, b, c):
    total_bonus = ceil(a / b * (5 + c))
    list_ot_score.append((total_bonus, a))
    return list_ot_score.sort()


for i in range(number_students):
    attendance_of_each_student = int(input())
    best_of_the_best(attendance_of_each_student, lectures, additional_bonus)

print(f"Max Bonus: {(list_ot_score[-1][0])}.")
print(F"The student has attended {(list_ot_score[-1][-1])} lectures.")