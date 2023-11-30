number = int(input())

possitive = []
negative = []
count_positive = 0
sum_negative = 0

for _ in range(number):
    num = int(input())
    if num >= 0:
        possitive.append(num)
        count_positive += 1
    else:
        negative.append(num)
        sum_negative += num
print(possitive)
print(negative)
print(F"Count of positives: {count_positive}")
print(F"Sum of negatives: {sum_negative}")
