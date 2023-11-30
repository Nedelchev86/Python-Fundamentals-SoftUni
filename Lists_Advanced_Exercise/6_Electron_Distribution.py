number_of_electrons = int(input())
electron_list = []

while number_of_electrons:
    n = len(electron_list) + 1
    shell_value = min(2 * (n ** 2), number_of_electrons)
    electron_list.append(shell_value)
    number_of_electrons -= shell_value

print(electron_list)