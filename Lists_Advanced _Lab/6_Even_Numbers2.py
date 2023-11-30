# numbers = list(map(int, input().split(", ")))
#
# filter_number = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
#
# print(filter_number)
#
#
#
#
numbers = list(map(int, input().split(", ")))
idices = list(map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers))))
filtred = list(filter(lambda x: x != "no", idices))
print(filtred)

