employees_1 = int(input())
employees_2 = int(input())
employees_3 = int(input())

all_employees_per_hours = employees_1 + employees_2 + employees_3

students_count = int(input())
hours = 0

while students_count > 0:
    students_count -= all_employees_per_hours
    hours += 1
    if hours % 4 == 0:
        hours += 1
print(F"Time needed: {hours}h.")
