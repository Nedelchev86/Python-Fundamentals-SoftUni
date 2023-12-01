food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

for days in range(1, 31):
    food -= 300
    if days % 2 == 0:
        hay -= 0.05 * food
    if days % 3 == 0:
        cover -= weight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2F}, Hay: {hay/1000:.2F}, Cover: {cover/1000:.2F}.")
