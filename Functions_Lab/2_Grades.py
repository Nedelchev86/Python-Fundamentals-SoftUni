def grade_category(grade):
    result = None
    if grade <= 2.99:
        result = "Fail"
    elif grade <= 3.49:
        result = "Poor"
    elif grade <= 4.49:
        result = "Good"
    elif grade <= 5.49:
        result = "Very Good"
    elif grade <= 6.00:
        result = "Excellent"
    return result


grade_input = float(input())
print(grade_category(grade_input))
