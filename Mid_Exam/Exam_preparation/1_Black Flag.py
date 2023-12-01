days = int(input())

plunder_for_a_day = int(input())
expected_plunder = int(input())
plunder = 0

for i in range(1, days +1):
    plunder += plunder_for_a_day
    if i % 3 == 0:
        plunder += 0.5 * plunder_for_a_day
    if i % 5 == 0:
        plunder = plunder * 0.7

if plunder >= expected_plunder:
    print(F"Ahoy! {plunder:.2F} plunder gained.")
else:
    print(f"Collected only {(plunder / expected_plunder ) * 100:.2F}% of the plunder.")