import re

people = input().split(", ")

pattern = r"[A-Za-z]"
pattern2 = r"\d"

race = {}

while True:
    data = input()
    if data == "end of race":
        break
    name = re.findall(pattern, data)
    real_name = "".join(name)
    digit = re.findall(pattern2, data)
    digit_sum = sum([int(x) for x in digit])

    if real_name in people:
        race[real_name] = race.get(real_name, 0) + digit_sum

sorted_list = sorted(race.items(), key=lambda x: -x[1])

for index, x in enumerate(sorted_list, 1):
    if index == 1:
        print(F"1st place: {x[0]}")
    elif index == 2:
        print(F"2nd place: {x[0]}")
    elif index == 3:
        print(F"3rd place: {x[0]}")
