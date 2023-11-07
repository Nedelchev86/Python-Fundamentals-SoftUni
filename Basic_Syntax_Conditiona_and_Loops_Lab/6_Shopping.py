budget =int(input())

while budget >= 0:
    cost = input()
    if cost == "End":
        print("You bought everything needed.")
        break
    budget -= int(cost)
else:
    print("You went in overdraft!")