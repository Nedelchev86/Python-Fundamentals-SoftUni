courses = input().split(", ")
user_input = input()

while user_input != "course start":
    current_input = user_input.split(":")
    command = current_input[0]
    lesson_title = current_input[1]

    if command == "Add":
        if lesson_title not in courses:
            courses.append(lesson_title)
    if command == "Insert":
        idx = int(current_input[2])
        if lesson_title not in courses:
            courses.insert(idx, lesson_title)
    if command == "Remove":
        if lesson_title in courses:
            courses.remove(lesson_title)
            exerice = lesson_title+"-Exercise"
            if exerice in courses:
                courses.remove(exerice)
    if command == "Swap":
        lesson_title2 = current_input[2]
        if lesson_title in courses and lesson_title2 in courses:
            index1 = courses.index(lesson_title)
            index2 = courses.index(lesson_title2)
            courses[index1], courses[index2] = courses[index2], courses[index1]
            exerice = lesson_title+"-Exercise"
            exerice2 = lesson_title2+"-Exercise"
            if exerice in courses:
                courses.remove(exerice)
                courses.insert(index2 +1, exerice)
            if exerice2 in courses:
                courses.remove(exerice2)
                courses.insert(index1+1, exerice2)

    if command == "Exercise":
        if lesson_title in courses:
            idx = int(courses.index(lesson_title))
            courses.insert(idx+1, lesson_title+"-Exercise")
        else:
            courses.append(lesson_title)
            courses.append(lesson_title+"-Exercise")

    user_input = input()

for i in range(0, len(courses)):
    print(F"{i+1}.{courses[i]}")

