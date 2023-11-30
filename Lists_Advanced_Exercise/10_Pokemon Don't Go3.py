pokemons = [int(x) for x in input().split()]
total = 0

while pokemons:
    idx = int(input())
    if 0 <= idx < len(pokemons):
        removed = pokemons.pop(idx)
        total += removed
    elif idx < 0:
        removed = pokemons[0]
        fist_element = pokemons[-1]
        pokemons[0] = pokemons[-1]
        total += removed
    else:
        removed = pokemons.pop()
        last_element = pokemons[0]
        pokemons.append(last_element)
        total += removed

    pokemons = [x + removed if x <= removed else x - removed for x in pokemons]
print(total)
