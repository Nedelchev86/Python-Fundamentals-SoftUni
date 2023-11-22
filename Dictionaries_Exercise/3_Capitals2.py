# country = input().split(", ")
# capital_cities = input().split(", ")
#
# my_dict = dict(zip(country, capital_cities))
# for key, value in my_dict.items():
#     print(f"{key} -> {value}")
#


my_dict = dict(zip(input().split(", "), input().split(", ")))
for key, value in my_dict.items():
    print(f"{key} -> {value}")
