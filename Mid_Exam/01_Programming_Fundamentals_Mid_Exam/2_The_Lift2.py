waiting_people = int(input())
lift_placec = list(map(int, input().split(" ")))
people_in_lift = []
for i in lift_placec:
    waiting_people -= (4 - i)
    people_in_lift.append(str(4 - i))
if waiting_people < 0:
    print("The lift has empty spots!")
else:
    print(F"There isn't enough space! {waiting_people} people in a queue!")
print(" ".join(people_in_lift))
