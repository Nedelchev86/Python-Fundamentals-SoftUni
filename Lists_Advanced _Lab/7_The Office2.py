employees_happiness = input().split()
factor = int(input())

employees_happiness_2 = list(map(lambda x: int(x) * factor, employees_happiness))


filtres = list(filter(lambda x: x  >= (sum(employees_happiness_2) / len(employees_happiness_2)), employees_happiness_2))

if len(filtres) > len(employees_happiness) / 2:

    print(F"Score: {len(filtres)}/{len(employees_happiness_2)}. Employees are happy!")
else:
    print(F"Score: {len(filtres)}/{len(employees_happiness_2)}. Employees are not happy!")