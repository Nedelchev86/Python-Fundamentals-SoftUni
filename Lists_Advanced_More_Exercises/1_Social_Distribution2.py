numbers = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

for i in range(len(numbers)):
    if numbers[i] < minimum_wealth:
        difference = minimum_wealth - numbers[i]
        max_number = max(numbers)
        if max_number - difference >= minimum_wealth:
            numbers[numbers.index(max_number)] -= difference
            numbers[i] += difference
if sum(numbers) >= len(numbers) * minimum_wealth:
    print(numbers)
else:
    print("No equal distribution possible")