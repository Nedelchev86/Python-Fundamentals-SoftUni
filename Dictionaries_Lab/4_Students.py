text = input()
courses = dict()

while ":" in text:
    (name, id, course) = text.split(":")

    # name = data[0]
    # id = data[1]
    # course = data[2]

    if course not in courses.keys():
        courses[course] = {}
    courses[course][id] = name
    text = input()

search = text.replace("_", " ")

for id in courses[search]:
    print(F"{courses[search][id]} - {id}")
