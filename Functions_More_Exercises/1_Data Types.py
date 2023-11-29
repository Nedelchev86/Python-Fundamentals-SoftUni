def data_type(string, num):
    if string == "int":
        return int(num) * 2
    if string == "real":
        return f"{float(num) * 1.5:.2F}"
    if string == "string":
        return f"${num}$"


print(data_type(input(), input()))