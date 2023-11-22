# number = int(input())
# students = {}
# removed = []
# for _ in range(number):
#     name = input()
#     grade = float(input())
#     if name not in students:
#         students[name] = []
#     students[name].append(grade)
#
# for name, grade in students.items():
#     average_grade = (sum(grade) / len(grade))
#     if average_grade < 4.50:
#         continue
#     else:
#         print(F"{name} -> {average_grade:.2F}")


number = int(input())
students = {}
removed = []
for _ in range(number):
    name = input()
    grade = float(input())
    students[name] = students.get(name, [].append(grade))
    students[name].append(grade)


for name, grade in students.items():
    average_grade = (sum(grade) / len(grade))
    if average_grade < 4.50:
        continue
    else:
        print(F"{name} -> {average_grade:.2F}")
