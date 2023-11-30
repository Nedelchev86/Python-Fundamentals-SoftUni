nums = int(input())
possitive = []
negative = []
for _ in range(nums):
    num = int(input())
    if num >= 0:
        possitive.append(num)
    else:
        negative.append(num)

print(possitive)
print(negative)
print(F"Count of positives: {len(possitive)}")
print(F"Sum of negatives: {sum(negative)}")