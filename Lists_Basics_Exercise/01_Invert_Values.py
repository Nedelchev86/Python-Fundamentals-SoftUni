
list_of_numbers = input().split()
opposite_numbers = []

for elements in list_of_numbers:
    opposite_numbers.append(-int(elements))
print(opposite_numbers)

# print([-(int(x)) for x in input().split()])