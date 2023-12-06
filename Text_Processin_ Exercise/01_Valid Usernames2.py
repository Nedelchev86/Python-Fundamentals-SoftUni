# email = input().split(", ")
# valid = True
#
# for email in email:
#     valid = True
#     if not 3 <= len(email) <= 16:
#         valid = False
#         continue
#     for char in email:
#         if not (char.isalnum() or char == "_" or char == "-"):
#             valid = False
#             continue
#     if " " in email:
#         valid = False
#         continue
#     if valid:
#         print(email)


email = input().split(", ")
valid = True

for email in email:
    valid = True
    if not 3 <= len(email) <= 16:
        continue
    for char in email:
        if not (char.isdigit() or char.isalpha() or char == "_" or char == "-"):
            valid = False
    if valid:
        print(email)
