# current_data = input()
# company_users = {}
#
# while current_data != "End":
#     company_name, employee_id = current_data.split(" -> ")
#     if company_name not in company_users:
#         company_users[company_name] = {employee_id: ""}
#     if employee_id not in company_users[company_name]:
#         company_users[company_name][employee_id] = ""
#     current_data = input()
# for key, value in company_users.items():
#     print(key)
#     for i in value:
#         print(f"-- {i}")

# current_data = input()
# company_users = {}
#
# while current_data != "End":
#     company_name, employee_id = current_data.split(" -> ")
#     if company_name not in company_users:
#         company_users[company_name] = {employee_id: ""}
#     if employee_id not in company_users[company_name]:
#         company_users[company_name][employee_id] = ""
#     current_data = input()
# for key, value in company_users.items():
#     print(key)
#     print("\n".join([f'-- {x}' for x in value]))


current_data = input()
company_users = {}

while current_data != "End":
    company_name, employee_id = current_data.split(" -> ")
    company_users[company_name] = company_users.get(company_name, {})
    company_users[company_name][employee_id] = ""
    current_data = input()
for key, value in company_users.items():
    print(key)
    print("\n".join([f'-- {x}' for x in value]))