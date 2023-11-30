numbers = list(map(int, input().split(", ")))

indices = list(map(lambda x:x if numbers[x] % 2 == 0 else "no", range(len(numbers))))

indices_to_print = list(filter(lambda x: x != "no", indices))

print(indices_to_print)