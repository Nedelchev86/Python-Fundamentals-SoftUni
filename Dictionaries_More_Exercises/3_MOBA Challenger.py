players_pool = {}

while True:
    data = input()
    if data == "Season end":
        break

    if "->" in data:
        player, position, skill = [x if x.isalpha() else int(x) for x in data.split(" -> ")]

        if player not in players_pool:
            players_pool[player] = {}
        if position not in players_pool[player]:
            players_pool[player][position] = 0
        if players_pool[player][position] < skill:
            players_pool[player][position] = skill

    elif "vs" in data:
        player1, player2 = data.split(" vs ")
        find = False
        if player1 in players_pool and player2 in players_pool:
            for position1 in players_pool[player1]:
                for position2 in players_pool[player2]:
                    if position1 == position2:
                        if players_pool[player1][position1] == players_pool[player2][position2]:
                            find = True
                            break

                        elif players_pool[player1][position1] > players_pool[player2][position2]:
                            del players_pool[player2]
                            find = True
                            break

                        elif players_pool[player1][position1] < players_pool[player2][position2]:
                            del players_pool[player1]
                            find = True
                            break
                    if find:
                        break


for player, totalSkill in sorted(players_pool.items(), key=lambda x: (-sum(i for i in x[1].values()), x[0])):
    if len(players_pool[player]) == 0:
        continue
    print(f'{player}: {sum(totalSkill.values())} skill')

    for user, skill in sorted(players_pool[player].items(), key=lambda x: (-x[1], x[0])):
        print(f'- {user} <::> {skill}')
