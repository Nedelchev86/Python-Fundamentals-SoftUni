input_data = input()

while input_data != "stop playing":
    unique = True
    input_data = [int(x) for x in input_data.split()]
    for nums in input_data:
        if input_data.count(nums) > 1:
            unique = False
            break

    if unique:
        result = list(sorted([x + 2 if x % 2 == 0 else x for x in input_data]))
        print(f'Unique list: {",".join([str(x) for x in result])}')
    else:
        result = list(sorted([x + 3 if x % 2 != 0 else x for x in input_data]))
        print(f'Non-unique list: {":".join([str(x) for x in result])}')
    print(f"Output: {sum(result) / len(result):.2F}")
    input_data = input()


