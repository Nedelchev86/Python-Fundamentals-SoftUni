from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0

if students == 0 or lectures == 0:
    print(f"Max Bonus: {0}.")
    print(F"The student has attended {0} lectures.")


else:
    for i in range(students):
        attendances = int(input())
        student_bonus = ceil(attendances / lectures * (5 + additional_bonus))
        if student_bonus >= max_bonus:
            max_bonus = student_bonus
            student_attendance = attendances

if max_bonus != 0:
    print(f"Max Bonus: {max_bonus}.")
    print(F"The student has attended {student_attendance} lectures.")

