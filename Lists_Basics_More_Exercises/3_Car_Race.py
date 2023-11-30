
user_input = [int(x) for x in input().split(" ")]
left_race = user_input[:len(user_input)//2]
right_race = user_input[(len(user_input)//2)+1:]


time_left = 0
time_right = 0
for i in left_race:
    time_left += i
    if i == 0:
        time_left = time_left * 0.8
for j in right_race[::-1]:
    time_right += j
    if j == 0:
        time_right = time_right * 0.8

if time_left < time_right:
    print(F"The winner is left with total time: {time_left:.1F}")
else:
    print(F"The winner is right with total time: {time_right:.1F}")
