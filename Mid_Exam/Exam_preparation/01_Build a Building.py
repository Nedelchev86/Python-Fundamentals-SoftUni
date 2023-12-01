budget = float(input())
capital = float(input())
investors = int(input())

for i in range(1,investors+1):
    money = float(input())
    capital += money
    print(f"Investor {i} gave us {money:.2F}.")
    if capital >= budget:
        print(F"We will manage to build it. Start now! Extra money - {capital-budget:.2F}.")
        break
else:
    print(F"Project can not start. We need {budget-capital:.2F} more.")

