days_of_the_plunder = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
total_plunder = 0

for day in range(1, days_of_the_plunder+1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += daily_plunder * 0.50

    if day % 5 == 0:
        total_plunder -= total_plunder * 0.30
if total_plunder >= expected_plunder:
    print(F"Ahoy! {total_plunder:.2F} plunder gained.")
else:
    print(F"Collected only {(total_plunder / expected_plunder)* 100:.2F}% of the plunder.")
