pokemons = [int(x) for x in input().split()]
removed_list = []


while pokemons:
    idx = int(input())

    if idx >= 0 and idx < len(pokemons):
        removed = pokemons.pop(idx)
        removed_list.append(removed)
        pokemons = [x + removed if x <= removed else x - removed for x in pokemons]

    elif idx < 0:
        removed = pokemons.pop(0)
        fist_element = pokemons[-1]
        pokemons.insert(0, fist_element)
        removed_list.append(removed)
        pokemons = [x + removed if x <= removed else x - removed for x in pokemons]

    else:
        removed = pokemons.pop()
        last_element = pokemons[0]
        pokemons.append(last_element)
        removed_list.append(removed)
        pokemons = [x + removed if x <= removed else x - removed for x in pokemons]

print(sum(removed_list))