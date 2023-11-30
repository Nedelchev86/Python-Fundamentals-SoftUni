numbers = [int(j) for j in input().split()]
removed_elements = 0

while True:
    if len(numbers) <= 0:
        break
    idx = int(input())
    if 0 <= idx < len(numbers):
        element = int(numbers[idx])
        removed_elements += element
        for i in numbers:
            idx_i = numbers.index(i)
            if i <= element:
                numbers[idx_i] += element
            else:
                numbers[idx_i] -= element
        numbers.pop(idx)
    elif idx < 0:
        element = numbers[0]
        removed_elements += element
        numbers[0] = numbers[-1]
        for i in numbers:
            idx_i = numbers.index(i)
            if i <= element:
                numbers[idx_i] += element
            else:
                numbers[idx_i] -= element
    elif idx >= len(numbers):
        element = numbers[-1]
        removed_elements += element
        numbers[-1] = numbers[0]
        for i in numbers:
            idx_i = numbers.index(i)
            if i <= element:
                numbers[idx_i] += element
            else:
                numbers[idx_i] -= element

print(removed_elements)