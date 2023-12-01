food, hay, cover, weight = float(input()), float(input()), float(input()), float(input())

for i in range(1, 31):
    food -= 0.300
    if i % 2 == 0:
        hay -= (food * 0.05)
    if i % 3 == 0:
        cover -= weight / 3
    if food <= 0 or cover <= 0 or hay <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(F"Everything is fine! Puppy is happy! Food: {food:.2F}, Hay: {hay:.2F}, Cover: {cover:.2F}.")
