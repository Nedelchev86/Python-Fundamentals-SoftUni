# employees= input().split()
# factor = int(input())
#
# employees = list(map(lambda x: int(x) * factor, employees))
# filtered_employees_happiness = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))
#
#
#
# if len(filtered_employees_happiness) > len(employees) / 2:
#
#     print(F"Score: {len(filtered_employees_happiness)}/{len(employees)}. Employees are happy!")
# else:
#     print(F"Score: {len(filtered_employees_happiness)}/{len(employees)}. Employees are not happy!")


employees= list(map(int, input().split()))
factor = int(input())

filtered_employees_happiness = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))

if len(filtered_employees_happiness) > len(employees) / 2:

    print(F"Score: {len(filtered_employees_happiness)}/{len(employees)}. Employees are happy!")
else:
    print(F"Score: {len(filtered_employees_happiness)}/{len(employees)}. Employees are not happy!")
