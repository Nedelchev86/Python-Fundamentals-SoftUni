text = input()
courses = {}

while ":" in text:
    name, id_, course = text.split(":")
    if course not in courses:
        courses[course] = {}
    courses[course][id_] = name
    text = input()

searched = text.replace("_", " ")

for key,value in courses[searched].items():
    print(f"{value} - {key}")
