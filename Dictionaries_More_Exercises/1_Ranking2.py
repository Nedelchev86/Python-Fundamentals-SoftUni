contests = {}
students_name = {}

while True:
    first_input = input()
    if first_input == "end of contests":
        break
    contest, password = first_input.split(":")
    contests[contest] = password

while True:
    second_input = input()
    if second_input == "end of submissions":
        break
    contest, password, username, points = second_input.split("=>")
    points = int(points)
    if contest in contests and contests[contest] == password:
        if username not in students_name:
            students_name[username] = {}
        if contest not in students_name[username]:
            students_name[username][contest] = 0
        if points > students_name[username][contest]:
            students_name[username][contest] = points
# best_points = 0
# best_student = ""
# 
# for students, course in students_name.items():
#     if sum(students_name[students].values()) > best_points:
#         best_points = sum(students_name[students].values())
#         best_student = students

best_student = {name: sum(students_name[name].values()) for name in students_name}
best_points = max(best_student, key=best_student.get)

print(f"Best candidate is {best_points} with total {best_student[best_points]} points.")
print("Ranking:")
students_name = dict(sorted(students_name.items()))
for key, value in students_name.items():
    print(key)
    value = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
    for course, points in value.items():
        print(f"#  {course} -> {points}")