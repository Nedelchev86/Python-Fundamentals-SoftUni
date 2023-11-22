courses = {}
while True:
    data = input().split(" : ")
    course_name = data[0]
    if course_name == "end":
        break
    student_name = data[1]
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for key, value in courses.items():
    print(F"{key}: {len(value)}")
    for name in value:
        print(F"-- {name}")