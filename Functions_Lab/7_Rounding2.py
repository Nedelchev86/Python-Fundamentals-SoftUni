#
# print(list(map(lambda x: round(float(x)), input().split())))

def rounding(float_numbers):
    rounded = []
    for i in float_numbers:
        rounded.append(round(i))
    return  rounded

data = list(map(float, input().split()))

print(rounding(data))