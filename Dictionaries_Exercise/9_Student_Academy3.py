nums = int(input())
student_academy = {}

for _ in range(nums):
    name, grade = input() , float(input())
    if name not in student_academy:
        student_academy[name] = []
    student_academy[name].append(grade)

for key, value in student_academy.items():
    if sum(value) / len(value) >= 4.5:
        print(f"{key} -> {sum(value) / len(value):.2F}")
