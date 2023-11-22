# country = input().split(", ")
# capital = input().split(", ")
#
# data = dict(zip(country, capital))
# for word in data:
#     print(F"{word} -> {data[word]}")


country = input().split(", ")
capital = input().split(", ")

data = {country[index]:capital[index] for index in range(len(country))}
for word in data:
    print(F"{word} -> {data[word]}")