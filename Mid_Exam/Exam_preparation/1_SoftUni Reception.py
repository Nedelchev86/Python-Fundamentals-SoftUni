first = int(input())
second = int(input())
third = int(input())
students = int(input())
count = 0
total_per_hourd = first + second + third

for i in range(1, students):
    count += 1
    if i % 4 == 0:
        continue
    students -= total_per_hourd
    if students <= 0:
        break
print(f"Time needed: {count}h.")
