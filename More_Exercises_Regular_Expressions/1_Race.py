import re
names = input().split(", ")
race = dict()
while True:
    data = input()
    if data == "end of race":
        break
    pattern_name = re.findall(r"[A-Za-z]", data)
    pattern_digit = re.findall(r"\d", data)
    name = "".join(pattern_name)
    digit = sum([int(x) for x in pattern_digit])
    if name in names:
        if name not in race:
            race[name] = 0
        race[name] += digit

race_sorted = dict(sorted(race.items(), key=lambda item: -item[1]))


if len(race_sorted) >= 3:
    print(F"1st place: {list(race_sorted)[0]}")
    print(F"2nd place: {list(race_sorted)[1]}")
    print(F"3rd place: {list(race_sorted)[2]}")
elif len(race_sorted.keys()) == 2:
    print(F"1st place: {list(race_sorted)[0]}")
    print(F"2nd place: {list(race_sorted)[1]}")
elif len(race_sorted.keys()) == 1:
    print(F"1st place: {list(race_sorted)[0]}")

