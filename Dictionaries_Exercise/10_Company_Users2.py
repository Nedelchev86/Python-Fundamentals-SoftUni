employees = {}
while True:
    data = input()
    if data == "End":
        break
    data = data.split(" -> ")
    company = data[0]
    id_of_employee = data[1]
    if company not in employees:
        employees[company] = []
    if id_of_employee not in employees[company]:
        employees[company].append(id_of_employee)

for key, value in employees.items():
    print(key)
    for name in value:
        print(F"-- {name}")
