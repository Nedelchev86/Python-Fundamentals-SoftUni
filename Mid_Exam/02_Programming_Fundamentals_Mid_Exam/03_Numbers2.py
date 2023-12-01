#just test

numbers = [int(x) for x in input().split()]
result = list(map(str, [x for x in sorted(numbers, reverse=True) if x > (float(sum(numbers) / len(numbers)))]))

if len(result) == 0:
    print("No")
else:
    print(" ".join(result[:5]))