courses = {}

while True:
    current_data = input()
    if current_data == "end":
        break
    course, student = current_data.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for i in value:
        print(f"-- {i}")




