numbers = input().split(", ")
baggars_count = int(input())

baggars = [0] * baggars_count

for idx in range(len(numbers)):
    baggars_idx = idx % baggars_count
    num = int(numbers[idx])
    baggars[baggars_idx] += num


print(baggars)