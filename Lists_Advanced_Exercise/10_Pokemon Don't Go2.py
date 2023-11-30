numbers = [int(n) for n in input().split()]
removed_elements = []

while True:
    if len(numbers) <= 0:
        print(sum(removed_elements))
        break
    idx = int(input())

    if 0 <= idx < len(numbers):
        removed_num = numbers[idx]
        removed_elements.append(removed_num)
        numbers.pop(idx)
        for i in numbers:
            idx_i = numbers.index(i)
            if i <= removed_num:
                numbers[idx_i] += removed_num
            else:
                numbers[idx_i] -= removed_num

    elif idx < 0:
        removed_num = numbers[0]
        numbers[0] = numbers[-1]
        removed_elements.append(removed_num)
        for i in numbers:
            idx_i = numbers.index(i)
            if i <= removed_num:
                numbers[idx_i] += removed_num
            else:
                numbers[idx_i] -= removed_num
    elif idx >= len(numbers):
        removed_num = numbers[-1]
        numbers[-1] = numbers[0]
        removed_elements.append(removed_num)
        for i in numbers:
            idx_i = numbers.index(i)
            if i <= removed_num:
                numbers[idx_i] += removed_num
            else:
                numbers[idx_i] -= removed_num
