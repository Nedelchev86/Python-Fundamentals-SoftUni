
def calculator(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a/b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


operation = input()
first = int(input())
second = int(input())

print(calculator(first, second, operation))
