# my_dict = {}
#
# while True:
#     current_input = input()
#     if current_input == "statistics":
#         break
#     current_input = current_input.split(":")
#     key = current_input[0]
#     value = int(current_input[1])
#
#     if key not in my_dict:
#         my_dict[key] = 0
#     my_dict[key] += value
#
# print("Products in stock:")
# for key, value in my_dict.items():
#     print(F"- {key}: {value}")
# print(f"Total Products: {len(my_dict)}")
# print(f"Total Quantity: {sum(my_dict.values())}")


my_dict = {}

while True:
    current_input = input()
    if current_input == "statistics":
        break
    current_input = current_input.split(":")
    key = current_input[0]
    value = int(current_input[1])

    if key not in my_dict:
        my_dict[key] = 0
    my_dict[key] += value

print("Products in stock:")
[print(F"- {key}: {value}") for (key, value) in my_dict.items()]
print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")
