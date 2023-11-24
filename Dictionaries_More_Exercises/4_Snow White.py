dwarf = {}
result_list = []

name2 = "name"
hat2 = "hat"
physic2 = "physic"
hat_len = "hat len"

while True:
    data = input()
    if data == "Once upon a time":
        break
    name, color, physics = [int(x) if x.isdigit() else x for x in data.split(" <:> ")]
    dwarf[color] = dwarf.get(color, {})
    dwarf[color][name] = dwarf[color].get(name, 0)
    if dwarf[color][name] < physics:
        dwarf[color][name] = physics


for hat in dwarf:
    for name, physic in dwarf[hat].items():
        result_list.append({hat_len: len(dwarf[hat]), name2: name, physic2: physic, hat2: hat})
for show in sorted(result_list, key=lambda item: (-item[physic2], -item[hat_len])):
    print(f"({show[hat2]}) {show[name2]} <-> {show[physic2]}")