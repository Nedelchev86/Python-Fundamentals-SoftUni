# def calculator(command, num1, num2):
#     if command == "multiply":
#         return num1 * num2
#     elif command == "divide":
#         return num1 // num2
#     elif command == "add":
#         return num1 + num2
#     elif command == "subtract":
#         return num1 - num2
#
# operator = input()
# num_1, num_2 = int(input()), int(input())
# print(calculator(operator, num_1, num_2))

def calculator(command, num1, num2):
    if command == "multiply":
        return num1 * num2
    elif command == "divide":
        return num1 // num2
    elif command == "add":
        return num1 + num2
    elif command == "subtract":
        return num1 - num2

operator = input()
num_1, num_2 = int(input()), int(input())
print(calculator(num1 = num_1, num2 = num_2, command=operator))

