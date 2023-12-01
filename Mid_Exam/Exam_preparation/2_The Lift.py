people = int(input())
lift_list = [int(x) for x in input().split()]

for i in range(len(lift_list)):
    lift = int(lift_list[i])
    if people > 3:
        free_space = 4 - lift
        people -= free_space
        lift_list[i] += free_space
    else:
        lift_list[i] += people
        people = 0


if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

elif len(lift_list) * 4 > sum(lift_list):
    print("The lift has empty spots!")

print(" ".join([str(x) for x in lift_list]))
