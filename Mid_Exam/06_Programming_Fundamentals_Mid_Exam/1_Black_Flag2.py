days = int(input())
plunder_for_day = int(input())
expected_plunder = int(input())
total_plunder = 0

for i in range(1, days+1):
    total_plunder += plunder_for_day
    if i % 3 == 0:
        total_plunder += plunder_for_day * 0.5
    if i % 5 == 0:
        total_plunder = total_plunder * 0.7
if total_plunder >= expected_plunder:
    print(F"Ahoy! {total_plunder:.2F} plunder gained.")
else:
    percent = (total_plunder / expected_plunder) * 100
    print(F"Collected only {percent:.2F}% of the plunder.")