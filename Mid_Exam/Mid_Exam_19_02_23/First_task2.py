experience_for_tank = int(input())
count = int(input())
experience = 0

for battle in range(1, count + 1):
    current_experience = int(input())
    if battle % 3 == 0:
        current_experience += current_experience * 0.15
    if battle % 5 == 0:
        current_experience -= current_experience * 0.10
    if battle % 15 == 0:
        current_experience += current_experience * 0.05
    experience += current_experience

    if experience >= experience_for_tank:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break
else:
    print(f"Player was not able to collect the needed experience, {experience_for_tank - experience:.2F} more needed.")
