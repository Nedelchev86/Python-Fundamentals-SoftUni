
waiting = ""
current_String = ""
nums = ""

data = input()

for el in range(len(data)):
    if data[el].isdigit():
        nums += data[el]
        if el < len(data) -1:
            if not data[el+1].isdigit():
                waiting += (current_String * int(nums))
                current_String = ""
                nums = ""
            else:
                continue
        else:
            waiting += (current_String * int(nums))
    else:
        current_String += data[el].upper()
print(f"Unique symbols used: {len(set(waiting))}")
print(waiting)
