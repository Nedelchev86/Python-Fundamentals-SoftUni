contest_dict = {}
individual = {}

while True:
    current_data = input()
    if current_data == "no more time":
        break
    username, contest, points = [int(x) if x.isdigit() else x for x in current_data.split(" -> ")]
    if contest not in contest_dict:
        contest_dict[contest] = {}
    if username not in contest_dict[contest]:
        contest_dict[contest][username] = 0
    if contest_dict[contest][username] < points:
        contest_dict[contest][username] = points

for key, value in contest_dict.items():
    print(f"{key}: {len(value)} participants")
    for index, (name, point) in enumerate((sorted(value.items(), key=lambda x: (-x[1], x[0]))), 1):
        print(f"{index}. {name} <::> {point}")
        if name not in individual:
            individual[name] = 0
        individual[name] += point

print("Individual standings:")
for index, (user, score) in enumerate(sorted(individual.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{index}. {user} -> {score}")
