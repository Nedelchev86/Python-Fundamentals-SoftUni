waiting_people = int(input())
lift_placec = list(map(int, input().split(" ")))

for i in range(len(lift_placec)):
    if waiting_people > 3:
        current_free_lift_plaacec = 4 - (lift_placec[i])
        waiting_people -= current_free_lift_plaacec
        lift_placec[i] += current_free_lift_plaacec
    else:
        lift_placec[i] += waiting_people
        waiting_people = 0

if waiting_people > 0:
    print(F"There isn't enough space! {waiting_people} people in a queue!")
elif len(lift_placec) * 4 > sum(lift_placec):
    print("The lift has empty spots!")
print(" ".join([str(x) for x in lift_placec]))