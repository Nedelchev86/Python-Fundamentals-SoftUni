data = input().split()
bakery = {}
search_word = input().split()

for i in range(0, len(data), 2):
    food = data[i]
    quantity = data[i+1]
    bakery[food] = int(quantity)

for search in search_word:
    if search in bakery.keys():
        print(F"We have {bakery[search]} of {search} left")
    else:
        print(F"Sorry, we don't have {search}")
