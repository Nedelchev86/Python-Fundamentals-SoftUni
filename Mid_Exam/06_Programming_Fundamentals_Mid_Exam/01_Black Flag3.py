days = int(input())
total_plunder = 0
dayly_plunder = int(input())
expected_plunder = int(input())

for i in range(1, days +1):
    total_plunder += dayly_plunder
    if i % 3 == 0:
        total_plunder += dayly_plunder * 0.5
    if i % 5 == 0:
        total_plunder -= total_plunder * 0.3

if total_plunder >= expected_plunder:
    print(F"Ahoy! {total_plunder:.2F} plunder gained.")
else:
    print(F"Collected only {((total_plunder / expected_plunder) * 100):.2F}% of the plunder.")