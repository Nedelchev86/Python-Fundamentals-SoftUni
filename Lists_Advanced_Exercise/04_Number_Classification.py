numbers = [int(num) for num in input().split(", ")]

positive = [x for x in numbers if x >= 0]
negative = [x for x in numbers if x < 0]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

print(F"Positive: {', '.join([str(x) for x in positive])}")
print(F"Negative: {', '.join([str(x) for x in negative])}")
print(F"Even: {', '.join([str(x) for x in even])}")
print(F"Odd: {', '.join([str(x) for x in odd])}")



# numbers = [int(num) for num in input().split(", ")]
#
# positive = [str(x) for x in numbers if x >= 0]
# negative = [str(x) for x in numbers if x < 0]
# even = [str(x) for x in numbers if x % 2 == 0]
# odd = [str(x) for x in numbers if x % 2 != 0]
#
# print(F"Positive: {', '.join(positive)}")
# print(F"Negative: {', '.join(negative)}")
# print(F"Even: {', '.join(even)}")
# print(F"Odd: {', '.join(odd)}")
