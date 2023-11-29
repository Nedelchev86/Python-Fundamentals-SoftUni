# x = lambda a, b: a * b
#
# print(x(int(input()), int(input())))
#

def pectangle_area(a, b):
    return a * b


width, height = int(input()), int(input())
print(pectangle_area(width, height))