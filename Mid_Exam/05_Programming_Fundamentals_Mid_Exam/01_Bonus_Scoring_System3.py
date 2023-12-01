from math import  ceil

students = int(input())
lectures = int(input())
bonus = int(input())
total = 0
max = 0

if lectures == 0 or students == 0:
    print("Max Bonus: 0.")
    print(F"The student has attended 0 lectures.")
else:
    for i in range(students):
        attendances = int(input())
        if attendances == 0:
            continue
        total = attendances / lectures * (5 + bonus)
        if total > max:
            max = total
            best_attendances = attendances
    print(F"Max Bonus: {ceil(max)}.")
    print(F"The student has attended {best_attendances} lectures.")


