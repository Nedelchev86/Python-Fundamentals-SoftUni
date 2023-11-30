team_a = 11
team_b = 11
info = input().split()
player_loses = []
terminated = False

for cards in info:
    if cards not in player_loses:
        player_loses.append(cards)
        if "A" in cards:
            team_a -= 1
        elif "B" in cards:
            team_b -= 1
        if team_a < 7 or team_b < 7:
            terminated = True
            break

print(F"Team A - {team_a}; Team B - {team_b}")
if terminated:
    print(("Game was terminated"))

