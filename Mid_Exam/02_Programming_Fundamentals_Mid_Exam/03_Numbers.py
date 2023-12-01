# numbers = list(map(int, input().split()))
# average_number = sum(numbers) / len(numbers)
#
# new_list = [x for x in numbers if x > average_number]
# new_list = sorted(new_list, reverse=True)
# new_list = list(map(str, new_list))
# if len(new_list) == 0:
#     print("No")
# else:
#     print(" ".join(new_list[:5]))

def top_5(data):
    avg = sum(data) / len(data)

    temp_sum = [x for x in sorted(data, reverse=True) if x > avg]

    if len(temp_sum) != 0:
        return ' '.join(map(str, temp_sum[:5]))
    else:
        return 'No'


numbers = list(map(int, input().split()))
print(top_5(numbers))
